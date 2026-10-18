# Roadmap: strengthen the framework before building a platform

**Current local release:** v0.5. See [capability status](CAPABILITY_STATUS.md) for what actually runs. This document describes priorities, not delivered functionality or commitments.

## North star

An independent practitioner can start from an unfamiliar company, opportunity, problem, or mandate, select appropriate methods, produce defensible work, preserve decisions and their evidence, and revisit that work as the world changes. It should remain portable across models and agents.

A capability earns its place when it saves meaningful human effort **and** improves the quality, clarity, or continuity of decisions. Large prompt catalogs, dashboards, agent role counts, and artifact volume are not success measures.

## P0: fidelity and repeatable use

- [x] Private engagement structure, evidence/decision references, revision proposals and explicit impact traversal.
- [x] Local Opportunity Solution Tree with evidence-linked proposals and recorded review events.
- [x] Method catalog with prerequisites, limits and conservative candidate selection.
- [x] Fictional, repeatable local example demonstrating revision of knowledge and unchanged prior decision history.
- [x] Public-facing README and ABOUT that distinguish available capabilities from aspirations.
- [ ] Audit external method and skill libraries at individual capability level; represent overlap, variants, licenses and status without inflating coverage.
- [ ] Build a method-choice record that persists why alternatives were rejected and when selection should be reviewed.
- [ ] Benchmark a realistic solo consulting engagement through independent human assessment, including counterfactual methods and alternatives.

**P0 gate:** A skilled user can complete one bounded engagement with explicit evidence, method choice, professionally useful decision, changing facts, and a reviewable delta. Tests cover failure cases and the output is independently evaluated. Current structural tests do not meet this gate.

## P1: research and knowledge that can be maintained

- [ ] Read-only source adapters with rights, freshness, duplication and identity controls.
- [ ] Typed support/opposition of claims, contradictions, review windows and method/knowledge version references.
- [ ] Audited proposal, approval and supersession workflows, including genuine reviewer identity before any production claim.
- [ ] Scoped dependency analysis and selective update proposals for analyses and derived artifacts.
- [ ] End-to-end case covering company and market research, with source quality checked independently.

**P1 gate:** New research changes a previously supported conclusion, and the system can show the evidence, old and proposed view, affected decisions, and which outputs need review, without silent rewriting.

## P2: skill quality and cross-disciplinary delivery

- [ ] Real skill evaluation against a baseline, using blinded substantive assessment and repeatable cases.
- [ ] Vet, pin and install optional third-party skills with author/license/security review; support safe upgrades and rollback.
- [ ] Add high-demand specialty methods only where a demonstrated gap exists: market sizing, pricing, customer research, product discovery, financial scenarios, diligence and organizational diagnosis.
- [ ] Make agent adapters execute bounded tasks and return records, costs, sources, outputs, and review needs. Hermes first for testing, but not required by core.
- [ ] Export professionally reviewable memos and models with explicit artifact/version provenance.

**P2 gate:** Demonstrate real increases in decision usefulness and reduced analyst effort on at least three different engagement classes, with independent reviewers and disclosed limitations.

## P3: interoperability, not platform expansion

- [ ] Stable input/output contract for approved handoffs to software, creative and PM systems.
- [ ] Scoped import/export of workspaces and canonical knowledge without a required UI or provider.
- [ ] Tool-neutral schemas, compatibility tests, migration policy and a clear contribution process.

**Not in this repository's immediate scope:** portal UI, custom domains, hosted billing, customer CRM, investment fund management, media production engines, and generalized multi-agent infrastructure. Those can be separate projects or adapters.

## Release and publication checklist

Before public distribution, choose an owner-approved license, check all dependencies and attributed materials, remove client data, document supported Python versions, validate a clean fresh-clone install, and publish benchmark methodology rather than unverified quality claims.
