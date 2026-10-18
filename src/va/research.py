"""Operator-mediated research execution: evidence snapshots, exact excerpts, review drafts.

This module neither browses the web nor makes factual judgments. It stores one
source file locally, checks excerpts against that source, and maintains lineage.
Imported content is untrusted data and is never interpreted as instructions.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

from . import core, ledger, change_model

MAX_SOURCE_BYTES = 512 * 1024
ALLOWED_SUFFIXES = {'.txt', '.md', '.csv', '.tsv'}


def _digest(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def _snapshot_path(case: Path, sha: str) -> Path:
    if len(sha) != 64 or any(c not in '0123456789abcdef' for c in sha):
        raise ValueError('Invalid source snapshot digest')
    return case / 'research' / 'snapshots' / (sha + '.txt')


def _records(case: Path, name: str) -> list[dict]:
    return core.read_json(case / (name + '.json'))


def _registered_source(case: Path, ident: str) -> dict:
    src = next((x for x in _records(case, 'sources') if x['id'] == ident), None)
    if not src:
        raise ValueError('Source ID not found in this engagement')
    return src


def _captured_text(case: Path, src: dict) -> str:
    if 'snapshot_sha256' not in src:
        raise ValueError('Source was registered without a captured text snapshot')
    path = _snapshot_path(case, src['snapshot_sha256'])
    # No symlink traversal through material created outside the controlled flow.
    if path.is_symlink() or not path.is_file():
        raise ValueError(f'Missing or unsafe source snapshot: {src["id"]}')
    raw = path.read_bytes()
    if len(raw) > MAX_SOURCE_BYTES or _digest(raw) != src['snapshot_sha256']:
        raise ValueError(f'Corrupted source snapshot: {src["id"]}')
    try:
        return raw.decode('utf-8')
    except UnicodeDecodeError as exc:
        raise ValueError(f'Snapshot is no longer UTF-8: {src["id"]}') from exc


def import_file(case: Path, filename: Path, *, title: str, locator: str,
                source_type: str = 'document', publisher: str = 'unverified',
                published_at: str | None = None) -> dict:
    """Capture user-authorized UTF-8 text. URL is an identifier, not a fetch command."""
    if not title.strip() or not locator.strip() or not source_type.strip():
        raise ValueError('Source title, locator and source type required')
    if not publisher.strip():
        raise ValueError('Publisher must be specified or marked unverified')
    filename = Path(filename)
    if filename.is_symlink() or not filename.is_file() or filename.suffix.lower() not in ALLOWED_SUFFIXES:
        raise ValueError('Source must be a regular .txt/.md/.csv/.tsv file, not a symlink')
    if filename.stat().st_size > MAX_SOURCE_BYTES:
        raise ValueError('Source exceeds 512 KiB limit')
    raw = filename.read_bytes()
    if not raw.strip() or len(raw) > MAX_SOURCE_BYTES or b'\x00' in raw:
        raise ValueError('Source empty, oversized, or not plain text')
    try:
        raw.decode('utf-8')
    except UnicodeDecodeError as exc:
        raise ValueError('Source must be UTF-8 text') from exc
    audit = ledger.verify(case)
    if not audit['passed']:
        raise ValueError('Engagement journal integrity check failed')
    sha = _digest(raw)
    same_locator = [s for s in _records(case, 'sources') if s.get('locator') == locator and 'snapshot_sha256' in s]
    for old in same_locator:
        if old['snapshot_sha256'] == sha:
            return {'source_id': old['id'], 'snapshot_sha256': sha, 'created': False,
                    'possible_changes': [], 'note': 'Identical snapshot already captured for this locator'}
    dest = _snapshot_path(case, sha)
    dest.parent.mkdir(parents=True, exist_ok=True)
    if (case / 'research').is_symlink() or dest.parent.is_symlink() or not dest.parent.resolve().is_relative_to(case.resolve()):
        raise ValueError('Snapshot storage must remain within the engagement')
    if dest.exists() and dest.read_bytes() != raw:
        raise ValueError('Digest collision or mismatching source snapshot')
    if not dest.exists():
        # Exclusive creation. A failure to journal may leave an unreferenced, private snapshot.
        with dest.open('xb') as f:
            f.write(raw)
            f.flush()
            os.fsync(f.fileno())
    rec = core.append_record(case, 'sources', {
        'title': title.strip(), 'locator': locator.strip(), 'source_type': source_type.strip(),
        'publisher': publisher.strip(), 'published_at': published_at,
        'accessed_at': core.now(), 'independent_verification': 'not_verified',
        'permissions': 'operator_supplied_rights_review_needed',
        'snapshot_sha256': sha, 'snapshot_relative_path': str(dest.relative_to(case)),
        'snapshot_bytes': len(raw), 'notes': 'Captured by operator; authenticity and accuracy unverified',
    })
    changes = []
    for old in same_locator:
        if old['snapshot_sha256'] != sha:
            changes.append({'previous_source_id': old['id'],
                            'previous_sha256': old['snapshot_sha256'],
                            'downstream_to_review': change_model.impacted(case, old['id'])['downstream']})
    return {'source_id': rec['id'], 'snapshot_sha256': sha, 'created': True,
            'possible_changes': changes,
            'note': 'Same locator may refer to a revised source; compare content manually before updating claims'}


def add_excerpt_claim(case: Path, source_id: str, statement: str, excerpt: str) -> dict:
    """Allow operator interpretation only when its quotation is present in captured data."""
    src = _registered_source(case, source_id)
    material = _captured_text(case, src)
    if not statement.strip() or not excerpt.strip() or len(excerpt) > 600:
        raise ValueError('Nonempty statement and excerpt up to 600 characters are required')
    if excerpt not in material:
        raise ValueError('Exact excerpt not found in captured source text')
    claim = core.append_record(case, 'claims', {
        'statement': statement.strip(), 'source_ids': [source_id],
        'direct_excerpt': excerpt, 'snapshot_sha256': src['snapshot_sha256'],
        'claim_type': 'operator_interpretation', 'status': 'unknown', 'confidence': 'unrated',
        'counterevidence_ids': [], 'falsification_test': '', 'last_reviewed_at': None,
        'independent_verification': 'not_verified',
    })
    return {'claim_id': claim['id'], 'source_id': source_id,
            'exact_excerpt_matched': True, 'claim_validated_as_true': False}


def audit(case: Path) -> dict:
    journal = ledger.verify(case)
    errors = list(journal['errors'])
    captured = {s['id']: s for s in _records(case, 'sources') if 'snapshot_sha256' in s}
    checked_quotes = 0
    for sid, src in captured.items():
        try:
            _captured_text(case, src)
        except ValueError as exc:
            errors.append(str(exc))
    for claim in _records(case, 'claims'):
        if 'direct_excerpt' not in claim:
            continue
        refs = claim.get('source_ids', [])
        if len(refs) != 1 or refs[0] not in captured:
            errors.append(f'{claim["id"]}: excerpt claim has no captured source')
            continue
        src = captured[refs[0]]
        if claim.get('snapshot_sha256') != src['snapshot_sha256']:
            errors.append(f'{claim["id"]}: snapshot digest differs from source')
            continue
        try:
            if claim['direct_excerpt'] not in _captured_text(case, src):
                errors.append(f'{claim["id"]}: excerpt absent from captured source')
            else:
                checked_quotes += 1
        except ValueError as exc:
            errors.append(str(exc))
    # A new capture with the same locator is only a possible update, not proof
    # of supersession. Identify artifacts relying on an older capture.
    latest_locator = {src['locator']: src['id'] for src in captured.values()}
    older = {sid for sid, src in captured.items() if latest_locator[src['locator']] != sid}
    stale_candidates = []
    for art in _records(case, 'artifacts'):
        if art.get('kind') != 'research-evidence':
            continue
        artifact_path = case / 'deliverables' / f'research-evidence-{art["sha256"][:16]}.md'
        if (art.get('path') != str(artifact_path.relative_to(case))
                or artifact_path.is_symlink() or not artifact_path.is_file()
                or _digest(artifact_path.read_bytes()) != art['sha256']):
            errors.append(f'{art["id"]}: artifact snapshot missing, moved or altered')
        old_refs = sorted(older.intersection(art.get('source_ids', [])))
        if old_refs:
            stale_candidates.append({'artifact_id': art['id'], 'older_source_ids': old_refs,
                                     'status': 'requires_review_not_automatically_superseded'})
    return {'passed': not errors, 'errors': errors, 'captured_sources': len(captured),
            'matched_excerpt_claims': checked_quotes,
            'independent_factual_verification': False, 'stale_candidate_artifacts': stale_candidates}


def _clean(value: object) -> str:
    return ' '.join(str(value).replace('\x00', '').split())


def brief(case: Path, *, question: str = '', save: bool = True) -> dict:
    """Write an immutable evidence register, not an AI-authored analytical conclusion."""
    check = audit(case)
    if not check['passed']:
        raise ValueError('Research audit failed: ' + '; '.join(check['errors']))
    engagement = core.read_json(case / 'engagement.json')
    sources = _records(case, 'sources')
    claims = _records(case, 'claims')
    captured = {s['id']: s for s in sources if 'snapshot_sha256' in s}
    linked = [cl for cl in claims if 'direct_excerpt' in cl and cl.get('source_ids') and cl['source_ids'][0] in captured]
    if not linked:
        raise ValueError('At least one exact-excerpt claim is needed for a research brief')
    q = question.strip() or engagement.get('objective', '')
    if not q.strip():
        raise ValueError('Research question or engagement objective required')
    evidence_version = _digest(ledger.canonical({'sources': list(captured.values()), 'claims': linked}))
    lines = [f'# {_clean(engagement["name"])}: research evidence brief', '',
             '**Working draft. Excerpts match captured files, but the sources and interpretations have not been independently verified.**', '',
             '**Question:** ' + _clean(q), '', '## Observations and interpretations', '']
    for claim in linked:
        sid = claim['source_ids'][0]
        src = captured[sid]
        lines += [f'### {claim["id"]} | {sid}', '',
                  f'**Interpretation (unverified):** {_clean(claim["statement"])}', '',
                  '**Exact excerpt from captured text:**', '']
        lines += ['> ' + segment for segment in claim['direct_excerpt'].splitlines()]
        lines += ['', f'**Source:** {_clean(src["title"])} | {_clean(src["locator"])}',
                  f'**Snapshot SHA-256:** `{src["snapshot_sha256"]}`', '']
    uncaptured = [c['id'] for c in claims if c not in linked]
    latest_locator = {src['locator']: src['id'] for src in captured.values()}
    older = [src for src in captured.values() if latest_locator[src['locator']] != src['id']]
    if older:
        lines += ['## Possible source revisions', '',
                  'Sources using the same locator have different snapshots. They may represent changes; reconcile their claims before relying on this draft.', '']
        for src in older:
            lines += [f'- {src["id"]} may be an earlier snapshot of {latest_locator[src["locator"]]}.', '']
    lines += ['## Gaps and independent review', '',
              '- No causal conclusion, market-size calculation, or commercial recommendation has been established by this document.',
              '- Review source origin, publication date, completeness, permissions, conflicting evidence, and interpretation.',
              '- Decide what research or specialist review should follow.',
              f'- Other claims not backed by a captured exact excerpt: {", ".join(uncaptured) or "none"}.',
              '', '## Source register', '']
    for src in captured.values():
        lines += [f'- **{src["id"]}** {_clean(src["title"])}: {_clean(src["locator"])} | '
                  f'captured {src["accessed_at"]} | `{src["snapshot_sha256"]}` | source authenticity not verified']
    lines += ['', f'Evidence record version: `{evidence_version}`', '',
              'No human review or publication approval is implied.', '']
    output = '\n'.join(lines)
    digest = _digest(output.encode('utf-8'))
    relative = Path('deliverables') / f'research-evidence-{digest[:16]}.md'
    dest = case / relative
    if not save:
        return {'preview': output, 'sha256': digest, 'evidence_version': evidence_version, 'source_ids': list(captured),
                'claim_ids': [cl['id'] for cl in linked], 'status': 'review_required'}
    if dest.exists() and dest.read_text(encoding='utf-8') != output:
        raise ValueError('Existing brief differs from its content hash')
    if not dest.exists():
        with dest.open('x', encoding='utf-8') as f:
            f.write(output)
    for art in _records(case, 'artifacts'):
        if art.get('kind') == 'research-evidence' and art.get('sha256') == digest:
            return {'artifact_id': art['id'], 'path': str(dest), 'created': False,
                    'sha256': digest, 'status': 'draft_review_required'}
    art = core.append_record(case, 'artifacts', {
        'kind': 'research-evidence', 'path': str(relative), 'sha256': digest,
        'status': 'draft_review_required', 'claim_ids': [cl['id'] for cl in linked],
        'source_ids': list(captured), 'source_snapshot_hashes': {sid:src['snapshot_sha256'] for sid,src in captured.items()},
        'publication_authorized': False, 'evidence_version': evidence_version,
    })
    return {'artifact_id': art['id'], 'path': str(dest), 'created': True,
            'sha256': digest, 'status': 'draft_review_required'}
