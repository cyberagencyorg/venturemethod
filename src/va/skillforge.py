"""Passive third-party skill candidate catalog. No fetching, installation or running."""
from __future__ import annotations
import json
import re
from pathlib import Path
from urllib.parse import urlparse
from .core import ROOT, now
from .ledger import write_atomic

FILE = ROOT / 'config' / 'external-skills.json'
APPROX_PERMISSIVE = {'MIT','Apache-2.0','BSD-2-Clause','BSD-3-Clause','ISC','CC0-1.0'}


def list_candidates() -> list[dict]:
    return json.loads(FILE.read_text(encoding='utf8'))['candidates']


def register_candidate(name: str, upstream: str, commit: str, license_id: str,
                       rationale: str) -> dict:
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', name) or len(name) > 64:
        raise ValueError('Skill name must be a valid Agent Skills slug')
    u = urlparse(upstream)
    if u.scheme != 'https' or not u.hostname or u.username or u.password:
        raise ValueError('A public HTTPS upstream URL without credentials is required')
    if not re.fullmatch(r'[a-fA-F0-9]{40}', commit):
        raise ValueError('An exact 40-character upstream Git commit is required')
    if not rationale.strip(): raise ValueError('State the capability gap')
    registry = json.loads(FILE.read_text(encoding='utf8'))
    if any(x['name'] == name for x in registry['candidates']):
        raise ValueError('Candidate already exists; review before revision')
    status = 'license-review-required' if license_id not in APPROX_PERMISSIVE else 'security-review-required'
    candidate = {'name': name, 'upstream': upstream, 'commit': commit.lower(),
                 'claimed_license': license_id, 'license_verified': False,
                 'execution_reviewed': False, 'scripts_reviewed': False,
                 'data_permissions_reviewed': False, 'provenance_reviewed': False,
                 'evaluation_passed': False, 'approved_by': None,
                 'rationale': rationale, 'review_date': now(), 'status': status,
                 'eligible_for_execution': False}
    registry['candidates'].append(candidate)
    write_atomic(FILE, registry)
    return candidate
