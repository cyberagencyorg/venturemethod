# Version 1.0 release gate: implementation and independent evidence

Technical verification: 2026-10-24 on implementation branch `feat/portable-adoption-v1`. The code is versioned \`0.9.0\`; **1.0 is not yet certified or released**.

| Requirement | Available evidence | Status |
| --- | --- | --- |
| Portable reference format | Pinned official \`skills-ref\` validator runs on all 26 first-party skills and the portable adapter | Automated verified |
| Typed contracts | 10 JSON Schema 2020-12 definitions, Python and Node validation, cross-reference and negative tests | Automated verified |
| Bounded host assessment | Snapshot from explicit host files, source-anchored gap proposal, no-op and typed read-only work plan | Automated verified on fixtures |
| External distribution | Self-contained Agent Skill with host-specific guide, SHA-256 inventory verification, no overwrite; isolated Python wheel installation | Automated verified |
| Tool interoperability | Python MCP in-memory test, independent Node client to Python server, typed work-plan and provider registry endpoints, no write tools | Automated verified |
| Specialist quality | Paired evaluation verifier and reviewer protocol exist, no live independent agent results | BLOCKED |
| Real host adoption | No documented native skill discovery and use in both Codex and Hermes on actual host project | BLOCKED |
| Tool/authority security in real runtimes | Unit path/symlink/authorization checks exist, but no hostile input or write-attempt traces in live harnesses | BLOCKED |
| Repeated results and performance | No verified end-to-end baseline improvements, human attention/cost or regression outcomes | BLOCKED |
| Version 1.0 approval | Requires accountable decision after evidence review | BLOCKED |

See \`docs/V1_HOST_VALIDATION_RUNBOOK.md\` and \`evals/portable/PROTOCOL.md\`.

Do not equate a successful structured test, a valid skill directory, a compiled JSON Schema, a local MCP handshake or an agent self-review with verified professional competence. No one has yet authenticated specialist execution, tested actual host migration boundaries, or approved 1.0.

Do not merge an unverified claim into the main branch. PR #13 remains the independent review.
