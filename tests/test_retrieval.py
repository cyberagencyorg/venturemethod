"""Retrieval has no live network during CI: explicit fake DNS and transport."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from src.va import core,research,retrieval

URL='https://public.example.org/report'
class RetrievalTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        with patch.object(core,'ENGAGEMENT_ROOT',Path(self.tmp.name)):
            self.case=core.new_engagement('Controlled public source case','company','other','quick')
        core.update_engagement(self.case,objective='Check whether demand supports a pilot')

    def get(self,body=b'The report says demand rose 12%.',mime='text/plain',status=200):
        with patch.object(retrieval,'public_ips',return_value=['93.184.216.34']) as dns,\
             patch.object(retrieval,'request',return_value=(status,mime,body)) as network:
            result=retrieval.fetch(self.case,URL,allowed_hosts=['public.example.org'],
                                   title='Test bulletin',publisher='Unverified')
            dns.assert_called_once_with('public.example.org')
            network.assert_called_once_with('public.example.org','/report','93.184.216.34',8)
            return result

    def test_snapshot_exact_quote_and_idempotency(self):
        src=self.get()
        self.assertTrue(src['created'])
        r=research.add_excerpt_claim(self.case,src['source_id'],'Report suggests a change','demand rose 12%')
        self.assertFalse(r['claim_validated_as_true'])
        self.assertTrue(research.audit(self.case)['passed'])
        self.assertIn(src['source_id'],Path(research.brief(self.case)['path']).read_text())
        self.assertFalse(self.get()['created'])

    def test_html_text_excludes_scripts(self):
        src=self.get(mime='text/html',
                     body=b'<html><script>fictional data</script><p>Observed five buyers</p></html>')
        research.add_excerpt_claim(self.case,src['source_id'],'Source mentions buyers','Observed five buyers')
        with self.assertRaises(ValueError):
            research.add_excerpt_claim(self.case,src['source_id'],'Bad','fictional data')

    def test_revision_marks_old_artifact_candidate(self):
        src=self.get()
        research.add_excerpt_claim(self.case,src['source_id'],'Changed demand','demand rose 12%')
        old=research.brief(self.case)
        newer=self.get(body=b'Updated report: demand was flat.')
        self.assertNotEqual(src['source_id'],newer['source_id'])
        self.assertTrue(newer['possible_changes'])
        self.assertTrue(Path(old['path']).exists())
        self.assertTrue(research.audit(self.case)['stale_candidate_artifacts'])

    def test_raw_byte_corruption_rejected(self):
        src=self.get()
        raw=self.case/'research'/'raw'/(src['raw_sha256']+'.bin')
        raw.write_bytes(b'altered')
        self.assertFalse(research.audit(self.case)['passed'])
        with self.assertRaises(ValueError):
            self.get()

    def test_url_refusal_is_strict(self):
        bad=['http://public.example.org/report','https://127.0.0.1/report',
             'https://localhost/report','https://user:pass@public.example.org/report',
             'https://public.example.org:8080/report','https://other.example.org/report',
             'https://public.example.org.attacker.org/report','https://public.example.org/a#fragment']
        for url in bad:
            with self.subTest(url=url),self.assertRaises(ValueError):
                retrieval.validate_url(url,['public.example.org'])
        with self.assertRaises(ValueError):
            retrieval.validate_url(URL,['*.example.org'])

    def test_mixed_dns_addresses_rejected(self):
        answers=[(None,None,None,None,('93.184.216.34',443)),
                 (None,None,None,None,('127.0.0.1',443))]
        with patch.object(retrieval.socket,'getaddrinfo',return_value=answers):
            with self.assertRaises(ValueError):
                retrieval.public_ips('public.example.org')

    def test_dns_failure_halts_before_transport(self):
        with patch.object(retrieval,'public_ips',side_effect=ValueError('private')) as dns,\
             patch.object(retrieval,'request') as request:
            with self.assertRaises(ValueError):
                retrieval.fetch(self.case,URL,allowed_hosts=['public.example.org'],title='x')
            dns.assert_called_once()
            request.assert_not_called()

    def test_untrusted_status_mime_and_body_checked(self):
        for status,mime,raw in [(302,'text/plain',b'redirect'),(200,'application/pdf',b'pdf'),
                               (200,'text/plain',b''),(200,'text/plain',b'\xff'),
                               (200,'text/plain',b'x'*(retrieval.MAX_RAW_BYTES+1))]:
            with self.subTest(status=status,mime=mime),self.assertRaises(ValueError):
                self.get(status=status,mime=mime,body=raw)
        self.assertEqual(core.read_json(self.case/'sources.json'),[])

    def test_request_transport_rejects_compression_before_read(self):
        class Response:
            status=200
            def getheader(self,k,default=''):
                return {'Content-Type':'text/plain','Content-Encoding':'gzip'}.get(k,default)
            def read(self,size): raise AssertionError('should not read')
        class Connection:
            def __init__(self,*args,**kwargs): pass
            def request(self,*args,**kwargs): pass
            def getresponse(self): return Response()
            def close(self): pass
        with patch.object(retrieval,'PinnedTLS',Connection):
            with self.assertRaisesRegex(ValueError,'Compressed'):
                retrieval.request('public.example.org','/report','93.184.216.34',8)

    def test_source_unverified_even_when_tls_fetch_passes(self):
        self.get()
        r=core.read_json(self.case/'sources.json')[0]
        self.assertEqual(r['independent_verification'],'not_verified')
        self.assertEqual(r['http_status'],200)

if __name__=='__main__': unittest.main()
