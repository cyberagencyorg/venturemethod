import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.va import core, ledger, ost, demo


class DemoTests(unittest.TestCase):
    def test_end_to_end_synthetic_loop(self):
        with tempfile.TemporaryDirectory() as td:
            with patch.object(core, 'ENGAGEMENT_ROOT', Path(td)):
                result = demo.build('Fictional Harbor Supplies Demo')
                case = Path(result['path'])
                self.assertTrue(result['fictional'])
                self.assertIn(result['decision'], result['downstream_record_ids'])
                self.assertTrue(result['affected_ost_nodes'])
                self.assertEqual(result['original_decision_still_references'], result['original_claim'])
                self.assertNotEqual(result['before_brief'], result['after_brief'])
                self.assertTrue(Path(result['before_brief']).exists())
                self.assertTrue(Path(result['after_brief']).exists())
                self.assertEqual(len(core.read_json(case / 'decisions.json')), 1)
                self.assertEqual(core.read_json(case / 'decisions.json')[0]['claim_ids'], [result['original_claim']])
                self.assertTrue(ledger.verify(case)['passed'])
                self.assertTrue(ost.verify(case)['passed'])
                with self.assertRaises(FileExistsError):
                    demo.build('Fictional Harbor Supplies Demo')

    def test_reject_non_fictional_label(self):
        with tempfile.TemporaryDirectory() as td:
            with patch.object(core, 'ENGAGEMENT_ROOT', Path(td)):
                with self.assertRaises(ValueError):
                    demo.build('Real client name')
                self.assertFalse(list(Path(td).iterdir()))


if __name__ == '__main__':
    unittest.main()
