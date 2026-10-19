# Getting started

## Requirements

Python 3.11 or newer. No third-party Python packages are required for the offline commands below. From the repository root, run `python vm.py --help` for supported operations.

For work on an actual company, client or venture, begin with [the first-engagement guide](FIRST_ENGAGEMENT.md). It covers a complete local operator workflow from setup through research capture, optional method selection, human/agent handoff, and an unapproved draft returned for review.

## 1. Inspect a fully fictional work cycle

```bash
python vm.py demo
python vm.py ost show fictional-harbor-supplies-demo
python vm.py trace fictional-harbor-supplies-demo --id DEC-0001
python vm.py impact fictional-harbor-supplies-demo --id CLM-0001
python vm.py audit fictional-harbor-supplies-demo
```

The demonstration is **entirely synthetic**. It does not contact real participants, access the web, validate an external source, or authorize a consequential decision. All created files are local, private by default, and gitignored. Running `demo` again with the same name stops rather than overwriting your example. To create a second run, use `python vm.py demo --name "Fictional Second Demo"`.

Open both Markdown files under `engagements/fictional-harbor-supplies-demo/deliverables/`. Compare their cited claims. The second brief contains a **proposed** successor, but the old decision still references its original claim. That is intentional. Then inspect the OST revision journal under `discovery/`.

## 2. Compare frameworks

```bash
python vm.py frameworks --goal discover_need --evidence observed
python vm.py frameworks --goal allocate_capital --evidence provisional
python vm.py frameworks --goal resolve_systemic --evidence minimal
```

Framework metadata shows applicability, prerequisites, expected deliverables and situations to avoid. It does not produce market findings or select a universally correct method. Use [the selection protocol](METHOD_SELECTION.md) and record the rationale for any consequential choice.

## 3. Create a real, private engagement

```bash
python vm.py new "Example Business" --type company --industry logistics --mode quick
python vm.py intake example-business --objective "Understand operational constraints" --approval-owner "Engagement owner"
python vm.py route example-business
python vm.py plan example-business
python vm.py source-add example-business --title "Authorized interview notes" --locator "local:interview-1" --kind interview
python vm.py claim-add example-business --text "A participant reported slow order reconciliation" --source SRC-0001
python vm.py check example-business
```

These last two statements are example commands, not actual findings. Use genuine observations and appropriate storage permissions for real work. A new source record does not prove the source's accuracy. An agent should not synthesize observations that did not occur.

## 4. Generate a reviewable working draft

```bash
python vm.py generate example-business --type decision-brief
python vm.py generate example-business --type context-pack
python vm.py audit example-business
python -m unittest discover -s tests -v
```

The generated briefs are local, immutable, content-addressed Markdown drafts. `audit` inspects event integrity; it is not independent factual verification, legal clearance, or human approval.

## 5. Bring your own agent if appropriate

Skill instructions live under `skills/*/SKILL.md`. The portable adapter is at `.agents/skills/venturemethod/SKILL.md`. Use reviewed instructions and scoped context with your preferred compatible agent. Hermes can be tested first, but no particular model or runtime is required by the CLI. Do not grant an agent unrestricted credentials or write access to reviewed shared skills.

See [skill governance](SKILL_GOVERNANCE.md) and [security](SECURITY.md) for boundaries.

## 6. Compose a work proposal across methods and capabilities

The new [composition guide](WORK_COMPOSITION.md) describes how to choose goals and inspect methods, agents, skills, tool needs and open gaps. The command plans work; it never silently runs a model or agent:

```bash
python vm.py capabilities
python vm.py compose example-business --goal map_market
python vm.py compose example-business --goal map_market \
  --method market-sizing --evidence minimal --save
```

A saved proposal is tied to the engagement's current source/claim snapshot and registry versions, so it can be compared with a later proposal without overwriting the earlier reasoning. The operator remains responsible for review and execution.
