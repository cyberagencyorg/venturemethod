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
            "evidence_refs": gap["evidence_refs"],
            "evidence_verification": "excerpt_matched" if gap.get("evidence_quotes") else "reference_only",
        })
    return {
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
