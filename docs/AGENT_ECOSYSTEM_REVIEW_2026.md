# Agent ecosystem and architecture: adversarial review

**Project:** Khan's Venture Method Framework  
**Date:** 2026-10-19  
**Repository baseline:** `cyberagencyorg/venturemethod` main at `053bed3ec3d3884ea25530dd73a4397436a8e0e5`  
**Method:** Direct inspection of repository tree, manifests, representative skills, CI workflow, adoption/routing/composition/ledger/operator/research source, and current primary documentation for agent runtimes and open protocols. This is a design audit, not a runtime interoperability or professional quality benchmark.

## Verdict

Keep the core intent and much of the existing source. **Do not select LangGraph, CrewAI, Google ADK, Hermes, PydanticAI, or any other single runtime as Venture Method's parent architecture.** The repository should become a *professional capability substrate* that external humans and agents can adopt at any stage and at any level of integration.

The current project is stronger at **self-contained, offline, single-user engagement bookkeeping** than **external discovery and composition**. That is an inversion of its intended value proposition.

Make three independently consumable layers:

1. **Reference and skill distribution.** Relevant methods, templates, agent skills, role definitions, and review standards usable from files alone, no Python or engagement required.
2. **Interoperability and optional execution.** Canonical JSON Schemas, read-only first MCP interface, runtime adapters, portable work contracts, receipts and reviews. The host owns its model loop and execution environment.
3. **Optional knowledge and governance.** Evidence records, evolving claims, temporal relationships, decisions, approvals and dependency impact; usable through the same interfaces and not mandatory for a one-off task.

A host can select one method from layer 1 without adopting layers 2–3.

## Verified inventory

- 144 files in the inspected Git tree: 33 `.py`, 39 `.json`, 27 `SKILL.md` including the project adapter, 42 other `.md`, plus CI, ignore and `pyproject.toml`.
- `venturemethod.json` correctly calls itself a *project-specific adoption map*, not a standard.
- `AGENTS.md`, `ADOPT.md`, `.agents/skills/venturemethod/SKILL.md` offer narrative discovery, but host-native discovery/install/compatibility is untested beyond CLI and GitHub CI.
- `src/va/adoption.py` uses lexical routing, at most two matched domains, and hard-coded representative methods; it never inspects an actual host project, distinguishes existing coverage, or benchmarks applicability.
- 34 method entries (`config/frameworks-v3.json`); an overlapping 14-item method list (`config/methods.json`); 26 concise first-party skill files (`config/skills-registry.json`).
- `config/agent-roles.json`: seven role descriptions with `max_delegation_depth: 0`; these are not instantiated agents or enforced authorization.
- `config/tool-contracts.json`: eight descriptive tool contracts; there is no MCP tool/resource server, remote API, A2A endpoint, or installed host runtime adapter.
- `config/external-skills.json`: empty candidate catalog. No external skill provider is demonstrably installed and selected at task time.
- `src/va/ledger.py` has a local event hash-chain. This provides tamper evidence within the local workflow, not authenticated actors, secure multi-writer transactions, temporal entity resolution or federated knowledge exchange.
- `pyproject.toml` has metadata and a Python package declaration; no console-script entrypoint, dependency lock, TypeScript client or published protocol SDK. GitHub CI tests only Python 3.11, structural skill checks, basic method commands and one adoption example.
- The most recent main-branch GitHub Actions runs are successful. Successful deterministic unit tests must not be represented as evaluation of agentic competence or cross-runtime support.

## The most damaging gaps

| Priority | Missing capability | Consequence | Proof of repair |
|---|---|---|---|
| **P0** | Standard consumption interface | External agents need manual file-reading conventions, CLI knowledge, or repository-specific glue | MCP stdio read-only server, true Agent Skills validation, and two verified consumer harnesses |
| **P0** | Canonical typed contract | Method, skill, provider, role, tools, task and evaluation metadata are disjoint; a JSON file alone does not provide semantics or compatibility | JSON Schema and runtime validators for shared contract IDs, versions and relations; fixtures in Python and TypeScript |
| **P0** | In-flight host project assessment | `adopt` maps keywords, not actual project state or previous work; easy to prescribe redundant work | A bounded, explicitly authorized, read-only host assessment with evidence for gaps and “no intervention” outcome |
| **P0** | Substantive skill quality | Most first-party skills are short procedural sketches; no verified current specialist execution | Real representative tasks, baseline vs skill, blinded expert grading and non-trigger tests |
| **P0** | Agent and tool integration | Proposed roles and tools aren't invocable providers and permissions are descriptive | One tested adapter to an existing agent runtime, with scoped read-only methods, receipts and failed-action tests |
| **P0** | Context trust and authorization | Untrusted sources and external skills could be confused with instructions; proposed approvals cannot enforce privileges | Provenance and taint labels, host-scope allowlists, runtime permission enforcement, explicit side-effect approvals |
| **P1** | Context engineering and retrieval | Full manuals and static catalogs are poor context windows; instructions are not selected semantically | Search, ranking, progressive loading, token budget, freshness and contradiction flags, refusal to overselect |
| **P1** | Persistent knowledge interoperability | Gitignored local case JSON isn't portable across sessions/hosts, shareable by authorized teams, or genuinely current | Export/import, stable namespaced IDs, temporal updates, source-backed relationships and selective projection rebuild |
| **P1** | Durable execution | No pause/resume, idempotent multi-step execution, retries or tool-call receipts through an agent runtime | Use host runtime's native checkpoints; test interruption and recovery; do not build a competing scheduler |
| **P1** | Observability and cross-runtime evaluation | Local unit tests and manual eval packet generation cannot diagnose real agent failures | Portable trace and eval records, OTel-compatible telemetry where running code, automated comparisons and human review |
| **P1** | Packaging and compatibility | Python CLI works only for someone who checks out and runs the repo; dependency boundaries remain implicit | Portable distribution and install docs, versioned compatibility matrix, releases and schema conformance tests |
| **P2** | Hosted agent collaboration/UI | A2A, AG-UI, ACP and hosted APIs are absent | Implement only where a real remote agent service, UI or editor integration needs them; avoid premature protocol sprawl |

**P0 here means a blocker to the specific goal of arbitrary compatible agent/project adoption, not a claim that the current local CLI is broken.**

## What to learn from leading frameworks (without replacing this framework with theirs)

| Ecosystem | Relevant design pattern | Venture Method's response |
|---|---|---|
| **LangGraph / LangChain Deep Agents** | Persistent checkpoints and stores, context-isolated subagents, interruptions, tools and selective skill loading | Let hosts with LangGraph run the work; expose Venture Method through skills and tools, store independent source evidence |
| **PydanticAI** | Typed models, composable capabilities/toolsets, model-independent execution, test and eval integration | Adopt typed capability contracts and composable provider selection, not its entire runtime |
| **OpenAI Agents SDK** | Distinguish manager-as-tool vs handoff, structured outputs, guardrails, trace metadata, session continuity | Define delegation/return semantics in work contracts; adapters decide native handoff mechanics |
| **Google ADK / Microsoft Agent Framework** | Agents and deterministic workflows as separate abstractions, explicit tools, state and review | Allow agent loops for open-ended work, deterministic workflows for prescribed operations; remain vendor independent |
| **CrewAI / Mastra** | Role/task/crew composition or TypeScript-native application workflows | Use as optional provider adapters when suited to a host; don't invent a Venture Method “crew” DSL first |
| **Temporal** | Durable execution, retries, approval waits, replay discipline, activity side-effect separation | Optional for long-running workflows. Not necessary to read a method or produce a one-off artifact |
| **Inspect AI / Anthropic Skill Creator** | Evaluations for real agents, reusable datasets/scorers, blind with/without-skill outputs and skill-trigger tests | Adopt eval formats/bridges, benchmark cases, reviewer rubrics and recorded improvements before marketing competence |
| **Graphiti / temporal KG** | Source provenance, valid time and ingestion time, incremental fact changes and relational retrieval | Study model for optional knowledge layer; build minimal temporal/provenance semantics first, not a mandatory graph database |
| **Anthropic knowledge-work plugins** | Domain skills, role-specific workflows and tool categories rather than assuming one app | Catalog as versioned, license-reviewed specialist providers; add domains by measured task need |

Authoritative sources: https://docs.langchain.com/oss/javascript/langgraph/thinking-in-langgraph ; https://pydantic.dev/docs/ai/overview/ ; https://developers.openai.com/api/docs/guides/agents/sdk ; https://learn.microsoft.com/en-us/agent-framework ; https://docs.temporal.io/ai ; https://inspect.aisi.org.uk/agents.html ; https://github.com/anthropics/skills/tree/main/skills/skill-creator ; https://github.com/getzep/graphiti ; https://github.com/anthropics/knowledge-work-plugins .

## Interoperability: where each protocol fits

- **Agent Skills** (`SKILL.md`): best first default for portable *procedures*, with metadata discoverable before instructions, progressive optional references/assets, and no runtime requirement. Source: https://agentskills.io/specification
- **MCP**: exposes *discoverable resources, prompts and tools* to an existing agent runtime. Build local stdio server first with read-only tools. Recent specification: `2026-07-28` (https://modelcontextprotocol.io/specification/2026-07-28). Server must authenticate and authorize if remotely exposed.
- **A2A**: remote independent *agent-to-agent* tasks and delegation, using agent cards. Do not implement until Venture Method actually exposes an executing, separately reachable agent service (https://a2a-protocol.org/latest/specification/).
- **AG-UI**: live agent-to-user app interaction and event streaming. Optional future UI adapter, not a core requirement (https://docs.ag-ui.com/introduction).
- **ACP**: coding agent / editor interface. Consider only for IDE-hosted use; it does not replace skill discovery or MCP (https://agentclientprotocol.com/get-started/introduction).
- **OpenAPI, JSON Schema and simple CLI**: stable contracts for non-agent consumers; these coexist with the above. `venturemethod.json` is useful as an internal index, but cannot honestly claim that every external LLM will auto-discover it.

Interoperability is behavioral, not merely syntactic. A published schema or MCP server can still provide poor method selection, stale knowledge, dangerous context exposure or unusable results.

## Recommended data contracts

Provide published, versioned schemas, validated in two languages and independent from the Python implementation, for:

1. **Method:** identity, domain, question type, evidence threshold, applicability, anti-patterns, authoritative source, outputs, known limitations, version.
2. **Capability/provider:** capability and task IDs, provider type, compatible skills/tools/runtime, license, supply-chain pin, implemented/benchmarked state, scope and permissions.
3. **Work contract:** host project reference, objective, phase, existing artifacts/decisions, authorized inputs, selected methods, roles, tools, output contract, cost/time/side-effect budget, no-op option, review and stopping rules.
4. **Evidence/claim:** source identity, content hash, collected time, valid/effective time, quotation location, statement/interpretation, support/conflict links, sensitivity, confidence rationale.
5. **Execution receipt:** run ID, work contract hash, provider/runtime/model where known, tools invoked, state transitions, inputs/outputs by immutable reference, failure, review and costs.
6. **Evaluation:** scenario version, comparator, with-skill and baseline outputs, reviewer identity/policy, rubric, factual issues, outcome and aggregate limits.

**Require stable namespace/version boundaries.** A framework method is not the same object as an agent skill; a skill can implement part of several methods. Emit machine-readable integrity and capability status, avoiding “implemented” unless corresponding behavior is verified.

## Portability architecture

```text
existing person / agent / project (host owns objective, tools and authority)
                          |
                  DISCOVER / CONSULT
            README | SKILL.md | ADOPT.md
                          |
         OPTIONAL CAPABILITY/CONTEXT RESOLVER
        search -> check applicability -> propose
         -> select or do nothing -> context pack
                          |
           VERSIONED DECLARATIVE CONTRACTS
   Method + Skill + Provider + Work + Evidence + Eval
             /                       \
  Host agent runtime                Human/manual
  (Hermes/Claude/Codex/             no agent required
   LangGraph/PydanticAI...)
             |
     Optional MCP read-only server
             |
  Optional authorized side-effect adapters + execution receipts
             |
    Optional engagement knowledge / revision / impact store
```

Nothing above should require all participants to move their project into Venture Method, use Python, install a portal or transfer proprietary data.

## Security boundaries

Host project material, external web content, downloaded skill instructions, marketplace records and external agent responses are **untrusted relative to the host's instructions**. A “read-only” manifest is advisory unless the exposed tool implementations actually lack write effects.

- Limit file access to explicit project or engagement roots; resolve symlinks and reject escapes. Do not crawl other repositories, desktops or connected accounts by default.
- Separate reading a source from trusting a claim; quoted text can contain prompt injection and must never become executable instructions.
- Record which model/tool is receiving any client excerpts. A compact handoff can still disclose sensitive text.
- Put validation and approval at the tool/side-effect boundary, not just in an agent prompt.
- Use least-privilege tools, idempotency keys and dry runs. Remote MCP requires session-appropriate authentication/authorization, quotas and isolation.
- Pin and validate third-party skills and package provenance, review executables and licenses, test prompt injection and malicious skill content.
- Avoid publishing raw traces, prompts, secrets or client names. Make telemetry payload-redacted by default and retention configurable.
- A local SHA-256 history establishes detectable changes only under defined trust assumptions; hashes alone don't establish authorship or source veracity.

## Research and memory architecture

Avoid prematurely requiring a knowledge graph. Establish four distinct kinds of context:

- **Working context:** current job, immediate inputs, relevant prior decisions and token budget.
- **Procedural knowledge:** selected methods, skills, policies and examples, with pinned versions.
- **Evidence / semantic knowledge:** source-backed entities, observations, facts, interpretations, hypotheses, relationships and uncertainty.
- **Episodic / operational history:** events, approvals, past executions, outcomes, and subsequent changes.

Use a **context compiler** that builds a small, purpose-specific packet with source/claim version IDs, confidence, expiry and conflict flags. It must include relevant current work and avoid summarizing away disagreements or implicit approval boundaries.

For continuing use, add stable entity references, temporal validity, change proposals, and explicit dependency links. SQLite plus full-text and optional vector retrieval can be sufficient initially; Postgres/pgvector or graph projections can be introduced with demonstrated scale or query needs. Never use embeddings as the authoritative store of truth.

## Architectural implementation order

### Phase 1 — Make reference adoption real (P0)

- Create `schemas/v1/` for method, capability, provider, work unit and evaluation.
- Normalize duplicate catalogs to one canonical source (including original-source attribution). Compile derived indexes.
- Improve Agent Skills metadata and references; test spec validation and actual discovery in **Hermes + one distinct host**.
- Create a deterministic no-modification `vm inspect` or equivalent resolver that accepts explicit *host-state context*, suggests at most a few relevant interventions with evidence, and can return “none”.
- Add a minimal read-only MCP stdio server exposing `catalog.search`, `method.get`, `skill.get`, `project.assess` (only on supplied/authorized context) and `context.pack`. Tests must prove absence of write surfaces.

### Phase 2 — Evaluate usefulness, not folder count (P0)

- Pick (a) a new venture, (b) an in-flight fractional CPO/product engagement and (c) a cross-functional sales/marketing/operations assignment.
- For each compare an unassisted baseline against selectively using Venture Method; include a fourth **no-intervention** task.
- Score routing precision, false-positive method choices, fact grounding, method fidelity, deliverable utility, latency, human attention/cost, regressions and safety.
- Use actual multiple agent runtimes, Inspect AI / skill-creator style fixtures, independent expert review and transcript/receipt logging.

### Phase 3 — Operational depth and knowledge portability (P1)

- Bring in narrowly selected, reviewed external product, sales, marketing, finance and operations skill providers.
- Introduce source-backed context assembly with permissioned access to existing work, temporal claim changes and affected-output notices.
- Implement import/export contracts with stable IDs; add appropriate knowledge indexes/projections and redaction.
- Make one approved external handoff round trip through a real runtime and return a verifiable receipt.

### Phase 4 — Optional production infrastructure only when demanded (P1/P2)

- Pick a durable engine for genuinely long-running jobs: use runtime-native checkpoints or Temporal, not a homegrown scheduler.
- Add a hosted MCP/A2A agent service only when a real remotely delegated capability exists.
- Add AG-UI or editor/ACP adapters only for a concrete interface that needs them.
- Multi-tenancy, audit signatures, database transactions, role-based access and incident handling are prerequisites for sensitive shared/hosted use.

## Explicit no-go decisions

- Do not rewrite the repository in TypeScript solely because TypeScript agent SDKs are popular.
- Do not package a second LangGraph/Temporal/CrewAI within this framework.
- Do not make permanent twenty-agent teams the default.
- Do not force host projects into a Venture Method engagement folder.
- Do not vendor an entire third-party skill library before task-level evidence and licensing review.
- Do not require an MCP/A2A service for the simplest use case, reading a `SKILL.md`.
- Do not call an empty method/provider mapping “AI-native competence.”
- Do not treat passing structural tests, agent self-reviews, GitHub stars, or impressive demos as independent benchmarks.

## Immediate acceptance test

A coding agent with access to a separate, already-active product repo receives one sentence: “Consider Khan's Venture Method Framework if it would help; preserve current work.” Without installing Python or starting a new engagement, it must:

1. Inspect relevant host context only when authorized.
2. Discover the Venture Method entry point from the provided path/repo link.
3. Identify exactly which single method/skill is useful, or correctly decline intervention.
4. Cite the selected method's source and explain how it fits the existing project state.
5. Make a bounded, reversible contribution or return a concrete recommendation without changing unrelated project files.
6. Preserve host authority, scope and any confidential data.
7. Produce an inspectable decision/quality record only if the host asks for it.

Repeat against a second, non-coding harness with different tool availability. Once this works and is independently evaluated, the framework will have met its core portability claim in a meaningful way.
