# Venture Method

**The right methods. Better decisions. Knowledge that keeps up.**

**Venture Method is Brad Khan's adaptive, AI-native, agent-compatible framework for investigating opportunities, developing ventures, shaping products, and making evidence-grounded decisions across markets, capital, and organizations.**

For venture builders, founders, CEOs, CPOs, investors, family offices, researchers, and operators who routinely cross disciplines and need their work to stay connected as things change. Start with a company, idea, market, product, or mandate. Select methods that actually fit the question. Work from evidence to options, decisions, execution, and revision.

**It is not another collection of prompts or a rigid, one-size-fits-all product process.** Established methods remain distinct. Specialized skills can be evaluated and improved. Knowledge and decisions have a history. You can work locally, manually, or with your preferred compatible agent.

> **Current release: private experimental framework, v0.6.** The offline CLI, method catalog, typed engagement records, draft decision briefs, Opportunity Solution Tree, integrity checks, and revision-impact inspection work locally. It does **not** yet perform autonomous research, execute AI agents, independently validate evidence, authenticate approvals, or provide a hosted service.

[Run the fictional demonstration](#try-it-in-a-minute) · [The case for Venture Method](ABOUT.md) · [Method selection](docs/METHOD_SELECTION.md) · [Architecture](docs/ARCHITECTURE.md) · [Contribute](CONTRIBUTING.md)

## Why another framework?

A strategy deck, discovery tree, PRD, market report, and financial model may all describe the same situation. Too often they are produced independently. New evidence arrives, but no one knows which assumptions, decisions, or deliverables it affects.

And before any of those artifacts are created, there is another question: **which intellectual tools are appropriate for this problem?** A market-entry question is not a product discovery exercise. A customer interview does not validate an entire business model. A canvas is not a business. A roadmap is not a strategy.

Venture Method connects five disciplines of work:

1. **Understand the situation.** Define the mandate, find relevant sources, distinguish observations from interpretations, and identify what remains unknown.
2. **Choose deliberately.** Compare frameworks and methods by the question they answer, their prerequisites, and their limits. Do not run every framework by default.
3. **Develop and test options.** Use research, models, hypotheses, experiments, commercial analysis, product discovery, or organizational diagnosis as warranted.
4. **Record decisions and consequences.** Preserve alternatives, the evidence considered, and the conditions that would reopen a decision.
5. **Keep learning.** Propose changes when knowledge evolves, identify downstream work requiring review, and retain the previous record.

The aim is not more documents. It is **better judgment, less repeated setup, and work that remains intelligible after the original session ends**.

## Try it in a minute

Python 3.11+ is required. The core demo has no third-party Python dependencies and makes **no model or network calls**.

```bash
python vm.py demo
python vm.py ost show fictional-harbor-supplies-demo
python vm.py impact fictional-harbor-supplies-demo --id CLM-0001
python vm.py audit fictional-harbor-supplies-demo
```

The demo creates an **explicitly fictional** client engagement under the gitignored `engagements/` directory. It includes invented interview notes, a claim, hypothesis, option, draft decision, reviewable Opportunity Solution Tree, two immutable working briefs, and a proposed claim revision. Follow the chain to see what would need reconsideration when new information contradicts an earlier assumption.

To compare methods instead of generating a project:

```bash
python vm.py frameworks --goal map_market --evidence minimal
python vm.py frameworks --goal discover_need --evidence observed
python vm.py skills list
```

The selector displays candidate methods and their applicability cautions. It does **not** choose a supposedly correct framework on your behalf or run the framework automatically.

### Start your own engagement

```bash
python vm.py new "Example Company" --type company --industry logistics --mode quick
python vm.py intake example-company \
  --objective "Understand the main growth constraint" \
  --approval-owner "Engagement owner" \
  --risk-level medium
python vm.py route example-company
python vm.py plan example-company
```

[Detailed commands and examples](docs/GETTING_STARTED.md)

## One framework, different work

| Your role | A question it helps structure | Relevant work |
|---|---|---|
| **Founder or venture builder** | Is this a venture worth pursuing? | Customer discovery, business models, uncertainty tests, capital options |
| **Product manager or CPO** | Which outcomes and opportunities should the team pursue? | Continuous discovery, Opportunity Solution Trees, prioritization, experiments |
| **CEO or fractional executive** | What is actually constraining the organization? | Operating models, market assessment, systems diagnosis, strategic choices |
| **VC, family office, or investment team** | What should we believe before committing capital? | Diligence, market structure, assumptions, scenario analysis, decision history |
| **Researcher or advisor** | How do I turn unfamiliar context into credible work? | Source review, methods selection, documented reasoning, reviewable deliverables |

These are intended use cases, not claims that the current offline prototype replaces specialist judgment or investment review.

## Methods, skills, and workflows are not the same thing

A **framework** organizes thinking. A **method** specifies how to investigate or decide. A **skill** packages instructions and supporting resources for an agent. A **workflow** coordinates methods, skills, people, approvals, and repeated learning.

The repository currently catalogs **34 methods** and includes **26 original portable skill specifications**. Among the represented traditions are Teresa Torres's continuous discovery and Opportunity Solution Trees; Jobs to Be Done; Strategyzer canvases and experiments; product operating models; Wardley Mapping; market and competitive analysis; real options; scenarios; and venture diligence.

The method catalog is **selection metadata**, not proof that all 34 methods have complete executable implementations. Only some are supported by working local commands. See [method selection](docs/METHOD_SELECTION.md), [capability status](docs/CAPABILITY_STATUS.md), and [research and attribution](docs/RESEARCH_AND_METHODS.md).

The project studies and may interoperate with [Huryn's PM Skills](https://github.com/phuryn/pm-skills), [Product on Purpose](https://github.com/product-on-purpose/pm-skills), [Dean Peters's PM Skills](https://github.com/deanpeters/Product-Manager-Skills), [PM Brain](https://github.com/phuryn/pm-brain), [BMAD](https://github.com/bmad-code-org/BMAD-METHOD), [Spec Kit](https://github.com/github/spec-kit), and the [Agent Skills standard](https://agentskills.io/specification). They are independent works. Their skills are **not** bundled wholesale, and upstream popularity is not treated as evidence of quality. Attribution, permissions, version pins, and evaluation are required before adopting third-party material.

## Knowledge that stays revisable

```text
Source -> Claim -> Hypothesis / Option -> Decision -> Action -> Outcome
            |                                |
            +---- Opportunity tree           +---- Deliverable
                            New information
                                  |
                         Proposed change
                                  |
                   Dependency review and decision
```

Source and claim references are engagement-scoped. The local journal preserves recorded history. Revisions are proposed as new records rather than silently overwriting their predecessors. A dependency command identifies **explicitly linked** downstream records that require consideration.

This is **not** yet a collaborative knowledge platform: concurrent editing, authenticated approval, semantic contradiction detection, automated refresh, and selective regeneration of published artifacts remain future capabilities. Read the [change-control design](docs/LIVING_KNOWLEDGE_AND_CHANGE_CONTROL_V3.md).

## What works today

| Available locally | Not yet implemented |
|---|---|
| Private engagement initialization and intake | Automated public/private source ingestion and verification |
| Deterministic capability routing and method comparison | Expert-level agentic framework application |
| Evidence-linked claims, options, hypotheses, decisions and outcomes | Authenticated approvals, team collaboration and permissions service |
| Local hash-chained journals and reference checks | Production-grade transactional knowledge service |
| Working-draft Opportunity Solution Trees with proposed changes | Automated customer interview extraction and expert validation |
| Immutable Markdown decision briefs and context packs | Native slides, spreadsheets, financial models or external publication |
| Skill registry, review scaffolding, structural tests | Real comparative AI evaluations and autonomous agent execution |

**Local tests:** run `python -m unittest discover -s tests -v` and `python vm.py skills check`. Structural test success does not establish business accuracy or professional output quality.

## Portable by design

The core runs locally with Python and human-operated commands. Skill instructions follow a portable folder convention and can be made available to supported agent tools. Hermes is a useful first adapter, **not** a required runtime. Open ASS and separate creative tools can receive approved handoffs without becoming dependencies.

Client data in `engagements/` is ignored by Git by default. Do not commit sensitive case files, install unreviewed agent skills, or treat a source reference as factual verification. See [security](docs/SECURITY.md) and [skill governance](docs/SKILL_GOVERNANCE.md).

## Help build the quality bar

This project is meant to be useful to one serious practitioner first, and eventually portable to others. We welcome improvements grounded in strong methods, realistic cases, reproducible evaluations, and careful review.

Read [the project's purpose](ABOUT.md), [quality and contribution standards](CONTRIBUTING.md), and [capability gaps](docs/CAPABILITY_STATUS.md). Please **do not** add a skill merely to increase the count.

**Release note:** The repository does not yet include a public redistribution license. Before publishing or accepting external contributions, the owner should choose and add an appropriate license, then review all third-party materials.
