"""Local draft claim revision and downstream impact inspection.

Not a merge engine, authenticated approval system, or multi-user concurrency layer.
Old records and decisions remain unchanged until an authorized workflow handles them.
"""
from __future__ import annotations
from pathlib import Path
from .core import read_json, require_references, append_record
from . import ledger

LINK_FIELDS=('source_ids','claim_ids','counterevidence_ids','decision_id','action_id',
             'target_id','supersedes_id','entity_ids','hypothesis_ids','option_ids')

def record_lookup(case:Path) -> dict[str,tuple[str,dict]]:
    result={}
    for col in ledger.COLLECTIONS:
        for item in read_json(case/(col+'.json')):
            result[item['id']]=(col,item)
    return result

def impacted(case:Path, target_id:str) -> dict:
    records=record_lookup(case)
    if target_id not in records: raise ValueError('Unknown target in this engagement')
    impacted_records=[]
    visited={target_id}
    frontier=[target_id]
    while frontier:
        t=frontier.pop(0)
        for ident,(col,item) in records.items():
            if ident in visited: continue
            references=[]
            for field in LINK_FIELDS:
                r=item.get(field,[])
                if (t in r if isinstance(r,list) else r==t): references.append(field)
            if references:
                impacted_records.append({'id':ident,'collection':col,'via':t,
                                         'fields':references,'action':'review_needed_not_auto_rewritten'})
                visited.add(ident)
                frontier.append(ident)
    return {'engagement':case.name, 'target':target_id, 'downstream':impacted_records,
            'note':'Dependency traversal is conservative and only covers recorded explicit links. No publication or approval occurs.'}

def propose_claim_revision(case:Path, claim_id:str, statement:str, rationale:str, source_ids:list[str]) -> dict:
    require_references(case,'claims',[claim_id]);require_references(case,'sources',source_ids)
    if not statement.strip() or not rationale.strip(): raise ValueError('Nonempty new statement and rationale required')
    claims=read_json(case/'claims.json')
    old=next(x for x in claims if x['id']==claim_id)
    if any(x.get('supersedes_id')==claim_id for x in claims):
        raise ValueError('Competing successor exists. Review lineage before another draft revision.')
    new=append_record(case,'claims',{
        'statement':statement, 'source_ids':source_ids, 'confidence':'unrated',
        'status':'unknown', 'claim_type':'unclassified', 'counterevidence_ids':[],
        'falsification_test':'', 'last_reviewed_at':None,
        'supersedes_id':claim_id, 'revision_status':'proposed_unapproved',
        'revision_rationale':rationale,
    })
    return {'new_claim':new['id'],'supersedes':claim_id,'prior_statement':old['statement'],
            'revision_status':'proposed_unapproved','impact_on_predecessor':impacted(case,claim_id),
            'note':'Existing decisions still cite the earlier claim. No implicit approval or replacement.'}
