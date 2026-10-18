"""Prepare paired skill evaluations; report human scores without inventing agent runs."""
from __future__ import annotations
import json
from pathlib import Path
from typing import Any
from .core import ROOT, slugify, skill_metadata
from .ledger import write_atomic

DIMENSIONS = ('selection','accuracy','task_usefulness','method_fidelity',
              'traceability','privacy_authority','efficiency')


def prepare(skill: str, workspace: Path) -> dict[str, Any]:
    skill = slugify(skill)
    skill_path = ROOT / 'skills' / skill
    skill_metadata(skill_path)
    fixture = json.loads((ROOT / 'evals' / (skill + '.json')).read_text(encoding='utf8'))
    if fixture.get('skill') != skill or len(fixture.get('tests',[])) < 3:
        raise ValueError('Invalid or insufficient eval fixture')
    if workspace.exists() and any(workspace.iterdir()):
        raise ValueError('Evaluation workspace must be empty to prevent accidental overwrite')
    workspace.mkdir(parents=True,exist_ok=True)
    for branch in ('baseline','candidate'):
        (workspace / branch).mkdir()
    manifest = {'skill': skill, 'skill_path': str(skill_path),
                'status': 'pending_independent_agent_runs',
                'baseline': 'Same task WITHOUT skill (new skill) or with previous pinned skill version (revision)',
                'candidate': 'Same task with current skill; each case must run with isolated context',
                'dimensions': list(DIMENSIONS), 'tests':fixture['tests'],
                'instructions': 'Place one named <case>.md per branch; reviewer fills blinded scorecard. No scores are generated automatically.'}
    write_atomic(workspace/'manifest.json', manifest)
    template = {'reviewer': None, 'blind_review': False,
                'ratings': {branch: {t['case']: {d: None for d in DIMENSIONS}
                                   for t in fixture['tests']} for branch in ('baseline','candidate')},
                'notes': [], 'run_metadata': {}, 'approval': 'not_granted'}
    write_atomic(workspace/'review.json', template)
    return {'workspace': str(workspace), 'cases':len(fixture['tests']),
            'status':manifest['status'], 'skill':skill}


def summarize(workspace: Path) -> dict[str, Any]:
    manifest=json.loads((workspace/'manifest.json').read_text(encoding='utf8'))
    review=json.loads((workspace/'review.json').read_text(encoding='utf8'))
    cases=[t['case'] for t in manifest['tests']]
    gaps=[]; totals={}
    for branch in ('baseline','candidate'):
        numbers=[]
        for case in cases:
            output=workspace/branch/(case+'.md')
            if not output.is_file() or not output.read_text(encoding='utf8').strip():
                gaps.append(f'{branch}/{case}.md missing')
            score=review['ratings'][branch][case]
            for dim in DIMENSIONS:
                value=score.get(dim)
                if not isinstance(value,int) or isinstance(value,bool) or not 0<=value<=4:
                    gaps.append(f'{branch}/{case} {dim} rating missing or invalid')
                else: numbers.append(value)
        totals[branch] = round(sum(numbers)/len(numbers), 3) if numbers and len(numbers)==len(cases)*len(DIMENSIONS) else None
    if not review.get('reviewer') or not review.get('blind_review'):
        gaps.append('named reviewer and blind_review=true required for comparative grading')
    done=not gaps
    result={'skill':manifest['skill'], 'status':'review-complete' if done else 'incomplete',
            'baseline_average':totals['baseline'], 'candidate_average':totals['candidate'],
            'difference':round(totals['candidate']-totals['baseline'],3) if done else None,
            'missing':gaps, 'authorization':'none; review does not automatically promote or install skills',
            'limitations':['Scores reflect reviewer judgments, not verified factual correctness',
                'No independent agent executions or token/time costs are inferred from these files']}
    write_atomic(workspace/'summary.json',result)
    return result
