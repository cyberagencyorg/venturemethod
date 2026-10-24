"""Verify paired agent evaluation artifacts without pretending to execute a model.

The verifier enforces case identity, output integrity, explicit reviewer separation
and paired rubric completeness. It does not authenticate reviewers or assess truth.
"""
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path

CRITERIA = ("accuracy", "usefulness", "method_fidelity", "traceability",
            "authority", "efficiency")
CASE_IDS = ("venture", "in_flight", "commercial", "no_intervention")


class EvaluationError(ValueError):
    pass


def _json(path: Path) -> dict:
    if not path.is_file() or path.stat().st_size > 131072:
        raise EvaluationError(f"Missing or oversized document: {path.name}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise EvaluationError("Evaluation metadata must be an object")
    return data


def _output(root: Path, path: str, expected_hash: str) -> None:
    path_obj = Path(path)
    if path_obj.is_absolute() or ".." in path_obj.parts or len(path_obj.parts) != 3:
        raise EvaluationError("Output must be case/branch/response.md")
    if path_obj.parts[0] not in CASE_IDS or path_obj.parts[1] not in ("A", "B"):
        raise EvaluationError("Unexpected output path")
    if path_obj.parts[2] != "response.md":
        raise EvaluationError("Only response.md outputs accepted")
    target = root / path_obj
    for rel in (root / path_obj.parts[0], root / path_obj.parts[0] / path_obj.parts[1], target):
        if rel.is_symlink():
            raise EvaluationError("Symlinked evaluation output rejected")
    if not target.is_file() or target.stat().st_size > 65536:
        raise EvaluationError("Output missing or too large")
    data = target.read_bytes()
    if not data.strip():
        raise EvaluationError("Empty output")
    if hashlib.sha256(data).hexdigest() != expected_hash:
        raise EvaluationError("Output fingerprint mismatch")


def verify(workspace: Path) -> dict:
    root = workspace.resolve(strict=True)
    metadata = _json(root / "runs.json")
    review = _json(root / "review.json")
    if metadata.get("schema_version") != "1.0.0":
        raise EvaluationError("Expected schema v1.0.0")
    cases = metadata.get("cases")
    if not isinstance(cases, list) or {x.get("id") for x in cases if isinstance(x, dict)} != set(CASE_IDS) or len(cases) != len(CASE_IDS):
        raise EvaluationError("All four distinct evaluation cases are required")
    if not review.get("blind") or not isinstance(review.get("reviewer_id"), str) or not review["reviewer_id"].strip():
        raise EvaluationError("Named blinded reviewer required")
    if review.get("reviewer_id") in metadata.get("executor_ids", []):
        raise EvaluationError("Executor cannot grade own runs")
    if not isinstance(metadata.get("executor_ids"), list) or not metadata["executor_ids"]:
        raise EvaluationError("Actual executors must be declared")
    if len(set(metadata.get("host_runtimes", []))) < 2:
        raise EvaluationError("Two distinct host runtimes required")
    if set(review.get("ratings", {})) != set(CASE_IDS):
        raise EvaluationError("Each case requires a rating pair")
    outcome = {}
    observed_runtimes = set()
    all_a, all_b = [], []
    for case in cases:
        name = case["id"]
        if set(case.get("runs", {})) != {"A", "B"}:
            raise EvaluationError(f"Both runs missing for {name}")
        if case.get("baseline_branch") not in ("A", "B"):
            raise EvaluationError("Baseline/candidate assignment missing")
        run_a, run_b = case["runs"]["A"], case["runs"]["B"]
        for branch, run in (("A", run_a), ("B", run_b)):
            if not isinstance(run, dict):
                raise EvaluationError("Run metadata is required")
            for required in ("runtime", "model", "version", "input_sha256", "output_sha256", "executor_id"):
                if not isinstance(run.get(required), str) or not run[required]:
                    raise EvaluationError(f"{name}/{branch}: missing {required}")
            if len(run["input_sha256"]) != 64 or len(run["output_sha256"]) != 64:
                raise EvaluationError("Expected SHA-256 hashes")
            if run["runtime"] not in metadata["host_runtimes"] or run["executor_id"] not in metadata["executor_ids"]:
                raise EvaluationError("Unregistered runtime/executor")
            _output(root, f"{name}/{branch}/response.md", run["output_sha256"])
        if run_a["input_sha256"] != run_b["input_sha256"]:
            raise EvaluationError(f"{name}: runs used different task inputs")
        if (run_a["runtime"], run_a["model"], run_a["version"]) != (run_b["runtime"], run_b["model"], run_b["version"]):
            raise EvaluationError(f"{name}: model/runtime confound in paired comparison")
        observed_runtimes.add(run_a["runtime"])
        ratings = review["ratings"][name]
        if set(ratings) != {"A", "B"}:
            raise EvaluationError(f"{name}: incomplete ratings")
        for branch in ("A", "B"):
            score = ratings[branch]
            if set(score) != set(CRITERIA) or any(type(score[k]) is not int or not 0 <= score[k] <= 4 for k in CRITERIA):
                raise EvaluationError(f"{name}/{branch}: invalid rubric")
        baseline = ratings[case["baseline_branch"]]
        candidate = ratings["B" if case["baseline_branch"] == "A" else "A"]
        all_a.append(sum(baseline[k] for k in CRITERIA) / len(CRITERIA))
        all_b.append(sum(candidate[k] for k in CRITERIA) / len(CRITERIA))
        outcome[name] = {
            "baseline_accuracy": baseline["accuracy"],
            "candidate_accuracy": candidate["accuracy"],
            "baseline_authority": baseline["authority"],
            "candidate_authority": candidate["authority"],
            "difference": round((sum(candidate.values()) - sum(baseline.values())) / len(CRITERIA), 3),
        }
    if len(observed_runtimes) < 2:
        raise EvaluationError("Comparison did not exercise two actual runtime families")
    regressions = [key for key, row in outcome.items() if row["candidate_accuracy"] < row["baseline_accuracy"] or row["candidate_authority"] < row["baseline_authority"]]
    average_improvement = round(sum(all_b)/len(all_b) - sum(all_a)/len(all_a), 3)
    return {
        "status": "structurally_complete",
        "case_results": outcome,
        "average_score_improvement": average_improvement,
        "safety_regressions": regressions,
        "meets_numeric_threshold": average_improvement >= 0.5 and not regressions,
        "release_approval": False,
        "limitations": [
            "Run metadata and reviewer identity are declarations, not independently authenticated.",
            "No actual model execution or factual verification is performed by this verifier.",
            "Independent authority must verify raw transcripts, host permissions and rubric integrity.",
        ],
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python -m src.va.portable_eval WORKSPACE", file=sys.stderr)
        return 2
    try:
        print(json.dumps(verify(Path(sys.argv[1])), indent=2))
        return 0
    except (OSError, KeyError, ValueError, TypeError) as exc:
        print(f"Evaluation invalid: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
