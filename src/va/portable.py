"""Portable, read-only Venture Method consumption. No host runtime is owned here.

The host supplies bounded project state and remains responsible for file access,
agent execution, output approval, and any mutation. Assessment is conservative:
no evidenced unmet capability means no recommendation.
"""
from __future__ import annotations

import hashlib
import json
import os
import stat
import re
from pathlib import Path
from typing import Any

from .core import ROOT

PACKAGE_LIBRARY = Path(__file__).resolve().parent / "_library"


def library_path(relative: str) -> Path:
    """Source checkout or wheel-bundled read-only reference library."""
    source = ROOT / relative
    if source.is_file():
        return source
    return PACKAGE_LIBRARY / relative

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
    return json.loads(library_path(name).read_text(encoding="utf-8"))


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
    for kind, candidates in (("method", ids), ("skill", names), ("capability", caps)):
        for ident in candidates:
            _check_id(ident, kind)
    for skill in skills:
        if skill.get("path") != f"skills/{skill['name']}":
            raise ContractError(f"Invalid first-party skill path for {skill['name']}")
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
    root = (ROOT if (ROOT / rel).is_file() else PACKAGE_LIBRARY).resolve()
    absolute = (root / rel).resolve()
    if not absolute.is_relative_to(root) or not absolute.is_file():
        raise ContractError("Skill path missing or outside catalog")
    content = absolute.read_text(encoding="utf-8")
    if len(content) > 40000:
        raise ContractError("Skill exceeds safe reading budget")
    return {"id": skill_id, "path": str(rel), "content": content,
            "status": item["status"], "release": item["release"]}


def _read_regular_file(root: Path, parts: tuple[str, ...]) -> bytes:
    """Open every component relative to a pinned directory descriptor.

    O_NOFOLLOW closes the check/open symlink race; fstat rejects special
    files including FIFOs/devices. Fail closed on platforms lacking dir_fd.
    """
    if os.name != "posix" or not hasattr(os, "O_NOFOLLOW"):
        raise ContractError("Secure scoped inspection requires POSIX O_NOFOLLOW")
    fds = []
    try:
        directory_flags = os.O_RDONLY | os.O_DIRECTORY | os.O_NOFOLLOW | os.O_CLOEXEC
        base = os.open(root, directory_flags)
        fds.append(base)
        for segment in parts[:-1]:
            fd = os.open(segment, directory_flags, dir_fd=fds[-1])
            fds.append(fd)
        file_flags = os.O_RDONLY | os.O_NOFOLLOW | os.O_NONBLOCK | os.O_CLOEXEC
        final = os.open(parts[-1], file_flags, dir_fd=fds[-1])
        fds.append(final)
        info = os.fstat(final)
        if not stat.S_ISREG(info.st_mode):
            raise ContractError("Only ordinary files may be inspected")
        if info.st_size > MAX_DOCUMENT_BYTES:
            raise ContractError("Inspected file exceeds read budget")
        chunks = []
        remaining = MAX_DOCUMENT_BYTES + 1
        while remaining:
            chunk = os.read(final, min(8192, remaining))
            if not chunk:
                break
            chunks.append(chunk)
            remaining -= len(chunk)
        payload = b"".join(chunks)
        if len(payload) > MAX_DOCUMENT_BYTES:
            raise ContractError("File expanded beyond read budget")
        return payload
    finally:
        for fd in reversed(fds):
            os.close(fd)


def inspect_paths(project_root: Path, included_paths: list[str]) -> list[dict]:
    """Read only explicitly authorized UTF-8 files, without following symlinks.

    Returned text remains host-confidential. Caller decides where it goes.
    """
    root = project_root.resolve(strict=True)
    if not root.is_dir() or not isinstance(included_paths, list) or not 1 <= len(included_paths) <= MAX_DOCUMENTS:
        raise ContractError("Expected a directory and 1 to 16 explicit files")
    out, seen, total = [], set(), 0
    for rel in included_paths:
        if not isinstance(rel, str) or not rel or len(rel) > 240:
            raise ContractError("Invalid relative filename")
        p = Path(rel)
        if p.is_absolute() or not p.parts or any(part in ("", ".", "..") for part in p.parts):
            raise ContractError("Traversal or absolute path is forbidden")
        if rel in seen:
            raise ContractError("Duplicate file")
        seen.add(rel)
        payload = _read_regular_file(root, p.parts)
        total += len(payload)
        if total > MAX_CONTEXT_BYTES:
            raise ContractError("Inspected content exceeds total read budget")
        if b"\x00" in payload:
            raise ContractError("Binary file not accepted")
        try:
            content = payload.decode("utf-8")
        except UnicodeDecodeError as exc:
            raise ContractError("Only UTF-8 text accepted") from exc
        out.append({"id": f"file:{rel}", "path": rel,
                    "sha256": hashlib.sha256(payload).hexdigest(),
                    "text": content})
    return out


def validate_host(state: dict) -> dict:
    if not isinstance(state, dict) or state.get("schema_version") != SCHEMA_VERSION:
        raise ContractError("Unsupported or missing host schema_version")
    if not isinstance(state.get("task"), str) or not 1 <= len(state["task"].strip()) <= 4000:
        raise ContractError("Host task is required")
    if not isinstance(state.get("project"), str) or not 1 <= len(state["project"]) <= 120:
        raise ContractError("Host project identifier is required")
    allowed = {"schema_version", "task", "project", "authorization", "resources", "gaps", "covered_capabilities"}
    if set(state) - allowed:
        raise ContractError("Unexpected host contract properties")
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
    if len(covered) != len(set(str(x) for x in covered)):
        raise ContractError("Duplicate covered capabilities")
    if any(not isinstance(x, str) or x not in c["capabilities"] for x in covered):
        raise ContractError("Unknown covered capability")
    refs = set()
    resource_by_id = {}
    for resource in resources:
        if not isinstance(resource, dict) or set(resource) - {"id", "sha256", "text", "path"} or not isinstance(resource.get("id"), str):
            raise ContractError("Invalid resource")
        if not SAFE_REF.fullmatch(resource["id"]) or resource["id"] in refs:
            raise ContractError("Unsafe or duplicate resource ID")
        refs.add(resource["id"])
        resource_by_id[resource["id"]] = resource
        if not isinstance(resource.get("sha256"), str) or not re.fullmatch("[0-9a-f]{64}", resource["sha256"]):
            raise ContractError("Resources must be fingerprinted")
        if "text" in resource:
            if not isinstance(resource["text"], str) or len(resource["text"].encode("utf8")) > MAX_DOCUMENT_BYTES:
                raise ContractError("Resource text exceeds budget")
            if hashlib.sha256(resource["text"].encode("utf8")).hexdigest() != resource["sha256"]:
                raise ContractError("Resource text does not match fingerprint")
    if len(json.dumps(state, ensure_ascii=False).encode("utf8")) > MAX_CONTEXT_BYTES:
        raise ContractError("Host state exceeds budget")
    gap_ids = set()
    for gap in gaps:
        if not isinstance(gap, dict) or set(gap) - {"capability_id", "status", "priority", "reason", "evidence_refs", "skill_id", "evidence_quotes"} or gap.get("capability_id") not in c["capabilities"]:
            raise ContractError("Unknown gap capability")
        if gap["capability_id"] in gap_ids:
            raise ContractError("Contradictory or duplicate capability assessments must be reconciled")
        gap_ids.add(gap["capability_id"])
        if gap.get("status") not in ("unmet", "covered", "uncertain"):
            raise ContractError("Gap must have explicit status")
        if gap.get("priority") not in PRIORITY:
            raise ContractError("Gap must have explicit priority")
        evidence = gap.get("evidence_refs")
        if not isinstance(evidence, list) or len(evidence) > 8 or any(r not in refs for r in evidence):
            raise ContractError("Gap evidence references must resolve")
        if not isinstance(gap.get("reason"), str) or not 1 <= len(gap["reason"]) <= 800:
            raise ContractError("Gap requires a bounded rationale")
        quotes = gap.get("evidence_quotes", [])
        if not isinstance(quotes, list) or len(quotes) > 8:
            raise ContractError("Evidence anchors must be a bounded array")
        for anchor in quotes:
            if not isinstance(anchor, dict) or set(anchor) != {"resource_id", "quote"}:
                raise ContractError("Evidence anchor requires resource_id and quote")
            rid, quote = anchor["resource_id"], anchor["quote"]
            if rid not in evidence or not isinstance(quote, str) or not 4 <= len(quote) <= 1000:
                raise ContractError("Evidence anchor must cite a supplied source")
            source_text = resource_by_id[rid].get("text")
            if source_text is None or quote not in source_text:
                raise ContractError("Evidence anchor is not an exact excerpt in supplied text")
        if "skill_id" in gap:
            if gap["skill_id"] not in c["capabilities"][gap["capability_id"]]["eligible_skill_ids"]:
                raise ContractError("Selected skill does not implement the declared capability")
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
        # An arbitrary first skill in a registry is not a professional selection.
        preferred = item.get("skill_id")
        if preferred is None and len(choices) != 1:
            exclusions.append({"capability_id": cid, "reason": "skill_selection_requires_review"})
            continue
        sid = preferred or choices[0]
        if sid not in choices:
            raise ContractError("Unsupported skill choice")
        candidates.append((PRIORITY[item["priority"]], cid, sid, item))
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
            "evidence_verification": "excerpt_matched" if item.get("evidence_quotes") else "reference_only",
            "execution_verified": False,
        }
        decision = "consult"
        exclusions += [{"capability_id": other[1], "reason": "lower_priority"}
                       for other in candidates[1:]]
    # Bind the entire assessment to exact task, gaps and inputs, not hashes alone.
    digest = hashlib.sha256(json.dumps(host, ensure_ascii=False, sort_keys=True,
                                    separators=(",", ":")).encode("utf-8")).hexdigest()
    return {
        "schema_version": SCHEMA_VERSION, "project": host["project"],
        "decision": decision, "selected": chosen, "exclusions": exclusions,
        "context_sha256": digest, "state": "advisory_only",
        "effects": [], "host_authority": "retained",
        "limitations": [
            "Host-authored gaps are not independently assessed; excerpt matching establishes location, not factual truth.",
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


def snapshot_project(*, project: str, task: str, root: Path, paths: list[str]) -> dict:
    """Construct a source-backed host-state draft without guessing unmet needs.

    Inspection is explicit and read-only. The caller must authorize use of
    captured private text by any downstream model or remote service.
    """
    state = {
        "schema_version": SCHEMA_VERSION,
        "project": project,
        "task": task,
        "authorization": "host_read_only",
        "resources": inspect_paths(root, paths),
        "covered_capabilities": [],
        "gaps": [],
    }
    return validate_host(state)


def propose_gap(state: dict, *, capability_id: str, skill_id: str, resource_id: str,
                quote: str, reason: str, priority: str = "high") -> dict:
    """Explicit host-authored hypothesis, checked against an exact source quote.

    This function does NOT independently decide that a gap exists. It returns a
    new state plus a purely advisory, reversible assessment. No host writes.
    """
    import copy
    draft = copy.deepcopy(validate_host(state))
    if any(item["capability_id"] == capability_id for item in draft["gaps"]):
        raise ContractError("Capability already assessed; reconcile existing host decision")
    draft["gaps"].append({
        "capability_id": capability_id, "status": "unmet",
        "priority": priority, "reason": reason, "skill_id": skill_id,
        "evidence_refs": [resource_id],
        "evidence_quotes": [{"resource_id": resource_id, "quote": quote}],
    })
    result = assess(draft)
    return {"proposed_host_state": draft, "assessment": result,
            "warning": "A matched quote does not establish the proposed gap's correctness."}
