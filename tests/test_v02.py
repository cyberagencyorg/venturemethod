"""Structural and adversarial tests, not skill effectiveness benchmarks."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from src.va import core, ledger, routing, artifacts, skillforge


class ReleaseTwoTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.eng_root = Path(self.tmp.name) / 'cases'
        self.patcher = patch.object(core, 'ENGAGEMENT_ROOT', self.eng_root)
        self.patcher.start()
        self.addCleanup(self.patcher.stop)

    def case(self, name='Synthetic Alpha', kind='venture'):
        return core.new_engagement(name,kind)

    def test_ledger_integrity_and_sequence(self):
        case = self.case()
        s = core.add_source(case,'Internal notes','local:notes','interview')
        c = core.add_claim(case,'An interviewee alleged a workflow issue',[s['id']])
        core.add_hypothesis(case,'A prototype improves completion','Completion improves in a test','Conduct controlled test',[c['id']])
        audit = ledger.verify(case)
        self.assertTrue(audit['passed'],audit)
        self.assertEqual(audit['events'],3)
        self.assertEqual(json.loads((case/'hypotheses.json').read_text())[0]['id'],'HYP-0001')

    def test_reject_cross_engagement_reference(self):
        a = self.case('Private Client A','client')
        b = self.case('Private Client B','client')
        source = core.add_source(a,'Private Client A research','local:private','memo')
        with self.assertRaisesRegex(ValueError,'Unknown sources'):
            core.add_claim(b,'Cross-tenant unsupported', [source['id']])
        self.assertEqual(core.read_json(b/'claims.json'),[])

    def test_projection_tampering_detected_and_repaired(self):
        case = self.case()
        core.add_source(case,'Legal filing','local:filing','filing')
        j = case/'sources.json'
        sources = core.read_json(j)
        sources[0]['title'] = 'Fabricated Title'
        core.write_json(j,sources)
        self.assertFalse(ledger.verify(case)['passed'])
        self.assertFalse(core.quality_check(case)['ready_for_review'])
        self.assertTrue(ledger.repair(case)['passed'])
        self.assertEqual(core.read_json(j)[0]['title'],'Legal filing')

    def test_journal_tampering_refuses_repair(self):
        case=self.case()
        core.add_source(case,'A','local:A','memo')
        journal=case/'events.jsonl'
        journal.write_text(journal.read_text().replace('local:A','local:B'))
        self.assertFalse(ledger.verify(case)['passed'])
        with self.assertRaises(ValueError): ledger.repair(case)

    def test_missing_reference_rejected_prior_to_write(self):
        case=self.case()
        with self.assertRaises(ValueError): core.add_decision(case,'Buy?','Yes',['CLM-9999'])
        self.assertEqual(ledger.verify(case)['events'],0)

    def test_immutable_ids_and_record_chain(self):
        case=self.case()
        with self.assertRaises(ValueError): core.append_record(case,'sources',{'id':'SRC-2222'})
        src=core.add_source(case,'A','local:A','memo')
        self.assertEqual(src['id'],'SRC-0001')
        self.assertEqual(ledger.verify(case)['events'],1)

    def test_intake_change_routes_and_records(self):
        case=self.case('Prototype Buyer','client')
        core.update_engagement(case,objective='Develop product pricing and go-to-market strategy for operations buyers',
            requested_output='Client strategy memo',risk_level='high',approval_owner='Director')
        route=routing.recommend(case)
        self.assertIn('growth',route['inferred_domains'])
        self.assertIn('adversarial-review',route['recommended_skills'])
        self.assertEqual(route['status'],'heuristic')
        self.assertTrue(ledger.verify(case)['passed'])
        self.assertEqual(core.read_json(case/'engagement_changes.json')[0]['id'],'CHG-0001')

    def test_no_context_route_is_provisional(self):
        case=self.case()
        route=routing.recommend(case)
        self.assertEqual(route['status'],'provisional')
        self.assertIn('objective',route['missing_intake'])
        self.assertIn('collect admissible evidence',route['next_step'])

    def test_generated_brief_is_draft_and_traced(self):
        case=self.case()
        core.update_engagement(case,objective='Investigate potential venture',approval_owner='Human reviewer')
        s=core.add_source(case,'Unverified hypothetical interview','local:synthetic','synthetic')
        c=core.add_claim(case,'A fictional operator described rework',[s['id']])
        core.add_option(case,'Test a limited intervention',[c['id']])
        d=core.add_decision(case,'Run a test?','Prepare interview protocol',[c['id']])
        core.add_action(case,'Draft protocol',d['id'],'Human researcher')
        result=artifacts.write_artifact(case,'decision-brief')
        body=Path(result['path']).read_text()
        self.assertIn('No independent factual verification',body)
        self.assertIn('CLM-0001',body)
        self.assertIn('SRC-0001',body)
        self.assertFalse(result['publication_authorized'])
        self.assertTrue(ledger.verify(case)['passed'])

    def test_no_artifact_when_ledger_invalid(self):
        case=self.case()
        core.add_source(case,'A','local:A','memo')
        (case/'sources.json').write_text('[]')
        with self.assertRaisesRegex(ValueError,'Journal integrity'):
            artifacts.write_artifact(case,'context-pack')

    def test_external_skills_never_auto_approved(self):
        file=Path(self.tmp.name)/'candidates.json'
        file.write_text(json.dumps({'schema_version':'1.0','candidates':[]}))
        with patch.object(skillforge,'FILE',file):
            c=skillforge.register_candidate('example-skill','https://github.com/example/repo',
                                            'a'*40,'MIT','Gap in evaluation methodology')
            self.assertFalse(c['eligible_for_execution'])
            self.assertFalse(c['license_verified'])
            with self.assertRaises(ValueError):
                skillforge.register_candidate('example-skill','https://github.com/example/repo','b'*40,
                                               'MIT','Another reason')
            with self.assertRaises(ValueError):
                skillforge.register_candidate('bad-skill','http://evil.invalid/repo','c'*40,
                                               'MIT','No trust')

    def test_approval_is_not_inferred_from_decision(self):
        case=self.case()
        core.update_engagement(case,objective='Test risk',approval_owner='Person')
        d=core.add_decision(case,'Proceed?','Research first')
        self.assertEqual(d['status'],'draft')
        self.assertFalse(d['approval_evidence'])
        a=core.add_action(case,'Research question',d['id'],'Operator')
        self.assertEqual(a['authorization'],'pending')


if __name__ == '__main__': unittest.main()

class SkillEvalTests(unittest.TestCase):
    def test_eval_does_not_pretend_ran(self):
        from src.va import skill_evals
        with tempfile.TemporaryDirectory() as d:
            target = Path(d)/'evaluation'
            result = skill_evals.prepare('go-to-market',target)
            self.assertEqual(result['status'],'pending_independent_agent_runs')
            report = skill_evals.summarize(target)
            self.assertEqual(report['status'],'incomplete')
            self.assertIsNone(report['candidate_average'])
            self.assertIsNone(report['difference'])
            self.assertTrue(report['missing'])

    def test_partial_grades_never_count_as_pass(self):
        from src.va import skill_evals
        with tempfile.TemporaryDirectory() as d:
            target = Path(d)/'eval'
            skill_evals.prepare('systems-diagnosis',target)
            review = json.loads((target/'review.json').read_text())
            review['reviewer']='Human'
            review['blind_review']=True
            review['ratings']['candidate']['typical']['accuracy']=4
            (target/'review.json').write_text(json.dumps(review))
            result=skill_evals.summarize(target)
            self.assertEqual(result['status'],'incomplete')

class ProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        patcher=patch.object(core,'ENGAGEMENT_ROOT',Path(self.tmp.name))
        patcher.start()
        self.addCleanup(patcher.stop)
        self.case=core.new_engagement('Reference Lab','company')

    def test_trace_source_claim_decision_and_reviews(self):
        e=core.add_entity(self.case,'Fictional Brand','trade_brand','N/A')
        source=core.add_source(self.case,'Record','local:notes','synthetic')
        claim=core.add_claim(self.case,'Fictional observation',[source['id']])
        decision=core.add_decision(self.case,'Test?','Investigate',[claim['id']])
        review=core.add_review(self.case,'claim',claim['id'],'inconclusive','Reviewer',
                                'Only one hypothetical account exists',[source['id']])
        t=core.trace(self.case,decision['id'])
        ids={x['id'] for x in t['nodes']}
        self.assertTrue({decision['id'],claim['id'],source['id'],review['id']}<=ids)
        self.assertNotIn(e['id'],ids)
        self.assertTrue(ledger.verify(self.case)['passed'])

    def test_review_does_not_grant_action(self):
        source=core.add_source(self.case,'A','local:a','memo')
        c=core.add_claim(self.case,'Some claim',[source['id']])
        d=core.add_decision(self.case,'Go?','Proceed',[c['id']])
        core.add_review(self.case,'decision',d['id'],'recommend','Colleague','Proposed after preliminary review')
        self.assertEqual(core.read_json(self.case/'decisions.json')[0]['status'],'draft')
        self.assertIsNone(core.read_json(self.case/'decisions.json')[0]['approval_evidence'])

    def test_artifacts_are_content_addressed_and_repeat_idempotent(self):
        core.update_engagement(self.case,objective='Assess',approval_owner='Reviewer')
        first=artifacts.write_artifact(self.case,'decision-brief')
        second=artifacts.write_artifact(self.case,'decision-brief')
        self.assertEqual(first['artifact_id'],second['artifact_id'])
        self.assertFalse(second['created'])
        self.assertEqual(len(core.read_json(self.case/'artifacts.json')),1)
        core.add_source(self.case,'New note','local:note','memo')
        third=artifacts.write_artifact(self.case,'decision-brief')
        self.assertNotEqual(third['sha256'],first['sha256'])
        self.assertTrue(Path(first['path']).exists())

    def test_review_cannot_attach_other_case_source(self):
        other=core.new_engagement('Other Company','company')
        remote=core.add_source(other,'Private','local:private','memo')
        claim=core.add_claim(self.case,'Claim without source')
        with self.assertRaises(ValueError):
            core.add_review(self.case,'claim',claim['id'],'supported','Reviewer',
                            'Unsupported', [remote['id']])

    def test_later_intake_edits_detected(self):
        core.update_engagement(self.case,objective='Scope A')
        core.update_engagement(self.case,risk_level='low')
        obj=core.read_json(self.case/'engagement.json')
        obj['objective']='Unauthorized modification'
        core.write_json(self.case/'engagement.json',obj)
        self.assertFalse(core.quality_check(self.case)['ready_for_review'])
