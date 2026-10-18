import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from src.va import core

class CoreTests(unittest.TestCase):
    def test_slugs_are_restricted(self):
        self.assertEqual(core.slugify("Acme / Discovery"), "acme-discovery")
        for s in ("..", "!!!", " / "):
            with self.assertRaises(ValueError): core.slugify(s)
    def test_engagement_lifecycle_and_quality(self):
        with tempfile.TemporaryDirectory() as d, patch.object(core, "ENGAGEMENT_ROOT", Path(d)):
            case = core.new_engagement("Acme Test", "client")
            self.assertEqual(core.plan(case)["recommended_skills"][0], "intake-scoping")
            self.assertFalse(core.quality_check(case)["ready_for_review"])
            engagement = core.read_json(case / "engagement.json")
            engagement["objective"] = "Evaluate a documented operational problem"
            core.write_json(case / "engagement.json", engagement)
            src = core.add_source(case, "Interview", "local:transcript-1", "interview")
            claim = core.add_claim(case, "Operations manager reports rework", [src["id"]])
            decision = core.add_decision(case, "Investigate?", "Conduct interviews", [claim["id"]])
            self.assertEqual(decision["id"], "DEC-0001")
            self.assertTrue(core.quality_check(case)["ready_for_review"])
            self.assertIn("CLM-0001", core.report(case))
    def test_broken_reference_fails_check(self):
        with tempfile.TemporaryDirectory() as d, patch.object(core, "ENGAGEMENT_ROOT", Path(d)):
            case = core.new_engagement("Bad ref", "venture")
            e = core.read_json(case / "engagement.json"); e["objective"] = "Test"
            core.write_json(case / "engagement.json", e)
            with self.assertRaises(ValueError):
                core.add_claim(case, "Unsupported", ["SRC-9999"])
            src = core.add_source(case, "Notes", "local:a", "memo")
            core.add_claim(case, "Supported reference", [src["id"]])
            path = case / "claims.json"
            claims = core.read_json(path)
            claims[0]["source_ids"] = ["SRC-9999"]
            core.write_json(path, claims)
            self.assertTrue(core.quality_check(case)["blockers"])
    def test_skill_contracts(self):
        self.assertTrue(core.validate_skills()["passed"], core.validate_skills())

if __name__ == "__main__": unittest.main()
