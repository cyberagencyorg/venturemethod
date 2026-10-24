"""Exercise actual bounded host files through snapshot, explicit proposal and no-op."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from src.va.portable import snapshot_project, propose_gap, assess, context_pack, ContractError


class HostAdoptionFlowTests(unittest.TestCase):
    def test_in_flight_snapshot_no_op_then_one_source_grounded_intervention(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "README.md").write_text(
                "An accepted product specification exists and implementation is in flight.",
                encoding="utf-8")
            (root / "proposal.md").write_text(
                "Proposed expansion. The proposal uses unsourced figures. "
                "Existing accepted requirements should remain unchanged.",
                encoding="utf-8")
            before = {(p.name, p.read_bytes()) for p in root.iterdir() if p.is_file()}
            state = snapshot_project(project="active-product", task="Audit a new claim in an existing spec",
                                     root=root, paths=["README.md", "proposal.md"])
            self.assertEqual(assess(state)["decision"], "none")
            plan = propose_gap(
                state, capability_id="engagement", skill_id="evidence-audit",
                resource_id="file:proposal.md", quote="The proposal uses unsourced figures",
                reason="A proposed decision rests on an unsourced market figure")
            self.assertEqual(plan["assessment"]["decision"], "consult")
            self.assertEqual(plan["assessment"]["selected"]["skill_id"], "evidence-audit")
            self.assertEqual(plan["assessment"]["selected"]["evidence_verification"], "excerpt_matched")
            self.assertIn("Evidence Audit", context_pack(plan["proposed_host_state"])["instructions"])
            self.assertEqual(assess(state)["decision"], "none")
            self.assertEqual(before, {(p.name, p.read_bytes()) for p in root.iterdir() if p.is_file()})
            with self.assertRaises(ContractError):
                propose_gap(plan["proposed_host_state"], capability_id="engagement",
                            skill_id="evidence-audit", resource_id="file:proposal.md",
                            quote="The proposal uses unsourced figures", reason="duplicate")
            with self.assertRaises(ContractError):
                propose_gap(state, capability_id="engagement", skill_id="evidence-audit",
                            resource_id="file:proposal.md", quote="fabricated external evidence",
                            reason="not supported")

    def test_existing_coverage_remains_authoritative(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "accepted.md").write_text("All requested acceptance checks are complete.")
            state = snapshot_project(project="complete", task="Keep the accepted behavior",
                                     root=root, paths=["accepted.md"])
            state["covered_capabilities"] = ["product"]
            out = propose_gap(state, capability_id="product", skill_id="product-requirements",
                              resource_id="file:accepted.md", quote="All requested acceptance checks",
                              reason="Request a new PRD")
            self.assertEqual(out["assessment"]["decision"], "none")
            self.assertEqual(out["assessment"]["exclusions"][0]["reason"], "already_covered")


if __name__ == "__main__":
    unittest.main()
