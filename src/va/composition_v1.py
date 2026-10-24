"""Versioned, host-owned composition of multiple advisory professional capabilities.

This deliberately does not run agents, delegate, write project files or give
tool privileges. Explicit dependency closure and bounded topological ordering
prevent a high-priority downstream method from skipping its prerequisites.
"""
from __future__ import annotations

import hashlib
import json

from .portable import ContractError, PRIORITY, SCHEMA_VERSION, catalog, validate_host


def compose(host_state: dict, max_units: int = 3) -> dict:
    if type(max_units) is not int or not 1 <= max_units <= 8:
        raise ContractError("max_units must be between 1 and 8")
    host = validate_host(host_state)
    catalogs = catalog()
    covered = set(host.get("covered_capabilities", []))
    gaps = {x["capability_id"]: x for x in host["gaps"]}
    context_hash = hashlib.sha256(
        json.dumps(host, ensure_ascii=False, sort_keys=True,
                   separators=(",", ":")).encode("utf-8")).hexdigest()

    candidates = {}
    exclusions = {}
    for cid, item in gaps.items():
        cap = catalogs["capabilities"][cid]
        skills = cap["eligible_skill_ids"]
        if cid in covered or item["status"] == "covered":
            exclusions[cid] = "already_covered"
        elif item["status"] != "unmet" or not item["evidence_refs"]:
            exclusions[cid] = "insufficient_evidence"
        elif not skills:
            exclusions[cid] = "no_first_party_skill"
        elif item.get("skill_id") is None and len(skills) != 1:
            exclusions[cid] = "skill_selection_requires_review"
        else:
            candidates[cid] = item

    # Reject dependency cycles even if only reached through a lower-priority
    # candidate. An unsafe ordering must never silently become a work proposal.
    def closure(cid: str, chain: tuple[str, ...] = ()) -> list[str]:
        if cid in chain:
            raise ContractError("Dependency cycle in requested capabilities")
        if cid in covered or (cid in gaps and gaps[cid]["status"] == "covered"):
            return []
        if cid not in candidates:
            raise ContractError(f"Unresolved prerequisite: {cid}")
        result = []
        for dep in candidates[cid].get("depends_on", []):
            result.extend(closure(dep, chain + (cid,)))
        result.append(cid)
        return list(dict.fromkeys(result))

    for cid in sorted(candidates):
        try:
            closure(cid)
        except ContractError as exc:
            if "cycle" in str(exc):
                raise
            exclusions[cid] = "unresolved_prerequisite"
    candidates = {k:v for k,v in candidates.items() if k not in exclusions}

    selected = []
    for cid in sorted(candidates, key=lambda name: (PRIORITY[candidates[name]["priority"]], name)):
        if cid in selected:
            continue
        try:
            need = [x for x in closure(cid) if x not in selected]
        except ContractError:
            exclusions[cid] = "unresolved_prerequisite"
            continue
        if len(selected) + len(need) > max_units:
            exclusions[cid] = "composition_limit"
            continue
        selected.extend(need)

    units = []
    for cid in selected:
        gap = candidates[cid]
        sid = gap.get("skill_id") or catalogs["capabilities"][cid]["eligible_skill_ids"][0]
        if sid not in catalogs["skills"]:
            raise ContractError("Mapped skill missing from canonical catalog")
        unit_hash = hashlib.sha256((context_hash + ":" + cid + ":" + sid).encode()).hexdigest()
        work = {
            "schema_version": SCHEMA_VERSION, "id": "consult-" + unit_hash[:16],
            "host_project": host["project"], "objective": host["task"],
            "phase": host.get("phase", "unknown"),
            "existing_artifacts": gap["evidence_refs"],
            "selected_capabilities": [cid],
            "allowed_tools": [], "authorized_effects": [],
            "review": {"owner": "host_authority_unspecified",
                       "status": "pending", "required_before_effects": True},
            "stop_when": "Return one bounded, evidenced recommendation. No implicit execution or publication.",
            "outputs": ["One host-reviewed, source-backed recommendation or justified no-op"],
        }
        units.append({
            "unit": work, "capability_id": cid, "skill_id": sid,
            "depends_on": [x for x in gap.get("depends_on", []) if x in selected],
            "preconditions_covered": [x for x in gap.get("depends_on", [])
                                      if x in covered or (x in gaps and gaps[x]["status"] == "covered")],
            "evidence_refs": gap["evidence_refs"],
            "evidence_verification": "excerpt_matched" if gap.get("evidence_quotes") else "reference_only",
        })
    result = {
        "schema_version": SCHEMA_VERSION, "project": host["project"],
        "context_sha256": context_hash,
        "status": "advisory_composition" if units else "no_intervention",
        "units": units,
        "excluded": [{"capability_id": key, "reason": value}
                     for key, value in sorted(exclusions.items())],
        "effects": [], "host_authority": "retained",
        "limitations": [
            "Host-supplied gaps and prerequisites are hypotheses, not validated professional judgments.",
            "Every unit retains zero tool rights and requires host review.",
            "Composition proposes an order; no agents or actions were executed.",
        ],
    }
    verify_composition(result)
    return result


def verify_composition(plan: dict) -> dict:
    """Check cross-unit relationships and advisory restrictions.

    A validated document is not an authorization, trusted signature, or proof
    that any capability was executed. Structural JSON Schema validation
    remains a separate compatibility check.
    """
    import re
    if not isinstance(plan, dict) or plan.get("schema_version") != SCHEMA_VERSION:
        raise ContractError("Invalid composition version")
    if not isinstance(plan.get("project"), str) or not plan["project"].strip():
        raise ContractError("Composition project missing")
    digest = plan.get("context_sha256")
    if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise ContractError("Invalid source context fingerprint")
    units = plan.get("units")
    excluded = plan.get("excluded")
    if not isinstance(units, list) or not isinstance(excluded, list) or len(units) > 8:
        raise ContractError("Invalid composition inventory")
    if plan.get("effects") != [] or plan.get("host_authority") != "retained":
        raise ContractError("Composition attempts to elevate host authority")
    status = plan.get("status")
    if status not in ("no_intervention", "advisory_composition"):
        raise ContractError("Invalid composition status")
    if (status == "no_intervention") != (len(units) == 0):
        raise ContractError("Composition status disagrees with work units")
    seen, work_ids = set(), set()
    for item in units:
        if not isinstance(item, dict):
            raise ContractError("Malformed composition unit")
        cap = item.get("capability_id")
        work = item.get("unit")
        if not isinstance(cap, str) or cap in seen or not isinstance(work, dict):
            raise ContractError("Repeated or malformed capability in composition")
        if work.get("id") in work_ids or not isinstance(work.get("id"), str):
            raise ContractError("Duplicate or invalid work unit identity")
        work_ids.add(work["id"])
        if work.get("host_project") != plan["project"] or work.get("selected_capabilities") != [cap]:
            raise ContractError("Work unit not bound to the declared project and capability")
        if work.get("schema_version") != SCHEMA_VERSION:
            raise ContractError("Work unit contract version mismatch")
        if work.get("allowed_tools") != [] or work.get("authorized_effects") != []:
            raise ContractError("Advisory composition cannot grant tool or execution rights")
        review = work.get("review")
        if not isinstance(review, dict) or review.get("status") != "pending" or review.get("required_before_effects") is not True:
            raise ContractError("Work unit must remain pending host review")
        deps = item.get("depends_on")
        if not isinstance(deps, list) or len(deps) != len(set(str(x) for x in deps)) or any(
            not isinstance(dep, str) or dep not in seen for dep in deps
        ):
            raise ContractError("Prerequisites must be distinct, present, and ordered before dependents")
        already_covered = item.get("preconditions_covered")
        if not isinstance(already_covered, list) or len(already_covered) != len(set(str(x) for x in already_covered)) or any(
            not isinstance(dep, str) or dep in seen or dep in deps for dep in already_covered
        ):
            raise ContractError("Covered prerequisites must be distinct from pending dependencies")
        if item.get("evidence_verification") not in ("excerpt_matched", "reference_only"):
            raise ContractError("Unsupported evidence grade")
        if not isinstance(item.get("evidence_refs"), list) or not item["evidence_refs"]:
            raise ContractError("Unanchored composition unit")
        seen.add(cap)
    excluded_ids = set()
    for item in excluded:
        if not isinstance(item, dict) or not isinstance(item.get("capability_id"), str) or not isinstance(item.get("reason"), str):
            raise ContractError("Malformed exclusion")
        if item["capability_id"] in seen or item["capability_id"] in excluded_ids:
            raise ContractError("Selected and excluded capabilities cannot overlap")
        excluded_ids.add(item["capability_id"])
    return {
        "status": "verified_advisory_structure",
        "units": len(units),
        "context_sha256": digest,
        "authorization": "none",
        "warning": "Structural validation is not independent source verification, permission, or executed competence.",
    }
