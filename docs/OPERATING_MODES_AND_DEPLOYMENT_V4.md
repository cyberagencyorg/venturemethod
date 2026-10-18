# Venture Architecture v0.4: operating modes and deployment blueprint

Status: **design target**, except where explicitly noted. The current repository is an offline, single-writer CLI. It is not a hosted portal, authenticated multi-tenant API, autonomous global research network or complete executive operating system.

## Design requirement

One portable methodology and evidence model can serve different users without assuming they share a model provider, orchestrator, cloud vendor, Git host, industry, jurisdiction or professional role. In a run, choose the smallest suitable process. An independent agent should not need to ingest the entire corpus of skills.

## Personas and scopes

| Mode | Primary decision loop | Durable outputs | Different constraints |
| --- | --- | --- | --- |
| Solo venture architect | Intake -> understand -> alternatives -> validate -> act -> reflect | Working thesis, options, experiments, commercialization, proposals | Low overhead, fast switching, high work quality |
| Fractional CPO / CTO / strategist | Organization diagnosis -> product goals -> customer evidence -> mandate -> delivery -> outcomes | Company/product intelligence, OSTs by outcome, decision rights, product operating model, roadmap, executive brief | Client confidentiality, multiple teams, authority boundaries, continuity across engagements |
| Venture studio network | Geography/sector landscape -> source opportunities -> qualification -> diligence -> incubation -> capital -> portfolio value creation -> exit | Opportunity pipeline, relationship graph, diligence rooms, portfolio KPIs, transaction and capital provenance | Entity and jurisdiction resolution, local language, trusted partners, deal-specific conflicts, investment approval, portfolio concentration |
| Client contributor / external team | Assigned workspace -> use permitted methods -> submit proposed work -> review | Scoped evidence, changes, specialist outputs | Minimum privileges, collaboration, no cross-tenant knowledge access |
| General public / community user | Create private workspace -> install skill packs -> work locally or on own infrastructure | Portable skills, method guides, open templates | Minimal setup, offline mode, interoperable APIs, configurable trust and localization |

Network-level opportunity sourcing is **not** Torres's product Opportunity Solution Tree. A deal pipeline can contain company, founder, market, investor, institution, financing opportunity, jurisdiction and legal entity records. A product team within a venture may then maintain one OST for a specific customer outcome.

## Separation of concerns (must be enforceable)

1. **Domain core**: versioned entities, evidence, claims, theories/hypotheses, alternatives, decisions, action/outcome history, identities, permissions, methodology records and artifact dependencies. Portability-first schemas and pure functions. Today only a subset is implemented as local JSON/JSONL.
2. **Knowledge services**: source connectors, ingestion, provenance, deduplication, entity resolution, search, semantic/graph projections, change suggestions, freshness, conflict review. Not implemented.
3. **Method / skill registry**: skill packages following the Agent Skills format; version and source pins; executable validations; framework selection rules; objective/eval metadata; licensing and supply-chain checks. Only passive registry, basic validator and evaluation scaffolding exist.
4. **Work and orchestration API**: runs, tasks, resource budgets, permissions, reviewers, human approval checkpoints, artifacts and events. Not implemented as an API.
5. **Agent adapters**: Hermes, Codex, Claude, local models, remote LLM endpoints, human-led CLI workflows. Adapter runs an approved task contract and cannot bypass core authorization. Hermes is first adapter to test, not required for domain persistence.
6. **Artifact adapters**: Markdown/JSON canonical first; optional DOCX/PDF, slides, spreadsheets, Figma, Linear, GitHub, messaging. Every published artifact names its source snapshot, decision and method/skill release IDs. Not implemented beyond local Markdown drafts.
7. **Experience layer**: CLI, TUI, REST/OpenAPI, MCP server, browser portal, embeddable widgets. New UIs must not become authoritative storage.

```
                    bradkhan.com | cyberagency.org | humanscaled.com
                                     portal / mobile web
                                              |
                             BFF / session authorization / tenancy
                                              |
                             Work API / method selector / approvals
                          +-------------------+-------------------+
                          |                   |                   |
                    Knowledge API      Job scheduler        Artifact API
                    (versioned)          + queues             + storage
                          |                   |                   |
              Postgres + row-level      Hermes adapter       Docs/Slides/etc
              policies + object         Codex adapter
              storage, search           Model API adapter
                          |
                  Tenant-scoped history and audited events
```

Arrows represent planned boundaries, not running software.

## What should be in Git versus the engagement datastore

**Git**: public/open source skills, method definitions, workflows, schemas, CLI code, runbooks, fixtures, evaluation specifications, benchmark results that are safe to publish, partner integrations. Use protected branches, changesets, semver, release pins, test gates, CODEOWNERS, signed provenance for distribution where practical.

**Private knowledge datastore**: confidential source material, client claims, investment decisions, engagement changes, private hypotheses, documents, contracts, customer interviews and permissions. Use transactional event persistence, stable globally unique IDs, tenant-scoped access control and immutable audit records in production; Git-based private workspaces can be supported as an export/import option but are not the source of authorization truth.

**Derived artifacts and projections**: search/vector/graph indexes and rendered presentations are reproducible from authorized snapshots where feasible; artifact versions and approvals must remain observable independently from the generated bytes.

Change control proposal: `source_ingested -> extraction_proposed -> evidence_review -> affected_nodes -> alternative_change_set -> reviewer_accept / reject / edit -> re-evaluate decisions -> selectively refresh artifacts -> publish if approved`.

Any autonomous refresh should be a *proposal*, not a change to an investment recommendation, contracted deliverable or external communication.

## Hermes first, portable by design

Hermes documents Agent Skills compatible project skill directories at `.agents/skills/` and `.hermes/skills/`; the repository now includes `.agents/skills/venture-architecture/SKILL.md`. Project skills require explicit trust in Hermes. Use `hermes skills trust` only on reviewed repos. Launch Hermes within the repo, then invoke the skill or run the CLI. See official upstream docs: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/skills.md

For cross-tool sharing, an `~/.agents/skills/` installation can be configured as Hermes `skills.external_dirs`. Critical caveat: the Hermes documentation indicates agent skill-management operations can change shared external files if the process has write permission. Mount reviewed shared skill packs read-only and never let autonomous skills overwrite published method packages.

Hermes also documents a session API and `/v1/skills`, `/v1/toolsets` endpoints, subject to `API_SERVER_KEY` and version-specific support: https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/api-server.md. Do not expose it directly to a public domain or rely on its API key as client-level multi-tenant authorization. Have a server-side adapter use the API and pass per-run least-privilege context.

Provider-neutral task contract (target, not yet implemented):

```
RunRequest: tenant_id, workspace_id, goal, scope, input_refs,
  source_snapshot, requested_methods, skill_release_pins,
  authorization, budget, confidentiality, deadline, output_contract
RunResult: run_id, agent_adapter, model/provider refs, tool events,
  evidence refs, drafted changes, produced artifacts, costs,
  review_state, errors, provenance
```

All generated content is untrusted until checked. The model, prompt, and skill versions need capture when a run matters to reproducibility.

## Portal domains and brand boundaries

Suggested domain layering (not provisioned):

- `studio.humanscaled.com`: holding-company studio work, portfolio landscape, thesis and capital allocation dashboard.
- `workbench.cyberagency.org`: client-facing engagements, strategy, research, delivery and scoped collaboration.
- `workspace.bradkhan.com`: personal operator view across authorized roles and tasks.

Prefer one platform with **separate tenants and role-scoped views** rather than three independent databases. Custom domains should be presentation and entry boundaries, not an implied grant of cross-tenant access. Legal entity and contracting relationships need explicit representations. A shared identity may access multiple workspaces only through audited role grants.

The initial private portal can be a single-user app behind authenticated access; an external client portal requires application-level authorization, invitation flows, tenant isolation, session and token management, billing/usage policy and security testing. A reverse proxy or Cloudflare Access alone is not a complete multi-tenant permissions system.

## Sequenced deployment

**D0, available now:** Python CLI, Markdown/JSON and isolated local engagements. Hermes project skill adapter. No services, shared secrets or cloud required.

**D1, next build:** Local FastAPI/OpenAPI service wrapper over an authenticated, transactional database with private workspace authorization, plus test harness. Keep CLI as a client of common domain actions, not a second implementation. SQLite can suit local single-user mode; Postgres should support hosted multi-user mode.

**D2:** Job queue for bounded research and run requests, Hermes worker, independent reviewer UI, snapshots, artifact preview and diff, secure per-run credentials. Add background research freshness and country/market watcher schedules with evidence changes as suggestions.

**D3:** Client/partner invitations, portal role views, institutional/partner networks, bilingual research, multiple agent adapters, consent/permission retention, network-level opportunity pipeline and portfolio analytics. Do security/load/compliance work before broader public rollout.

**D4:** Published public templates and skill marketplace, self-host deployment option, evaluation leaderboard, reproducible method/skill bundles, and multi-brand portal configuration. Have a migration path and support policy.

## Failure modes and mitigations

- Model dependency: core is model-free, adapters removable; no secret model memory as sole source of truth.
- Privilege escalation: no direct tool credentials in browser; least-privilege service tokens, tenant guards at storage and API layer.
- Supply-chain / skill prompt injection: pin and review skills, restrict executable dependencies, isolate adapters and prohibit auto-updating trusted code.
- Residency and jurisdiction: classification by tenant/record, configurable storage regions, cross-border transfer review, deletion/export controls, jurisdiction-aware retention.
- Network opportunity selection bias: track geography/language/source coverage, false negatives, partner conflicts, political/legal constraints and local context interpretation.
- Platform overengineering: make every phase earn its existence by delivering a validated user task end to end.
