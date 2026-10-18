# Adversarial architecture review (v0.2, October 2026)

This is an evaluation of the actual local implementation, not a retrospective claim that the full platform exists.

## High-priority failure modes

| Finding | Priority | Current status | Acceptance condition |
| --- | --- | --- | --- |
| No autonomous/connected research, source refresh or entity resolution | Critical | Not built | Dated primary-source collection, deduplication, permissions and contradiction tests against real external data |
| Agent skill quality unevaluated on real agent outputs | Critical | Paired evaluation scaffolds only | Real, isolated with/without skill runs across multiple models and domains, blinded grading and measured cost |
| Journal has a single local writer and no database transactions | High | Hash chain and replay; no concurrency | Postgres transactional event store and tested recovery from interruption/concurrent writers |
| Scopes/permissions editable locally; no verified authentication | High | Human approval state not inferred | Authenticated signers, RBAC, explicit tool authorizations and audit policy |
| Semantic model not persisted as typed, globally resolvable ontology | High | Entity candidates and local references | Versioned typed schemas, identity merges, external IDs, support/challenge edges and migration tests |
| No external license scanner or executable skill sandbox | High | Passive candidate registry refuses execution | Pin/license/attribution/security review with sandbox and security tests |
| Artifact generation currently just Markdown | High | Immutable, source-linked drafts | Audience-specific live documents, slides, financial models and contract-specific validators |
| No actual bridge to Open ASS or Creative Studio | Medium | Contracts documented | Signed approved adapter requests, dry runs, idempotent statuses and return results |
| Evidence status lacks robust independent corroboration calculus | High | Sources, claims, human review assertions | Separate observed facts, management claims, inference, estimates and contradictions; freshness and confidence calibration |
| Router has simplistic lexical matching | High | Explainable/abstains on insufficient objective | Benchmark task selection with alternatives, cost, prerequisites and evidence maturity |
| Global skill learning could accidentally leak client material | Critical | Files isolated; no pooled store | Consent-controlled anonymization and adversarial no-leak tests across many engagements |
| Templates could bias questions toward a software product | Medium | Venture/industry/service/marketing/capital modules added | Cross-domain blinded evaluations including stop/no-go and non-product outcomes |

## What is actually verified

- Deterministic unit tests for journal integrity, recovered projections, source/claim/decision linkages, cross-case record rejection, route behavior, no auto-approvals, draft artifacts, candidate-only external skill entries and incomplete skill evaluations.
- 25 SKILL.md folders pass structural validation.
- Reproduction of one fictional end-to-end engagement via CLI is recorded in `examples/synthetic-operator/` after release build.

## What is not verified

- Historical or current truth of any customer/industry/market claim.
- Correct method choice on unseen real-world tasks.
- Better business outcomes compared with experienced consultants and product leaders.
- Safe production use with regulated or confidential clients.
- AI model agent execution, multi-agent collaboration, independent research quality or ROI.

## Release decisions

v0.2 is suitable for local experimentation, method engineering and evaluating the operating architecture. It is **not** a live autonomous consultancy, a secure enterprise data platform, a certified source verification engine or a deployable unattended worker.

Next release must prioritize actual domain execution and evidence quality rather than multiplying static Markdown skills.
