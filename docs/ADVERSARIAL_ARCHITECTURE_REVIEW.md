# Adversarial architecture review

**Project:** Khan's Venture Method Framework (Venture Method)  
**Review date:** 2026-10-19  
**Baseline inspected:** private `cyberagencyorg/venturemethod` v0.6 at commit `1d9e4a4b55d80def4ed5e23e261d7ac22deeaa87`; README/ABOUT revision on `docs/purpose-and-operating-scope`.  
**Status:** Technical and conceptual audit, not a professional certification or live agent benchmark.

## Executive assessment

The fundamental separation among engagement knowledge, professional methods, skills, workflow, execution adapters, and evidence review is worth retaining. The project has also made two good choices: it does not mandate one AI runtime, and it makes source and decision history explicit.

The present implementation is a reliable **offline prototype of selected record and planning operations**, not yet a working cross-disciplinary agentic framework. The main risk is mistaking catalog metadata and concise skill instructions for delivered professional capability.

The direction needs sharpening more than replacement: **a mandate must resolve into a constrained, executable, testable plan of work using appropriate methods and capabilities, backed by a continuously maintained engagement knowledge record.** The framework is accountable for that composition and continuity. Specialist systems remain replaceable.

## Evidence from the inspected code

- `config/frameworks-v3.json` contains **34** method/framework records, most with `verified_in_runtime: false`. `config/methods.json` has a second, shorter **14**-entry method list. These are overlapping sources, not yet one canonical method registry.
- `skills/` contains **26** original `SKILL.md` files. Twenty-four have **44 lines**, one 45, and one 52. The common structure is introduction, inputs, five procedural steps, outputs, quality checks, handoff and evaluation reference. They are useful skeletons; none has a full demonstrated end-to-end execution.
- The `evals/` directory contains **25** skill-specific JSON fixtures for **26** skill files. The Opportunity Solution Tree skill lacks a matching eval fixture. `src/va/skill_evals.py` prepares baseline and candidate folders with reviewer scorecards; it **does not execute agents**. Results require externally supplied output and ratings. No empirical claims should derive from the fixtures alone.
- `config/external-skills.json` currently has **zero candidates**. `src/va/skillforge.py` registers untrusted, pinned metadata but does not fetch, audit, install or execute external skills.
- `src/va/routing.py` uses explicit **keyword matching** and a maximum of two inferred capability families in normal routing. It is explainable and conservative, but it cannot understand domain semantics or automatically match a method to a verified implementation.
- `AGENTS.md` is global agent guidance, while `.agents/skills/venturemethod/SKILL.md` is an entry skill. **There is no versioned agent-role registry or runtime agent orchestrator.**
- The local model in `src/va/core.py` supports engagement, sources, claims, hypotheses, options, decisions, actions, outcomes and entities. The append-only journal has a SHA-256 chain and projections. It **does not provide independent authenticity, authenticated writers, database transactions, multi-user isolation or automatic source validation**.
- The OST implementation and revision/impact traversal provide useful bounded prototypes. They do not perform real interviews, reliably resolve semantic contradictions, or automatically regenerate affected outputs.
- `python -m unittest discover -s tests -q` returned **48 passing local tests** in the inspected v0.6 archive. These test local code and structural behavior, not factual analysis quality or client results.
- `pyproject.toml` declares version `0.5.0` while README release language refers to v0.6. This is a small but concrete example of configuration drift.
- The private repository has no settled public redistribution license. A private repository does not itself authorize incorporation of third-party skill text.

## Risk-ordered findings

| Priority | Area | Finding | Correction and proof required |
| --- | --- | --- | --- |
| **P0** | Core work model | No runnable composition tying mandate, method, skill, human/agent role, tools, evidence, output and review together | Define a typed work-unit contract and execute one real, bounded engagement end-to-end |
| **P0** | Research and truth | No live source ingestion or independent verification; source records can contain unsupported assertions | Read-only source adapters, provenance with accessed/valid times, evidence quality checks, and a contradiction case |
| **P0** | Quality | Skill fixtures exist but no actual paired model runs or independent expert artifact review | Run equivalent tasks with and without selected skills, blinded assessment, factual audits, cost/time accounting |
| **P0** | Operational completeness | Product and venture methods dominate; marketing, sales, HR, legal, finance, data and daily operations mostly have names rather than usable procedures | Build an audited capability-to-provider matrix; validate one cross-functional engagement instead of bulk importing skill folders |
| **P1** | Agent roles | No definitions of role responsibilities, required context, delegation boundaries, allowed tools, stop conditions or evidence contracts | Version role contracts and a read-only capability/permission registry; run controlled multi-role review |
| **P1** | Methods | Two overlapping catalogs; no formal provenance/version/fidelity map from methods to usable skills and examples | One canonical method registry with aliases, prerequisites, cautions, references, supported tasks and evaluation state |
| **P1** | Living knowledge | Local journal is single-writer and snapshots do not resolve competing edits, outdated derived artifacts or semantic conflict | Proposal/review/adoption records, dependency edges, materialized current views, explicit stale-status and selective recomputation |
| **P1** | Security and permissions | Gitignored data, self-described approvals and prose safeguards are not runtime access controls | Enforce workspace scope, tool allowlists, read/write distinctions, approval tokens, redaction and audit at adapters |
| **P1** | Tool integration | No executed research, CRM, analytics, artifact generation or agent adapters | A tool registry: input/output schema, auth scope, side effects, data classification, reliability and mockable tests |
| **P1** | Execution controls | No durable task state or clear semantics for retry, cancel, partial completion and handoff | Work-unit lifecycle with idempotency, retries, receipts, actual outputs and exception handling |
| **P1** | Human experience | Onboarding is CLI-oriented and documentation-heavy; unclear if one useful task is simpler than working unaided | A one-command real example, low-friction manual path, no excessive questions or compulsory ceremony |
| **P2** | Domain specificity | Global work needs languages, legal entities, institutions, currencies, local partners and permissions | Optional geographic/sector packs and localized source/financial conventions; never assume country interchangeability |
| **P2** | Governance & business model | Publication, licensing, attribution, contributor review and skill supply-chain process not finalized | License decision before open release; SBOM/provenance for vendored materials and versioned compatibility rules |
| **P2** | Packaging | Versions, titles, docs and catalogs can drift | Generate release/version/catalog surfaces from canonical metadata and test for consistency |

**Priority interpretation:** P0 blocks a credible claim that the framework can do professional work with agents. P1 blocks secure, repeatable operation. P2 limits scale and public adoption. A P2 category may move up for a particular mandate.

## The organizing architecture

```text
Person / team / agent / CLI
            |
      MANDATE + CONTEXT
   objective, scope, authority,
   stakes, beneficiaries, constraints
            |
      WORK COMPOSER
   necessary work, alternatives,
   confidence, cost, prerequisites
            |
     +------+--------+--------+---------+
     |               |                  |
  METHOD         CAPABILITY          WORKFLOW
 when/why         what skill         order, review,
 to apply        can execute          dependencies
     |               |                  |
     +---------------+------------------+
                     |
              WORK UNIT CONTRACT
  role | allowed tools | required evidence | outputs
  budget | risk | stop/escalate | verifier | lineage
                     |
          AGENT / HUMAN / TOOL EXECUTION
                     |
            RESULT + VERIFICATION
                     |
        ENGAGEMENT KNOWLEDGE + HISTORY
    sources, claims, hypotheses, decisions, work
                     |
            CHANGE/IMPACT REVIEW
            (feeds into work composer)
```

The knowledge layer serves the entire work cycle. It should not force all tasks through a linear product development process. A short request can use a single work unit and a light evidence standard. High-stakes engagements can coordinate research, expert review and approval.

**Scope boundary:** Venture Method owns selection, composition, context, evidence/decision history, review and outcomes. It should not become its own CRM, accounting platform, video editor, coding environment or general portal. Those are tools or specialist systems used through explicit contracts.

## Definitions that must remain distinct

| Object | Owns | Does not automatically own |
| --- | --- | --- |
| **Theory** | Explanatory claims about how the world works | A machine-executable procedure |
| **Framework** | A representation or structure for inquiry | Evidence that its application was correct |
| **Method** | Steps, preconditions and limits for analysis/action | Tool credentials or authority |
| **Capability** | A kind of work that can be performed, regardless of implementation | Any one vendor or model |
| **Skill** | Bounded reusable instructions/assets/code and expected result | Long-lived client memory, authority to act |
| **Agent role** | Task perspective, goals, allowed tools, required context, decision authority and escalation | An independent organization or unrestricted autonomy |
| **Tool adapter** | Real interface to a data source or action with permissions and effects | A business judgment |
| **Workflow** | Composition, ordering, retries, reviews, dependencies and state | Domain expertise by itself |
| **Knowledge record** | Versioned evidence, interpretation, relationships and outcomes | The assumption that everything recorded is true |
| **Artifact** | A view or deliverable based on a particular knowledge/method snapshot | Current truth forever |

A skill can support more than one method, and a method may be performed manually or by several skills. A reusable agent role should select skills and tools for a task, not embed its own private copy of the methodology. Agent roles should be **few and composable**, not a fixed 24-agent organization deployed for every engagement.

## Agent design: minimum viable contracts

Start with **roles**, not persistent personalities:

| Role | Normal job | Required boundary |
| --- | --- | --- |
| **Engagement lead** | Clarify mandate, decompose work, request approvals, track dependencies | Cannot invent authority or approve its own consequential actions |
| **Researcher** | Source acquisition, interviews/synthesis when evidence exists, competitor and market assessment | Cite each substantive claim; do not claim interviews took place without recordings/notes |
| **Domain specialist** | Apply selected method in product, commercial, finance, operations or venture work | State assumptions, domain limitations and required qualified review |
| **Analyst/modeler** | Quantification, scenarios, financial/technical analysis, reproducibility | Document units, assumptions, formulas, inputs, sensitivity and uncertainty |
| **Execution coordinator** | Produce agreed work, integrate external tools and receive results | Side effects restricted by authorization and adapter permissions |
| **Independent critic** | Test evidence, methods, logic, alternatives and work-product fitness | Access to source snapshots; separate reviewer from author where consequential |
| **Knowledge steward** | Maintain provenance, revisions, impact queue and reconciled views | Cannot silently rewrite accepted history or transfer confidential information |

These are proposed **task profiles**, not implemented agents. One human/agent can perform multiple roles for low-stakes tasks, but a consequential review should avoid an agent certifying its own output.

A role contract needs at least `role_id`, objectives, required inputs, compatible capability IDs, method/skill references, allowed tool classes, allowed read/write scopes, review owner, output contract, budget, time/step limits, stopping conditions, delegation rules, and evaluation fixtures.

### Why this matters

Without those contracts, a model can appear to have a sophisticated team merely by announcing roles. The architecture must specify what each role is permitted to know and do, which artifacts are passed to whom, and what constitutes completion.

## Skill-library coverage without library bloat

There are three layers to inventory:

1. **Professional capability**: e.g. quantitative market sizing, pricing research, customer interviews, revenue forecasting, marketing execution, hiring.
2. **Method variants**: e.g. qualitative JTBD interview versus quantitative Outcome-Driven Innovation; these must not be conflated.
3. **Providers**: original Venture Method skill, pinned external skill library, custom organization pack, tool-native workflow, or a human specialist.

Every catalog item should record: canonical capability ID, tasks, domain, available methods, provider/version/license, inputs, required tools, rights, data scopes, output schema, quality gates, measured benchmark results, known failure modes and install state.

**Sources verified for audit:** Huryn PM Skills, Product on Purpose, Dean Peters (license-restricted), PM Brain, BMAD, Spec Kit, Agent Skills specification, Anthropic's knowledge-work plugins, and upstream author sources for strategy/product/venture methods.

Anthropic's root README advertises eleven primary plugins, while the repository has additional packages, including **operations, human-resources, design, engineering and small-business**, each with its own versioned plugin manifest. Do not assume a frozen count or that every directory is part of the currently advertised marketplace. Its operational coverage, especially sales, marketing, HR, finance and process work, should fill actual gaps in the capability inventory after review, not be pasted wholesale into the core.

## Knowledge, change and Git strategy

Git is appropriate for the **framework source**: method definitions, skills, agent contracts, evaluation cases, templates, code and release notes. Use protected main, reviewed PRs, versioned releases, exact upstream pins, provenance notices and CI. Separate ordinary feature work from methodology changes; methodological changes should carry evaluation evidence.

Engagement knowledge may begin in local files, but the production model requires scoped identities, authorized writers, immutable event records, read models and revision proposals. A hash chain detects unsynchronized edits; it does not authenticate authors or prevent an attacker from rewriting an entire unanchored chain.

Suggested lifecycle:

```text
new evidence -> proposed claim revision -> conflict/impact graph
             -> reviewer accepts/rejects/requests more research
             -> current view advances -> affected work marked stale
             -> selective re-evaluation -> reviewed replacement artifact
```

Store a snapshot manifest with each artifact: source IDs and hashes, claim versions, method and skill versions, model/tool versions where relevant, assumptions, author/reviewer, time, audience and approvals. Artifacts may have dated revisions while their underlying knowledge remains continuously maintained.

Where data is regulated or commercially sensitive, a gitignored folder is not a sufficient access-control strategy. Enforce tenant permissions in the execution path and provide deletion/retention rules for sensitive sources.

## Tools and execution

The first tool architecture should be small and replaceable:

- **Read-only research** with source provenance and as-of timestamps.
- **Data analysis** with verifiable calculations and unit checks.
- **Artifact generation** returning editable files and provenance manifests.
- **One task-system adapter** to test real bidirectional handoffs.

Hermes can be the first agent runtime; a human-only fallback and a second compatible runtime should run the same fixtures. Model vendor independence is achieved through capabilities, contracts and tests, not by saying “agnostic” in a README.

A tool record must declare `read/write` side effects, authentication scope, allowed data class, rate/cost limits, schema and reversibility. A tool response is an untrusted observation until assessed, not an instruction to the agent.

## Required evaluations

Four separate questions should be tested, since success in one does not imply success in the others:

1. **Routing:** Did the system choose an appropriate method, skill, role and tool for the mandate? Did it avoid irrelevant methods?
2. **Execution:** Could it actually gather required inputs and produce the contracted output with correct permissions, recovery and traceability?
3. **Substance:** Is the work factually supported, numerically correct, commercially plausible, useful to the audience and better than an appropriate baseline?
4. **Iteration:** Can new conflicting evidence update the knowledge view and affected deliverables without changing unrelated history or leaking across engagements?

Use high-quality expert reviewers and paired comparisons, with realistic incomplete-data scenarios. Include negative cases where the right answer is “we do not yet know,” “ask a specialist,” “do nothing,” or “do not pursue.”

Test against at least three distinct real or permissioned mandates: fractional CPO, venture origination/diligence, and an ongoing client/commercial engagement. Add a simple task to measure unnecessary overhead.

## Prioritized next release

**Workstream A: Make the pieces compose (P0).** One canonical capability/method/provider registry and one typed work-unit/agent-role contract. Map all existing 26 skills and 34 method records to it. Reject dangling IDs. Add explicit distinctions among specified, installed, executed and independently evaluated.

**Workstream B: Prove one real research-to-deliverable path (P0).** Choose a bounded market/product/company assessment; connect actual sources, produce a strong editable output with citations and alternatives, and evaluate with/without selected skills. Include human approval and an evidence update.

**Workstream C: Operational breadth by tested packs (P0/P1).** Audit Anthropic's and other providers' sales, marketing, data, finance and operations workflows; implement the most relevant combination in one cross-functional client case. Add more domains only when a real engagement exercises them.

**Workstream D: Hardening (P1).** Agent/runtime permissions, versioned source snapshots, revision conflicts, traceable downstream change handling, real tool adapters, failure recovery, portability and security tests.

**Explicitly deferred:** browser portal, hosted multi-tenancy, full CRM/ERP, automated fund execution, autonomous legal sign-off, broad plugin marketplace launch. These may become separate interfaces or products later.

## Recommendation

Keep the overall architecture, repair its **missing composition layer**, and prove serious work before adding an impressive number of agents or skill files.

Publication quality should be demonstrated through credible case studies and independently scored outputs. The distinctive asset is a transferable professional method for doing complex work over time, with agent-assisted execution and preserved institutional learning, rather than a large library of instructions.
