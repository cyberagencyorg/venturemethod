"""Explainable, conservative offline routing; recommendations, not autonomous research.

Never infer client truth or approvals from keywords. Treat intent inference as
provisional; accept explicit objective and requested output as higher authority.
"""
from __future__ import annotations
import re
from pathlib import Path
from typing import Any
from .core import BUNDLES, PROFILES, read_json

# Domain groups are deliberately functional rather than role/persona-specific.
CAPABILITIES = {
 'discovery': {'terms': ('customer','user','interview','needs','problem','demand','research'),
               'skills': ('opportunity-discovery','evidence-audit')},
 'strategy': {'terms': ('strategy','strategic','position','competitive','differentiate','moat','thesis'),
              'skills': ('market-landscape','systems-diagnosis','strategic-options','adversarial-review')},
 'product': {'terms': ('product','feature','prd','requirements','roadmap','prototype','app development'),
             'skills': ('product-discovery','product-requirements','experiment-design')},
 'venture': {'terms': ('venture','startup','founder','business model','incubate','validate an idea'),
             'skills': ('venture-thesis','business-model','experiment-design')},
 'capital': {'terms': ('investment','investor','capital','valuation','fundraising','financial','unit economics','diligence'),
             'skills': ('venture-diligence','financial-scenarios','capital-landscape','business-model','adversarial-review')},
 'operations': {'terms': ('operations','operational','manual','process','operating','workflow','transformation','organization','capability','talent','people'),
                'skills': ('company-investigation','problem-mapping','service-blueprint','operating-model')},
 'growth': {'terms': ('marketing','gtm','go-to-market','launch','channel','pricing','sales','brand','positioning','campaign'),
            'skills': ('go-to-market','market-landscape','commercial-offer','business-model','strategic-options','artifact-quality')},
 'brand': {'terms': ('brand','identity','messaging','copy','voice','subbrand','narrative'),
           'skills': ('brand-architecture','commercial-offer','artifact-quality')},
 'institutional': {'terms': ('regulatory','jurisdiction','government','procurement','public sector','policy','municipal','permit'),
           'skills': ('institutional-landscape','capital-landscape','adversarial-review')},
 'delivery': {'terms': ('deliverable','memo','proposal','brief','slide','deck','report','plan'),
              'skills': ('intake-scoping','evidence-audit','artifact-quality')},
}


def _match(text: str, term: str) -> bool:
    return bool(re.search(r'(?<!\w)' + re.escape(term) + r'(?!\w)', text, flags=re.I))


def recommend(case: Path) -> dict[str, Any]:
    e = read_json(case / 'engagement.json')
    kind=e['kind']
    objective=str(e.get('objective') or '')
    scope=str(e.get('scope') or '')
    requested=str(e.get('requested_output') or '')
    # What work is required comes from the objective, not just the requested file format.
    description = ' '.join((objective,scope)) or requested
    terms={domain: sorted([term for term in data['terms'] if _match(description,term)])
           for domain,data in CAPABILITIES.items()}
    # Format terms should not hijack substantive work for every memo/report.
    if kind!='deliverable': terms['delivery']=[]
    domains=sorted((d for d,hits in terms.items() if hits),key=lambda d:(-len(terms[d]),d))
    provisional=not objective.strip()
    base={'client':['intake-scoping'], 'venture':['venture-thesis'],
          'company':['company-investigation'], 'industry':['market-landscape'],
          'product':['product-discovery'], 'transformation':['problem-mapping'],
          'diligence':['venture-diligence'], 'deliverable':['intake-scoping','artifact-quality']}
    if provisional or not domains:
        skills=list(BUNDLES[kind])
    else:
        skills=list(base[kind])
        # Two strongly matching families are usually enough for an initial plan.
        for domain in domains[:2]:
            for skill in CAPABILITIES[domain]['skills']:
                if skill not in skills: skills.append(skill)
    if kind=='deliverable' and 'artifact-quality' not in skills:
        skills.append('artifact-quality')
    if e.get('risk_level')=='high' or kind=='diligence':
        if 'adversarial-review' not in skills: skills.append('adversarial-review')
    if not any(read_json(case/(c+'.json')) for c in ('sources','claims')):
        next_step='Establish first-party context and collect admissible evidence before substantive conclusions'
        if 'evidence-audit' not in skills and not provisional: skills.append('evidence-audit')
    elif not read_json(case/'decisions.json'):
        next_step='Clarify options and accountable decision; do not imply approval'
    else:
        next_step='Review claim support, alternatives, and the decision record'
    missing=[k for k in ('objective','approval_owner')
             if not str(e.get(k,'')).strip() or e.get(k)=='unassigned']
    return {
        'engagement_id':e['id'], 'profile':e['mode'],
        'steps':PROFILES[e['mode']], 'inferred_domains':domains,
        'why':{d:terms[d] for d in domains}, 'recommended_skills':skills,
        'status':'provisional' if provisional else 'heuristic',
        'missing_intake':missing, 'next_step':next_step,
        'method':'transparent objective-first lexical heuristic; advisory; do not treat as semantic understanding',
        'risk_level':e.get('risk_level','unknown'),
    }
