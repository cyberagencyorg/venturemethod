# Living knowledge: version, branching, review, propagation (v0.3 design)

## Governing premise

The durable product is **evolving, accountable knowledge**, not a set of static artifacts. A deck, financial model, PRD or memo is a view of specific underlying entities/claims/decisions as of a version, for an audience and approval state. A file export is a derivative that should be reproducible from the approved snapshot and render configuration.

## Lifecycle

1. **Observe / ingest:** retain a dated immutable source record and content fingerprint subject to rights and privacy constraints. Evidence may be external, internal, reported or inferred; keep types separate.
2. **Reconcile:** perform entity identity resolution, source deduplication and claim comparison. New evidence can support, weaken, contradict or leave existing claims unchanged.
3. **Propose:** create draft successor knowledge and a change-set containing what changed, why, supporting/refuting evidence, affected stakeholders, reversibility and proposed review.
4. **Assess impact:** traverse the dependency graph both directly and transitively; list stale or potentially affected hypotheses, decisions, plans, models, narratives, public claims and downstream contracts.
5. **Review:** independent actor assesses meaning, evidence, method appropriateness and permission, not merely JSON validity.
6. **Adopt:** authorized approval binds a precise proposal + record version + evidence snapshot + actor identity, then updates the canonical read model atomically. Never infer approval from a branch merge alone.
7. **Regenerate selectively:** only dependent views with meaningful invalidation and matching audience/scope should update. Some require fresh human judgment and cannot be auto-rewritten.
8. **Reassess:** maintain review dates, freshness policies, decision reopen conditions and learned outcomes. Schedule review based on volatility and decision consequence, not a universal weekly sweep.

## Distinct stores / control planes

**Methods-and-skills repository:** public or internal source code and reusable instructions. Protected `main`, short feature branches, PR-based updates, SemVer releases, pinned upstream SHA/URL/license, automated style/schema/security/fixture checks, required owner review for breaking methodology changes. No client information.

**Private engagement knowledge:** one tenant/engagement permission boundary, never committed to the public methodology repository. Can begin as local versioned Markdown and JSON with Git for solo work; use a private encrypted Git repository per engagement where appropriate. When multiple actors write concurrently, move canonical events and approvals to a transactional database with RBAC and audit logs. Git diffs alone do not provide transactional business truth, consent or access control.

**Artifacts and media:** object storage with content digests, access restrictions and retention rules; Git may hold small textual source and manifest but not large or sensitive raw datasets. A generated file references exact knowledge snapshot, generator version, method variants and reviewer disposition.

**Work management:** issues and PRs link to knowledge IDs and decisions; they do not replace evidence or decision lineage. Authorized external effects need their own explicit tool permissions.

## Git / collaboration policy

- `main` represents accepted method/skill code, not "the one true current interpretation" of a customer's business.
- `feature/<issue>-<topic>` for small code changes; `method/<id>-<change>` for technique changes; `release/<version>` only if release maintenance requires it.
- Each PR includes: **problem**, proposed method/skill change, evidence for change, affected downstream contracts, licensing/provenance, regression fixtures, failures, rollback and human owner.
- No automatic rebase/squash of epistemic histories without preserving original immutable source/proposal/decision IDs. Squashing implementation commits is acceptable if immutable business event IDs persist elsewhere.
- Private engagement exploration can use `hypothesis/<topic>` branches for solo prototypes, but long-lived competing interpretations belong in explicit hypothesis versions/alternative branches of the knowledge graph with an accountable merge decision. No automatic truth merge.
- Release tags pin skills, framework catalog, schema versions, quality gates and dependency hashes. `engagement.lock` pins the exact method and skill versions used for a client output.

## What has been implemented in v0.3

- Existing v0.2 hash-chained, local single-writer journal, event replay checks, source/claim/decision references and independent review assertions.
- New claim successor proposal: `claim-revise`. Preserves the old claim and creates an **unapproved** new claim with `supersedes_id`; rejects a second direct successor from the same predecessor in the current local linear history.
- New reverse dependency inspection: `impact`. Reports directly and transitively linked records that need reassessment. Old decisions are **not** silently repointed to new evidence.
- Structural regression tests for a changed claim with an existing decision and against cross-case source references.

## What is specifically NOT implemented

- Authenticated approvals, cryptographic signer verification, atomic adoption/merge and multi-writer concurrency.
- Automatic semantic contradiction detection or calibrated confidence updates.
- Automatic real-world source refresh or model-invoked revisions.
- Complete ontology dependency edges, complete graph diff, precise incremental artifact rebuild and synchronization with external Docs/Sheets/Slides/Linear.
- Secure client data administration, GDPR/retention processing, legal admissibility, real-time cross-client authorization.
- Immutable external anchoring of journal head. The local hash chain detects accidental/naive tampering, but a privileged actor could rewrite and rehash the whole local log.

Do not equate `proposed_unapproved`, `reviewed`, `merged`, `published`, or `validated`. These are separate transitions.

## Acceptance tests for first production-worthy knowledge release

- Contradict a market-size figure. Verify all relevant downstream financial models, ICP choices and investor-deck slides are identified; unrelated outputs remain unchanged.
- Update a customer interview. Verify interpretation remains attributed and does not rewrite the raw source; a contradictory account can coexist.
- Change a venture's pricing assumptions. Verify model recalculation is tied to exact dataset version and does not silently rewrite signed contracts.
- Simultaneously propose incompatible claim versions. Require an explicit conflict resolution/merge decision; do not use last-write-wins.
- Attempt cross-client source reuse and secret leakage through public skill/PR logs. Reject the operation and record an audit incident.
- Prove a removed/deprecated upstream skill does not break a previously released engagement. Pin or sandbox its dependency.
- Open a previous release as-of a date, reconstruct its evidence and approved render, then compare to today's current view.
- Validate a decision restart after months of inactivity without feeding an entire unbounded chat history back into a model.
