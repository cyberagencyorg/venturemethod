"""CLI for external consumption; the legacy va.py remains available."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from .portable import ContractError, assess, catalog_search, context_pack, inspect_paths, method_get, skill_get, snapshot_project, propose_gap, work_plan, provider_catalog
from .portable_export import export_skill, verify_export
from .composition_v1 import compose, verify_composition


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="venturemethod")
    sub = parser.add_subparsers(dest="command", required=True)
    search = sub.add_parser("search", help="Discover capability IDs (lexical, advisory)")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=6)
    inspect = sub.add_parser("inspect", help="Inspect explicitly authorized local UTF-8 files")
    inspect.add_argument("--root", type=Path, required=True)
    inspect.add_argument("--file", action="append", required=True, dest="files")
    assess_cmd = sub.add_parser("assess", help="Assess a host-provided, read-only JSON contract")
    assess_cmd.add_argument("context", type=Path)
    pack = sub.add_parser("pack", help="Build bounded reference packet")
    pack.add_argument("context", type=Path)
    pack.add_argument("--max-chars", type=int, default=8000)
    verify_plan = sub.add_parser("verify-composition", help="Reject inconsistent or privilege-bearing composition artifacts")
    verify_plan.add_argument("plan", type=Path)
    composition = sub.add_parser("compose", help="Propose up to eight ordered advisory capabilities with explicit dependencies")
    composition.add_argument("context", type=Path)
    composition.add_argument("--limit", type=int, default=3)
    plan = sub.add_parser("plan", help="Produce a typed, non-executable work proposal")
    plan.add_argument("context", type=Path)
    providers = sub.add_parser("providers", help="Inspect canonical first-party provider maturity")
    m = sub.add_parser("method")
    m.add_argument("id")
    s = sub.add_parser("skill")
    s.add_argument("id")
    export = sub.add_parser("export-skill", help="Dry-run or explicitly export a self-contained agent skill")
    export.add_argument("--destination", type=Path, required=True)
    export.add_argument("--apply", action="store_true", help="Create the new skill directory")
    verify = sub.add_parser("verify-export", help="Verify every exported file against its manifest and optional trusted bundle digest")
    verify.add_argument("--destination", type=Path, required=True)
    verify.add_argument("--expected-sha256", type=str)
    snapshot = sub.add_parser("snapshot", help="Produce a read-only host-state draft from explicitly nominated project files")
    snapshot.add_argument("--root", type=Path, required=True)
    snapshot.add_argument("--file", action="append", dest="files", required=True)
    snapshot.add_argument("--task", required=True)
    snapshot.add_argument("--project", required=True)
    propose = sub.add_parser("propose", help="Propose one exact-source-anchored capability gap without modifying files")
    propose.add_argument("--context", type=Path, required=True)
    propose.add_argument("--resource-id", required=True)
    propose.add_argument("--quote", required=True)
    propose.add_argument("--capability", required=True)
    propose.add_argument("--skill", required=True)
    propose.add_argument("--reason", required=True)
    propose.add_argument("--priority", default="high")
    args = parser.parse_args(argv)
    try:
        if args.command == "search":
            obj = catalog_search(args.query, args.limit)
        elif args.command == "inspect":
            obj = {"resources": inspect_paths(args.root, args.files),
                   "disclosure_warning": "Contains authorized project text. Do not upload without host permission."}
        elif args.command == "verify-composition":
            if args.plan.stat().st_size > 131072:
                raise ContractError("Composition document exceeds size limit")
            obj = verify_composition(json.loads(args.plan.read_text(encoding="utf-8")))
        elif args.command == "snapshot":
            obj = snapshot_project(project=args.project, task=args.task,
                                   root=args.root, paths=args.files)
        elif args.command in ("assess", "pack", "propose", "plan", "compose"):
            # No filesystem crawling. The file is explicitly provided by the caller.
            if args.context.stat().st_size > 131072:
                raise ContractError("Context file exceeds budget")
            state = json.loads(args.context.read_text(encoding="utf-8"))
            if args.command == "assess":
                obj = assess(state)
            elif args.command == "pack":
                obj = context_pack(state, args.max_chars)
            elif args.command == "plan":
                obj = work_plan(state)
            elif args.command == "compose":
                obj = compose(state, max_units=args.limit)
            else:
                obj = propose_gap(state, capability_id=args.capability,
                                  skill_id=args.skill, resource_id=args.resource_id,
                                  quote=args.quote, reason=args.reason,
                                  priority=args.priority)
        elif args.command == "export-skill":
            obj = export_skill(args.destination, apply=args.apply)
        elif args.command == "verify-export":
            obj = verify_export(args.destination, expected_bundle_sha256=args.expected_sha256)
        elif args.command == "providers":
            obj = provider_catalog()
        elif args.command == "method":
            obj = method_get(args.id)
        else:
            obj = skill_get(args.id)
        print(json.dumps(obj, indent=2, ensure_ascii=False))
        return 0
    except (ContractError, ValueError, KeyError, OSError) as exc:
        print(f"venturemethod: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
