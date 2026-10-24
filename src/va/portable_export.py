"""Explicit, self-contained Agent Skill distribution for an authorized host.

Dry-run by default. Never overwrite an existing skill or modify unrelated host
files. The host can remove the exported directory to roll back the installation.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from .portable import ContractError, catalog, library_path

EXPORTED_SKILL = """---
name: venturemethod
description: Consult an independent venture, product, research or organizational method library selectively, only when a current project has an evidenced unmet need. Preserve the host workflow and decline unnecessary intervention.
metadata:
  version: "0.9.0"
---
# Venture Method, host-consumable reference

This directory is a self-contained, read-only reference. It does not grant the
agent permission to use new tools, read new files, delegate, publish or modify
the host project. The user's current task and existing project rules prevail.

1. Inspect the relevant host materials only within existing host permissions.
2. Identify one specific, currently unmet need citing the actual source and
   checking that prior work does not already cover it.
3. Consult [the adoption instructions](references/ADOPT.md), then only the
   relevant named file in \`references/skills/\` if one is justified.
4. If nothing useful and new is warranted, decline intervention.
5. Separate observation, source assertion, inference and authorization;
   follow the selected skill's documented exclusions.
6. Offer the smallest reversible contribution and obtain host approval before
   modifying anything. Do not transfer confidential excerpts to external tools.
7. Report uncertainties and whether the skill was actually executed or merely
   consulted. Never claim specialist certification based on these references.

The [capability index](assets/catalog.json) and
[portable integration guide](references/PORTABLE_ADOPTION.md) are optional
and should only be loaded as needed. Mapped does not mean implemented,
benchmark-tested or authorized.
"""


def export_skill(destination: Path, *, apply: bool = False) -> dict:
    """Return explicit export plan or write a new, isolated native skill folder."""
    if destination.name != "venturemethod":
        raise ContractError("Destination must end in /venturemethod")
    if not destination.is_absolute():
        raise ContractError("Specify an absolute destination")
    cursor = destination
    while cursor != cursor.parent:
        if cursor.is_symlink():
            raise ContractError("Symlinked export path rejected")
        cursor = cursor.parent
    if destination.exists() and (not destination.is_dir() or any(destination.iterdir())):
        raise ContractError("Destination exists and is not empty; remove it explicitly first")
    c = catalog()
    assets = {
        "SKILL.md": EXPORTED_SKILL,
        "references/ADOPT.md": library_path("ADOPT.md").read_text(encoding="utf-8"),
        "references/PORTABLE_ADOPTION.md": library_path("docs/PORTABLE_ADOPTION.md").read_text(encoding="utf-8"),
        "assets/catalog.json": json.dumps({
            "schema_version": "1.0.0",
            "methods": c["methods"], "capabilities": c["capabilities"],
            "skills": c["skills"],
            "warning": "Reference records; implementation and competence not implied."
        }, indent=2),
    }
    for item in c["skills"].values():
        name = item["name"]
        assets[f"references/skills/{name}.md"] = library_path(
            f"{item['path']}/SKILL.md").read_text(encoding="utf-8")
    file_list = [{"path": name, "sha256": hashlib.sha256(body.encode()).hexdigest()}
                 for name, body in sorted(assets.items())]
    manifest = {"schema_version": "1.0.0", "files": file_list,
                "destination": str(destination), "effects": ["create_new_skill_directory"] if apply else []}
    if apply:
        destination.mkdir(parents=True, exist_ok=True)
        for rel, body in assets.items():
            target = destination / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(body, encoding="utf-8")
        # Manifest does not hash itself; it inventories the skill's source files.
        (destination / "assets" / "export-manifest.json").write_text(
            json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest
