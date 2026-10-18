"""Offline, explicit work composition. Planning only; NEVER invokes an agent or tool.

A catalog mapping is not evidence that a skill can execute a method competently.
A declared tool permission is not an enforced permission. Human approval is out of band.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .core import ROOT, read_json
from . import methodology


def _read(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding='utf-8'))
    if not isinstance(data, dict) or data.get('schema_version') != '1.0':
        raise ValueError(f'Unsupported composition registry: {path.name}')
    return data


def registry(root: Path | None = None) -> dict[str, Any]:
    """Cross-check every first-party skill, method, role and tool without imports."""
    root = root or ROOT
    data = _read(root / 'config' / 'work-composition.json')
    agents = _read(root / 'config' / 'agent-roles.json')
    tools = _read(root / 'config' / 'tool-contracts.json')
    skills = json.loads((root / 'config' / 'skills-registry.json').read_text(encoding='utf-8'))['skills']
    methods = methodology.load_catalog(root / 'config' / 'frameworks-v3.json')
    skill_ids = {s['name'] for s in skills}
    method_ids = {m['id'] for m in methods}
    role_ids = {r['id'] for r in agents['roles']}
    tool_ids = {t['id'] for t in tools['tools']}
    cap_ids = {c['id'] for c in data['capabilities']}
    if (len(role_ids) != len(agents['roles']) or len(tool_ids) != len(tools['tools'])
            or len(cap_ids) != len(data['capabilities']) or len(skill_ids) != len(skills)):
        raise ValueError('Duplicate identifiers in composition registry')
    for role in agents['roles']:
        if (not role.get('responsibility') or role.get('approval_authority') != 'none; named human review required'
                or set(role.get('allowed_tool_effects', [])) - {'read', 'draft'}):
            raise ValueError(f'Unsafe or incomplete role definition: {role["id"]}')
    used_skills: set[str] = set()
    for cap in data['capabilities']:
        if cap['default_role'] not in role_ids:
            raise ValueError(f'Unknown role for capability: {cap["id"]}')
        unknown_skills = set(cap['eligible_skill_ids']) - skill_ids
        if unknown_skills:
            raise ValueError(f'Unregistered skills in {cap["id"]}: {sorted(unknown_skills)}')
        used_skills.update(cap['eligible_skill_ids'])
        if set(cap['required_tool_ids']) - tool_ids:
            raise ValueError(f'Unknown tools for capability: {cap["id"]}')
        if cap['status'] not in ('mapped', 'gap_no_first_party_skill'):
            raise ValueError(f'Unknown capability status: {cap["id"]}')
    if used_skills != skill_ids:
        raise ValueError(f'Unmapped first-party skills: {sorted(skill_ids-used_skills)}')
    linked_methods: set[str] = set()
    for link in data['method_links']:
        m = link['method_id']
        if m not in method_ids or m in linked_methods:
            raise ValueError(f'Missing method or duplicate method mapping: {m}')
        linked_methods.add(m)
        if link['capability_id'] not in cap_ids:
            raise ValueError(f'Unknown capability for method {m}')
        cap = next(c for c in data['capabilities'] if c['id'] == link['capability_id'])
        if link['skill_id'] is not None and link['skill_id'] not in cap['eligible_skill_ids']:
            raise ValueError(f'Method {m} references a skill outside capability {cap["id"]}')
        if link['coverage'] not in ('partial_instruction_only', 'no_first_party_skill'):
            raise ValueError(f'Invalid coverage state for {m}')
        if link['execution_verified'] is not False:
            raise ValueError(f'Method {m} cannot assert verified execution')
        if (link['skill_id'] is None) != (link['coverage'] == 'no_first_party_skill'):
            raise ValueError(f'Inconsistent capability gap for {m}')
    if linked_methods != method_ids:
        raise ValueError(f'Unmapped framework methods: {sorted(method_ids-linked_methods)}')
    for tool in tools['tools']:
        if tool['effect'] not in ('read', 'draft', 'external_write'):
            raise ValueError(f'Unknown tool effect: {tool["id"]}')
        if tool['availability'] not in ('local', 'unimplemented'):
            raise ValueError(f'Invalid tool availability: {tool["id"]}')
        if tool['effect'] == 'external_write' and tool['availability'] == 'local':
            raise ValueError(f'External write tool cannot be implicitly available: {tool["id"]}')
    return {'composition': data, 'roles': agents['roles'], 'tools': tools['tools'],
            'methods': methods, 'skills': skills}


def inventory(root: Path | None = None) -> dict[str, Any]:
    reg = registry(root)
    links = reg['composition']['method_links']
    gaps = [x['method_id'] for x in links if x['skill_id'] is None]
    return {
        'capabilities': reg['composition']['capabilities'],
        'method_count': len(reg['methods']), 'mapped_method_count': len(links),
        'first_party_skill_count': len(reg['skills']), 'role_definitions': reg['roles'],
        'tool_contracts': reg['tools'],
        'methods_without_first_party_skill': gaps,
        'status': 'catalog bindings verified; executable expertise not established',
    }


def _digest(source: Path) -> str:
    return hashlib.sha256(source.read_bytes()).hexdigest()


def compose(case: Path, *, goals: list[str], method_ids: list[str] | None = None,
            evidence: str = 'minimal', save: bool = False, root: Path | None = None) -> dict[str, Any]:
    """Build a reproducible *proposal*, requiring explicit selection of methods.

    No model calls, no network calls, no tools invoked, no approval inferred.
    """
    root = root or ROOT
    reg = registry(root)
    if not goals or len(set(goals)) != len(goals) or set(goals) - set(methodology.GOALS):
        raise ValueError('Pass distinct, supported --goal values')
    if evidence not in methodology.EVIDENCE:
        raise ValueError('Unknown evidence class')
    methods = {m['id']: m for m in reg['methods']}
    links = {x['method_id']: x for x in reg['composition']['method_links']}
    caps = {x['id']: x for x in reg['composition']['capabilities']}
    roles = {x['id']: x for x in reg['roles']}
    tools = {x['id']: x for x in reg['tools']}
    selected = method_ids or []
    if len(selected) != len(set(selected)) or set(selected) - set(methods):
        raise ValueError('Unknown or repeated --method selected')
    if any(not set(methods[mid]['goals']) & set(goals) for mid in selected):
        raise ValueError('Every selected method must serve at least one explicit goal')
    if any(not isinstance(g, str) or not g for g in goals):
        raise ValueError('Invalid goal')
    e = read_json(case / 'engagement.json')
    if e.get('id') != case.name:
        raise ValueError('Engagement identifier mismatch')
    if not e.get('objective', '').strip():
        raise ValueError('Complete engagement objective via intake before composition')
    sources = read_json(case / 'sources.json')
    claims = read_json(case / 'claims.json')
    linked_claims = [cl for cl in claims if cl.get('source_ids')]
    observed_records_present = bool(sources and linked_claims)
    independently_verified_source_present = any(
        s.get('independent_verification') == 'verified' for s in sources)
    if save and not selected:
        raise ValueError('Choose at least one --method before saving a proposal')
    options = []
    for goal in goals:
        matches = methodology.compare(goal, evidence, catalog=reg['methods'])
        options.append({'goal': goal, 'candidates': [
            {**x, 'capability_id': links[x['id']]['capability_id'],
             'skill_id': links[x['id']]['skill_id'],
             'coverage': links[x['id']]['coverage']}
            for x in matches['candidates']]})
    units = []
    for i, method_id in enumerate(selected, 1):
        method = methods[method_id]
        link = links[method_id]
        cap = caps[link['capability_id']]
        role = roles[cap['default_role']]
        related_goals = [g for g in goals if g in method['goals']]
        available_evidence = methodology.EVIDENCE.index(evidence) >= methodology.EVIDENCE.index(method['minimum_evidence'])
        tool_contracts = [tools[x] for x in cap['required_tool_ids']]
        if any(t['effect'] not in role['allowed_tool_effects'] for t in tool_contracts):
            raise ValueError(f'Role {role["id"]} is not eligible for required tool class')
        blocked = []
        if not available_evidence:
            blocked.append(f'Requires evidence class {method["minimum_evidence"]}, not {evidence}')
        if methodology.EVIDENCE.index(method['minimum_evidence']) >= methodology.EVIDENCE.index('observed') and not observed_records_present:
            blocked.append('Method requires recorded sources and claims linked to them; none found')
        if method['minimum_evidence'] == 'verified' and not independently_verified_source_present:
            blocked.append('No source record has independently verified status')
        if link['skill_id'] is None:
            blocked.append('No first-party skill implements this method')
        if any(x['availability'] != 'local' for x in tool_contracts):
            blocked.append('A required tool is not implemented')
        units.append({
            'id': f'WU-{i:03d}', 'goal_ids': related_goals,
            'method_id': method_id, 'method_reference': method['source'],
            'capability_id': cap['id'], 'role_id': role['id'],
            'skill_id': link['skill_id'], 'skill_coverage': link['coverage'],
            'required_tool_ids': cap['required_tool_ids'],
            'evidence_requirement': method['minimum_evidence'],
            'expected_output': method['output'],
            'why_applicable': method['fit'], 'when_not_to_use': method['avoid'],
            'review_owner': e.get('approval_owner', 'unassigned'),
            'manual_execution_only': True,
            'status': 'blocked_for_evidence_or_provider' if blocked else 'manual_method_review_required',
            'blockers': blocked,
        })
    report = {
        'schema_version': '1.0', 'kind': 'work_composition_proposal',
        'engagement_id': e['id'], 'engagement_mode': e['mode'],
        'requested_goals': goals, 'declared_evidence': evidence,
        'selected_method_ids': selected,
        'evidence_index': {'source_count': len(sources), 'source_linked_claim_count': len(linked_claims),
                           'independently_verified_source_recorded': independently_verified_source_present,
                           'limitation': 'Record existence and status fields do not establish factual correctness'},
        'method_options': options, 'work_units': units,
        'context_snapshot': {
            'engagement_sha256': _digest(case / 'engagement.json'),
            'sources_sha256': _digest(case / 'sources.json'),
            'claims_sha256': _digest(case / 'claims.json'),
            'methods_sha256': _digest(root / 'config' / 'frameworks-v3.json'),
            'composition_sha256': _digest(root / 'config' / 'work-composition.json'),
            'roles_sha256': _digest(root / 'config' / 'agent-roles.json'),
            'tools_sha256': _digest(root / 'config' / 'tool-contracts.json'),
        },
        'status': 'method_selection_required' if not selected else 'proposed_not_executed',
        'assurance': 'Catalog coverage means instructions exist. No agent execution, independent verification, or approval occurred.',
    }
    if save:
        # Write only beneath gitignored engagement; versioned by input digest.
        body = (json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2) + '\n').encode('utf-8')
        short_hash = hashlib.sha256(body).hexdigest()[:16]
        target_dir = case / 'plans'
        target_dir.mkdir(exist_ok=True)
        target = target_dir / f'composition-{short_hash}.json'
        if target.exists() and target.read_bytes() != body:
            raise ValueError('Refusing overwrite of a previous plan')
        if not target.exists():
            target.write_bytes(body)
        report['saved_to'] = str(target.relative_to(case))
    return report
