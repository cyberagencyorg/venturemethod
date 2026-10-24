"""Portable, read-only Venture Method consumption. No host runtime is owned here.

The host supplies bounded project state and remains responsible for file access,
agent execution, output approval, and any mutation. Assessment is conservative:
no evidenced unmet capability means no recommendation.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

from .core import ROOT

SCHEMA_VERSION = "1.0.0"
MAX_CONTEXT_BYTES = 128 * 1024
MAX_DOCUMENT_BYTES = 32768
MAX_DOCUMENTS = 16
MAX_QUERY = 240
SAFE_ID = re.compile(r"^[a-z][a-z0-9-]{0,63}$")
SAFE_REF = re.compile(r"^[A-Za-z0-9][A-Za-z0-9:._/-]{0,159}$")
PRIORITY = {"critical": 0, "high": 1, "medium": 2, "low": 3}


class ContractError(ValueError):
    """Untrusted or internally inconsistent host contract."""


def _load(name: str) -> Any:
    return json.loads((ROOT / name).read_text(encoding="utf-8"))


def _check_id(value: Any, label: str) -> str:
    if not isinstance(value, str) or not SAFE_ID.fullmatch(value):
        raise ContractError(f"Invalid {label}")
    return value


def catalog() -> dict:
    """Read the existing canonical inventories without claiming mapped = implemented."""
    methods = _load("config/frameworks-v3.json")["items"]
    skills = _load("config/skills-registry.json")["skills"]
    links = _load("config/work-composition.json")["capabilities"]
    ids = [item["id"] for item in methods]
    names = [item["name"] for item in skills]
    caps = [item["id"] for item in links]
    if len(set(ids)) != len(ids) or len(set(names)) != len(names) or len(set(caps)) != len(caps):
        raise ContractError("Duplicate catalog identifier")
    for item in links:
        for skill in item["eligible_skill_ids"]:
            if skill not in names:
                raise ContractError(f"Unknown skill in capability {item['id']}: {skill}")
    return {
        "methods": {item["id"]: item for item in methods},
        "skills": {item["name"]: item for item in skills},
        "capabilities": {item["id"]: item for item in links},
    }


def catalog_search(query: str, limit: int = 6) -> dict:
    if not isinstance(query, str) or not 1 <= len(query.strip()) <= MAX_QUERY:
        raise ContractError("query must contain 1 to 240 characters")
    if type(limit) is not int or not 1 <= limit <= 20:
        raise ContractError("limit must be 1 to 20")
    words = set(re.findall(r"[a-z0-9]+", query.lower()))
    source = catalog()
    candidates = []
    for ident, item in source["capabilities"].items():
        phrase = (ident + " " + item["title"]).lower()
        score = sum(1 for word in words if word in re.findall(r"[a-z0-9]+", phrase))
        if score:
            candidates.append({"id": ident, "title": item["title"],
                               "score": score, "status": item["status"]})
    candidates.sort(key=lambda x: (-x["score"], x["id"]))
    return {"schema_version": SCHEMA_VERSION, "matches": candidates[:limit],
            "note": "Lexical discovery only; never proof of applicability or execution."}


def method_get(method_id: str) -> dict:
    return dict(catalog()["methods"][_check_id(method_id, "method ID")])


def skill_get(skill_id: str) -> dict:
    item = catalog()["skills"][_check_id(skill_id, "skill ID")]
    rel = Path(item["path"]) / "SKILL.md"
    root = ROOT.resolve()
    absolute = (ROOT / rel).resolve()
    if not absolute.is_relative_to(root) or not absolute.is_file():
        raise ContractError("Skill path missing or outside catalog")
    content = absolute.read_text(encoding="utf-8")
    if len(content) > 40000:
        raise ContractError("Skill exceeds safe reading budget")
    return {"id": skill_id, "path": str(rel), "content": content,
            "status": item["status"], "release": item["release"]}


def inspect_paths(project_root: Path, included_paths: list[str]) -> list[dict]:
    """Inspect explicitly nominated files only, forbidding symlinks and root escape.

    Files are not transmitted or stored here. Returned text is deliberately bounded;
    callers must authorize its disclosure to their own model/runtime separately.
    """
    root = project_root.resolve(strict=True)
    if not root.is_dir() or not 1 <= len(included_paths) <= MAX_DOCUMENTS:
        raise ContractError("Expected a directory and 1 to 16 explicit files")
    out, seen, total = [], set(), 0
    for rel in included_paths:
        if not isinstance(rel, str) or not rel or len(rel) > 240:
            raise ContractError("Invalid relative filename")
        p = Path(rel)
        if p.is_absolute() or any(part in ("", ".", "..") for part in p.parts):
            raise ContractError("Traversal or absolute path is forbidden")
        if rel in seen:
            raise ContractError("Duplicate file")
        seen.add(rel)
        candidate = root / p
        # Reject symbolic links at *every* path segment, including directories.
        cursor = root
        for segment in p.parts:
            cursor = cursor / segment
            if cursor.is_symlink():
                raise ContractError(f"Symlink not permitted: {rel}")
        resolved = candidate.resolve(strict=True)
        if not resolved.is_relative_to(root) or not resolved.is_file():
            raise ContractError(f"Path outside authorized files: {rel}")
        size = resolved.stat().st_size
        total += size
        if size > MAX_DOCUMENT_BYTES or total > MAX_CONTEXT_BYTES:
            raise ContractError("Inspected content exceeds read budget")
        data = resolved.read_bytes()
        if b"\x00" in data:
            raise ContractError("Binary file not accepted")
        try:
            content = data.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise ContractError("Only UTF-8 text accepted") from exc
        out.append({"id": f"file:{rel}", "path": rel,
                    "sha256": hashlib.sha256(data).hexdigest(),
                    "text": content})
    return out


def validate_host(state: dict) -> dict:
    if not isinstance(state, dict) or state.get("schema_version") != SCHEMA_VERSION:
        raise ContractError("Unsupported or missing host schema_version")
    if not isinstance(state.get("task"), str) or not 1 <= len(state["task"].strip()) <= 4000:
        raise ContractError("Host task is required")
    if not isinstance(state.get("project"), str) or not 1 <= len(state["project"]) <= 120:
        raise ContractError("Host project identifier is required")
    if state.get("authorization") != "host_read_only":
        raise ContractError("Only explicitly authorized read-only host context is permitted")
    resources = state.get("resources")
    gaps = state.get("gaps")
    covered = state.get("covered_capabilities", [])
    if not isinstance(resources, list) or not isinstance(gaps, list) or not isinstance(covered, list):
        raise ContractError("resources, gaps and covered_capabilities must be arrays")
    if len(resources) > MAX_DOCUMENTS or len(gaps) > 24 or len(covered) > 40:
        raise ContractError("Host context too large")
    c = catalog()
    if any(not isinstance(x, str) or x not in c["capabilities"] for x in covered):
        raise ContractError("Unknown covered capability")
    refs = set()
    for resource in resources:
        if not isinstance(resource, dict) or not isinstance(resource.get("id"), str):
            raise ContractError("Invalid resource")
        if not SAFE_REF.fullmatch(resource["id"]) or resource["id"] in refs:
            raise ContractError("Unsafe or duplicate resource ID")
        refs.add(resource["id"])
        if not isinstance(resource.get("sha256"), str) or not re.fullmatch("[0-9a-f]{64}", resource["sha256"]):
            raise ContractError("Resources must be fingerprinted")
        if "text" in resource and (not isinstance(resource["text"], str) or len(resource["text"].encode("utf8")) > MAX_DOCUMENT_BYTES):
            raise ContractError("Resource text exceeds budget")
    if len(json.dumps(state, ensure_ascii=False).encode("utf8")) > MAX_CONTEXT_BYTES:
        raise ContractError("Host state exceeds budget")
    for gap in gaps:
        if not isinstance(gap, dict) or gap.get("capability_id") not in c["capabilities"]:
            raise ContractError("Unknown gap capability")
        if gap.get("status") not in ("unmet", "covered", "uncertain"):
            raise ContractError("Gap must have explicit status")
        if gap.get("priority") not in PRIORITY:
            raise ContractError("Gap must have explicit priority")
        evidence = gap.get("evidence_refs")
        if not isinstance(evidence, list) or len(evidence) > 8 or any(r not in refs for r in evidence):
            raise ContractError("Gap evidence references must resolve")
        if not isinstance(gap.get("reason"), str) or not 1 <= len(gap["reason"]) <= 800:
            raise ContractError("Gap requires a bounded rationale")
    return state


def assess(state: dict) -> dict:
    """Conservative assessment; no guessed gaps, no host reads, no side effects."""
    host = validate_host(state)
    c = catalog()
    covered = set(host.get("covered_capabilities", []))
    candidates = []
    exclusions = []
    for item in host["gaps"]:
        cid = item["capability_id"]
        cap = c["capabilities"][cid]
        if cid in covered or item["status"] == "covered":
            exclusions.append({"capability_id": cid, "reason": "already_covered"})
            continue
        if item["status"] != "unmet" or not item["evidence_refs"]:
            exclusions.append({"capability_id": cid, "reason": "insufficient_evidence"})
            continue
        choices = [sid for sid in cap["eligible_skill_ids"] if sid in c["skills"]]
        if not choices:
            exclusions.append({"capability_id": cid, "reason": "no_first_party_skill"})
            continue
        candidates.append((PRIORITY[item["priority"]], cid, choices[0], item))
    candidates.sort(key=lambda x: (x[0], x[1]))
    decision = "none"
    chosen = None
    if candidates:
        _, cid, sid, item = candidates[0]
        chosen = {
            "capability_id": cid, "skill_id": sid,
            "instruction_path": c["skills"][sid]["path"] + "/SKILL.md",
            "skill_status": c["skills"][sid]["status"],
            "evidence_refs": item["evidence_refs"], "reason": item["reason"],
            "priority": item["priority"],
            "execution_verified": False,
        }
        decision = "consult"
        exclusions += [{"capability_id": other[1], "reason": "lower_priority"}
                       for other in candidates[1:]]
    resource_fingerprints = sorted((r["id"], r["sha256"]) for r in host["resources"])
    digest = hashlib.sha256(json.dumps(resource_fingerprints, separators=(",", ":")).encode()).hexdigest()
    return {
        "schema_version": SCHEMA_VERSION, "project": host["project"],
        "decision": decision, "selected": chosen, "exclusions": exclusions,
        "context_sha256": digest, "state": "advisory_only",
        "effects": [], "host_authority": "retained",
        "limitations": [
            "Gap assertions and evidence are supplied by the host, not independently proven.",
            "No skill was executed or independently evaluated by this assessment.",
            "The host must approve any later data access, tool execution or changes.",
        ],
    }


def context_pack(state: dict, max_chars: int = 8000) -> dict:
    if type(max_chars) is not int or not 256 <= max_chars <= 16000:
        raise ContractError("max_chars must be 256 to 16000")
    result = assess(state)
    if result["decision"] == "none":
        return {"assessment": result, "instructions": "No justified intervention. Preserve existing host work."}
    selected = result["selected"]
    instructions = skill_get(selected["skill_id"])["content"]
    if len(instructions) > max_chars:
        # Never emit clipped procedures that could lose their safety constraints.
        return {"assessment": result, "instructions": None,
                "error": "Selected skill exceeds context budget; read it directly."}
    return {"assessment": result, "instructions": instructions}
