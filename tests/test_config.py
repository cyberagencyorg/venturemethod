import json
import unittest
from pathlib import Path
from src.va.core import ROOT, BUNDLES, PROFILES, TYPES

class ConfigTests(unittest.TestCase):
    def test_every_recommended_skill_exists(self):
        for group in BUNDLES.values():
            for skill in group:
                self.assertTrue((ROOT / 'skills' / skill / 'SKILL.md').is_file(), skill)
    def test_every_type_has_bundle(self):
        self.assertEqual(set(TYPES), set(BUNDLES))
    def test_modes_are_distinct(self):
        self.assertLess(len(PROFILES['quick']),len(PROFILES['standard']))
        self.assertLess(len(PROFILES['standard']),len(PROFILES['deep']))
    def test_methods_include_selection_cautions(self):
        data=json.loads((ROOT / 'config' / 'methods.json').read_text())
        self.assertGreaterEqual(len(data),10)
        for method in data:
            self.assertTrue(method['reference'].startswith('https://'))
            self.assertTrue(method['avoid_when'])

if __name__=='__main__': unittest.main()
