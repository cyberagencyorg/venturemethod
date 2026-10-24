# Version 1.0 stabilization review

Date: 24 October 2026
Baseline: audit PR #13. Implementation: draft PR #14, candidate package 0.9.0.

## Product boundary

Venture Method is a selective professional reference and composition system. It is not the host's agent operating system, tool authority, memory database or project-management mandate. The consumer keeps its accepted decisions, artifacts, instruction precedence and ability to decline consultation.

## Priority order and acceptance evidence

| Priority | Product deficiency | Implemented and verified | Remaining acceptance evidence |
| --- | --- | --- | --- |
| P0-1 | External discoverability | Portable self-contained Agent Skill, capability/skill/method search, Python wheel, CLI and local stdio MCP | Native Codex/Hermes discover and choose relevant methods in separate host repositories |
| P0-2 | Typed and trustworthy contracts | 12 JSON Schema 2020-12 contracts; composition advisory permissions are always empty, approvals pending; semantic composition verifier detects identity/dependency errors | Actual external host honors typed boundaries under adversarial instructions |
| P0-3 | Authentic host assessment | Explicit POSIX-safe file snapshot, SHA-256 sources, exact-quote proposed gaps, no-op when no evidence, dependencies and host-covered assumptions retained | Real in-flight project assessment corroborated by independent reviewer, including correct abstention |
| P0-4 | Specialist effectiveness | Evidence-audit and product-requirements procedures improved; paired evaluation protocol and artifact verifier exist | Blinded same-model baseline comparison across Codex/Hermes cases; no material accuracy or authority regression |
| P0-5 | Interoperable execution interface | Independent Node client to Python MCP stdio tested; external Open ASS static checkout accepts a self-contained exported skill | Live native agent tool calls, scope-denial probes and permission receipts |

## Defects corrected in this stabilization series

1. Composition output schemas previously checked only the existence of authorization fields, allowing malformed yet structurally accepted privileged work units. The advisory schema now derives from the canonical work-unit contract and enforces zero tools, zero authorized effects and pending review. Independent Python and Node negative tests attempt escalation.
2. Published plans previously allowed identity or prerequisite inconsistency that required consumers to inspect every field manually. `verify-composition` now checks project binding, unit identities, sequential dependencies, exclusions and authorizations.
3. Catalog discovery previously searched capability names, missing named skills and established methodologies. Search now spans all three canonical identity families and returns related matched IDs without claiming applicability.
4. First-use composition previously required manual state JSON editing to add multiple dependent capabilities. The CLI now supports successive explicit-source proposals and `--depends-on`, followed by `compose` and `verify-composition`.
5. Host-covered prerequisites previously disappeared from composition. They now remain visible under `preconditions_covered`, clearly treated as host-reported completion rather than externally verified fact.

## Out of scope for P0

No graph persistence, model router, agent manager, unbounded filesystem crawler, hosted API, automatic publication, delegated writes or forced engagement initialization. Those require concrete buyer/consumer evidence before authorization or implementation.

## Release decision

Technical build passes 151 tests (verified CI commit `6a70fc78f6b92de2164eccba3f76df3c08d38815`) and 12 JavaScript-validated schemas, an isolated wheel smoke, official skill validation, a Node-to-Python MCP round trip, and a pinned Open ASS checkout distribution smoke test.

**Not approved as 1.0.** Static compatibility is not an independent agent benchmark. An external host can still provide an invented gap, so source quote matching cannot establish analytical truth. Live Codex/Hermes trials, blinded outcome evaluation, real permission-denial evidence and an accountable human release decision remain open in issue #16.

Keep PR #13 review-only and PR #14 draft until explicit acceptance. No release/tag or main-branch merge merely because CI is green.
