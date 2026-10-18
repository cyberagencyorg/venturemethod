"""Tests for offline composition: validation, truthful statuses and frozen planning inputs."""
from __future__ import annotations
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.va import core, composition


class CompositionTests(unittest.TestCase):
    def make_case(self, root: Path, kind: str = 'product') -> Path:
        with patch.object(core, 'ENGAGEMENT_ROOT', root):
            case = core.new_engagement('Fictional Product Review', kind, 'services', 'quick')
        core.update_engagement(case, objective='Understand why customers abandon onboarding',
                               approval_owner='Review owner', risk_level='medium')
        return case

    def test_every_skill_has_an_eval_fixture(self):
        # Fixtures alone do not establish substantive success, but missing fixtures are a catalog defect.
        registered={x['name'] for x in composition.registry()['skills']}
        fixtures={p.stem for p in (core.ROOT/'evals').glob('*.json')}
        self.assertEqual(registered,fixtures)

    def test_catalog_covers_every_skill_and_method(self):
        data = composition.inventory()
        self.assertEqual(data['method_count'], 34)
        self.assertEqual(data['mapped_method_count'], 34)
        self.assertEqual(data['first_party_skill_count'], 26)
        self.assertIn('jtbd-odi', data['methods_without_first_party_skill'])
        self.assertEqual(len(data['role_definitions']), 7)
        self.assertTrue(all(x['approval_authority'].startswith('none') for x in data['role_definitions']))

    def test_without_explicit_method_does_not_auto_select(self):
        with tempfile.TemporaryDirectory() as td:
            case = self.make_case(Path(td))
            result = composition.compose(case, goals=['discover_need'], evidence='minimal')
            self.assertEqual(result['status'], 'method_selection_required')
            self.assertEqual(result['work_units'], [])
            self.assertTrue(result['method_options'][0]['candidates'])
            self.assertTrue(any(c['readiness'] == 'collect_inputs_first'
                                for c in result['method_options'][0]['candidates']))

    def test_valid_ost_plan_still_cannot_claim_execution(self):
        with tempfile.TemporaryDirectory() as td:
            case = self.make_case(Path(td))
            source=core.add_source(case,'Fictional interview transcript','local:interview-1','interview')
            core.add_claim(case,'Fictional participant reported difficult onboarding',[source['id']])
            result = composition.compose(case, goals=['discover_need'],
                                         method_ids=['opportunity-solution-tree'], evidence='observed')
            unit = result['work_units'][0]
            self.assertEqual(unit['skill_id'], 'opportunity-solution-tree')
            self.assertEqual(unit['role_id'], 'researcher')
            self.assertEqual(unit['status'], 'manual_method_review_required')
            self.assertTrue(unit['manual_execution_only'])
            self.assertEqual(result['status'], 'proposed_not_executed')
            self.assertIn('No agent execution', result['assurance'])

    def test_declared_evidence_without_records_does_not_pass(self):
        with tempfile.TemporaryDirectory() as td:
            case=self.make_case(Path(td))
            unit=composition.compose(case,goals=['discover_need'],
                         method_ids=['opportunity-solution-tree'],evidence='observed')['work_units'][0]
            self.assertEqual(unit['status'],'blocked_for_evidence_or_provider')
            self.assertTrue(any('recorded sources' in b for b in unit['blockers']))

    def test_missing_method_provider_is_explicit(self):
        with tempfile.TemporaryDirectory() as td:
            case = self.make_case(Path(td))
            unit = composition.compose(case, goals=['discover_need'],
                       method_ids=['jtbd-odi'], evidence='verified')['work_units'][0]
            self.assertIsNone(unit['skill_id'])
            self.assertTrue(any('No first-party skill' in b for b in unit['blockers']))
            self.assertEqual(unit['status'], 'blocked_for_evidence_or_provider')

    def test_evidence_requirement_and_gap_cannot_be_bypassed_by_name(self):
        with tempfile.TemporaryDirectory() as td:
            case = self.make_case(Path(td))
            unit = composition.compose(case, goals=['discover_need'],
                     method_ids=['opportunity-solution-tree'], evidence='minimal')['work_units'][0]
            self.assertEqual(unit['status'], 'blocked_for_evidence_or_provider')
            self.assertIn('Requires evidence class observed', unit['blockers'][0])

    def test_multi_domain_plan(self):
        with tempfile.TemporaryDirectory() as td:
            case = self.make_case(Path(td), 'venture')
            result = composition.compose(case, goals=['map_market', 'design_business'],
                     method_ids=['market-sizing', 'business-model-canvas'], evidence='minimal')
            self.assertEqual([x['capability_id'] for x in result['work_units']],
                             ['market-intelligence', 'venture-design'])
            self.assertEqual(len(result['method_options']), 2)
            self.assertEqual(result['selected_method_ids'], ['market-sizing', 'business-model-canvas'])

    def test_wrong_goal_and_unknown_method_rejected(self):
        with tempfile.TemporaryDirectory() as td:
            case = self.make_case(Path(td))
            with self.assertRaises(ValueError):
                composition.compose(case, goals=['map_market'], method_ids=['opportunity-solution-tree'])
            with self.assertRaises(ValueError):
                composition.compose(case, goals=['discover_need'], method_ids=['missing-method'])
            with self.assertRaises(ValueError):
                composition.compose(case, goals=['discover_need','discover_need'])

    def test_requires_objective_and_refuses_unselected_plan_save(self):
        with tempfile.TemporaryDirectory() as td:
            with patch.object(core, 'ENGAGEMENT_ROOT', Path(td)):
                case = core.new_engagement('Empty Brief', 'client')
            with self.assertRaisesRegex(ValueError,'objective'):
                composition.compose(case, goals=['discover_need'])
            core.update_engagement(case, objective='Interview likely buyers')
            with self.assertRaisesRegex(ValueError,'Choose'):
                composition.compose(case, goals=['discover_need'], save=True)
            self.assertFalse((case / 'plans').exists())

    def test_saved_proposals_reproducible_and_not_overwritten(self):
        with tempfile.TemporaryDirectory() as td:
            case = self.make_case(Path(td))
            args = dict(goals=['discover_need'], method_ids=['jtbd-progress'], evidence='minimal', save=True)
            r1=composition.compose(case, **args)
            path1=case / r1['saved_to']
            assert path1.exists()
            original=path1.read_bytes()
            r2=composition.compose(case, **args)
            self.assertEqual(r1['saved_to'],r2['saved_to'])
            core.update_engagement(case, scope='B2B sales segment only')
            r3=composition.compose(case, **args)
            self.assertNotEqual(r3['saved_to'],r2['saved_to'])
            self.assertEqual(path1.read_bytes(),original)
            self.assertNotEqual(r3['context_snapshot']['engagement_sha256'], r2['context_snapshot']['engagement_sha256'])

    def test_corrupted_mapping_fails_closed(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td)
            (root/'config').mkdir()
            source=core.ROOT/'config'
            for name in ('work-composition.json','agent-roles.json','tool-contracts.json',
                         'skills-registry.json','frameworks-v3.json'):
                (root/'config'/name).write_bytes((source/name).read_bytes())
            mapping = json.loads((root/'config'/'work-composition.json').read_text())
            mapping['method_links'][0]['skill_id']='nonexistent-agent-skill'
            (root/'config'/'work-composition.json').write_text(json.dumps(mapping))
            with self.assertRaises(ValueError):
                composition.registry(root)

    def test_roles_do_not_implicitly_gain_external_write(self):
        with tempfile.TemporaryDirectory() as td:
            root=Path(td); (root/'config').mkdir()
            source=core.ROOT/'config'
            for name in ('work-composition.json','agent-roles.json','tool-contracts.json',
                         'skills-registry.json','frameworks-v3.json'):
                (root/'config'/name).write_bytes((source/name).read_bytes())
            roles = json.loads((root/'config'/'agent-roles.json').read_text())
            roles['roles'][0]['allowed_tool_effects'].append('external_write')
            (root/'config'/'agent-roles.json').write_text(json.dumps(roles))
            with self.assertRaisesRegex(ValueError,'Unsafe'):
                composition.registry(root)

    def test_proposals_do_not_call_network_or_models(self):
        with tempfile.TemporaryDirectory() as td:
            case=self.make_case(Path(td))
            before=list(case.iterdir())
            composition.compose(case,goals=['discover_need'],method_ids=['opportunity-solution-tree'], evidence='observed')
            self.assertEqual(before,list(case.iterdir()))


if __name__ == '__main__': unittest.main()
