# Khan's Venture Method Framework

**An adaptive, AI-native framework for venture architecture, product leadership, business strategy, and cross-functional execution.**

Created by Brad Khan. Also called **Venture Method**. Built for professional use by people working alone, with teams, or with AI agents.

You might be assessing a company, designing a venture, leading product, advising an executive team, or investigating an unfamiliar market. The assignment rarely fits within one discipline. You need to work out what is happening, decide which questions matter, find the right expertise, produce useful work, and follow through.

Khan's Venture Method Framework is designed to make that work reusable. It brings established methods, specialist skills, research, work products, and a persistent record of decisions into one adaptable way of working.

You can start with one question or run a long engagement. The methods change with the problem. The knowledge carries forward.

[About the project](ABOUT.md) · [What belongs in the framework](docs/FRAMEWORK_SCOPE.md) · [Getting started](docs/GETTING_STARTED.md) · [Current capabilities](docs/CAPABILITY_STATUS.md)

## What you can use it for

| Situation | Work you might need |
| --- | --- |
| **Building a venture** | Opportunity research, customer discovery, business model design, experiments, pricing, capital options, launch planning |
| **Leading a product** | Research synthesis, Opportunity Solution Trees, product strategy, requirements, prioritization, operating cadence, measurement |
| **Running or advising a company** | Market and organizational assessment, commercial strategy, process improvement, finance, hiring, marketing, sales |
| **Evaluating an investment** | Industry analysis, diligence, scenario modelling, risks, competing theses, follow-up questions |
| **Doing client work** | A scoped investigation, proposal, strategy, delivery plan, or ongoing advisory engagement |

These are areas the framework is designed to support. They are not all automated in the current release.

## How it works

Start by describing the mandate. It might be a company name, a problem, a market, an idea, or a specific deliverable.

Venture Method helps organize the work around a few practical questions:

1. **What do we need to understand?** Establish context, distinguish evidence from assumptions, and identify missing information.
2. **How should we approach it?** Choose from established frameworks and methods according to their purpose, evidence requirements, costs, and limitations.
3. **What work needs doing?** Use appropriate specialist skills and workflows. Research, strategic analysis, product discovery, financial modelling, sales, marketing, and operational work may all be relevant.
4. **What did we decide and do?** Keep the reasons, alternatives, approvals, work products, and results together.
5. **What changed?** Revisit affected assumptions and decisions as new information arrives, without erasing the earlier record.

You don't have to run all five as a formal sequence. A small task should stay small.

### Methods, skills, and knowledge

A framework such as an Opportunity Solution Tree helps organize a product outcome, customer opportunities, solutions, and assumption tests. An interview skill helps conduct or analyze the research behind it. A workflow may coordinate those skills with review and follow-up. The engagement's knowledge should survive all of them.

Venture Method keeps these concerns separate so you can replace a skill, switch agents, or choose another method without losing the work.

The project currently draws on product management, venture design, strategic analysis, systems thinking, commercial operations, and investment disciplines. [Method selection](docs/METHOD_SELECTION.md) explains how to compare approaches. [Research references](docs/RESEARCH_AND_METHODS.md) credits the external work we study.

## Try the current prototype

The repository contains an **offline experimental implementation**, not a finished autonomous advisor. Python 3.11+ is required for the local CLI. The demonstration is fictional and makes no network or model calls.

```bash
python vm.py demo
python vm.py ost show fictional-harbor-supplies-demo
python vm.py impact fictional-harbor-supplies-demo --id CLM-0001
python vm.py audit fictional-harbor-supplies-demo
```

The example includes customer evidence, a hypothesis, a decision, an Opportunity Solution Tree, and a proposed change. You can inspect how the earlier decision remains intact while its supporting claim is reconsidered.

To compare applicable methods or start an engagement:

```bash
python vm.py frameworks --goal map_market --evidence minimal
python vm.py frameworks --goal discover_need --evidence observed
python vm.py new "Example Company" --type company --industry logistics --mode quick
python vm.py plan example-company
```

The local implementation includes engagement records, method metadata, 26 original skill specifications, draft decision briefs, proposed revisions, basic dependency inspection, and structural tests. It cannot yet conduct independent research, run arbitrary agent workflows, produce verified financial analyses, or manage a team with authenticated approvals. See [capability status](docs/CAPABILITY_STATUS.md).

## Built to travel

Venture Method should work with a person operating manually, Hermes, or another compatible agent. Its methods and engagement records should not depend on a particular model, dashboard, CRM, or project management application.

Specialist libraries have plenty to teach us. We study the PM skill collections by [Paweł Huryn](https://github.com/phuryn/pm-skills) and [Product on Purpose](https://github.com/product-on-purpose/pm-skills), [Anthropic's knowledge-work plugins](https://github.com/anthropics/knowledge-work-plugins), and other sources. Their skills are not all included here. Each integration needs a defined role, license review, version pin, and real evaluation.

For software delivery, creative production, CRM work, or other specialist execution, the framework should hand work to a suitable system and bring the results back. It doesn't need to become every one of those systems.

## Contributing

The framework is being developed for real use first. Contributions should improve the quality of a method, the usefulness of a workflow, the reliability of the knowledge record, or the results of a representative case. Adding another skill name is not an improvement by itself.

See [ABOUT.md](ABOUT.md), [CONTRIBUTING.md](CONTRIBUTING.md), and the [scope and design rules](docs/FRAMEWORK_SCOPE.md).

**Status:** Private development repository. No public redistribution license has been chosen. The current tests verify local behavior and structure, not professional competence or factual accuracy.
