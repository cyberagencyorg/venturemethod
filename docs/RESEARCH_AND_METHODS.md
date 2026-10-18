# Research basis and curated methods (as of October 18, 2026)

## Decision frameworks: reference, do not blindly import

| Domain | Leading techniques | Responsible use |
| --- | --- | --- |
| Strategic diagnosis | Systems thinking, causal models, Wardley Mapping, value chains, PESTLE, Five Forces | Decide what is changing, who has power and dependencies, avoid overconfidence |
| Customer and opportunity | Jobs to Be Done, continuous discovery, opportunity solution trees, behavioral interviews | Seek customer accounts and actual behavior before solutions |
| Business design | Business Model Canvas, Value Proposition Canvas, unit economics, pricing research | Treat business model as hypotheses, not validation |
| Product | SVPG Product Operating Model, dual-track discovery/delivery, PRFAQ, product strategy, outcome metrics | Accountable teams and explicit problems, not feature factories |
| Testing | GV Design Sprint, Lean Startup, pretotyping, assumption tests, pre-mortems | Match test cost to downside and uncertainty; state sample limitations |
| Delivery | Shape Up, OKRs, risk-based milestones, Spec Kit handoff | Capacity, appetite and testable outputs; no rigid cadence everywhere |
| Venture and capital | venture thesis, stage-gate capital, real options, funding instruments, downside cases | Make risk and dilution explicit; qualified review for legal/financial matters |
| Transformation | Business capability mapping, service blueprinting, decision rights, process analysis | Build operating capacity, not merely an org chart |
| Market and GTM | Customer segmentation, substitution analysis, positioning, ICP, channel economics | Separate reachable buyers from market size and hypothetical demand |
| Epistemic review | Provenance audit, source triangulation, counterfactuals, uncertainty ledgers | A sourced argument can still be wrong; test decisive premises |

Select methods using `config/methods.json`. Avoid applying the same canvas to every engagement. Distinct frameworks may be incompatible; record reasoning rather than combining their vocabulary mechanically.

## Contemporary AI skill sources to study

| Reference | What merits examination | Reuse consideration |
| --- | --- | --- |
| [Agent Skills](https://agentskills.io/specification) | Portable SKILL.md, metadata, progressive disclosure | Open specification |
| [Anthropic skill creator](https://github.com/anthropics/skills/tree/main/skills/skill-creator) | Generate, improve, evaluate skills and triggering | Review specific content licenses before importing |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | 69 skills / 42 workflows in 9 plugins, strong PM flow coverage | MIT; preserve notices when copied |
| [product-on-purpose/pm-skills](https://github.com/product-on-purpose/pm-skills) | 68 skills, Triple Diamond, examples, CI contracts, skill quality | Apache-2.0; preserve notices |
| [product-on-purpose/agent-skills-toolkit](https://github.com/product-on-purpose/agent-skills-toolkit) | Skill scoring, grading and library maintenance | Review license and implementation before reuse |
| [deanpeters/Product-Manager-Skills](https://github.com/deanpeters/Product-Manager-Skills) | 77 methods with context/failure guidance and intelligence suite | CC BY-NC-SA 4.0; do NOT republish derivative skill content in commercial product without rights |
| [RefoundAI/lenny-skills](https://github.com/refoundai/lenny-skills) | Broad product and growth expertise linked to sources | Underlying Lenny/podcast content is separately owned; study links, not import bulk text |
| [slavingia/skills](https://github.com/slavingia/skills) | Lightweight founder validation/pricing/distribution | Verify reuse license before importing |
| [obra/superpowers](https://github.com/obra/superpowers) | Independent review, planning, task isolation and testing discipline | Engineering-oriented; do not replace business evidence |
| [BMAD Method](https://github.com/bmad-code-org/BMAD-METHOD) | Scale-adaptive specialist workflows and handoffs | More software-oriented; optional reference |
| [GitHub Spec Kit](https://github.com/github/spec-kit) | Spec, plan, tasks, converge and idea-assessment extension | Use for downstream executable requirements |
| [skills.sh](https://skills.sh/) | Discovery/catalog of agent skills | Install count is not a performance benchmark |

## Source caution

- Vendor claims, GitHub stars and directory installs are adoption indicators, not causal evidence of effectiveness.
- Original framework authors and publishers should be attributed. Reproduce their protected templates only with appropriate rights.
- Research timestamps matter. Validate methods, skill versions and licenses at the point of vendoring.
- Do not confuse a skill capable of producing a *plausible document* with an agent that has independently verified the content.

## Core design conclusion

The differentiator is not the size of the skill collection. It is the combination of **method selection + client-specific context + evidence traceability + cross-functional capability + independent evaluations + accountable decisions**.
