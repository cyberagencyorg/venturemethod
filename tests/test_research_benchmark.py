"""Prepared evaluations require a named reviewer, ratings, and unchanged packets."""
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from src.va import core,research_benchmark

class BenchmarkTests(unittest.TestCase):
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        root=Path(self.tmp.name)
        with patch.object(core,'ENGAGEMENT_ROOT',root):
            self.case=core.new_engagement('Research comparison','company','other','quick')
        self.a=root/'simple.md';self.a.write_text('Baseline report with incomplete evidence.')
        self.b=root/'detailed.md';self.b.write_text('Alternative report describing evidence and assumptions.')

    def run_prep(self):
        return research_benchmark.prepare(self.case,baseline=self.a,candidate=self.b,
                            question='Is the evidence sufficient for a pilot?')

    def fill(self,home):
        review=core.read_json(home/'review.json')
        review['reviewer']='External reviewer'
        review['independent_reviewer']=True
        for label in ('A','B'):
            review['ratings'][label]={dim:3 for dim in research_benchmark.DIMENSIONS}
            review['justifications'][label]='Examined evidence and alternative analyses'
        core.write_json(home/'review.json',review)
        return review

    def test_no_automatic_quality_score(self):
        home=Path(self.run_prep()['workspace'])
        self.assertTrue((home/'A.md').is_file() and (home/'B.md').is_file())
        result=research_benchmark.summarize(home)
        self.assertEqual(result['status'],'incomplete')
        self.assertIsNone(result['candidate_average'])

    def test_manual_scoring_and_blinding_flag(self):
        home=Path(self.run_prep()['workspace'])
        review=self.fill(home)
        result=research_benchmark.summarize(home)
        self.assertEqual(result['status'],'externally_scored_identity_unverified')
        self.assertEqual(result['difference'],0)
        review['reviewer_had_access_to_key']=True
        core.write_json(home/'review.json',review)
        self.assertEqual(research_benchmark.summarize(home)['status'],'incomplete')

    def test_modified_packet_disqualifies_comparison(self):
        home=Path(self.run_prep()['workspace']);self.fill(home)
        (home/'A.md').write_text('tampered report')
        self.assertEqual(research_benchmark.summarize(home)['status'],'incomplete')

    def test_bool_is_not_a_numeric_rating(self):
        home=Path(self.run_prep()['workspace'])
        review=self.fill(home)
        review['ratings']['A']['reasoning']=True
        core.write_json(home/'review.json',review)
        self.assertEqual(research_benchmark.summarize(home)['status'],'incomplete')

    def test_identical_reports_are_not_valid_comparison(self):
        self.b.write_bytes(self.a.read_bytes())
        with self.assertRaisesRegex(ValueError,'Identical'):
            self.run_prep()

    def test_symlink_inputs_rejected(self):
        self.b.unlink();self.b.symlink_to(self.a)
        with self.assertRaises(ValueError):
            self.run_prep()

    def test_corrupt_evidence_prevents_benchmark(self):
        (self.case/'events.jsonl').write_text('bad event\n')
        with self.assertRaises(ValueError):
            self.run_prep()

if __name__=='__main__': unittest.main()
