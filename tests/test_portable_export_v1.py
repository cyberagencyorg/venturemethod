"""Portable distribution is explicit, reproducible, and never overwrites."""
import json
import tempfile
import unittest
from pathlib import Path
from src.va.portable_export import export_skill, verify_export
from src.va.portable import ContractError


class ExportTests(unittest.TestCase):
    def test_dry_run_and_explicit_apply_with_rollback(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / ".agents" / "skills" / "venturemethod"
            planned = export_skill(target)
            self.assertFalse(target.exists())
            self.assertEqual(planned["effects"], [])
            result = export_skill(target, apply=True)
            self.assertTrue((target / "SKILL.md").is_file())
            self.assertTrue((target / "references" / "ADOPT.md").is_file())
            self.assertTrue((target / "assets" / "catalog.json").is_file())
            self.assertTrue((target / "references" / "skills" / "evidence-audit.md").is_file())
            self.assertEqual(result["effects"], ["create_new_skill_directory"])
            self.assertEqual(verify_export(target, expected_bundle_sha256=planned["bundle_sha256"])["status"], "integrity_checked")
            catalog = json.loads((target / "assets" / "catalog.json").read_text())
            self.assertIn("engagement", catalog["capabilities"])
            with self.assertRaises(ContractError):
                export_skill(target, apply=True)

    def test_changed_export_or_unexpected_asset_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            target = Path(temp) / "venturemethod"
            original = export_skill(target, apply=True)
            (target / "references" / "skills" / "evidence-audit.md").write_text("modified")
            with self.assertRaises(ContractError):
                verify_export(target)
            with self.assertRaises(ContractError):
                verify_export(target, expected_bundle_sha256="0"*64)
            (target / "references" / "skills" / "evidence-audit.md").unlink()
            with self.assertRaises(ContractError):
                verify_export(target)

    def test_reject_symlink_and_wrong_target(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            with self.assertRaises(ContractError):
                export_skill(root / "not-venturemethod")
            symlink = root / "external"
            symlink.symlink_to(root, target_is_directory=True)
            with self.assertRaises(ContractError):
                export_skill(symlink / "venturemethod", apply=True)


if __name__ == "__main__":
    unittest.main()
