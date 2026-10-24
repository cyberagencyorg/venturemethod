"""Contract suite for metadata, provider maturity, evidence and work boundaries."""
import json
import unittest
from pathlib import Path

from jsonschema import Draft202012Validator, ValidationError
from src.va.portable import catalog

SCHEMAS = Path(__file__).parents[1] / "schemas" / "v1"


def validator(name):
    data = json.loads((SCHEMAS / f"{name}.schema.json").read_text(encoding="utf8"))
    Draft202012Validator.check_schema(data)
    return Draft202012Validator(data)


class ExtendedContractTests(unittest.TestCase):
    def test_every_registered_skill_matches_canonical_schema(self):
        v = validator("skill")
        for skill in catalog()["skills"].values():
            v.validate(skill)

    def test_provider_status_has_semantics_not_one_misleading_flag(self):
        provider = {
            "schema_version": "1.0.0", "id": "product-skill", "kind": "first_party_skill",
            "version": "0.1.0", "license": "internal", "source": "skills/product-requirements",
            "capability_ids": ["product"], "skill_ids": ["product-requirements"],
            "permissions": {"effects": ["read"], "scopes": []},
            "maturity": {"specified": True, "available": True, "installed": False,
                         "executed": False, "independently_evaluated": False}
        }
        v = validator("provider")
        v.validate(provider)
        provider["maturity"]["independently_evaluated"] = True
        with self.assertRaises(ValidationError):
            v.validate(provider)

    def test_evidence_and_work_accept_precise_status_only(self):
        evidence = {
            "schema_version": "1.0.0", "id": "source-claim", "source_id": "document-1",
            "source_sha256": "0"*64, "collected_at": "2026-10-24T12:00:00Z",
            "status": "unknown", "kind": "publisher_assertion",
            "sensitivity": "confidential", "statement": "Unverified client claim",
            "support_refs": []
        }
        validator("evidence").validate(evidence)
        unit = {
            "schema_version": "1.0.0", "id": "review-proposal",
            "host_project": "sample", "objective": "Review unsupported claims",
            "phase": "in_flight", "existing_artifacts": ["document-1"],
            "selected_capabilities": ["engagement"], "allowed_tools": [],
            "authorized_effects": ["read"], "review": {
                "owner": "host", "status": "pending", "required_before_effects": True
            }, "stop_when": "Sources evaluated and remaining gaps disclosed",
            "outputs": ["advisory"]
        }
        validator("work-unit").validate(unit)
        unit["authorized_effects"] = ["unbounded_write"]
        with self.assertRaises(ValidationError):
            validator("work-unit").validate(unit)


if __name__ == "__main__":
    unittest.main()
