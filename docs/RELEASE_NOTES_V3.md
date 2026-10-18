# v0.3 local architecture and audit release (2026-10-19)

## Changes
- Audited the intended system against Huryn PM Skills, Product on Purpose, Dean Peters, PM Brain, BMAD, GitHub Spec Kit, Agent Skills, Anthropic Skill Creator and skills.sh as a discovery source.
- Added a **34-entry methodology comparator catalog** with explicit goal, expected output, source, evidence level, relevance and contraindications.
- Added `frameworks` CLI command, with no automatic winner or fictitious competency scoring.
- Added **unapproved draft claim successor** operation (`claim-revise`) and a transitive dependency impact inspector (`impact`).
- Added architecture, knowledge governance, branching and adversarial audit documents.
- Added regression tests for the comparator and change mechanics.

## Unchanged limitations
- 25 first-party agent skill instruction folders, with structure validated but not empirically benchmarked.
- No live research connectors, semantic graph, real-time method learner, production security/permissions, user authentication, multi-writer merge, spreadsheet/slide exporter or autonomous agent runs.
- Upstream inventories are catalog-level, not individually benchmarked; no imported external skill contents.
- The local journal has no independently anchored integrity head, so privileged rewriting is possible.

## Validation
Run `python -m unittest discover -s tests -q` and the relevant CLI smoke test before using. All claims of performance beyond offline structural behavior require additional evidence.
