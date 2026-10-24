"""CLI for external consumption; the legacy va.py remains available."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from .portable import ContractError, assess, catalog_search, context_pack, inspect_paths, method_get, skill_get
from .portable_export import export_skill, verify_export


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
    args = parser.parse_args(argv)
    try:
        if args.command == "search":
            obj = catalog_search(args.query, args.limit)
        elif args.command == "inspect":
            obj = {"resources": inspect_paths(args.root, args.files),
                   "disclosure_warning": "Contains authorized project text. Do not upload without host permission."}
        elif args.command in ("assess", "pack"):
            # No filesystem crawling. The file is explicitly provided by the caller.
            if args.context.stat().st_size > 131072:
                raise ContractError("Context file exceeds budget")
            state = json.loads(args.context.read_text(encoding="utf-8"))
            obj = assess(state) if args.command == "assess" else context_pack(state, args.max_chars)
        elif args.command == "export-skill":
            obj = export_skill(args.destination, apply=args.apply)
        elif args.command == "verify-export":
            obj = verify_export(args.destination, expected_bundle_sha256=args.expected_sha256)
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
