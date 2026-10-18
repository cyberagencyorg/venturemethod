"""Single-page, operator-authorized public HTTPS source capture.

No credentials, redirects, crawling, proxies or non-public destinations. Resolve
and validate the address *before* connecting, then pin it for TLS to avoid
time-of-check/time-of-use DNS rebinding. Imported content is untrusted evidence.
"""
from __future__ import annotations

import hashlib
from html.parser import HTMLParser
import http.client
import ipaddress
from pathlib import Path
import re
import socket
import ssl
import tempfile
from urllib.parse import urlsplit
from . import research

MAX_RAW_BYTES = 512 * 1024
SAFE_MIMES = {'text/html', 'text/plain', 'text/markdown', 'text/csv', 'text/tab-separated-values'}
SKIP = {'script', 'style', 'noscript', 'template', 'svg', 'iframe'}


class _HTMLText(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.depth = 0
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.depth += 1
        elif not self.depth and tag in {'p','div','h1','h2','h3','li','tr','br','section'}:
            self.parts.append('\n')

    def handle_endtag(self, tag):
        if tag in SKIP and self.depth:
            self.depth -= 1
        elif not self.depth and tag in {'p','div','h1','h2','h3','li','tr','section'}:
            self.parts.append('\n')

    def handle_data(self, data):
        if not self.depth:
            self.parts.append(data)


def validate_url(url: str, hosts: list[str]) -> tuple[str,str]:
    if not url or len(url)>2048 or not hosts or '#' in url or any(c.isspace() or ord(c)<32 for c in url):
        raise ValueError('Short fragment-free URL and explicit host allowlist required')
    p=urlsplit(url)
    if p.scheme!='https' or p.username or p.password or p.port not in (None,443):
        raise ValueError('HTTPS on port 443, without credentials, is required')
    host=p.hostname
    if not host or host.endswith('.') or host.startswith('.') or len(host)>253:
        raise ValueError('Invalid public hostname')
    host=host.encode('idna').decode('ascii').lower()
    try:
        ipaddress.ip_address(host)
    except ValueError:
        pass
    else:
        raise ValueError('IP literal URLs are forbidden')
    if host=='localhost' or '.' not in host or any(
            not re.fullmatch(r'[a-z0-9](?:[a-z0-9-]*[a-z0-9])?', part)
            for part in host.split('.')):
        raise ValueError('Invalid public hostname')
    allowed=[]
    for name in hosts:
        if not name or name!=name.strip() or any(x in name for x in '/*:') or name.startswith('.') or name.endswith('.'):
            raise ValueError('Allowed hosts must be exact DNS hostnames')
        allowed.append(name.encode('idna').decode('ascii').lower())
    if host not in allowed:
        raise ValueError('Host not explicitly permitted')
    return host, (p.path or '/')+('?' + p.query if p.query else '')


def public_ips(host: str) -> list[str]:
    try:
        answers=socket.getaddrinfo(host,443,type=socket.SOCK_STREAM)
    except OSError as exc:
        raise ValueError('DNS resolution failed') from exc
    if not answers:
        raise ValueError('Host has no DNS addresses')
    ips=[]
    for answer in answers:
        ip=ipaddress.ip_address(answer[4][0])
        if not ip.is_global:
            raise ValueError('Host resolves to a non-public IP')
        if str(ip) not in ips:
            ips.append(str(ip))
    return ips


class PinnedTLS(http.client.HTTPSConnection):
    def __init__(self,host,ip,timeout):
        super().__init__(host,port=443,timeout=timeout,context=ssl.create_default_context())
        self.ip=ip

    def connect(self):
        raw=socket.create_connection((self.ip,443),timeout=self.timeout)
        try:
            self.sock=self._context.wrap_socket(raw,server_hostname=self.host)
        except Exception:
            raw.close()
            raise


def request(host: str, path: str, ip: str, timeout: int) -> tuple[int,str,bytes]:
    conn=PinnedTLS(host,ip,timeout)
    try:
        conn.request('GET',path,headers={
            'Host':host,'User-Agent':'VentureMethodResearch/0.1 (manual; no crawling)',
            'Accept':'text/html,text/plain,text/markdown,text/csv;q=0.9',
            'Accept-Encoding':'identity','Connection':'close'})
        response=conn.getresponse()
        status=response.status
        mime=response.getheader('Content-Type','').split(';')[0].strip().lower()
        if response.getheader('Content-Encoding','identity').lower()!='identity':
            raise ValueError('Compressed responses not supported')
        size=response.getheader('Content-Length')
        if size is not None and (not size.isdecimal() or int(size)>MAX_RAW_BYTES):
            raise ValueError('Invalid or oversized Content-Length')
        if status!=200:
            raise ValueError(f'HTTP {status}: redirect or non-success refused')
        if mime not in SAFE_MIMES:
            raise ValueError(f'Unsupported text MIME: {mime}')
        body=response.read(MAX_RAW_BYTES+1)
        if not body or len(body)>MAX_RAW_BYTES or b'\x00' in body:
            raise ValueError('Empty, oversized or binary response')
        return status,mime,body
    finally:
        conn.close()


def extracted_text(mime: str, body: bytes) -> str:
    try:
        text=body.decode('utf-8-sig','strict')
    except UnicodeDecodeError as exc:
        raise ValueError('UTF-8 content required') from exc
    if mime=='text/html':
        parser=_HTMLText()
        parser.feed(text)
        text='\n'.join(line.strip() for line in ''.join(parser.parts).splitlines() if line.strip())
    if not text.strip() or len(text.encode('utf8'))>MAX_RAW_BYTES:
        raise ValueError('Extracted text empty or too large')
    return text


def fetch(case: Path,url: str,*,allowed_hosts: list[str],title: str,
          publisher: str='unverified',source_type: str='web_page',timeout: int=8) -> dict:
    if not (1 <= timeout <= 20):
        raise ValueError('Timeout must be 1-20 seconds')
    if not research.audit(case)['passed']:
        raise ValueError('Research audit failed before fetch')
    host,path=validate_url(url,allowed_hosts)
    ip=public_ips(host)[0]
    status,mime,raw=request(host,path,ip,timeout)
    # Recheck substituted transport results; inputs are untrusted.
    if status!=200 or mime not in SAFE_MIMES or not raw or len(raw)>MAX_RAW_BYTES or b'\x00' in raw:
        raise ValueError('HTTP response rejected: status, MIME, size or binary content')
    text=extracted_text(mime,raw)
    sha=hashlib.sha256(raw).hexdigest()
    rawpath=case/'research'/'raw'/(sha+'.bin')
    rawpath.parent.mkdir(parents=True,exist_ok=True)
    if ((case/'research').is_symlink() or rawpath.parent.is_symlink()
            or not rawpath.parent.resolve().is_relative_to(case.resolve()) or rawpath.is_symlink()):
        raise ValueError('Unsafe research storage')
    if rawpath.exists():
        if rawpath.read_bytes()!=raw:
            raise ValueError('Raw source digest collision or modification')
    else:
        with rawpath.open('xb') as fp:
            fp.write(raw)
            fp.flush()
    with tempfile.TemporaryDirectory() as tmp:
        source=Path(tmp)/'extracted.txt'
        source.write_text(text,encoding='utf8')
        result=research.import_file(case,source,title=title,locator=url,
            source_type=source_type,publisher=publisher,
            capture_info={'raw_sha256':sha,'raw_content_type':mime,
                          'http_status':status,
                          'retrieval_policy':'exact-host-pinned-public-https-v1'})
    return {**result,'url':url,'raw_sha256':sha,
            'publisher_verified':False,'transport':'pinned-public-https',
            'permissions':'explicit_public_fetch_only'}
