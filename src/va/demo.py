"""Explicitly fictional, local-only demonstration of the decision/knowledge loop.

No model calls, web requests, client data, authenticated reviews or publications.
"""
from __future__ import annotations

from . import core, ost, artifacts, change_model, ledger


def build(name: str = 'Fictional Harbor Supplies Demo') -> dict:
    """Create a new synthetic example. Refuse to overwrite existing engagements."""
    if not name.lower().startswith('fictional '):
        raise ValueError('Demo name must begin with "Fictional " so synthetic material stays unmistakable')
    case = core.new_engagement(name, 'client', 'wholesale distribution (fictional)', 'quick')
    core.update_engagement(case,
        objective='FICTIONAL: investigate why merchant customers abandon requests for quotes',
        scope='Synthetic training case. No real company, interview, customer, or research was involved.',
        requested_output='Illustrative evidence-linked decision brief and OST working draft',
        approval_owner='Example operator (not authenticated)',
        risk_level='low')
    source = core.add_source(case, 'FICTIONAL customer interview transcript, synthesized for demonstration',
        'synthetic://harbor-supplies/interview-001', 'interview')
    claim = core.add_claim(case,
        'FICTIONAL interview participant says quote status is difficult to track after requesting pricing.', [source['id']])
    hypothesis = core.add_hypothesis(case,
        'FICTIONAL: uncertainty about quote status contributes to request abandonment',
        'A clear status update reduces abandonment in a consented pilot',
        'Run an instrumented pilot with an agreed comparison group', [claim['id']])
    option = core.add_option(case, 'Prototype proactive quote-status updates and compare against current workflow', [claim['id']])
    decision = core.add_decision(case,
        'What low-cost research or experiment should follow?',
        'DRAFT: validate the quote-status problem with additional customer research before designing a pilot',
        [claim['id']])
    ost.start(case, 'Improve repeat purchasing from wholesale buyers',
        'Share of buyers placing another order within 60 days', 'Fictional independent merchants')
    opportunity = ost.propose(case, 'opportunity', 'OST-ROOT',
        'Merchants cannot tell whether a pending quote needs their action', [claim['id']],
        'FICTIONAL observation, not validated customer evidence')
    ost.review(case, opportunity['proposal'], 'accept', 'fictional local reviewer',
        'Accept as a draft branch for demonstration, not a validated customer insight')
    solution = ost.propose(case, 'solution', opportunity['node_id'],
        'Offer a self-service quote-status view', [],
        'One possible solution among others')
    ost.review(case, solution['proposal'], 'accept', 'fictional local reviewer',
        'Retain as an unvalidated solution option in the example')
    test = ost.propose(case, 'test', solution['node_id'],
        'Run usability tasks before any build commitment', [],
        'Test the central assumption that buyers would understand status',
        'Task success percentage', 'At least 80% of 5 fictional test participants')
    ost.review(case, test['proposal'], 'accept', 'fictional local reviewer',
        'Accept as proposed test only; no experiments have been run')
    before = artifacts.write_artifact(case, 'decision-brief')
    follow_up = core.add_source(case, 'FICTIONAL contradictory interview note',
        'synthetic://harbor-supplies/interview-002', 'interview')
    successor = change_model.propose_claim_revision(case, claim['id'],
        'FICTIONAL contradictory research suggests delays in pricing approvals may matter more than visibility.',
        'Second synthetic observation changes the working interpretation; requires review', [follow_up['id']])
    dependency = change_model.impacted(case, claim['id'])
    ost_dependency = ost.affected(case, claim['id'])
    after = artifacts.write_artifact(case, 'decision-brief')
    integrity = ledger.verify(case)
    ost_integrity = ost.verify(case)
    if not integrity['passed'] or not ost_integrity['passed']:
        raise ValueError('Synthetic demonstration integrity checks failed')
    return {
        'fictional': True,
        'engagement': case.name,
        'path': str(case),
        'original_claim': claim['id'],
        'draft_successor': successor['new_claim'],
        'decision': decision['id'],
        'hypothesis': hypothesis['id'],
        'option': option['id'],
        'ost_events': ost_integrity['events'],
        'downstream_record_ids': [r['id'] for r in dependency['downstream']],
        'affected_ost_nodes': [n['id'] for n in ost_dependency['ost_nodes']],
        'before_brief': before['path'],
        'after_brief': after['path'],
        'original_decision_still_references': claim['id'],
        'notes': [
            'All sources, people, statements and outcomes are invented for demonstration.',
            'The new claim is unapproved. Decisions are not silently updated.',
            'Local OST reviews are not identity-verified approvals.',
            'No model, external research service or authenticated actor was used.'
        ],
    }
