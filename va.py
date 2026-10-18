#!/usr/bin/env python3
"""Venture Method CLI. Offline, single-writer, Python 3.11+."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from src.va.core import (ROOT, TYPES, PROFILES, safe_engagement, new_engagement,
    add_source, add_claim, add_decision, add_hypothesis, add_option, add_action,
    add_outcome, plan, quality_check, report, validate_skills, skill_metadata,
    update_engagement, add_entity, add_review, trace, BUNDLES)
from src.va import ledger, routing, artifacts, skillforge, skill_evals, methodology, change_model, ost, demo, composition, research


def printer(v): print(json.dumps(v, indent=2, ensure_ascii=False))


def main(argv=None):
    p = argparse.ArgumentParser(prog='va', description='Evidence-to-decision Venture Method workbench')
    sub = p.add_subparsers(dest='command', required=True)
    d = sub.add_parser('demo', help='Create an explicitly fictional, private end-to-end example')
    d.add_argument('--name', default='Fictional Harbor Supplies Demo')
    n = sub.add_parser('new', help='Create isolated local engagement')
    n.add_argument('name'); n.add_argument('--type', required=True, choices=TYPES)
    n.add_argument('--industry', default='unspecified'); n.add_argument('--mode', choices=list(PROFILES), default='standard')
    u = sub.add_parser('intake', help='Set the engagement contract and journal changes')
    u.add_argument('engagement')
    for arg in ('objective','scope','requested-output','approval-owner','risk-level'):
        u.add_argument('--' + arg)
    r = sub.add_parser('route', help='Explainable conservative capability selector'); r.add_argument('engagement')
    tr = sub.add_parser('trace',help='Show source-to-decision record references'); tr.add_argument('engagement'); tr.add_argument('--id',required=True)
    pl = sub.add_parser('plan'); pl.add_argument('engagement')
    ia=sub.add_parser('impact',help='Show recorded downstream dependencies before changing a claim/source')
    ia.add_argument('engagement'); ia.add_argument('--id',required=True)
    rc=sub.add_parser('claim-revise',help='Create an unapproved, immutable successor to a claim')
    rc.add_argument('engagement'); rc.add_argument('--claim',required=True)
    rc.add_argument('--statement',required=True); rc.add_argument('--rationale',required=True)
    rc.add_argument('--source',action='append',default=[])
    ck = sub.add_parser('check'); ck.add_argument('engagement')
    aud = sub.add_parser('audit'); aud.add_argument('engagement')
    rep = sub.add_parser('report'); rep.add_argument('engagement'); rep.add_argument('--out')
    gen = sub.add_parser('generate', help='Private deterministic artifact; no model execution')
    gen.add_argument('engagement'); gen.add_argument('--type', required=True, choices=['decision-brief','context-pack'])
    ent = sub.add_parser('entity-add'); ent.add_argument('engagement'); ent.add_argument('--name',required=True)
    ent.add_argument('--type',required=True); ent.add_argument('--jurisdiction',default='unknown')
    rev = sub.add_parser('review-add'); rev.add_argument('engagement')
    rev.add_argument('--target-type',required=True,choices=['claim','decision','entity'])
    rev.add_argument('--target',required=True); rev.add_argument('--verdict',required=True)
    rev.add_argument('--reviewer',required=True); rev.add_argument('--rationale',required=True)
    rev.add_argument('--source',action='append',default=[])
    a = sub.add_parser('source-add'); a.add_argument('engagement'); a.add_argument('--title', required=True)
    a.add_argument('--locator', required=True); a.add_argument('--kind', required=True)
    a = sub.add_parser('claim-add'); a.add_argument('engagement'); a.add_argument('--text', required=True)
    a.add_argument('--source', action='append', default=[])
    a = sub.add_parser('hypothesis-add'); a.add_argument('engagement')
    a.add_argument('--text', required=True); a.add_argument('--predict', required=True); a.add_argument('--test', required=True)
    a.add_argument('--claim', action='append', default=[])
    a = sub.add_parser('option-add'); a.add_argument('engagement'); a.add_argument('--text', required=True)
    a.add_argument('--claim', action='append', default=[])
    a = sub.add_parser('decision-add'); a.add_argument('engagement'); a.add_argument('--question', required=True)
    a.add_argument('--choice', required=True); a.add_argument('--claim', action='append', default=[])
    a = sub.add_parser('action-add'); a.add_argument('engagement'); a.add_argument('--text', required=True)
    a.add_argument('--decision', required=True); a.add_argument('--owner', required=True)
    a = sub.add_parser('outcome-add'); a.add_argument('engagement'); a.add_argument('--action', required=True)
    a.add_argument('--observation', required=True); a.add_argument('--source', action='append', default=[])
    s = sub.add_parser('skills'); s.add_argument('action', choices=['list','check','recommend'])
    s.add_argument('--type', choices=TYPES)
    ex = sub.add_parser('external-skills'); ex.add_argument('action', choices=['list','candidate-add'])
    ex.add_argument('--name'); ex.add_argument('--upstream'); ex.add_argument('--commit'); ex.add_argument('--license')
    ex.add_argument('--rationale')
    se=sub.add_parser('skill-eval',help='Prepare or summarize externally executed blinded skill evaluations')
    se.add_argument('action',choices=['prepare','summarize'])
    se.add_argument('--skill'); se.add_argument('--workspace',required=True)
    comp=sub.add_parser('compose', help='Plan explicitly selected methods, roles and tools; no execution')
    comp.add_argument('engagement')
    comp.add_argument('--goal', action='append', required=True, choices=methodology.GOALS)
    comp.add_argument('--method', action='append', default=[])
    comp.add_argument('--evidence', choices=methodology.EVIDENCE, default='minimal')
    comp.add_argument('--save', action='store_true', help='Save immutable proposal under private engagement')
    res=sub.add_parser('research', help='Capture text evidence and prepare traceable draft briefs (no web/model calls)')
    res.add_argument('action', choices=['import','claim','brief','audit'])
    res.add_argument('engagement')
    res.add_argument('--file', type=Path)
    res.add_argument('--title'); res.add_argument('--locator')
    res.add_argument('--kind', default='document'); res.add_argument('--publisher',default='unverified')
    res.add_argument('--published-at')
    res.add_argument('--source'); res.add_argument('--text'); res.add_argument('--excerpt')
    res.add_argument('--question'); res.add_argument('--preview', action='store_true')
    sub.add_parser('capabilities', help='Validate and display work composition coverage')
    sub.add_parser('methods', help='Show v0.2 methods registry')
    fw=sub.add_parser('frameworks', help='Compare v0.3 methodology candidates; explicit goal, no silent winner')
    fw.add_argument('--goal', choices=methodology.GOALS, required=True)
    fw.add_argument('--evidence', choices=methodology.EVIDENCE, default='minimal')
    osub=sub.add_parser('ost',help='Evidence-backed Opportunity Solution Trees (local working drafts)')
    osub.add_argument('action',choices=['start','propose','change','review','show','diff','audit'])
    osub.add_argument('engagement')
    for key in ('outcome','metric','segment','kind','parent','text','rationale','measure','threshold',
                'node','proposal','decision','reviewer','change-action'):
        osub.add_argument('--'+key)
    osub.add_argument('--claim',action='append',default=[])
    osub.add_argument('--from-event',type=int,default=0)
    osub.add_argument('--to-event',type=int)
    ns = p.parse_args(argv)
    try:
        case = safe_engagement(ns.engagement) if hasattr(ns,'engagement') else None
        if ns.command == 'demo': printer(demo.build(ns.name))
        elif ns.command == 'new': print(new_engagement(ns.name, ns.type, ns.industry, ns.mode))
        elif ns.command == 'ost':
            opts={}
            if ns.action=='start': opts=ost.start(case,ns.outcome or '',ns.metric or '',ns.segment or '')
            elif ns.action=='propose': opts=ost.propose(case,ns.kind or '',ns.parent or '',ns.text or '',ns.claim,ns.rationale or '',ns.measure or '',ns.threshold or '')
            elif ns.action=='change': opts=ost.change(case,ns.node or '',ns.change_action or '',ns.rationale or '',ns.text or '',ns.parent or '')
            elif ns.action=='review': opts=ost.review(case,ns.proposal or '',ns.decision or '',ns.reviewer or '',ns.rationale or '')
            elif ns.action=='show': opts=ost.state(case)
            elif ns.action=='diff': opts=ost.diff(case,ns.from_event,ns.to_event)
            else: opts=ost.verify(case)
            printer(opts)
            if ns.action=='audit' and not opts['passed']: return 2
        elif ns.command == 'intake':
            fields = {a.replace('-','_'): getattr(ns, a.replace('-','_')) for a in
                      ('objective','scope','requested-output','approval-owner','risk-level')
                      if getattr(ns,a.replace('-','_')) is not None}
            printer(update_engagement(case, **fields))
        elif ns.command == 'route': printer(routing.recommend(case))
        elif ns.command == 'plan': printer(plan(case))
        elif ns.command == 'impact':
            result=change_model.impacted(case,ns.id)
            result['ost']=ost.affected(case,ns.id)
            printer(result)
        elif ns.command == 'claim-revise': printer(change_model.propose_claim_revision(case,ns.claim,ns.statement,ns.rationale,ns.source))
        elif ns.command == 'trace': printer(trace(case, ns.id))
        elif ns.command == 'check':
            result=quality_check(case); printer(result)
            if result['blockers']: return 2
        elif ns.command == 'audit':
            result = ledger.verify(case)
            ost_result=ost.verify(case)
            result['ost_journal']=ost_result
            result['passed']=result['passed'] and ost_result['passed']
            printer(result)
            if not result['passed']: return 2
        elif ns.command == 'generate': printer(artifacts.write_artifact(case, ns.type))
        elif ns.command == 'report':
            output = report(case)
            if ns.out:
                path = Path(ns.out)
                if not path.resolve().is_relative_to(case.resolve()):
                    raise ValueError('Reports must be written inside their engagement directory')
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(output, encoding='utf8'); print(path)
            else: print(output)
        elif ns.command == 'entity-add': printer(add_entity(case,ns.name,ns.type,ns.jurisdiction))
        elif ns.command == 'review-add': printer(add_review(case,ns.target_type,ns.target,ns.verdict,ns.reviewer,ns.rationale,ns.source))
        elif ns.command == 'source-add': printer(add_source(case,ns.title,ns.locator,ns.kind))
        elif ns.command == 'claim-add': printer(add_claim(case,ns.text,ns.source))
        elif ns.command == 'hypothesis-add': printer(add_hypothesis(case,ns.text,ns.predict,ns.test,ns.claim))
        elif ns.command == 'option-add': printer(add_option(case,ns.text,ns.claim))
        elif ns.command == 'decision-add': printer(add_decision(case,ns.question,ns.choice,ns.claim))
        elif ns.command == 'action-add': printer(add_action(case,ns.text,ns.decision,ns.owner))
        elif ns.command == 'outcome-add': printer(add_outcome(case,ns.action,ns.observation,ns.source))
        elif ns.command == 'skills':
            if ns.action == 'check':
                r=validate_skills(); printer(r)
                if not r['passed']: return 2
            elif ns.action == 'recommend':
                if not ns.type: raise ValueError('--type required')
                printer({'type':ns.type,'skills':BUNDLES[ns.type]})
            else: printer([skill_metadata(q) for q in sorted((ROOT/'skills').iterdir()) if q.is_dir()])
        elif ns.command == 'external-skills':
            if ns.action == 'list': printer(skillforge.list_candidates())
            else:
                if not all((ns.name,ns.upstream,ns.commit,ns.license,ns.rationale)):
                    raise ValueError('--name --upstream --commit --license --rationale all required')
                printer(skillforge.register_candidate(ns.name,ns.upstream,ns.commit,ns.license,ns.rationale))
        elif ns.command == 'skill-eval':
            workspace=Path(ns.workspace)
            if ns.action=='prepare':
                if not ns.skill: raise ValueError('--skill required for prepare')
                printer(skill_evals.prepare(ns.skill,workspace))
            else: printer(skill_evals.summarize(workspace))
        elif ns.command == 'compose':
            printer(composition.compose(case, goals=ns.goal, method_ids=ns.method,
                                        evidence=ns.evidence, save=ns.save))
        elif ns.command == 'research':
            if ns.action == 'import':
                if not all((ns.file, ns.title, ns.locator)):
                    raise ValueError('research import requires --file --title --locator')
                printer(research.import_file(case,ns.file,title=ns.title,locator=ns.locator,
                       source_type=ns.kind,publisher=ns.publisher,published_at=ns.published_at))
            elif ns.action == 'claim':
                if not all((ns.source, ns.text, ns.excerpt)):
                    raise ValueError('research claim requires --source --text --excerpt')
                printer(research.add_excerpt_claim(case,ns.source,ns.text,ns.excerpt))
            elif ns.action == 'brief': printer(research.brief(case,question=ns.question or '',save=not ns.preview))
            else:
                result=research.audit(case);printer(result)
                if not result['passed']:return 2
        elif ns.command == 'capabilities': printer(composition.inventory())
        elif ns.command == 'methods': printer(json.loads((ROOT/'config'/'methods.json').read_text(encoding='utf8')))
        elif ns.command == 'frameworks': printer(methodology.compare(ns.goal,ns.evidence))
    except (ValueError, FileNotFoundError, FileExistsError, json.JSONDecodeError, KeyError) as exc:
        print(f'Error: {exc}', file=sys.stderr); return 2
    return 0

if __name__ == '__main__': sys.exit(main())
