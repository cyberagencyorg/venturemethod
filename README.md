# Venture Method

**Better decisions, with the reasoning still attached.**

Venture Method is a library of professional methods and agent-ready instructions, plus a local workbench for research, decisions, and revision history. It is built for problems that cross venture creation, product leadership, company strategy, investment, and operations.

Use one method in a project already underway, or keep an entire engagement organized over time. Your existing tools, judgment, and decisions stay in charge.

**[Use it in an existing project](ADOPT.md)** · **[Try the local workbench](docs/GETTING_STARTED.md)** · [Explore the methods](docs/METHOD_SELECTION.md) · [See what's implemented](docs/CAPABILITY_STATUS.md)

## Start with the problem

A company asks whether it should build software to improve customer retention. Starting with a product requirements document is easy. Establishing whether software is the right intervention is harder.

You might first need to verify the retention numbers, hear from customers, examine service operations, compare pricing and process changes against a software investment, and decide what evidence would justify a pilot.

That could involve customer discovery, business-model analysis, financial scenarios, or a simple operational review. The appropriate combination depends on the question and the evidence available. Venture Method helps organize that choice and preserve the work behind it.

The same approach applies when you're evaluating a venture, entering an unfamiliar market, advising a leadership team, or reviewing an investment.

## Two ways to use it

### 1. Bring the methods to the work you're already doing

You don't need to migrate a repository, install an agent framework, create an engagement, or change your existing process.

Give a compatible AI assistant with access to this repository the following instruction:

```text
Read ADOPT.md in cyberagencyorg/venturemethod.
Inspect the current project's context and decisions first.
Use only the Venture Method methods or skills that improve this task.
Keep the project's existing tools, files, and approved direction intact.
```

[**ADOPT.md**](ADOPT.md) is the portable entry point. It covers selective use, agent boundaries, and how to choose relevant skills without loading the whole library.

If you have a local checkout, you can also request optional, read-only suggestions:

```bash
python vm.py adopt --task "Assess a product already in delivery" --phase in-flight
```

This command uses simple lexical matching. It does not understand the whole project, run an agent, or make changes on your behalf.

### 2. Run a local engagement

The experimental CLI is useful when research, decisions, and subsequent changes need a durable record.

**Requirements:** Python 3.11+. The offline commands below require no model API key or third-party Python packages.

```bash
git clone https://github.com/cyberagencyorg/venturemethod.git
cd venturemethod

python vm.py doctor
python vm.py demo
python vm.py ost show fictional-harbor-supplies-demo
python vm.py audit fictional-harbor-supplies-demo
```

The demonstration is entirely fictional. It shows how an evidence-backed decision, an Opportunity Solution Tree, and a proposed revision can coexist without rewriting the original record.

To begin your own engagement:

```bash
python vm.py start "Market Assessment" \
  --type client \
  --objective "Decide whether a pilot is justified" \
  --owner "Engagement lead"

python vm.py status market-assessment
```

Continue with [the first-engagement walkthrough](docs/FIRST_ENGAGEMENT.md) for permitted source capture, exact excerpts, method selection, work packets, and reviewable drafts. Engagement data is stored locally in a gitignored directory, **not encrypted**.

## What the framework connects

| Layer | Purpose |
| --- | --- |
| **Mandate** | Define the decision, constraints, stakeholders, and desired outcome. |
| **Methods** | Compare approaches by the questions they answer, prerequisites, and limits. |
| **Skills** | Supply reusable procedures for research, product, strategy, business design, and review. |
| **Work composition** | Connect a goal to candidate methods, skills, roles, inputs, and deliverables. |
| **Evidence and decisions** | Preserve sources, claims, alternatives, decisions, and the reasoning behind them. |
| **Revision** | Inspect what a new claim or changed assumption may affect without erasing history. |

These layers can be used independently. A short assignment shouldn't require a full engagement process. Nor should the framework try to replace a CRM, coding agent, accounting system, or the tools a team already uses.

[Method selection](docs/METHOD_SELECTION.md) · [Work composition](docs/WORK_COMPOSITION.md) · [Framework scope](docs/FRAMEWORK_SCOPE.md)

## What works today

This repository contains an **offline experimental implementation**, not an autonomous consulting or venture-building system.

| Available now | Important limitation |
| --- | --- |
| Method catalog and deterministic comparison | Metadata helps narrow choices; it does not establish expert fit. |
| First-party skill instructions and portable agent entry point | Instructions are not independently validated professional capabilities. |
| Engagements, sources, claims, decisions, and event history | Local records do not verify that external claims are true or approvals are authentic. |
| Permission-bounded source capture and exact-excerpt checks | Source authenticity and interpretation still require review. |
| Opportunity Solution Tree drafts, dependency inspection, and proposed revisions | No automatic discovery interviews or reliable semantic reconciliation. |
| Work plans, packets, and draft briefs | No autonomous multi-agent execution, verified financial analysis, or publication workflow. |

Live collaboration, authenticated approvals, agent execution, rigorous skill benchmarks, and deeper integrations remain development work. The [capability register](docs/CAPABILITY_STATUS.md) distinguishes implemented code from intended behavior.

## Find your way around

| Location | What's there |
| --- | --- |
| [ADOPT.md](ADOPT.md) | Use selected methods and skills inside another project. |
| [skills/](skills/) | First-party skill specifications. |
| [config/frameworks-v3.json](config/frameworks-v3.json) | Method definitions, fit criteria, prerequisites, and source references. |
| [config/work-composition.json](config/work-composition.json) | Mapping between methods and supporting capabilities. |
| [docs/GETTING_STARTED.md](docs/GETTING_STARTED.md) | Local CLI walkthrough. |
| [docs/RESEARCH_AND_METHODS.md](docs/RESEARCH_AND_METHODS.md) | Research background and external method references. |
| [ABOUT.md](ABOUT.md) | Why the framework exists and how its boundaries were chosen. |
| [CONTRIBUTING.md](CONTRIBUTING.md) | Contribution and quality requirements. |

## Built to be questioned

A familiar framework is not necessarily an appropriate one. A skill file is not proof of competence. A polished deliverable is not evidence that its conclusions are correct.

The standard here is practical: better choices of method, credible sources, less repeated setup, clear accountability, and work that can be challenged or revised. Real evaluations must compare the result against doing the job without Venture Method.

The methods draw on established product, venture, strategy, and systems disciplines. Original authors and external libraries are credited in [research and methods](docs/RESEARCH_AND_METHODS.md); those libraries are not automatically installed or redistributed.

**Created by [Brad Khan](https://github.com/BradKhan).** [Project background](ABOUT.md).

**License:** This public repository does not currently have an open-source redistribution license. Public access does not grant permission to reuse or redistribute its code. See [contribution guidance](CONTRIBUTING.md).
