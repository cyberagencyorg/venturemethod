# Venture Architecture: system design and operating doctrine (v0.2)

## 1. Purpose and boundary

This is **a general-purpose intelligence-to-execution framework for ventures, products, organizations, clients, and bounded professional deliverables**. Product management is a supported function, not the umbrella. A firm may need a sales intervention rather than a product; a venture may need institutional capital rather than a software feature; an investor may need to decline a deal; a small request may require only one source-checked memo.

The target outcome is less repeated setup, less re-explaining client context, faster conversion of verified understanding into usable decisions, better independent review, and cumulative improvement of reusable methods without leaking one engagement into another.

Inputs: opportunity, organization, industry, problem, company, mandate, decision, or deliverable. Outputs: necessary intelligence, prioritized questions, mutually exclusive or compatible options, accountable decisions, proportionate actions, verified outcomes, and traceable artifacts.

Not the goal: one universal PM lifecycle, a prompt directory, ungoverned autonomous external action, company-specific hardcoding, or a synthetic appearance of verified research.

## 2. Four distinct operating products

1. **Knowledge workbench:** isolated engagement, objective, audience, rights, context, entities, evidence ledger, documented uncertainty and decisions.
2. **Methods and skills foundry:** domain-specific intellectual methods, skill selection, gap analysis, skill creation, local adaptations, pinning, blind paired evaluations, improvement, rollback.
3. **Artifact factory:** audience-specific output contracts, source tracking, review, deterministic scaffolding and optional native Docs/Sheets/Slides/PDF generators.
4. **Execution bridge:** optional, permissioned, idempotent handoffs to engineering, creative, project systems, outreach tools and human operators; ingests returned proof of action and observed outcomes.

Do not collapse these into one module or tie them to a single AI harness or vendor.

## 3. Semantic layers

| Layer | Owned objects | Fundamental question |
| --- | --- | --- |
| Reality and identification | entity, jurisdiction, ownership, capability, market, actor, event | What object are we talking about and what happened? |
| Epistemics | source, observation, claim, contradiction, inference, hypothesis, confidence, provenance | What is known, claimed, uncertain or contested, and why? |
| Intent and context | client mandate, scope, requested output, audience, rights, constraints, success criterion | What are we authorized and trying to accomplish? |
| Strategic deliberation | option, causal assumption, scenario, downside, opportunity cost, recommendation | What alternatives exist and what should we test or choose? |
| Agency and governance | decision, accountable owner, authorization, role, rule, approval | Who is entitled to decide and act? |
| Operations | task, workflow, plan, dependency, tool contract, resource | What needs to happen, by whom and within what limits? |
| Results and learning | artifact, experiment, observed outcome, skill evaluation, reusable sanitized lesson | Did it work, and what have we learned? |

Ontological identity, evidence status, decision status and execution authorization MUST NOT be conflated. A company is not its marketing website. A cited statement is not necessarily supported by the source. A reviewer's recommendation is not an approved commitment. A document is not an outcome. A graph relationship is not proof of causality.

## 4. Capability families

| Family | Representative intellectual questions | Artifact families |
| --- | --- | --- |
| Entity/industry intelligence | Who operates here, with what incentives and economic constraints? | dossiers, timelines, market/competitive maps |
| Customer/opportunity | Whose behavior must change, why, and with what evidence? | interviews, job maps, opportunity trees, experiments |
| Venture/business design | What value exchange, organization and economic model could work? | venture thesis, model comparison, validation plan |
| Strategy/power/systems | What dynamics, dependencies and leverage points drive outcomes? | systems maps, strategic options, scenarios |
| Product/experience | What to build, for whom, with what acceptance and learning criteria? | discovery brief, PRD, journey, experiment |
| Marketing/brand/commercial | How will customers understand, discover, buy and retain the offering? | positioning, offers, GTM, brand architecture, campaign briefs |
| Capital/investment | What financial instruments, economics and risks fit? | funding landscape, investment memo, scenarios, diligence |
| Organization/services | What capabilities, workflows, people, responsibilities and controls are needed? | service blueprint, operating model, change plan |
| Institutions/regulation | What legal, civic, regulatory or public programs shape viability? | jurisdictional map, eligibility matrix, partnership plan |
| Execution/instrumentation | How will approved work be carried out and measured? | task contracts, acceptance tests, observed-outcome reports |

An engagement can cross families, but should load only the skills needed to address a specific question. Access to a skill does not automatically entail loading or executing it.

## 5. Routing policy

Route in this order:

1. Understand the intended **decision or practical change**, not merely the named deliverable.
2. Read constraints, permissions, deadline, risk, evidence maturity and existing capacity.
3. Ask whether the correct first move is research, a small test, a recommendation, an operational intervention, a commercial artifact, or no action.
4. Select domain methods by their preconditions, known blind spots, and the minimal set of steps that can change the decision.
5. Invoke skills in dependency order only where necessary; preserve intermediate artifacts as addressable records, not conversational memory.
6. Route to a human decision owner for consequential actions, and return outcome evidence after execution.

**Implemented:** type profiles plus transparent keyword-based recommendations from objective, scope and requested output. This is a deterministic first selector, not intelligent method inference or a semantic classifier. Always inspect `why`, `missing_intake` and `status`; allow override through a future explicit routing decision record.

**Target router:** a cost-aware planner with precondition checks, causal hypotheses, capability coverage, learned selection benchmarks, counterexamples and residual uncertainty. It should be allowed to abstain rather than supply a false-best method.

## 6. Evidence and event model

Current record chain:

```
Source -> Claim -> (Hypothesis / Option) -> Decision -> Action -> Outcome
               \-> Artifact
Review -> [Claim | Decision | Entity]
```

Current local event journal stores immutable record creations and review assertions; projections are derived. Each event includes sequence, previous hash and hash of canonical content. This **detects divergence and accidental tampering** on a single-writer local filesystem. It is not a third-party timestamp, identity proof, immutable remote log, database transaction, verified source archive or defense against a malicious administrator replacing the entire journal.

A user's explicit intake edits are recorded separately in the same journal. Manually changing source/claim projection files breaks integrity checking. Clients should never directly edit projections. For production, migrate to a transactional append-only PostgreSQL event store with unique immutable IDs, tenant isolation and signed/anchored checkpoints. SQL/search/graph/vector layers should be projections from the canonical authorized record set, not disconnected copies.

## 7. Relationship to existing repos

- `BradKhan/open-ASS` is an **optional engineering adapter**. Transfer scoped requirements and acceptance tests only after the client decision contract authorizes execution. Never import client data by default.
- `cyberagencyorg/creative-studio` is an **optional creative adapter**. Pass audience, substantiated claims, approved brand profile and creative constraints. Clients such as OpenBox are separate engagements inside that studio, never an identity constraint here.
- External research systems and publishing apps are adapters with distinct credentials, rate limits, scopes and audit histories.

This repository's core must work offline and without these dependencies.

## 8. Cross-engagement learning without customer leakage

There are three levels of information with different reuse permissions:

- **Case-private facts:** source excerpts, pricing, people, identifiers, documents, results and negotiations. No automatic sharing.
- **Client-approved abstractions:** generic process patterns explicitly approved for broader use and scrubbed of identifying details.
- **Framework-global methods:** public methods, original skills, safe test fixtures, quality rubrics and general reusable knowledge.

Skill improvements should be traceable to documented failures and opt-in sanitized learnings, not to unconstrained pooled embeddings of confidential case materials. Model-training or third-party transmission requires a separate permission boundary.

## 9. Skill foundry as an experimental process

Find a capability gap -> search external/internal candidates -> legal/security review -> select baseline -> create/adapt original skill -> design positive, negative and adversarial tests -> run paired independent agent evaluations -> grade blind -> analyze variance and cost -> approve limited scope -> monitor regressions -> rollback if worse.

Current functionality: 25 original SKILL.md files with structural checks, three-case fixtures each, metadata-only external skill candidate registry, paired evaluation manifest generator and manual-score aggregation. It **does not run models, fetch skills, auto-update them, evaluate factual accuracy or prove they work in production**. Human-supplied scores must be distinguished from objective structural tests and measured business outcomes.

## 10. Deployment principles

- Local-first and git-native for methods, templates and code.
- Private local engagement directories excluded from version control by default.
- Explicit publication state, independent reviews for consequential deliverables.
- Least privilege and separate consent for reading connected data versus writing to it.
- Idempotent, signed scoped handoffs at future integration boundaries.
- Quantitative numbers labeled by unit, basis, uncertainty and provenance.
- No fake user interviews or market metrics.
- Reuse a method because it is useful, not because it is fashionable or popular.
