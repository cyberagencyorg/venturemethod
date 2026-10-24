"""Check external discovery is useful yet never mistaken for execution."""
import json
import unittest
from pathlib import Path
from jsonschema import Draft202012Validator
from src.va.portable import catalog_search, catalog, ContractError

ROOT=Path(__file__).resolve().parents[1]

class DiscoveryTests(unittest.TestCase):
    def test_search_by_skill_and_by_method_reaches_correct_capability(self):
        cases = [
            ("evidence-audit", "engagement", "evidence-audit", None),
            ("product-requirements", "product", "product-requirements", None),
            ("wardley-mapping", "strategy", None, "wardley-mapping"),
            ("opportunity-solution-tree", "customer-discovery",
             "opportunity-solution-tree", "opportunity-solution-tree"),
            ("commercial-offer", "commercial", "commercial-offer", None),
        ]
        for query, capability, skill, method in cases:
            with self.subTest(query=query):
                result=catalog_search(query)
                matching=next((x for x in result["matches"] if x["id"]==capability),None)
                self.assertIsNotNone(matching, f"No indexed match for {query}")
                if skill:
                    self.assertIn(skill,matching["matched_skill_ids"])
                if method:
                    self.assertIn(method,matching["matched_method_ids"])
                self.assertIn("do not establish",result["note"])

    def test_no_match_and_strict_limit(self):
        self.assertEqual(catalog_search("zxqynevermatched")["matches"], [])
        self.assertEqual(len(catalog_search("product",1)["matches"]),1)
        for value in (0,21,True,"3"):
            with self.assertRaises(ContractError):
                catalog_search("product",value)

    def test_response_validates_canonical_json_schema(self):
        schema=json.loads((ROOT/"schemas/v1/discovery.schema.json").read_text())
        checker=Draft202012Validator(schema)
        for query in ("evidence audit","Wardley mapping","marketing operations","customer discovery"):
            checker.validate(catalog_search(query))
        catalogue=catalog()
        results=catalog_search("discovery")
        for candidate in results["matches"]:
            capability=catalogue["capabilities"][candidate["id"]]
            self.assertTrue(set(candidate["matched_skill_ids"]).issubset(set(capability["eligible_skill_ids"])))

if __name__=="__main__":
    unittest.main()
