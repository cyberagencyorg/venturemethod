"""Explicit framework selection from sourced, versioned metadata.

This is a deterministic decision-support filter, not an agent, expert opinion,
or empirical assurance of method fitness. It never silently chooses a winner.
"""
from __future__ import annotations
import json
from pathlib import Path
from .core import ROOT

EVIDENCE = ('minimal', 'provisional', 'observed', 'verified')
GOALS = (
    'discover_need', 'map_market', 'choose_strategy', 'design_business',
    'prioritize', 'test_uncertainty', 'plan_delivery', 'transform_org',
    'allocate_capital', 'measure_outcomes', 'resolve_systemic',
    'understand_futures',
)


def load_catalog(path: Path | None = None) -> list[dict]:
    raw=json.loads((path or ROOT / 'config' / 'frameworks-v3.json').read_text(encoding='utf-8'))
    if raw.get('schema_version') != '0.3' or not isinstance(raw.get('items'), list):
        raise ValueError('Unsupported framework catalog')
    ids=set()
    for entry in raw['items']:
        for key in ('id','title','goals','minimum_evidence','fit','avoid','output','source','kind','cadence','verified_in_runtime'):
            if key not in entry: raise ValueError(f'Method record missing {key}')
        if entry['id'] in ids: raise ValueError('Duplicate method ID')
        if set(entry['goals'])-set(GOALS) or not entry['goals']: raise ValueError('Unknown or empty method goals')
        if entry['minimum_evidence'] not in EVIDENCE: raise ValueError('Unknown evidence class')
        if not entry['source'].startswith('https://'): raise ValueError('Method source must use HTTPS')
        if entry['verified_in_runtime'] is not False:
            raise ValueError('v0.3 catalog may not assert verified method execution')
        ids.add(entry['id'])
    return raw['items']


def compare(goal: str, evidence: str='minimal', *, catalog: list[dict] | None = None) -> dict:
    if goal not in GOALS: raise ValueError(f'Invalid goal; choose from {GOALS}')
    if evidence not in EVIDENCE: raise ValueError(f'Invalid evidence class; choose from {EVIDENCE}')
    candidates=[]
    for m in (catalog if catalog is not None else load_catalog()):
        if goal not in m['goals']: continue
        ready = EVIDENCE.index(evidence)>=EVIDENCE.index(m['minimum_evidence'])
        candidates.append({
            'id':m['id'], 'title':m['title'], 'readiness':'explore/apply' if ready else 'collect_inputs_first',
            'required_evidence':m['minimum_evidence'], 'fit':m['fit'], 'avoid':m['avoid'],
            'expected_output':m['output'], 'reference':m['source'],
            'runtime_validated':False,
        })
    return {'goal':goal,'available_evidence':evidence,'candidate_count':len(candidates),
            'candidates':sorted(candidates,key=lambda x:(x['readiness']!='explore/apply',x['id'])),
            'selection':'no automatic winner; compare prerequisites and failure modes',
            'warning':'These are library metadata and original selection cautions, not tested expert recommendations.'}
