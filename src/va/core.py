"""Deterministic engagement scaffolding and evidence-linked checks.

This module does NOT conduct research, validate external claims, call models,
access client systems, or imply that generated output is verified.
"""
from __future__ import annotations
import json
import re
import datetime as dt
from pathlib import Path
from typing import Any
from . import ledger

ROOT = Path(__file__).resolve().parents[2]
ENGAGEMENT_ROOT = ROOT / "engagements"
TYPES = ("client", "venture", "company", "industry", "product", "transformation", "diligence", "deliverable")
VALID_STATUS = ("unknown", "proposed", "supported", "disputed", "rejected")
PROFILES = {"quick": ["intake", "evidence", "options", "decision"],
            "standard": ["intake", "investigate", "diagnose", "options", "evaluate", "decide", "plan", "review"],
            "deep": ["intake", "investigate", "diagnose", "options", "evaluate", "experiment", "decide", "plan", "review", "learn"]}
BUNDLES = {
    "client": ["intake-scoping", "company-investigation", "problem-mapping", "strategic-options", "commercial-offer", "adversarial-review"],
    "venture": ["intake-scoping", "market-landscape", "opportunity-discovery", "venture-thesis", "business-model", "capital-landscape", "experiment-design", "adversarial-review"],
    "company": ["company-investigation", "market-landscape", "strategic-options", "operating-model", "adversarial-review"],
    "industry": ["market-landscape", "opportunity-discovery", "strategic-options", "adversarial-review"],
    "product": ["product-discovery", "opportunity-solution-tree", "opportunity-discovery", "product-requirements", "experiment-design", "adversarial-review"],
    "transformation": ["company-investigation", "problem-mapping", "service-blueprint", "operating-model", "strategic-options", "adversarial-review"],
    "diligence": ["company-investigation", "market-landscape", "venture-diligence", "financial-scenarios", "business-model", "adversarial-review"],
    "deliverable": ["intake-scoping", "evidence-audit", "artifact-quality", "adversarial-review"],
}

def now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()

def slugify(value: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    if not slug or len(slug) > 80:
        raise ValueError("Name must produce a 1-80 character slug")
    return slug

def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf8")

def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf8"))

def safe_engagement(slug: str) -> Path:
    if slugify(slug) != slug or slug != Path(slug).name:
        raise ValueError("Invalid engagement slug")
    case = ENGAGEMENT_ROOT / slug
    if not case.is_dir():
        raise FileNotFoundError(f"Engagement not found: {slug}")
    return case

def new_engagement(name: str, kind: str, industry: str = "unspecified", mode: str = "standard") -> Path:
    if kind not in TYPES:
        raise ValueError(f"Type must be one of: {', '.join(TYPES)}")
    if mode not in PROFILES:
        raise ValueError(f"Mode must be one of: {', '.join(PROFILES)}")
    slug = slugify(name)
    ENGAGEMENT_ROOT.mkdir(exist_ok=True)
    path = ENGAGEMENT_ROOT / slug
    path.mkdir(exist_ok=False)
    write_json(path / "engagement.json", {
        "id": slug, "name": name, "kind": kind, "industry": industry,
        "mode": mode, "created_at": now(), "status": "active",
        "objective": "", "scope": "", "constraints": [], "stakeholders": [],
        "data_classification": "confidential", "approval_owner": "unassigned",
        "risk_level": "unknown", "requested_output": "", "beneficiaries": [],
        "data_permissions": [], "budget": None, "deadline": None
    })
    for key in ledger.COLLECTIONS:
        write_json(path / f"{key}.json", [])
    (path / "events.jsonl").write_text("", encoding="utf8")
    (path / "deliverables").mkdir()
    (path / "notes").mkdir()
    (path / "README.md").write_text(
        f"# {name}\n\nConfidential engagement. Do not commit client information.\n\n"
        "Populate objective, constraints and owner in engagement.json.\n"
        "Treat all claims as unknown until evidence has been reviewed.\n", encoding="utf8")
    return path

def require_references(case: Path, collection: str, ids: list[str]) -> None:
    if not isinstance(ids, list) or any(not isinstance(i, str) for i in ids):
        raise ValueError("Reference IDs must be a list of strings")
    present = {r["id"] for r in read_json(case / f"{collection}.json")}
    unknown = set(ids) - present
    if unknown:
        raise ValueError(f"Unknown {collection} references in this engagement: {sorted(unknown)}")


def append_record(case: Path, collection: str, entry: dict[str, Any]) -> dict[str, Any]:
    if collection not in ledger.COLLECTIONS:
        raise ValueError("Unknown collection")
    # No user can override system IDs, timestamps or primary keys.
    if "id" in entry or "recorded_at" in entry:
        raise ValueError("Record IDs and timestamps are generated by the system")
    entries = read_json(case / f"{collection}.json")
    prefix = ledger.PREFIX[collection]
    next_num = max([int(x["id"].split("-")[-1]) for x in entries if re.fullmatch(prefix + r"-\d+", x.get("id", ""))] or [0]) + 1
    record = {**entry, "id": f"{prefix}-{next_num:04d}", "recorded_at": now()}
    ledger.append(case, collection, record)
    return record


def add_source(case: Path, title: str, locator: str, source_type: str, accessed_at: str | None = None) -> dict[str, Any]:
    if not title.strip() or not locator.strip() or not source_type.strip():
        raise ValueError("Source title, locator, and type required")
    return append_record(case, "sources", {"title": title, "locator": locator,
        "source_type": source_type, "accessed_at": accessed_at or now(),
        "published_at": None, "independent_verification": "not_verified",
        "notes": "", "permissions": "review_needed", "publisher": None})


def add_claim(case: Path, statement: str, source_ids: list[str] | None = None) -> dict[str, Any]:
    source_ids = source_ids or []
    require_references(case, "sources", source_ids)
    if not statement.strip(): raise ValueError("Claim text required")
    return append_record(case, "claims", {"statement": statement,
        "source_ids": source_ids, "confidence": "unrated", "status": "unknown",
        "claim_type": "unclassified", "counterevidence_ids": [],
        "falsification_test": "", "last_reviewed_at": None})


def add_decision(case: Path, question: str, choice: str, claim_ids: list[str] | None = None) -> dict[str, Any]:
    claim_ids = claim_ids or []
    require_references(case, "claims", claim_ids)
    if not question.strip() or not choice.strip(): raise ValueError("Decision question and choice required")
    return append_record(case, "decisions", {"question": question, "choice": choice,
        "claim_ids": claim_ids, "alternatives": ["do nothing / defer"], "rationale": "",
        "reversibility": "unassessed", "status": "draft", "owner": "unassigned",
        "review_trigger": "", "approval_evidence": None})


def add_hypothesis(case: Path, statement: str, predicts: str, test: str, claim_ids: list[str] | None = None) -> dict[str, Any]:
    claim_ids = claim_ids or []
    require_references(case, "claims", claim_ids)
    if not all(x.strip() for x in (statement, predicts, test)):
        raise ValueError("Hypothesis, prediction and proposed test are required")
    return append_record(case, "hypotheses", {"statement": statement, "prediction": predicts,
        "test": test, "claim_ids": claim_ids, "status": "untested", "confounders": []})


def add_option(case: Path, description: str, claim_ids: list[str] | None = None) -> dict[str, Any]:
    claim_ids = claim_ids or []
    require_references(case, "claims", claim_ids)
    if not description.strip(): raise ValueError("Option requires description")
    return append_record(case, "options", {"description": description, "claim_ids": claim_ids,
        "expected_upside": "unknown", "cost": "unknown", "downside": "unknown",
        "reversibility": "unknown", "status": "candidate"})


def add_action(case: Path, description: str, decision_id: str, owner: str) -> dict[str, Any]:
    require_references(case, "decisions", [decision_id])
    if not description.strip() or not owner.strip(): raise ValueError("Action and owner required")
    return append_record(case, "actions", {"description": description, "decision_id": decision_id,
        "owner": owner, "status": "proposed", "acceptance_criteria": "", "authorization": "pending"})


def add_outcome(case: Path, action_id: str, observation: str, source_ids: list[str]) -> dict[str, Any]:
    require_references(case, "actions", [action_id])
    require_references(case, "sources", source_ids)
    if not observation.strip(): raise ValueError("Outcome requires observed result")
    return append_record(case, "outcomes", {"action_id": action_id, "observation": observation,
        "source_ids": source_ids, "assessment": "unreviewed"})

def add_entity(case: Path, name: str, entity_type: str, jurisdiction: str, aliases: list[str] | None = None) -> dict[str, Any]:
    types = ("legal_company", "trade_brand", "person", "product", "institution", "market", "jurisdiction", "capability")
    if entity_type not in types or not name.strip():
        raise ValueError(f"Entity name and type ({', '.join(types)}) required")
    # An entity is a candidate identity pending explicit verification.
    return append_record(case, "entities", {"name":name, "entity_type":entity_type,
        "jurisdiction":jurisdiction, "aliases":aliases or [], "resolution":"unresolved",
        "external_ids":{}, "description":"", "source_ids":[]})


def add_review(case: Path, target_type: str, target_id: str, verdict: str,
               reviewer: str, rationale: str, source_ids: list[str] | None = None) -> dict[str, Any]:
    groups = {"claim":("claims", ("supported", "challenged", "inconclusive", "rejected")),
              "decision":("decisions", ("recommend", "revise", "defer", "reject")),
              "entity":("entities", ("resolved", "ambiguous", "disputed"))}
    if target_type not in groups or verdict not in groups[target_type][1]:
        raise ValueError("Review target type or verdict invalid")
    require_references(case, groups[target_type][0], [target_id])
    source_ids = source_ids or []
    require_references(case, "sources", source_ids)
    if not reviewer.strip() or not rationale.strip():
        raise ValueError("Review requires named reviewer and rationale")
    return append_record(case, "reviews", {"target_type":target_type,
        "target_id":target_id, "verdict":verdict, "reviewer_assertion":reviewer,
        "rationale":rationale, "source_ids":source_ids,
        "authorization": "review_only; NOT identity-verified or operational approval"})


def trace(case: Path, record_id: str) -> dict[str, Any]:
    if not re.fullmatch(r"[A-Z]{3,4}-\d{4}", record_id):
        raise ValueError("Invalid record ID")
    lookup = {}
    for c in ledger.COLLECTIONS:
        for record in read_json(case / f"{c}.json"):
            lookup[record["id"]] = (c, record)
    if record_id not in lookup: raise ValueError("Record does not exist in engagement")
    visited=set()
    edges=[]
    records=[]
    stack=[record_id]
    relations={"source_ids":"supported_or_cited_by_source", "claim_ids":"informed_by_claim",
               "decision_id":"proposed_under_decision", "action_id":"observed_after_action",
               "target_id":"assesses_record", "supersedes_id":"proposes_revision_of", "counterevidence_ids":"challenged_by_source"}
    while stack:
        current=stack.pop()
        if current in visited: continue
        visited.add(current)
        col,record=lookup[current]
        records.append({"collection":col, "id":current, "record":record})
        for field,relation in relations.items():
            value=record.get(field,[])
            refs = value if isinstance(value,list) else [value]
            for ref in refs:
                if isinstance(ref,str) and ref in lookup:
                    edges.append({"from":current,"to":ref,"relationship":relation})
                    if ref not in visited: stack.append(ref)
    # Include reviews of all touched nodes; reviews do not overwrite prior claims.
    for review in read_json(case/'reviews.json'):
        if review['target_id'] in visited and review['id'] not in visited:
            records.append({"collection":"reviews","id":review['id'],"record":review})
            edges.append({"from":review['id'],"to":review['target_id'],"relationship":"reviews"})
    return {"engagement_id":case.name, "root":record_id,"nodes":records,"edges":edges,
            "note":"References represent attribution, not proof of correctness or authorization"}

def update_engagement(case: Path, **updates: Any) -> dict[str, Any]:
    allowed = {"objective", "scope", "requested_output", "approval_owner", "risk_level", "deadline", "budget"}
    if not updates or set(updates) - allowed:
        raise ValueError(f"Engagement fields must be from {sorted(allowed)}")
    before = read_json(case / "engagement.json")
    after = {**before, **updates}
    if after.get("risk_level") not in ("unknown", "low", "medium", "high"):
        raise ValueError("risk_level must be unknown, low, medium, or high")
    if any(not isinstance(after[k], str) for k in ("objective", "scope", "requested_output", "approval_owner")):
        raise ValueError("Text engagement fields must be strings")
    append_record(case, "engagement_changes", {"changed_fields": list(updates),
        "before": {k: before.get(k) for k in updates}, "after": {k: after[k] for k in updates}})
    ledger.write_atomic(case / "engagement.json", after)
    return after

def plan(case: Path) -> dict[str, Any]:
    from .routing import recommend
    result = recommend(case)
    return {**result, "mode": result["profile"], "stages": result["steps"]}

def quality_check(case: Path) -> dict[str, Any]:
    item = read_json(case / "engagement.json")
    srcs = read_json(case / "sources.json")
    claims = read_json(case / "claims.json")
    decisions = read_json(case / "decisions.json")
    artifacts = read_json(case / "artifacts.json")
    hypotheses = read_json(case / "hypotheses.json")
    reviews = read_json(case / "reviews.json")
    actions = read_json(case / "actions.json")
    outcomes = read_json(case / "outcomes.json")
    source_ids = {s["id"] for s in srcs}
    claim_ids = {c["id"] for c in claims}
    audit = ledger.verify(case)
    # Edits through the CLI are recorded. Untracked manual edits cannot be
    # detected if no journaled change exists yet.
    changes = read_json(case / "engagement_changes.json")
    if changes:
        latest = {}
        for change in changes:
            latest.update(change["after"])
        for key, recorded in latest.items():
            if item.get(key) != recorded:
                audit["errors"].append(f"engagement.json differs from logged {key} change")
        audit["passed"] = not audit["errors"]
    blockers: list[str] = ["journal: " + x for x in audit["errors"]]
    cautions: list[str] = []
    if not item["objective"].strip(): blockers.append("engagement objective missing")
    if item["approval_owner"] == "unassigned": cautions.append("approval owner unassigned")
    for claim in claims:
        broken = set(claim.get("source_ids", [])) - source_ids
        if broken: blockers.append(f"{claim['id']} references missing sources: {sorted(broken)}")
        if claim.get("status") == "supported" and not claim.get("source_ids"):
            blockers.append(f"{claim['id']} claims support without a source")
        if claim.get("status") in ("unknown", "disputed"):
            cautions.append(f"{claim['id']} is {claim['status']}")
    for decision in decisions:
        broken = set(decision.get("claim_ids", [])) - claim_ids
        if broken: blockers.append(f"{decision['id']} references missing claims: {sorted(broken)}")
        if decision.get("status") == "approved" and not decision.get("claim_ids"):
            blockers.append(f"{decision['id']} approved without referenced claims")
        if decision.get("status") == "approved" and decision.get("owner") == "unassigned":
            blockers.append(f"{decision['id']} approved without accountable owner")
    action_ids = {a["id"] for a in actions}
    decision_ids = {d["id"] for d in decisions}
    for hypothesis in hypotheses:
        if set(hypothesis.get("claim_ids", [])) - claim_ids:
            blockers.append(f"{hypothesis['id']} references missing claims")
    for action in actions:
        if action.get("decision_id") not in decision_ids:
            blockers.append(f"{action['id']} references missing decision")
    for outcome in outcomes:
        if outcome.get("action_id") not in action_ids:
            blockers.append(f"{outcome['id']} references missing action")
        if set(outcome.get("source_ids", [])) - source_ids:
            blockers.append(f"{outcome['id']} references missing sources")
    all_ids = {r["id"] for col in ledger.COLLECTIONS for r in read_json(case / (col + ".json"))}
    for review in reviews:
        if review.get("target_id") not in all_ids:
            blockers.append(f"{review['id']} refers to missing target")
        if set(review.get("source_ids", [])) - source_ids:
            blockers.append(f"{review['id']} refers to missing sources")
    for artifact in artifacts:
        missing = set(artifact.get("claim_ids", [])) - claim_ids
        if missing: blockers.append(f"{artifact['id']} references missing claims: {sorted(missing)}")
    # OST is independently journaled; include its integrity in review readiness.
    from . import ost
    ost_check=ost.verify(case)
    if not ost_check['passed']:
        blockers.extend('ost journal: '+x for x in ost_check['errors'])
    if not claims: cautions.append("no claims have been recorded")
    if not srcs: cautions.append("no sources have been recorded")
    if not decisions: cautions.append("no decisions have been recorded")
    return {"engagement_id": item["id"], "ready_for_review": not blockers,
            "blockers": blockers, "cautions": cautions,
            "counts": {"sources": len(srcs), "claims": len(claims), "decisions": len(decisions), "artifacts": len(artifacts),
                       "hypotheses": len(hypotheses), "actions": len(actions), "outcomes": len(outcomes), "reviews": len(reviews)}, "journal": audit, "ost_journal": ost_check}

def report(case: Path) -> str:
    item = read_json(case / "engagement.json")
    sections = [f"# {item['name']} | Evidence & Decision Record", "",
                f"Type: {item['kind']} | Industry: {item['industry']} | Mode: {item['mode']}",
                f"Objective: {item['objective'] or '[NOT YET DEFINED]'}", "",
                "**Status: Working document. Not externally verified.**", ""]
    for key, label in (("sources", "Source register"), ("claims", "Claims and uncertainty"), ("decisions", "Decisions")):
        sections.extend([f"## {label}", ""])
        records = read_json(case / f"{key}.json")
        if not records: sections.extend(["None recorded.", ""])
        for r in records:
            content = r.get("statement") or r.get("question") or r.get("title")
            sections.append(f"- **{r['id']}** {content}")
            if key == "claims": sections.append(f"  - Status: {r['status']}; sources: {', '.join(r.get('source_ids', [])) or 'none'}")
            if key == "decisions": sections.append(f"  - Choice: {r['choice']}; status: {r['status']}; claims: {', '.join(r.get('claim_ids', [])) or 'none'}")
            if key == "sources": sections.append(f"  - Locator: {r['locator']}; independently verified: {r['independent_verification']}")
        sections.append("")
    check = quality_check(case)
    sections.extend(["## Readiness check", "", f"Ready for human review: {check['ready_for_review']}", ""])
    sections.extend(f"- BLOCKER: {x}" for x in check["blockers"])
    sections.extend(f"- CAUTION: {x}" for x in check["cautions"])
    sections.append("")
    return "\n".join(sections)

def skill_metadata(skill: Path) -> dict[str, str]:
    text = (skill / "SKILL.md").read_text(encoding="utf8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        raise ValueError(f"Invalid frontmatter: {skill.name}")
    header = text.split("\n---\n", 1)[0][4:]
    data = {}
    for line in header.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            data[k.strip()] = v.strip().strip('"\'')
    if not data.get("name") or not data.get("description"):
        raise ValueError(f"Skill requires name and description: {skill.name}")
    if data["name"] != skill.name:
        raise ValueError(f"Skill directory/name mismatch: {skill.name}")
    return data

def validate_skills() -> dict[str, Any]:
    errors = []
    checked = 0
    for path in sorted((ROOT / "skills").iterdir()):
        if path.is_dir():
            checked += 1
            try:
                skill_metadata(path)
                for section in ("## When to use", "## Inputs", "## Method", "## Outputs", "## Quality gates"):
                    if section not in (path / "SKILL.md").read_text(encoding="utf8"):
                        errors.append(f"{path.name}: missing {section}")
            except (ValueError, FileNotFoundError) as e:
                errors.append(str(e))
    return {"skill_count": checked, "errors": errors, "passed": not errors}
