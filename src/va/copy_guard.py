"""Read-only mechanical checks for project-owned writing restrictions.

This checks literal phrases and punctuation preferences; it does NOT evaluate
copy quality, positioning, factual accuracy or overall voice fidelity.

Usage: python -m src.va.copy_guard --rules /path/rules.json --text /path/draft.md
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

NAMED_CHARACTERS = {"em_dash": chr(0x2014), "en_dash": chr(0x2013)}


def _normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text.casefold()).strip()


def validate_rules(rules: dict) -> dict:
    if not isinstance(rules, dict) or rules.get("schema_version") != "1.0":
        raise ValueError("Rules require schema_version 1.0")
    for key in ("forbidden_phrases", "forbidden_characters"):
        if not isinstance(rules.get(key, []), list):
            raise ValueError(f"{key} must be an array")
    for phrase in rules.get("forbidden_phrases", []):
        if not isinstance(phrase, str) or not phrase.strip():
            raise ValueError("Forbidden phrases must be non-empty text")
    for char in rules.get("forbidden_characters", []):
        if char not in NAMED_CHARACTERS:
            raise ValueError("Only named punctuation restrictions are supported")
    return rules


def check(text: str, rules: dict) -> list[dict]:
    rules = validate_rules(rules)
    simplified = _normalize(text)
    problems = []
    for index, phrase in enumerate(rules.get("forbidden_phrases", []), start=1):
        if _normalize(phrase) in simplified:
            problems.append({"kind": "forbidden_phrase", "rule": index})
    for name in rules.get("forbidden_characters", []):
        if NAMED_CHARACTERS[name] in text:
            problems.append({"kind": "forbidden_character", "rule": name})
    return problems


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Check a draft against project-owned writing restrictions")
    parser.add_argument("--rules", required=True, type=Path)
    parser.add_argument("--text", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        rules = json.loads(args.rules.read_text(encoding="utf-8"))
        draft = args.text.read_text(encoding="utf-8")
        problems = check(draft, rules)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
        print("copy check configuration error: " + str(exc), file=sys.stderr)
        return 2
    if problems:
        for item in problems:
            print(f"FAIL: {item['kind']} {item['rule']}")
        return 1
    print("PASS: no explicit phrase or punctuation restrictions violated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
