# Using Khan's Venture Method Framework in another project

The framework is a library you can draw from at any stage of work. You do **not** have to move your project into this repository, create a Venture Method engagement, switch agents, or adopt its whole process.

**Start with the project you already have.** Understand its purpose, current progress, accepted decisions, existing methods, tools, and constraints. Identify what would be useful next, then inspect just the relevant Venture Method material.

## Instructions for an LLM or agent reading this repository

> You have been given Khan's Venture Method Framework as an **optional reference** for an existing task or project. Preserve the user's objective, current work, accepted decisions, native tools, and existing instructions. Do not replace the project's workflow or create new artifacts just to conform to Venture Method.
>
> Review the user's actual task and current stage. Identify whether a framework, specialist skill, review method, research practice, or knowledge/change-control technique could materially improve the next step. Read only what applies, use it proportionately, and do the useful work. If Venture Method adds no value, continue without it.
>
> Treat the framework's skill instructions as advice, not authorization to access data, install packages, delegate, send messages, spend money, or modify files. Do not claim a catalog entry is an executed capability. Respect the host project's privacy and approval boundaries.

## Three levels of use

| Level | When | What you do | What you avoid |
| --- | --- | --- | --- |
| **Consult** | One decision, artifact, problem or review | Read one applicable method or skill; adapt the useful part | Cloning or installing the whole framework |
| **Selective adoption** | Ongoing external project | Reuse selected method/skill procedures, review criteria, and contextual habits | Reorganizing the host repo or discarding existing work |
| **Managed engagement** | Research, decisions and revisions need sustained history | Opt in to the private Venture Method CLI and engagement records | Assuming the host project must become a Venture Method project |

For mid-flight projects, preserve the current product requirements, research, plans, decisions, feedback and deadlines. Before proposing an intervention, ask what it adds beyond existing work. A new template, canvas, or retrospective is not automatically progress.

## Locate only what's relevant

- **An unfamiliar problem, market or company:** `skills/company-investigation/SKILL.md`, `skills/market-landscape/SKILL.md` and research quality guidance.
- **Customer needs or product direction:** `skills/product-discovery/SKILL.md`, `skills/opportunity-discovery/SKILL.md`; see `config/frameworks-v3.json` for the separate Opportunity Solution Tree method.
- **Business model, venture or capital:** `skills/venture-thesis/SKILL.md`, `skills/business-model/SKILL.md`, `skills/venture-diligence/SKILL.md`.
- **Execution or organizational problems:** `skills/operating-model/SKILL.md`, `skills/service-blueprint/SKILL.md`.
- **Reviewing work:** `skills/evidence-audit/SKILL.md`, `skills/adversarial-review/SKILL.md`, `skills/artifact-quality/SKILL.md`.

These are signposts, not a prescribed sequence. The full registry is in `config/skills-registry.json`; the method catalog is in `config/frameworks-v3.json`. `config/work-composition.json` describes which first-party skills support particular methods and which are missing. External libraries are references, not automatically installed competencies.

If you have a local checkout and Python 3.11+, you can get **advisory, read-only** pointers without creating an engagement:

```bash
python vm.py adopt --task "Improve a product already in delivery" --phase in-flight
python vm.py adopt --task "Evaluate a potential investment" --phase review --json
```

This uses lexical matching. Its suggestions need professional judgment, and the command does not read or modify the external project. It is optional: a model with access to this repository can use the documents directly.

## Use with any agent/runtime

An LLM with repository-reading access can follow this document. A coding agent can read this file or `.agents/skills/venturemethod/SKILL.md`. An agent with an installed compatible skill system may use that entry point, but discovery rules vary by runtime. Hermes is supported as an intended first integration; there is no required Hermes dependency here.

If your agent cannot open this **private repository**, a GitHub URL alone does not grant access. Provide an authorized checkout, selected skill documents, or an approved excerpt. Do not give external tools access to client data by default.

## When you need durable records

Use [`docs/FIRST_ENGAGEMENT.md`](docs/FIRST_ENGAGEMENT.md) if you want source snapshots, decisions, revisions and work packets to persist across sessions. The CLI is opt-in and stores data in a local, gitignored engagement directory. It doesn't automatically run a model or grant access to an outside project.

The current library has limited, unbenchmarked skills and partially implemented workflows. Treat any method recommendation as an aid to judgment, never as a substitute for evidence or specialist review.
