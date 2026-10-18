"""Prepare blinded manual research report comparisons. Never self-grade."""
from __future__ import annotations
import hashlib
import json
from pathlib import Path
import secrets
from . import research
from .ledger import write_atomic

DIMENSIONS=('source_fidelity','reasoning','alternative_analysis','decision_usefulness',
            'uncertainty_handling','quantitative_rigor','practicality')
MAX_DOCUMENT=256*1024


def _read(path: Path) -> bytes:
    if path.is_symlink() or not path.is_file() or path.stat().st_size>MAX_DOCUMENT:
        raise ValueError('Benchmark inputs must be regular files <=256 KiB')
    raw=path.read_bytes()
    if not raw.strip() or len(raw)>MAX_DOCUMENT or b'\x00' in raw:
        raise ValueError('Benchmark needs nonempty plain-text reports')
    try:
        raw.decode('utf8')
    except UnicodeDecodeError as exc:
        raise ValueError('Benchmark reports must be UTF-8') from exc
    return raw


def prepare(case: Path,*,baseline: Path,candidate: Path,question: str) -> dict:
    if not question.strip():
        raise ValueError('Specify the actual research question')
    if not research.audit(case)['passed']:
        raise ValueError('Engagement evidence integrity is not valid')
    initial,trial=_read(baseline),_read(candidate)
    if initial==trial:
        raise ValueError('Identical baseline and candidate cannot be compared')
    parent=case/'benchmarks'
    if parent.is_symlink():
        raise ValueError('Benchmark directory cannot be symlinked')
    directory=parent/('comparison-'+secrets.token_hex(8))
    directory.mkdir(parents=True,exist_ok=False)
    branches=['baseline','candidate']
    if secrets.randbelow(2):
        branches.reverse()
    mapping=dict(zip(('A','B'),branches))
    inputs={'baseline':initial,'candidate':trial}
    for letter,branch in mapping.items():
        (directory/(letter+'.md')).write_bytes(inputs[branch])
    write_atomic(directory/'key.json',{
        'question':question,'mapping':mapping,
        'hashes':{branch:hashlib.sha256(raw).hexdigest() for branch,raw in inputs.items()},
        'audit_at_preparation':research.audit(case),
        'status':'prepared_not_scored',
        'instructions':'Keep this file from the reviewer until both packets have been scored.'})
    write_atomic(directory/'review.json',{
        'question':question,'reviewer':None,'independent_reviewer':False,
        'reviewer_had_access_to_key':False,
        'ratings':{letter:{dim:None for dim in DIMENSIONS} for letter in ('A','B')},
        'justifications':{'A':'','B':''},'fact_check_notes':[],
        'observed_time_and_cost':{},'status':'pending_independent_review',
        'guidance':'Score 0-4. Justify each packet and cite serious factual failures.'})
    return {'workspace':str(directory),'reviewer_files':['A.md','B.md','review.json'],
            'status':'pending_independent_review'}


def summarize(workspace: Path) -> dict:
    if workspace.is_symlink() or not workspace.is_dir():
        raise ValueError('Invalid benchmark workspace')
    key=json.loads((workspace/'key.json').read_text(encoding='utf8'))
    review=json.loads((workspace/'review.json').read_text(encoding='utf8'))
    gaps=[]
    if (not review.get('reviewer') or not review.get('independent_reviewer')
            or review.get('reviewer_had_access_to_key')):
        gaps.append('Named independent reviewer who did not see key required')
    if review.get('question')!=key['question']:
        gaps.append('Question was modified after packet preparation')
    avg={}
    for label in ('A','B'):
        packet=workspace/(label+'.md')
        try:
            raw=_read(packet)
            if hashlib.sha256(raw).hexdigest()!=key['hashes'][key['mapping'][label]]:
                gaps.append(f'{label}: packet hash mismatch')
        except (ValueError,OSError):
            gaps.append(f'{label}: packet missing, altered, or unsafe')
        numbers=[]
        for dim in DIMENSIONS:
            value=review.get('ratings',{}).get(label,{}).get(dim)
            if type(value) is not int or not 0<=value<=4:
                gaps.append(f'{label}/{dim}: missing or invalid score')
            else:
                numbers.append(value)
        if len(numbers)==len(DIMENSIONS):
            avg[label]=round(sum(numbers)/len(numbers),3)
        if not review.get('justifications',{}).get(label,'').strip():
            gaps.append(f'{label}: no written reviewer justification')
    result={'status':'incomplete' if gaps else 'externally_scored_identity_unverified',
            'missing':gaps, 'baseline_average':None,'candidate_average':None,'difference':None,
            'limitations':['Review identity and independence cannot be authenticated by this CLI',
                           'Human scores do not establish factual truth',
                           'No model runs, research quality or costs are fabricated']}
    if not gaps:
        result['baseline_average']=avg[next(k for k,v in key['mapping'].items() if v=='baseline')]
        result['candidate_average']=avg[next(k for k,v in key['mapping'].items() if v=='candidate')]
        result['difference']=round(result['candidate_average']-result['baseline_average'],3)
    write_atomic(workspace/'summary.json',result)
    return result
