"""Typed composition must refuse to transform advisory metadata into execution rights."""
import json
import tempfile
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator
from src.va.portable import provider_catalog, work_plan, ContractError, snapshot_project, propose_gap

ROOT = Path(__file__).resolve().parents[1]

class WorkPlanTests(unittest.TestCase):
    def test_typed_records_and_maturity(self):
        providers=provider_catalog()
        schema=json.loads((ROOT/"schemas/v1/provider.schema.json").read_text())
        validate=Draft202012Validator(schema)
        self.assertEqual(len(providers), 26)
        for item in providers.values():
            validate.validate(item)
            self.assertFalse(item["maturity"]["installed"])
            self.assertFalse(item["maturity"]["executed"])
            self.assertFalse(item["maturity"]["independently_evaluated"])
            self.assertEqual(item["permissions"]["effects"], ["read"])

    def test_real_host_context_to_typed_non_executable_work_unit(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp)
            (root/"proposal.md").write_text("The proposal lacks customer evidence.", encoding="utf-8")
            host=snapshot_project(project="active-product",
                task="Identify the unmet evidence requirement",
                root=root,paths=["proposal.md"])
            self.assertEqual(work_plan(host)["status"], "no_intervention")
            reviewed=propose_gap(host,capability_id="engagement",
                skill_id="evidence-audit",
                resource_id="file:proposal.md",
                quote="proposal lacks customer evidence",
                reason="A proposed product claim has no supporting customer evidence")
            prepared=work_plan(reviewed["proposed_host_state"])
            self.assertEqual(prepared["status"], "proposal_only")
            unit=prepared["work_unit"]
            Draft202012Validator(json.loads((ROOT/"schemas/v1/work-unit.schema.json").read_text())).validate(unit)
            self.assertEqual(unit["phase"], "unknown")
            self.assertEqual(unit["authorized_effects"], [])
            self.assertEqual(unit["allowed_tools"], [])
            self.assertEqual(unit["review"]["status"], "pending")
            self.assertEqual(unit["selected_capabilities"], ["engagement"])
            self.assertFalse(any("client" in x for x in unit["outputs"]))


if __name__=="__main__":
    unittest.main()
