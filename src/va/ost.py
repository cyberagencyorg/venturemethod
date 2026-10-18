"""Local, single-writer, evidence-linked Opportunity Solution Tree workbench.

This is a draft analysis structure, not a validated customer discovery result.
Reviews have a self-asserted reviewer label; there is NO authentication, RBAC,
collaborative merge, or external publication approval.  The JSONL journal is
hash-linked against accidental edits, NOT cryptographically anchored.
"""
from __future__ import annotations
import json
import os
import hashlib
from pathlib import Path
from .core import now, read_json

TYPES = ('outcome', 'opportunity', 'solution', 'test')
PARENTS = {'opportunity': ('outcome', 'opportunity'), 'solution': ('opportunity',), 'test': ('solution',)}
OBSERVATIONAL = {'interview', 'customer_research', 'field_observation', 'user_research', 'customer_interview'}


def _digest(record: dict) -> str:
    return hashlib.sha256(json.dumps(record, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode('utf8')).hexdigest()


def _path(case: Path) -> Path:
    return case / 'discovery' / 'ost-events.jsonl'


def _events(case: Path) -> list[dict]:
    p = _path(case)
    if not p.exists(): return []
    lines = p.read_text(encoding='utf8').splitlines()
    if any(not x.strip() for x in lines): raise ValueError('Empty OST event line')
    try: return [json.loads(s) for s in lines]
    except json.JSONDecodeError as ex: raise ValueError('Unreadable OST event journal') from ex


def verify(case: Path) -> dict:
    try: events = _events(case)
    except ValueError as exc: return {'passed':False,'errors':[str(exc)],'events':0}
    prev='GENESIS'; errors=[]
    for i,e in enumerate(events,1):
        if (e.get('seq')!=i or e.get('previous')!=prev or e.get('hash')!=_digest({k:v for k,v in e.items() if k!='hash'})):
            errors.append(f'Invalid OST event #{i}')
        prev=e.get('hash','')
    return {'passed':not errors,'errors':errors,'events':len(events),'head':prev if events else None}


def _append(case: Path, payload: dict) -> dict:
    audit=verify(case)
    if not audit['passed']: raise ValueError('OST journal integrity failed; refusing mutation')
    p=_path(case); p.parent.mkdir(parents=True,exist_ok=True)
    body={'seq':audit['events']+1,'previous':audit['head'] or 'GENESIS','at':now(),**payload}
    e={**body,'hash':_digest(body)}
    with p.open('a',encoding='utf8') as f:
        f.write(json.dumps(e,ensure_ascii=False,sort_keys=True,separators=(',',':'))+'\n')
        f.flush();os.fsync(f.fileno())
    return e


def _state(events: list[dict]) -> dict:
    nodes={}; pending={}; decisions={}; revision=0
    for e in events:
        if e.get('op')=='start':
            if nodes: raise ValueError('Multiple OST roots not supported in one engagement')
            nodes['OST-ROOT']={'id':'OST-ROOT','type':'outcome','parent':None,'text':e['outcome'],
                'metric':e['metric'],'segment':e['segment'],'created_at':e['at'], 'status':'working_draft'}
            revision+=1
        elif e.get('op')=='propose':
            pending[e['proposal']['id']]=e['proposal']
        elif e.get('op')=='review':
            pid=e['proposal_id']
            if pid not in pending or pid in decisions: raise ValueError('Invalid OST review lineage')
            proposal=pending[pid]
            if e['decision']=='accept':
                if proposal['action']=='add':
                    entry=proposal['node']; nodes[entry['id']]={**entry,'status':'working_draft'}
                elif proposal['action']=='revise':
                    node=nodes[proposal['node_id']]
                    node.update({'text':proposal['text'],'previous_text':node['text']})
                elif proposal['action']=='retire':
                    nodes[proposal['node_id']]['status']='retired'
                elif proposal['action']=='move':
                    nodes[proposal['node_id']]['parent']=proposal['parent']
                revision+=1
            decisions[pid]={'decision':e['decision'],'reviewer':e['reviewer'],'rationale':e['rationale'], 'at':e['at']}
    return {'revision':revision,'nodes':nodes,'proposals':pending,'reviews':decisions}


def state(case: Path, at_event: int | None = None) -> dict:
    audit=verify(case)
    if not audit['passed']: raise ValueError('OST journal integrity failed')
    ev=_events(case)
    if at_event is not None:
        if at_event<0 or at_event>len(ev): raise ValueError('Invalid event sequence')
        ev=ev[:at_event]
    result=_state(ev)
    # Count distinct registered interview documents, not independently verified people.
    sources={x['id']:x for x in read_json(case/'sources.json')}
    claims={x['id']:x for x in read_json(case/'claims.json')}
    refs={sid for node in result['nodes'].values() if node['type']=='opportunity'
          for cid in node.get('claim_ids',[]) for sid in claims.get(cid,{}).get('source_ids',[])
          if sources.get(sid,{}).get('source_type','').lower() in OBSERVATIONAL}
    result['research_readiness']={'observational_source_records':len(refs),
        'initial_interview_guideline_met_by_record_count':len(refs)>=3,
        'note':'Torres recommends 3 to 4 story-based customer interviews before an initial tree. Record count does not establish interview authenticity, independence or quality.'}
    return {'engagement':case.name,**result,'events_scanned':len(ev),
        'warning':'Locally recorded reviewer identity is self-asserted, not authenticated. Tree is a working draft.'}


def start(case: Path, outcome: str, metric: str, segment: str) -> dict:
    if _events(case): raise ValueError('OST already started for this engagement')
    if not all(isinstance(s,str) and s.strip() for s in (outcome,metric,segment)):
        raise ValueError('Outcome, measurable metric and target segment required')
    e=_append(case,{'op':'start','outcome':outcome.strip(),'metric':metric.strip(),'segment':segment.strip()})
    return {'root':'OST-ROOT','event_seq':e['seq'],'status':'working_draft','note':'Define observed opportunities from real customer evidence, not guesses.'}


def _ensure_source_claims(case: Path, claim_ids: list[str]) -> tuple[list, bool]:
    if any(not isinstance(q,str) for q in claim_ids): raise ValueError('Invalid claim IDs')
    data={x['id']:x for x in read_json(case/'claims.json')}
    missing=set(claim_ids)-set(data)
    if missing: raise ValueError(f'Claims outside current engagement or unknown: {sorted(missing)}')
    sources={s['id']:s for s in read_json(case/'sources.json')}
    primary=any(sources.get(sid,{}).get('source_type','').lower() in OBSERVATIONAL
        for cid in claim_ids for sid in data[cid].get('source_ids',[]))
    return [data[cid] for cid in claim_ids],primary


def propose(case: Path, kind: str, parent: str, text: str, claim_ids: list[str],
            rationale: str, measure: str = '', threshold: str = '') -> dict:
    if kind not in PARENTS: raise ValueError('Only opportunity, solution and test nodes can be proposed')
    s=state(case); nodes=s['nodes']
    if parent not in nodes or nodes[parent]['type'] not in PARENTS[kind] or nodes[parent]['status']=='retired':
        raise ValueError('Invalid parent type, missing or retired parent')
    if not text.strip() or not rationale.strip(): raise ValueError('Text and rationale required')
    _,primary=_ensure_source_claims(case,claim_ids)
    if kind=='opportunity' and (not claim_ids or not primary):
        raise ValueError('Opportunity requires a claim grounded in an interview or actual observational research source; conjecture belongs in a separate hypothesis')
    if kind=='test' and (not measure.strip() or not threshold.strip()):
        raise ValueError('Assumption test requires measure and prospective decision threshold')
    seq=s['events_scanned']+1
    proposal={'id':f'OSTP-{seq:05d}','action':'add','rationale':rationale.strip(),
              'node':{'id':f'OSTN-{seq:05d}','type':kind,'parent':parent,
                'text':text.strip(),'claim_ids':claim_ids,'measure':measure.strip(),
                'threshold':threshold.strip(),'created_at':now(),
                'evidence_status':'referenced_unverified'}}
    _append(case,{'op':'propose','proposal':proposal})
    return {'proposal':proposal['id'],'node_id':proposal['node']['id'],'status':'awaiting_local_review',
            'warning':'Source linkage is not independent source verification.'}


def change(case: Path, node_id: str, action: str, rationale: str,
           text: str = '', parent: str = '') -> dict:
    s=state(case); nodes=s['nodes']
    if action not in ('revise','retire','move'): raise ValueError('Unknown change action')
    if node_id not in nodes or node_id=='OST-ROOT' or nodes[node_id]['status']=='retired':
        raise ValueError('Only active non-root nodes can be changed')
    if not rationale.strip(): raise ValueError('Change rationale required')
    if action=='revise' and not text.strip(): raise ValueError('New text required')
    if action=='move':
        if parent not in nodes or nodes[parent]['type'] not in PARENTS[nodes[node_id]['type']]:
            raise ValueError('Invalid move target')
        cursor=parent
        while cursor:
            if cursor==node_id: raise ValueError('Move introduces cycle')
            cursor=nodes[cursor].get('parent')
    seq=s['events_scanned']+1
    proposal={'id':f'OSTP-{seq:05d}','action':action,'node_id':node_id,
              'rationale':rationale.strip(),'text':text.strip(),'parent':parent}
    _append(case,{'op':'propose','proposal':proposal})
    return {'proposal':proposal['id'],'status':'awaiting_local_review'}


def review(case: Path, proposal_id: str, decision: str, reviewer: str, rationale: str) -> dict:
    if decision not in ('accept','reject'): raise ValueError('Decision must be accept or reject')
    if not reviewer.strip() or not rationale.strip(): raise ValueError('Reviewer label and rationale required')
    s=state(case)
    if proposal_id not in s['proposals'] or proposal_id in s['reviews']:
        raise ValueError('Unknown or already reviewed OST proposal')
    proposal=s['proposals'][proposal_id]
    # Validate current parent and consistency; approvals can become stale.
    if decision=='accept' and proposal['action']=='add':
        p=proposal['node']['parent']; k=proposal['node']['type']
        if p not in s['nodes'] or s['nodes'][p]['status']=='retired' or s['nodes'][p]['type'] not in PARENTS[k]:
            raise ValueError('Proposal parent no longer valid')
    if decision=='accept' and proposal['action'] in ('move','revise','retire'):
        target=proposal['node_id']
        if target not in s['nodes'] or s['nodes'][target]['status']=='retired': raise ValueError('Target no longer active')
        if proposal['action']=='move':
            p=proposal['parent']; node=s['nodes'][target]
            if p not in s['nodes'] or s['nodes'][p]['status']=='retired' or s['nodes'][p]['type'] not in PARENTS[node['type']]:
                raise ValueError('Move parent no longer valid')
            cursor=p
            while cursor:
                if cursor==target: raise ValueError('Move introduces cycle')
                cursor=s['nodes'][cursor].get('parent')
        if proposal['action']=='retire' and any(n.get('parent')==target and n['status']!='retired' for n in s['nodes'].values()):
            raise ValueError('Retire child nodes before retiring parent')
    e=_append(case,{'op':'review','proposal_id':proposal_id,'decision':decision,'reviewer':reviewer,
                   'rationale':rationale})
    return {'proposal':proposal_id,'decision':decision,'event_seq':e['seq'],
      'warning':'This is a local recorded review only. It is not identity-verified authorization.'}


def diff(case: Path, from_event: int, to_event: int | None = None) -> dict:
    full=state(case); target=full['events_scanned'] if to_event is None else to_event
    if from_event>target: raise ValueError('from_event after to_event')
    a=state(case,from_event)['nodes']; b=state(case,target)['nodes']
    return {'from_event':from_event,'to_event':target,
        'added':[b[k] for k in sorted(set(b)-set(a))],
        'changed':[{'id':k,'from':a[k],'to':b[k]} for k in sorted(set(a)&set(b)) if a[k]!=b[k]],
        'deleted':[], 'note':'Nodes are never deleted: retired nodes preserve history.'}


def affected(case: Path, reference: str) -> dict:
    """Return OST nodes that directly cite a claim; conservative, no propagation."""
    st=state(case)
    affected_nodes=[{'id':n['id'],'type':n['type'],'text':n['text'],
                     'action':'review_proposed_when_source_changes'}
        for n in st['nodes'].values() if reference in n.get('claim_ids',[])]
    return {'reference':reference,'ost_nodes':affected_nodes,
        'note':'Direct recorded claim links only; not an automatic semantic impact analysis.'}
