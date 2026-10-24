# Version 1.0 release gate: implementation and independent evidence

Last technical verification: 2026-10-24, implementation branch \`feat/portable-adoption-v1\`. The code is versioned \`0.9.0\`; **1.0 is not yet certified or released**.

| Requirement | Available evidence | Status |
| --- | --- | --- |
| Portable reference format | Pinned official \`skills-ref\` validator runs on all 26 first-party skills and the portable adapter | Automated verified |
| Typed contracts | 10 JSON Schema 2020-12 definitions, Python and Node validation, cross-reference and negative tests | Automated verified |
| Bounded host assessment | Evidence-linked explicit host-state contract, correct abstention, controlled scan and integrity checks | Automated verified on fixtures |
| External distribution | Explicit self-contained skill export with non-overwrite and rollback path; Python wheel installation from outside checkout | Automated verified |
| Tool interoperability | Python SDK v2 in-memory test, Node SDK v2 to Python server over stdio, only read-only tools | Automated verified |
| Specialist quality | Paired evaluation structure and independent reviewer rubric exist, no live independent agent results | BLOCKED |
| Real host adoption | No documented native skill discovery and use in both Codex and Hermes on actual host project | BLOCKED |
| Tool/authority security in real runtimes | Unit path/symlink/authorization checks exist, but no hostile input or write-attempt traces in live harnesses | BLOCKED |
| Repeated results and performance | No verified end-to-end baseline improvements, human attention/cost or regression outcomes | BLOCKED |
| Version 1.0 approval | Requires accountable decision after evidence review | BLOCKED |

See \`docs/V1_HOST_VALIDATION_RUNBOOK.md\` and \`evals/portable/PROTOCOL.md\`.

Do not equate a successful structured test, a valid skill directory, a compiled JSON Schema, a local MCP handshake or an agent self-review with verified professional competence. No one has yet authenticated specialist execution, tested actual host migration boundaries, or approved 1.0.

Do not merge an unverified claim into the main branch. PR #13 remains the independent review.
