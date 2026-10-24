"""The evaluator must reject incomplete or self-reviewed records."""
import hashlib
import json
import tempfile
import unittest
from pathlib import Path

from src.va.portable_eval import verify, EvaluationError, CRITERIA, CASE_IDS


class PortableEvaluationTests(unittest.TestCase):
    def make_pair(self, root: Path):
        ids = ("builder", "provider")
        runs, ratings = [], {}
        for index, name in enumerate(CASE_IDS):
            runtime = "Codex" if index % 2 == 0 else "Hermes"
            pairs = {}
            score_pair = {}
            for b in ("A", "B"):
                folder = root / name / b
                folder.mkdir(parents=True, exist_ok=True)
                data = f"{name}: {b} response for evaluation".encode()
                (folder / "response.md").write_bytes(data)
                pairs[b] = {"runtime": runtime, "model": "test-model",
                            "version": "test", "executor_id": ids[0] if b == "A" else ids[1],
                            "input_sha256": hashlib.sha256(name.encode()).hexdigest(),
                            "output_sha256": hashlib.sha256(data).hexdigest()}
                score_pair[b] = {k: 2 if b == "A" else 3 for k in CRITERIA}
            runs.append({"id": name, "baseline_branch": "A", "runs": pairs})
            ratings[name] = score_pair
        (root / "runs.json").write_text(json.dumps({
            "schema_version": "1.0.0", "host_runtimes": ["Codex", "Hermes"],
            "executor_ids": list(ids), "cases": runs
        }))
        (root / "review.json").write_text(json.dumps({
            "reviewer_id": "reviewer", "blind": True, "ratings": ratings
        }))

    def test_pair_comparison_is_structurally_valid_not_approved(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_pair(root)
            result = verify(root)
            self.assertEqual(result["status"], "structurally_complete")
            self.assertTrue(result["meets_numeric_threshold"])
            self.assertFalse(result["release_approval"])

    def test_self_review_or_tampering_is_rejected(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_pair(root)
            (root / "review.json").write_text(
                (root / "review.json").read_text().replace('"reviewer_id": "reviewer"', '"reviewer_id": "builder"')
            )
            with self.assertRaises(EvaluationError):
                verify(root)
            self.make_pair(root)
            (root / "venture" / "A" / "response.md").write_text("tampered")
            with self.assertRaises(EvaluationError):
                verify(root)

    def test_reject_confounded_model_comparison(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_pair(root)
            data = json.loads((root / "runs.json").read_text())
            data["cases"][0]["runs"]["B"]["model"] = "different-model"
            (root / "runs.json").write_text(json.dumps(data))
            with self.assertRaises(EvaluationError):
                verify(root)

    def test_missing_runtime_and_case_invalid(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            self.make_pair(root)
            meta = json.loads((root / "runs.json").read_text())
            meta["host_runtimes"] = ["Codex"]
            (root / "runs.json").write_text(json.dumps(meta))
            with self.assertRaises(EvaluationError):
                verify(root)


if __name__ == "__main__":
    unittest.main()
