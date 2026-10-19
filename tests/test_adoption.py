"""Test reading Venture Method as an external, optional reference."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.va import adoption, core
from va import main


class AdoptionTests(unittest.TestCase):
    def test_method_examples_exist_and_support_declared_goals(self):
        from src.va import methodology
        catalog={m['id']:m for m in methodology.load_catalog()}
        for domain, ids in adoption.DOMAIN_EXAMPLES.items():
            self.assertIn(domain, adoption.DOMAIN_GOALS)
            for ident in ids:
                self.assertIn(ident, catalog)
                self.assertIn(adoption.DOMAIN_GOALS[domain], catalog[ident]['goals'])

    def test_manifest_has_real_entrypoints(self):
        data = adoption.manifest()
        self.assertEqual(data['name'], "Khan's Venture Method Framework")
        self.assertEqual(data['entrypoints']['adoption'], 'ADOPT.md')
        self.assertIn('ongoing_engagement', data['adoption_modes'])

    def test_midstream_product_task_never_activates_workflow(self):
        result = adoption.orient('Improve product discovery based on customer research', phase='in-flight')
        self.assertEqual(result['state'], 'read_only')
        self.assertEqual(result['phase'], 'in-flight')
        self.assertIn('project', result['guidance'])
        self.assertTrue(all((core.ROOT / s['instruction_path']).is_file() for s in result['suggested_skills']))
        self.assertTrue(all(not m['executed'] for m in result['method_candidates']))
        self.assertLessEqual(len(result['suggested_skills']), 4)

    def test_generic_task_does_not_invent_applicable_methods(self):
        result=adoption.orient('Clarify this paragraph without changing facts')
        self.assertEqual(result['matched_domains'],[])
        self.assertEqual(result['suggested_skills'],[])
        self.assertEqual(result['method_candidates'],[])
        self.assertIn('No specific domain', adoption.markdown(result))

    def test_adoption_does_not_create_engagement_or_touch_project(self):
        with tempfile.TemporaryDirectory() as temp:
            target=Path(temp)
            original=target/'PROJECT.md'
            original.write_text('Accepted scope and requirements')
            with patch.object(core, 'ENGAGEMENT_ROOT', target/'engagements'):
                adoption.orient('Evaluate competitor market strategy')
            self.assertEqual(original.read_text(),'Accepted scope and requirements')
            self.assertEqual(sorted(x.name for x in target.iterdir()),['PROJECT.md'])

    def test_user_input_and_options_are_validated(self):
        for task in ('', '   ', 'x'*4001):
            with self.assertRaises(ValueError): adoption.orient(task)
        with self.assertRaises(ValueError): adoption.orient('Research',phase='future')
        with self.assertRaises(ValueError): adoption.orient('Research',limit=0)

    def test_cli_plain_and_json_without_engagement(self):
        for args in (['adopt','--task','Review a market strategy','--phase','review'],
                     ['adopt','--task','Review a market strategy','--json']):
            out=io.StringIO()
            with contextlib.redirect_stdout(out):
                status=main(args)
            self.assertEqual(status,0)
            self.assertNotIn('engagement_id',out.getvalue())
            if '--json' in args:
                self.assertEqual(json.loads(out.getvalue())['state'],'read_only')
            else:
                self.assertIn('selective use',out.getvalue())

    def test_paths_and_pointers_are_non_executable(self):
        result=adoption.orient('Prepare venture investment diligence', phase='review')
        self.assertEqual(result['effect'],'No files read from or written to the host project. No engagement created.')
        self.assertTrue(result['suggested_skills'])
        self.assertFalse('automated' in adoption.markdown(result).lower() and 'validated' in adoption.markdown(result).lower())


if __name__=='__main__': unittest.main()
