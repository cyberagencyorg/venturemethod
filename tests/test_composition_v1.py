"""Multi-domain composition is explicitly justified and does not claim execution."""
import json
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator
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
        schema=json.loads((ROOT/"schemas/v1/composition-plan.schema.json").read_text())
        Draft202012Validator(schema).validate(plan)
        ws=json.loads((ROOT/"schemas/v1/work-unit.schema.json").read_text())
        for x in plan["units"]:
            Draft202012Validator(ws).validate(x["unit"])

    def test_limit_includes_dependencies_and_excludes_remaining(self):
        plan=compose(host(),max_units=2)
        self.assertEqual([x["capability_id"] for x in plan["units"]],["engagement","product"])
        self.assertIn({"capability_id":"commercial","reason":"composition_limit"},plan["excluded"])

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
