"""Tests for project-owned, read-only copy rules."""
import unittest

from src.va.copy_guard import check, validate_rules


class CopyGuardTests(unittest.TestCase):
    def test_phrase_matches_ignoring_case_and_whitespace(self):
        rules = {
            "schema_version": "1.0",
            "forbidden_phrases": ["an invented generic closer"],
            "forbidden_characters": [],
        }
        self.assertEqual(
            check("We end with AN   INVENTED GENERIC CLOSER here.", rules),
            [{"kind": "forbidden_phrase", "rule": 1}],
        )

    def test_does_not_erase_authority_or_modify_draft(self):
        text = "Preserve the source author and their actual position."
        rules = {"schema_version": "1.0", "forbidden_phrases": [], "forbidden_characters": []}
        self.assertEqual(check(text, rules), [])
        self.assertEqual(text, "Preserve the source author and their actual position.")

    def test_punctuation_rules(self):
        rules = {"schema_version": "1.0", "forbidden_phrases": [], "forbidden_characters": ["em_dash"]}
        self.assertEqual(check("An example" + chr(0x2014) + "another.", rules),
                         [{"kind": "forbidden_character", "rule": "em_dash"}])

    def test_bad_rules_fail_closed(self):
        for rules in (
            {}, {"schema_version": "0.9"},
            {"schema_version": "1.0", "forbidden_phrases": [""]},
            {"schema_version": "1.0", "forbidden_characters": ["arbitrary"]},
        ):
            with self.assertRaises(ValueError):
                validate_rules(rules)


if __name__ == "__main__":
    unittest.main()
