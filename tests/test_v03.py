import unittest
from pathlib import Path
from src.va import methodology

class V03MethodologyTests(unittest.TestCase):
    def test_catalog_is_valid(self):
        self.assertGreaterEqual(len(methodology.load_catalog()),30)
    def test_mutually_distinct_jtbd_schools(self):
        entries={m['id']:m for m in methodology.load_catalog()}
        self.assertNotEqual(entries['jtbd-progress']['output'],entries['jtbd-odi']['output'])
    def test_evidence_gate_not_claimed_as_execution(self):
        r=methodology.compare('measure_outcomes', 'minimal')
        exp={e['id']:e for e in r['candidates']}
        self.assertEqual(exp['ab-testing']['readiness'],'collect_inputs_first')
        self.assertFalse(exp['ab-testing']['runtime_validated'])
    def test_exploratory_methods_remain_possible(self):
        r=methodology.compare('test_uncertainty','minimal')
        exp={e['id']:e for e in r['candidates']}
        self.assertEqual(exp['risk-assumption-map']['readiness'],'explore/apply')
    def test_goal_is_explicit(self):
        with self.assertRaises(ValueError):
            methodology.compare('everything')
    def test_invalid_metadata_fails_closed(self):
        bad=Path('/tmp/va-invalid-frameworks.json')
        try:
            bad.write_text('{"schema_version":"0.3","items":[{"id":"x","title":"x"}]}')
            with self.assertRaises(ValueError):
                methodology.load_catalog(bad)
        finally: bad.unlink(missing_ok=True)
    def test_no_automatic_winner(self):
        r=methodology.compare('choose_strategy','observed')
        self.assertNotIn('recommended_method',r)
        self.assertGreater(r['candidate_count'],1)
if __name__=='__main__': unittest.main()
