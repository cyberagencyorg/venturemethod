"""Read-only, optional adoption guidance for an existing external project.

This provides discoverable pointers, not expert method selection or agent execution.
No project files are opened, no engagements are created, and nothing is installed.
"""
from __future__ import annotations

import json
from pathlib import Path

from .core import ROOT
from . import methodology, routing

PHASES = ('in-flight', 'starting', 'review', 'unknown')
# Representative starting points, not an ordered judgment of method quality.
# Each ID must also support the corresponding catalog goal; the code enforces that.
DOMAIN_EXAMPLES = {
    'discovery': ('continuous-discovery', 'opportunity-solution-tree', 'jtbd-progress'),
    'strategy': ('wardley-mapping', 'competitive-landscape', 'porter-five-forces'),
    'product': ('opportunity-solution-tree', 'outcome-roadmapping', 'north-star'),
    'venture': ('business-model-canvas', 'venture-diligence', 'market-sizing'),
    'capital': ('venture-diligence', 'real-options', 'shell-scenarios'),
    'operations': ('business-capability', 'causal-loop', 'leverage-points'),
    'growth': ('commercial-gtm', 'pricing-discovery', 'business-model-canvas'),
    'brand': ('competitive-positioning-alternatives-first', 'commercial-gtm', 'wardley-mapping'),
    'positioning': ('competitive-positioning-alternatives-first', 'commercial-gtm'),
    'institutional': ('pestle', 'wardley-mapping', 'market-sizing'),
    'delivery': ('outcome-roadmapping', 'shape-up', 'working-backwards'),
}

DOMAIN_GOALS = {
    'discovery': 'discover_need',
    'strategy': 'choose_strategy',
    'product': 'prioritize',
    'venture': 'design_business',
    'capital': 'allocate_capital',
    'operations': 'transform_org',
    'growth': 'design_business',
    'brand': 'choose_strategy',
    'positioning': 'choose_strategy',
    'copy': 'choose_strategy',
    'editorial': 'choose_strategy',
    'institutional': 'map_market',
    'delivery': 'plan_delivery',
}


def manifest() -> dict:
    """Validate the lightweight entrypoint map against the actual checkout."""
    src = ROOT / 'venturemethod.json'
    data = json.loads(src.read_text(encoding='utf-8'))
    if data.get('schema_version') != '1.0':
        raise ValueError('Unsupported adoption manifest')
    for group in ('entrypoints', 'catalogs'):
        if not isinstance(data.get(group), dict):
            raise ValueError(f'Missing {group} in manifest')
        for path in data[group].values():
            if not isinstance(path, str) or Path(path).is_absolute() or '..' in Path(path).parts:
                raise ValueError('Unsafe manifest path')
            if not (ROOT / path).is_file():
                raise ValueError(f'Manifest references missing file: {path}')
    return data


def orient(task: str, phase: str = 'in-flight', limit: int = 4) -> dict:
    """Advisory entrypoint: no engagement or local project access required."""
    if not isinstance(task, str) or not task.strip() or len(task) > 4000:
        raise ValueError('Specify a task between 1 and 4000 characters')
    if phase not in PHASES:
        raise ValueError(f'Phase must be one of: {PHASES}')
    if not isinstance(limit, int) or not 1 <= limit <= 8:
        raise ValueError('Limit must be between 1 and 8')
    data = manifest()
    hit = []
    for domain, config in routing.CAPABILITIES.items():
        terms = [term for term in config['terms'] if routing._match(task, term)]
        if terms:
            hit.append({'domain': domain, 'matched_terms': terms})
    hit.sort(key=lambda item: (-len(item['matched_terms']), item['domain']))
    selected_domains = hit[:2]
    registry = json.loads((ROOT / 'config' / 'skills-registry.json').read_text(encoding='utf-8'))
    skills_by_name = {s['name']: s for s in registry['skills']}
    skills=[]
    for item in selected_domains:
        for skill in routing.CAPABILITIES[item['domain']]['skills']:
            if skill in skills_by_name and skill not in [x['id'] for x in skills]:
                ref = skills_by_name[skill]['path'].rstrip('/') + '/SKILL.md'
                if not (ROOT / ref).is_file():
                    raise ValueError(f'Skill registry points to missing instruction file: {ref}')
                skills.append({'id':skill,'instruction_path':ref,'coverage':'instruction_only_unbenchmarked'})
            if len(skills) >= limit:
                break
        if len(skills) >= limit:
            break
    candidates=[]
    catalog={m['id']:m for m in methodology.load_catalog()}
    # Prefer a few representative methods across the matched domains. This is a
    # reading order, not a claim of suitability or method execution.
    for item in selected_domains:
        quota = max(1, (limit + len(selected_domains) - 1)//len(selected_domains))
        added=0
        for method_id in DOMAIN_EXAMPLES.get(item['domain'], ()):
            if added >= quota or len(candidates) >= limit:
                break
            method=catalog[method_id]
            if method_id in [x['id'] for x in candidates]:
                continue
            goal=DOMAIN_GOALS[item['domain']]
            if goal not in method['goals']:
                raise ValueError(f'Adoption example {method_id} does not support {goal}')
            candidates.append({
                'id':method['id'], 'title':method['title'],
                'minimum_evidence':method['minimum_evidence'],
                'fit':method['fit'], 'avoid':method['avoid'],
                'source':method['source'], 'executed':False,
            })
            added+=1
    instructions={
        'in-flight':'Read and respect the host project\'s existing work and decisions first. Identify a specific gap; do not restart discovery or migrate its files.',
        'starting':'Establish the immediate objective and constraints before choosing a method. Skip formal engagement setup unless continuing records are valuable.',
        'review':'Assess the current work against its own requirements, sources and outcomes. Suggest bounded improvements; do not replace it with a new process.',
        'unknown':'Inspect the current task and available context. Start with a small useful contribution, asking only for genuinely blocking information.',
    }
    return {
        'framework':'Khan\'s Venture Method Framework',
        'purpose':'selective_reference_adoption',
        'state':'read_only',
        'task':task.strip(), 'phase':phase,
        'entrypoint':data['entrypoints']['adoption'],
        'guidance':instructions[phase],
        'matched_domains':selected_domains,
        'suggested_skills':skills,
        'method_candidates':candidates,
        'optional_deep_work':data['entrypoints']['first_engagement'],
        'constraints':[
            'Host project instructions, current decisions and user authority take priority.',
            'Read only the relevant skill and method references; skip everything else.',
            'Suggestions are lexical and provisional; verify suitability and existing capabilities.',
            'Never install, execute, copy private data, or change files without authorization.',
            'A cited method or skill definition does not mean it was executed or evaluated.',
        ],
        'effect':'No files read from or written to the host project. No engagement created.',
    }


def markdown(result: dict) -> str:
    lines=[
        '# Venture Method: selective use',
        '',
        'This is a read-only guide for an existing task, not an instruction to take over the project.',
        '',
        f"**Phase:** {result['phase']}",
        f"**Task (operator supplied):** {result['task']}",
        '',
        result['guidance'],
        '',
        f"Start with [{result['entrypoint']}]({result['entrypoint']}).",
    ]
    if result['suggested_skills']:
        lines.extend(['','### Skill references worth inspecting'])
        for x in result['suggested_skills']:
            lines.append(f"- `{x['instruction_path']}` ({x['coverage']})")
    if result['method_candidates']:
        lines.extend(['','### Method candidates, not prescriptions'])
        for x in result['method_candidates']:
            lines.append(f"- **{x['title']}** (`{x['id']}`): needs {x['minimum_evidence']} evidence; avoid: {x['avoid']}. Source: {x['source']}")
    if not result['suggested_skills'] and not result['method_candidates']:
        lines.extend(['','No specific domain matched reliably. Read the adoption guide and use existing project expertise first.'])
    lines.extend(['','### Boundaries',*['- '+x for x in result['constraints']],''])
    return '\n'.join(lines)
