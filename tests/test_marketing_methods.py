"""Structural and routing tests for reusable positioning, voice and copy skills.

These tests do not establish writing quality or live agent improvements.
"""
import json
import unittest
from pathlib import Path

from src.va import adoption, composition, methodology, routing
from src.va.core import ROOT

SKILLS = (
    "marketing-context",
    "competitive-positioning",
    "marketing-copywriting",
    "brand-voice-preservation",
    "copy-editing",
    "human-writing-audit",
)


class MarketingMethodTests(unittest.TestCase):
    def test_each_skill_is_registered_and_has_a_real_instruction_and_eval(self):
        registry = json.loads((ROOT / "config/skills-registry.json").read_text())
        skills = {entry["name"]: entry for entry in registry["skills"]}
        for name in SKILLS:
            self.assertIn(name, skills)
            file = ROOT / skills[name]["path"] / "SKILL.md"
            self.assertTrue(file.is_file(), file)
            text = file.read_text()
            self.assertIn("name: " + name, text)
            self.assertIn("##", text)
            suite = json.loads((ROOT / "evals" / (name + ".json")).read_text())
            self.assertEqual(suite["skill"], name)
            self.assertEqual(suite["status"], "fixture_requires_live_agent_comparison")
            self.assertGreaterEqual(len(suite["tests"]), 3)

    def test_method_and_capability_are_consistent(self):
        methods = {entry["id"]: entry for entry in methodology.load_catalog()}
        key = "competitive-positioning-alternatives-first"
        self.assertIn(key, methods)
        self.assertIn("choose_strategy", methods[key]["goals"])
        self.assertFalse(methods[key]["verified_in_runtime"])
        composition.registry()

    def test_positioning_adoption_points_to_real_method_and_skill(self):
        data = adoption.orient(
            "Positioning for a new agency relative to buyer alternatives",
            phase="in-flight",
        )
        self.assertIn("positioning", [domain["domain"] for domain in data["matched_domains"]])
        self.assertIn("competitive-positioning", [x["id"] for x in data["suggested_skills"]])
        self.assertIn(
            "competitive-positioning-alternatives-first",
            [x["id"] for x in data["method_candidates"]],
        )
        self.assertEqual(data["effect"], "No files read from or written to the host project. No engagement created.")

    def test_copy_and_voice_tasks_can_be_discovered_without_forcing_every_skill(self):
        copy = adoption.orient("Write homepage copy for an AI services agency", limit=4)
        self.assertIn("marketing-copywriting", [x["id"] for x in copy["suggested_skills"]])
        edit = adoption.orient("Polish an existing bio preserving the author's voice", limit=4)
        edit_ids = [x["id"] for x in edit["suggested_skills"]]
        self.assertIn("brand-voice-preservation", edit_ids)
        self.assertIn("copy-editing", edit_ids)
        self.assertNotIn("marketing-copywriting", edit_ids)
        self.assertLessEqual(len(edit_ids), 4)

    def test_unrelated_text_does_not_trigger_marketing(self):
        data = adoption.orient("Clarify this paragraph without changing facts")
        self.assertEqual(data["suggested_skills"], [])
        self.assertEqual(data["matched_domains"], [])

    def test_templates_exist_without_project_private_data(self):
        for path in ("templates/marketing-context.md", "templates/copy-review-checklist.md"):
            self.assertTrue((ROOT / path).is_file())
        text = (ROOT / "templates/marketing-context.md").read_text()
        self.assertIn("Rejected phrase", text)
        self.assertIn("Document version", text)


if __name__ == "__main__":
    unittest.main()
