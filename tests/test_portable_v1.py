"""Security and contract tests for selective external adoption."""
import hashlib
import json
import os
import tempfile
import unittest
from pathlib import Path

from src.va import portable
from src.va.portable_cli import main


def file_ref(label, text):
    return {"id": label, "sha256": hashlib.sha256(text.encode()).hexdigest(), "text": text}


def state(gaps=None, covered=None):
    return {
        "schema_version": "1.0.0", "project": "external-test",
        "task": "Review existing product material and decide whether to intervene",
        "authorization": "host_read_only",
        "resources": [file_ref("file:README.md", "Product spec exists; evidence appendix is incomplete")],
        "gaps": gaps or [], "covered_capabilities": covered or [],
    }


def gap(cid="engagement", status="unmet", refs=None, priority="high"):
    return {"capability_id": cid, "status": status, "priority": priority,
            "reason": "A material claim lacks verifiable source reference",
            "evidence_refs": refs if refs is not None else ["file:README.md"],
            **({"skill_id": "evidence-audit"} if cid == "engagement" else
               {"skill_id": "product-requirements"} if cid == "product" else {})}


class PortableV1Tests(unittest.TestCase):
    def test_catalog_resolves_and_records_nonexecution(self):
        c = portable.catalog()
        self.assertIn("engagement", c["capabilities"])
        for cap in c["capabilities"].values():
            for sid in cap["eligible_skill_ids"]:
                self.assertIn(sid, c["skills"])
        self.assertFalse(portable.method_get("opportunity-solution-tree")["verified_in_runtime"])
        self.assertIn("SKILL.md", portable.skill_get("evidence-audit")["path"])

    def test_explicit_no_op_for_no_gap_and_already_covered(self):
        self.assertEqual(portable.assess(state())["decision"], "none")
        self.assertEqual(portable.assess(state([gap()], ["engagement"]))["decision"], "none")
        self.assertEqual(portable.assess(state([gap(status="uncertain")]))["decision"], "none")
        self.assertEqual(portable.assess(state([gap(refs=[])]))["decision"], "none")
        self.assertEqual(portable.assess(state([gap("sales-operations")]))["decision"], "none")
        ambiguous = gap()
        ambiguous.pop("skill_id")
        self.assertEqual(portable.assess(state([ambiguous]))["decision"], "none")

    def test_evidenced_capability_is_advisory_with_no_effects(self):
        result = portable.assess(state([gap()]))
        self.assertEqual(result["decision"], "consult")
        self.assertEqual(result["selected"]["capability_id"], "engagement")
        self.assertFalse(result["selected"]["execution_verified"])
        self.assertEqual(result["effects"], [])
        self.assertEqual(result["host_authority"], "retained")

    def test_priority_stable_and_bounded_to_one(self):
        result = portable.assess(state([gap("product", priority="low"), gap("engagement", priority="critical")]))
        self.assertEqual(result["selected"]["capability_id"], "engagement")
        self.assertEqual(len(result["exclusions"]), 1)
        self.assertEqual(result["exclusions"][0]["reason"], "lower_priority")

    def test_reject_unscoped_or_unfounded_context(self):
        invalid = state([gap(refs=["file:does-not-exist"])])
        with self.assertRaises(portable.ContractError):
            portable.assess(invalid)
        invalid = state()
        invalid["authorization"] = "trust_me"
        with self.assertRaises(portable.ContractError):
            portable.assess(invalid)
        invalid = state()
        invalid["resources"][0]["sha256"] = "fake"
        with self.assertRaises(portable.ContractError):
            portable.assess(invalid)
        invalid = state([gap()])
        invalid["resources"][0]["sha256"] = "a" * 64
        with self.assertRaises(portable.ContractError):
            portable.assess(invalid)
        invalid = state([gap()])
        invalid["gaps"][0]["skill_id"] = "commercial-offer"
        with self.assertRaises(portable.ContractError):
            portable.assess(invalid)

    def test_no_file_mutation_or_symlink_escape(self):
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as outside:
            p = Path(tmp)
            (p / "README.md").write_text("ok", encoding="utf-8")
            (p / "secret").symlink_to(Path(outside), target_is_directory=True)
            before = list(p.iterdir())
            inspected = portable.inspect_paths(p, ["README.md"])
            self.assertEqual(len(inspected), 1)
            self.assertEqual(list(p.iterdir()), before)
            for bad in ["../README.md", "/etc/passwd", "secret/protected", "README.md/../../x"]:
                with self.assertRaises((portable.ContractError, OSError, ValueError)):
                    portable.inspect_paths(p, [bad])

    def test_reject_duplicate_conflicting_gaps_and_fabricated_quotes(self):
        duplicate = state([gap(), gap(status="covered")])
        with self.assertRaises(portable.ContractError):
            portable.assess(duplicate)
        anchored = gap()
        anchored["evidence_quotes"] = [{
            "resource_id": "file:README.md",
            "quote": "evidence appendix is incomplete"
        }]
        result = portable.assess(state([anchored]))
        self.assertEqual(result["selected"]["evidence_verification"], "excerpt_matched")
        anchored["evidence_quotes"][0]["quote"] = "The customer interviews prove unanimous support"
        with self.assertRaises(portable.ContractError):
            portable.assess(state([anchored]))

    def test_reject_fifo_and_inner_symlink(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "source.md").write_text("expected")
            (root / "sub").mkdir()
            (root / "sub" / "link.md").symlink_to(root / "source.md")
            with self.assertRaises((portable.ContractError, OSError)):
                portable.inspect_paths(root, ["sub/link.md"])
            if hasattr(os, "mkfifo"):
                os.mkfifo(root / "pipe")
                with self.assertRaises((portable.ContractError, OSError)):
                    portable.inspect_paths(root, ["pipe"])

    def test_binary_and_oversize_denied(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            (p / "binary").write_bytes(b"\x00abc")
            (p / "big").write_bytes(b"z" * (portable.MAX_DOCUMENT_BYTES + 1))
            for name in ("binary", "big"):
                with self.assertRaises(portable.ContractError):
                    portable.inspect_paths(p, [name])

    def test_ref_only_context_pack_without_automatic_changes(self):
        packet = portable.context_pack(state([gap()]))
        self.assertIn("SKILL.md", packet["assessment"]["selected"]["instruction_path"])
        self.assertTrue(packet["instructions"])
        self.assertNotIn("secret token", json.dumps(packet))
        self.assertEqual(portable.context_pack(state())["assessment"]["decision"], "none")
        with self.assertRaises(portable.ContractError):
            portable.context_pack(state(), max_chars=10)

    def test_cli_missing_context_fails_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            self.assertEqual(main(["assess", str(Path(tmp) / "not-present.json")]), 2)

    def test_contracts_validate_both_adoption_states(self):
        from jsonschema import Draft202012Validator
        root = Path(__file__).parents[1] / "schemas" / "v1"
        for name, obj in (("host-state", state([gap()])),
                          ("adoption-decision", portable.assess(state([gap()]))),
                          ("adoption-decision", portable.assess(state()))):
            schema = json.loads((root / f"{name}.schema.json").read_text())
            Draft202012Validator.check_schema(schema)
            Draft202012Validator(schema).validate(obj)
        from src.va.portable import catalog
        c = catalog()
        for method in c["methods"].values():
            Draft202012Validator(json.loads((root / "method.schema.json").read_text())).validate(method)
        for cap in c["capabilities"].values():
            Draft202012Validator(json.loads((root / "capability.schema.json").read_text())).validate(cap)


if __name__ == "__main__":
    unittest.main()
