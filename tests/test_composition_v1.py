"""Multi-domain composition is explicitly justified and does not claim execution."""
import json
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator, ValidationError
import copy
from src.va.composition_v1 import compose
from src.va.portable import ContractError

ROOT=Path(__file__).resolve().parents[1]

def host():
    resources=[{"id":"doc:brief","sha256":"a"*64}]
    def gap(cid,skill,priority,deps=()):
        return {"capability_id":cid,"status":"unmet","priority":priority,
            "reason":f"Existing brief lacks verified {cid} analysis",
            "evidence_refs":["doc:brief"],"skill_id":skill,
            "depends_on":list(deps)}
    return {"schema_version":"1.0.0","project":"multi-domain-host",
        "task":"Assess the market, update product plan, and form a defensible commercial offer",
        "authorization":"host_read_only","resources":resources,"covered_capabilities":[],
        "gaps":[
            gap("engagement","evidence-audit","critical"),
            gap("product","product-requirements","high",["engagement"]),
            gap("commercial","commercial-offer","medium",["product"])
        ]}

class CompositionTests(unittest.TestCase):
    def test_ordered_justified_units_with_zero_effects(self):
        plan=compose(host())
        self.assertEqual(plan["status"],"advisory_composition")
        self.assertEqual([x["capability_id"] for x in plan["units"]],
                         ["engagement","product","commercial"])
        self.assertEqual(plan["effects"],[])
        for item in plan["units"]:
            self.assertEqual(item["unit"]["authorized_effects"],[])
            self.assertEqual(item["unit"]["allowed_tools"],[])
            self.assertEqual(item["unit"]["review"]["status"],"pending")
        self.assertEqual(plan["units"][2]["depends_on"],["product"])
        self.assertEqual(plan["units"][2]["preconditions_covered"],[])
        schema=json.loads((ROOT/"schemas/v1/composition-plan.schema.json").read_text())
        Draft202012Validator(schema).validate(plan)
        ws=json.loads((ROOT/"schemas/v1/work-unit.schema.json").read_text())
        for x in plan["units"]:
            Draft202012Validator(ws).validate(x["unit"])



    def test_structural_verifier_rejects_tampered_identity_and_dependencies(self):
        from src.va.composition_v1 import verify_composition
        source = compose(host())
        self.assertEqual(verify_composition(source)["status"], "verified_advisory_structure")
        for edit in ("tools", "effect", "approval", "reorder", "duplicate", "mismatch"):
            bad = copy.deepcopy(source)
            first = bad["units"][0]
            if edit == "tools":
                first["unit"]["allowed_tools"] = ["shell"]
            elif edit == "effect":
                first["unit"]["authorized_effects"] = ["execute"]
            elif edit == "approval":
                first["unit"]["review"]["status"] = "accepted"
            elif edit == "reorder":
                bad["units"] = bad["units"][::-1]
            elif edit == "duplicate":
                bad["units"][1]["capability_id"] = bad["units"][0]["capability_id"]
            else:
                first["unit"]["host_project"] = "unrelated"
            with self.subTest(edit=edit), self.assertRaises(ContractError):
                verify_composition(bad)

    def test_advisory_schema_rejects_privilege_escalation_and_invalid_unit(self):
        plan = compose(host())
        composition_schema = json.loads((ROOT/"schemas/v1/composition-plan.schema.json").read_text())
        validator = Draft202012Validator(composition_schema)
        validator.validate(plan)
        cases = [
            ("authorized_effects", ["execute"]),
            ("authorized_effects", ["external_write"]),
            ("allowed_tools", ["shell"]),
            ("phase", "arbitrary"),
        ]
        for key, value in cases:
            bad = copy.deepcopy(plan)
            bad["units"][0]["unit"][key] = value
            with self.subTest(key=key, value=value), self.assertRaises(ValidationError):
                validator.validate(bad)
        bad = copy.deepcopy(plan)
        bad["units"][0]["unit"]["review"]["status"] = "accepted"
        with self.assertRaises(ValidationError):
            validator.validate(bad)
        bad = copy.deepcopy(plan)
        bad["units"][0]["unit"]["review"]["required_before_effects"] = False
        with self.assertRaises(ValidationError):
            validator.validate(bad)
        bad = copy.deepcopy(plan)
        bad["units"][0]["unit"]["unexpected"] = "escape"
        with self.assertRaises(ValidationError):
            validator.validate(bad)
        bad = copy.deepcopy(plan)
        bad["units"] = []
        with self.assertRaises(ValidationError):
            validator.validate(bad)
        empty = compose({**host(), "gaps": []})
        validator.validate(empty)
        empty["units"] = copy.deepcopy(plan["units"])
        with self.assertRaises(ValidationError):
            validator.validate(empty)

    def test_advisory_contract_derives_from_canonical_work_schema(self):
        import copy
        comp = json.loads((ROOT/"schemas/v1/composition-plan.schema.json").read_text())
        canonical = json.loads((ROOT/"schemas/v1/work-unit.schema.json").read_text())
        canonical.pop("$id", None)
        canonical.pop("$schema", None)
        canonical["properties"]["allowed_tools"] = {"const": []}
        canonical["properties"]["authorized_effects"] = {"const": []}
        canonical["properties"]["review"]["properties"]["status"] = {"const": "pending"}
        canonical["properties"]["review"]["properties"]["required_before_effects"] = {"const": True}
        self.assertEqual(comp["$defs"]["advisory_work_unit"], canonical)

    def test_limit_includes_dependencies_and_excludes_remaining(self):
        plan=compose(host(),max_units=2)
        self.assertEqual([x["capability_id"] for x in plan["units"]],["engagement","product"])
        self.assertIn({"capability_id":"commercial","reason":"composition_limit"},plan["excluded"])


    def test_host_covered_preconditions_are_preserved_as_assumptions(self):
        h=host()
        h["covered_capabilities"]=["engagement"]
        composed=compose(h)
        self.assertEqual([u["capability_id"] for u in composed["units"]], ["product","commercial"])
        self.assertEqual(composed["units"][0]["preconditions_covered"], ["engagement"])
        self.assertEqual(composed["units"][0]["depends_on"], [])
        self.assertEqual(composed["units"][1]["depends_on"], ["product"])
        schema=json.loads((ROOT/"schemas/v1/composition-plan.schema.json").read_text())
        Draft202012Validator(schema).validate(composed)

    def test_no_op_already_covered_and_unverified(self):
        h=host()
        h["covered_capabilities"]=["engagement","product","commercial"]
        self.assertEqual(compose(h)["status"],"no_intervention")
        h=host()
        h["gaps"]=[]
        self.assertEqual(compose(h)["units"],[])

    def test_cycle_and_missing_dependency_block(self):
        h=host()
        h["gaps"][0]["depends_on"]=["commercial"]
        with self.assertRaises(ContractError):
            compose(h)
        h=host()
        h["gaps"][1]["depends_on"]=["sales-operations"]
        plan=compose(h)
        self.assertTrue(any(x["reason"]=="unresolved_prerequisite" for x in plan["excluded"]))

    def test_reject_unreasonably_large_or_boolean_limit(self):
        for amount in (True, 0, 9):
            with self.assertRaises(ContractError):
                compose(host(),max_units=amount)

if __name__=="__main__":
    unittest.main()
