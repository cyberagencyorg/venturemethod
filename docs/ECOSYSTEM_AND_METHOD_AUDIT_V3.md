# Cross-library methods audit: v0.3 (2026-10-19)

## Verdict and scope

The earlier approach conflated four different things: a **theory of how something works**, a **method for investigating or deciding**, an **executable agent skill**, and an **operating workflow/organizational practice**. A product operating model is not the same kind of object as a customer interview skill; a Wardley map is not a replacement for an opportunity-solution tree; and an artifact template is not evidence of proficiency.

The former 25 skills were original first-draft procedural documents. They are **not 25 tested expert capabilities**. The new 34-method catalog is **metadata and selection guidance**, not 34 implementations. The source catalog is **not an item-by-item audit of 214 advertised upstream entries**. It captures catalog-level evidence, explicitly marks incomplete individual skill review, and cannot support a comprehensive-coverage claim.

## Ecosystem, roles, limitations

| Source | Why retained | Important limitation |
| --- | --- | --- |
| [Huryn / pm-skills](https://github.com/phuryn/pm-skills) | Product methods, discovery, research, strategy, analytics, execution, growth, AI shipping; 69 skills/42 advertised workflows | Skill-name counts do not equal unique methods; verify individual execution, dependencies, upstream version and license |
| [Product on Purpose](https://github.com/product-on-purpose/pm-skills) | 68 advertised skills, framework-neutral activity taxonomy, quality contracts, workflows, iteration and 200+ samples | Already has capabilities that v0.2 incorrectly treated as future inventions; source count and taxonomy pages can drift |
| [Dean Peters](https://github.com/deanpeters/Product-Manager-Skills) | 77 advertised skills, deeper explanation, market intelligence, lifecycle and end-of-life | CC BY-NC-SA, do not blindly copy into redistributed/commercial framework; explicit permission may be needed |
| [Huryn / PM Brain](https://github.com/phuryn/pm-brain) | Ingest, provenance tagging, propagation into durable knowledge, weekly reviews, source immutability | README test claims are upstream claims; not independent proof, and not multi-user change governance |
| [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) | Right-sized agent workflows, explicit decisions and role handoff; v6.12 stable, v7 alpha at inspection | Primarily oriented around software creation, not a general venture epistemology |
| [Spec Kit](https://github.com/github/spec-kit) | Specs, decomposition, tasks, consistency checks and technical delivery gates | Helps post-decision implementation; does not validate initial strategic truth |
| [Anthropic Skill Creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | Test tasks, baseline-without-skill comparisons, skill revision process | Evaluation tooling still needs blinded reviewers and external reproducibility; per-skill license terms differ |
| [Agent Skills specification](https://agentskills.io/specification) | Interoperability, progressive loading, resource packaging | Standardized file format is not evidence of method competence |
| [skills.sh](https://skills.sh/) | Source discovery | Popularity and discoverability do not establish safety, originality or useful outcomes |

Claims about advertised counts come from project READMEs and marketplace metadata checked 2026-10-19. Counts should be pinned per release, diffed in a scheduled upstream review, and never added together as distinct coverage.

## A better capability ontology

- **Domain:** market analysis, venture capital, product, operations, talent, governance, creative, public policy, etc.
- **Outcome / decision class:** the actual decision being improved, not the job title of the requestor.
- **Theory or lens:** explanatory account, possibly contested, e.g. Jobs to Be Done.
- **Framework:** representation of factors and relationships, e.g. Business Model Canvas.
- **Method:** repeatable investigation or decision procedure, e.g. switching interview, market sizing.
- **Skill:** executable, tested instructions and tools producing an observable result under prerequisites.
- **Workflow:** directed composition of skills/methods with checkpoints, branches and repeat cycles.
- **Playbook:** reusable, context-sensitive workflow for a recurring mandate.
- **Artifact/view:** a materialized representation of governed knowledge at a specific time and purpose.
- **Adapter:** external read/write integration with permissions and provenance.

This prevents a false 1:1 mapping of methods to skill files. One skill may implement several methods; one method may require several skills. A workflow can use variants of the same method, and methods may have fundamentally different evidence requirements.

## Counterexamples to universal recipes

1. **Continuous discovery vs SVPG product model:** Torres provides repeated customer learning practices; Cagan addresses empowerment, team responsibilities, organizational capabilities and accountable outcomes. These reinforce one another when a product team exists; neither should be forced onto a fixed-scope creative deliverable.
2. **JTBD variants:** qualitative progress/switching narratives and ODI quantitative job-outcome measurement cannot be interchanged without changing the type and quantity of input evidence.
3. **Strategyzer vs Wardley:** business/value models describe how an offer creates/delivers/captures value; Wardley adds user-anchored value chains and evolution. Different diagnostic questions; sometimes complementary.
4. **Wardley vs systems dynamics:** one organizes value chains and evolutionary conditions; the other explores feedback, delays and causal structure. Neither proves causality by drawing arrows.
5. **Scenarios vs real options:** scenarios expose plausible alternative futures, not forecasts. Real options are about staged commitments and retaining flexibility. A probabilistic valuation is a special, higher-evidence case.
6. **Discovery vs build specifications:** speculation in an approved PRD does not become true because code passed tests. Technical correctness, business desirability and economic viability must be evaluated separately.
7. **Market sizing vs obtainable revenue:** TAM can be huge while realistic market access is negligible. Market sizing should not be a prerequisite for every narrow organizational intervention.

## Selection policy and missing tests

A serious selector should (a) state the decision class; (b) estimate its evidence maturity; (c) identify risks, costs, constraints and time horizon; (d) return candidate methods with tradeoffs and minimal prerequisites; (e) explain *why not* alternatives; (f) support expert override with rationale; (g) decide what to investigate first; and (h) remember outcomes so selection can be evaluated later.

v0.3 **only implements (a), some of (b), (d), and part of (e)** through an explicit goal selector. It does not infer goals robustly, optimize method portfolios, run agents, establish epistemic quality or learn from outcomes. `python va.py frameworks --goal map_market --evidence observed` lists candidate methods without selecting a winner.

The next step is a versioned mapping at **individual upstream skill and workflow level**, with explicit labels: `incorporated`, `adapted_with_rights`, `covered_by_other_skill`, `connected`, `out_of_scope`, `unexamined`. Each entry needs upstream SHA, license, selection conditions, inputs, outputs, quality rubric, variants, own baseline evaluation and actual runtime test result. No domain can be called covered because of generic prose alone.

## Sources checked

- Huryn PM Skills: https://github.com/phuryn/pm-skills
- Product on Purpose taxonomy: https://github.com/product-on-purpose/pm-skills/blob/main/site/src/content/docs/reference/categories.md
- Dean Peters: https://github.com/deanpeters/Product-Manager-Skills
- Huryn PM Brain: https://github.com/phuryn/pm-brain
- Torres: https://www.producttalk.org/getting-started-with-discovery/
- SVPG: https://www.svpg.com/product-model-concepts/
- Strategyzer: https://www.strategyzer.com/library/the-business-model-canvas
- Wardley Mapping: https://learnwardleymapping.com/introduction/
- Meadows: https://donellameadows.org/archives/leverage-points-places-to-intervene-in-a-system/
- Shell scenarios: https://www.shell.com/news-and-insights/scenarios/what-are-shell-scenarios.html
