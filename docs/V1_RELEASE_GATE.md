# Version 1.0 release gate: evidence, not an aspirational tag

Version 1.0 is **NOT approved** merely because schema tests and MCP wiring pass. Do not change the advertised version to 1.0 until these gates are satisfied with recorded evidence.

| Gate | Evidence required | Status |
| --- | --- | --- |
| Protocol correctness | Automated JSON Schema checks, round-trip MCP tool tests, packaged CLI install | Not yet verified in CI |
| Agent Skills conformance | Current skills-ref validator and actual native discovery in two unrelated hosts | Unverified |
| External adoption | Real Codex and Hermes (or a documented distinct second host) consume identical pinned revision from outside repo; no forced local workflow | Unverified |
| Host state fidelity | Unmet, covered, uncertain and unauthorized tests on an in-flight external repo; reviewer checks source references | Deterministic fixtures only |
| Specialist outcome | Minimum four blind baseline-vs-skill tasks including a no-intervention case, scored by independent reviewer; no material factual/safety regression | Unverified |
| Permissions | Host file boundary, symlink, traversal, injection, unauthorized tool attempts and data-leak probes across actual runtimes | Unit coverage only |
| Compatibility | One complete file-only reference path, one real MCP host invocation, written install/rollback instructions, versions pinned | Unverified |
| Quality | Correctly preserve earlier decisions, cite source evidence, avoid invented specialist credentials, improve task outcome vs baseline | Unverified |

Keep outputs, case definitions, host/runtime/model versions, tool permission manifests, file hash, observed timings/costs (if measurable), and reviewer rubrics. Publish anonymized evidence only with permission. Prefer an honest failed case to an invented pass.

**Merge and version policy:** This branch is implementation development. Treat \`0.9.x\` as release candidate until the table is backed by live evidence. PR #13 is audit-only and remains independent. Do not declare the entire method/skill catalog independently evaluated from a single successful task.
