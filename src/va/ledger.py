"""Local, tamper-evident event journal and record projections.

The hash chain detects changes relative to its recorded head. It does not prove
an author's identity or prevent an adversary with write access from rewriting it.
Single-writer local CLI assumption; external concurrency requires a database.
"""
from __future__ import annotations
import hashlib
import json
import os
from pathlib import Path
from typing import Any

COLLECTIONS = ('sources', 'claims', 'decisions', 'hypotheses', 'options',
               'actions', 'outcomes', 'experiments', 'artifacts', 'risks', 'entities',
               'engagement_changes', 'reviews')
PREFIX = dict(sources='SRC', claims='CLM', decisions='DEC', hypotheses='HYP',
              options='OPT', actions='ACT', outcomes='OUT', experiments='EXP',
              artifacts='ART', risks='RISK', entities='ENT', engagement_changes='CHG', reviews='REV')


def canonical(obj: Any) -> bytes:
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode('utf-8')


def read_log(case: Path) -> list[dict[str, Any]]:
    p = case / 'events.jsonl'
    if not p.exists():
        return []
    events = []
    for number, line in enumerate(p.read_text(encoding='utf8').splitlines(), 1):
        if not line.strip():
            raise ValueError(f'Empty event journal line {number}')
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f'Invalid journal line {number}') from exc
        events.append(event)
    return events


def digest(event_without_hash: dict[str, Any]) -> str:
    return hashlib.sha256(canonical(event_without_hash)).hexdigest()


def verify(case: Path, check_projections: bool = True) -> dict[str, Any]:
    errors = []
    try:
        events = read_log(case)
    except ValueError as exc:
        return {'passed': False, 'events': 0, 'errors': [str(exc)], 'head': None}
    previous = 'GENESIS'
    projections = {name: [] for name in COLLECTIONS}
    seen = set()
    for n, event in enumerate(events, 1):
        try:
            payload = {k: v for k, v in event.items() if k != 'hash'}
            if event.get('seq') != n or event.get('prev_hash') != previous or event.get('hash') != digest(payload):
                errors.append(f'Event {n}: sequence or hash chain mismatch')
            col, record = event['collection'], event['record']
            if col not in COLLECTIONS or not isinstance(record, dict):
                errors.append(f'Event {n}: invalid collection or record')
            else:
                identity = (col, record.get('id'))
                if identity in seen: errors.append(f'Event {n}: duplicate record ID')
                seen.add(identity)
                projections[col].append(record)
            previous = event.get('hash', '')
        except (KeyError, TypeError, AttributeError):
            errors.append(f'Event {n}: malformed event')
    if check_projections and (case / 'events.jsonl').exists():
        for name, records in projections.items():
            p = case / (name + '.json')
            try:
                actual = json.loads(p.read_text(encoding='utf8'))
                if canonical(actual) != canonical(records):
                    errors.append(f'{name}.json projection differs from journal')
            except (FileNotFoundError, json.JSONDecodeError):
                errors.append(f'{name}.json projection missing or unreadable')
    return {'passed': not errors, 'events': len(events), 'errors': errors,
            'head': previous if events else None}


def append(case: Path, collection: str, record: dict[str, Any]) -> None:
    if collection not in COLLECTIONS:
        raise ValueError('Unknown collection')
    integrity = verify(case)
    if not integrity['passed']:
        raise ValueError('Journal integrity failed: ' + '; '.join(integrity['errors']))
    events = read_log(case)
    body = {'seq': len(events) + 1, 'prev_hash': integrity['head'] or 'GENESIS',
            'collection': collection, 'record': record}
    event = {**body, 'hash': digest(body)}
    with (case / 'events.jsonl').open('a', encoding='utf8') as out:
        out.write(canonical(event).decode('utf8') + '\n')
        out.flush()
        os.fsync(out.fileno())
    # Projection may fail after event append. `repair` reconstructs it from valid journal.
    p = case / (collection + '.json')
    try:
        old = json.loads(p.read_text(encoding='utf8'))
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        raise ValueError(f'Projection unavailable after committed event; repair required: {p}') from exc
    write_atomic(p, [*old, record])


def write_atomic(path: Path, data: Any) -> None:
    p = path.with_name(path.name + '.tmp')
    try:
        p.write_bytes(json.dumps(data, indent=2, ensure_ascii=False).encode('utf8') + b'\n')
        os.replace(p, path)
    finally:
        p.unlink(missing_ok=True)


def repair(case: Path) -> dict[str, Any]:
    integrity = verify(case, check_projections=False)
    if not integrity['passed']:
        raise ValueError('Refusing to repair from invalid journal')
    projections = {name: [] for name in COLLECTIONS}
    for event in read_log(case):
        projections[event['collection']].append(event['record'])
    for name, records in projections.items():
        write_atomic(case / (name + '.json'), records)
    return verify(case)
