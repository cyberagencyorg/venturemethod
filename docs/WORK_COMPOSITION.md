# Work composition (experimental)

Venture Method needs to connect a real assignment to the procedures and resources needed to complete it. Until now, the method catalog, skill specifications, routing suggestions, and role guidance lived largely independently.

`vm.py compose` is the first **offline, nonexecuting** composition contract. It works from an engagement objective and explicitly named goals. It suggests applicable methods, shows gaps and prerequisites, and can prepare an immutable private proposal with the skill, role, tool class, output, and reviewer associated with each selected method. It does not execute a skill or activate an AI agent.

## Try it

From the repository root:

```bash
python vm.py capabilities
python vm.py new "Fictional Client Example" --type client --industry logistics --mode quick
python vm.py intake fictional-client-example \
  --objective "Assess demand for a logistics service before investing" \
  --approval-owner "Engagement owner"

# See alternatives, without silently choosing a favored framework.
python vm.py compose fictional-client-example --goal map_market --goal design_business

# Compose an explicitly selected plan. Saves a content-addressed draft privately.
python vm.py compose fictional-client-example \
  --goal map_market --goal design_business \
  --method market-sizing --method business-model-canvas \
  --evidence minimal --save
```

Private plan files are created inside the gitignored `engagements/<slug>/plans/`. A new engagement or source/claim snapshot creates a distinct filename when you save again; prior proposals are not overwritten. No client data is checked into the framework repository by this command.

The `--evidence` argument is **operator-declared**, not evidence validation. Methods requiring observed evidence are blocked if the engagement has no recorded source and linked claim. Recorded evidence remains unverified until it has undergone appropriate review. A record labelled `interview` is not proof an interview took place.

## Records and boundaries

| Record | Role in composition | Current truth |
| --- | --- | --- |
| `config/frameworks-v3.json` | Method inventory with goals, prerequisites and source reference | 34 cataloged methods; not executed/validated methods |
| `config/work-composition.json` | Mapping from method to capability and optional first-party skill | All cataloged methods linked; some missing real provider |
| `config/skills-registry.json` | First-party skill file inventory | 26 instruction specifications, not verified agents |
| `config/agent-roles.json` | Reusable task role contracts | Seven proposed roles; not running agents or authorization |
| `config/tool-contracts.json` | Tool class and side-effect inventory | Local read/draft facilities and unimplemented external adapters |
| `evals/*.json` | Independent assessment scenarios for skill quality | Fixtures only, no claim of live model benchmark scores |
| `engagements/<slug>/` | One mandate's source, decisions, revision history and draft outputs | Local, single-user; gitignored |

`python vm.py capabilities` checks that first-party skills, capabilities, methods, roles and tools have valid cross-references. A method-to-skill mapping means only that a relevant instruction file exists. The planner explicitly returns coverage as `partial_instruction_only` or `no_first_party_skill`.

The first gaps identified are **JTBD Outcome-Driven Innovation**, **Shape Up**, and **Design Sprint**, which have method records without first-party implementation. Marketing execution, sales operations and people operations have capability stubs with no first-party specialist skills. This is intentional visibility, not a recommendation to implement every capability ourselves.

## Why method choice remains explicit

The framework should not choose a well-known method because keywords match a problem description. For now, the operator selects a goal and reviews alternatives. The selected method must actually support a declared goal. The proposal preserves the method's source, limitations, minimum evidence and role/skill association.

Later evaluations should compare alternatives with representative cases, assess whether the proposed method was appropriate, and challenge whether a simpler approach would have produced a better result. Automated ranking should follow that evidence.

## Proposed task-role policy

Agent roles are task profiles rather than independent personalities. The registry currently defines engagement lead, researcher, specialist, analyst, execution coordinator, independent critic and knowledge steward. Each role is restricted to a **planning-level** read/draft tool class and lacks approval authority.

Do not treat registry metadata as enforcement. An actual agent runtime must enforce access to data, tools, external side effects, delegation limits and human approvals. Hermes may be the first adapter, but the work-unit contracts should also be usable manually or with other compatible agents.

## What is still missing

Actual tool invocation, sources fetched or independently verified, skill loading/execution, concurrent collaboration, execution receipts, task retries, role handoffs, user authentication, high-quality document generation, and meaningful professional evaluations. All work units are marked `manual_execution_only` and proposals are `proposed_not_executed`.

The next slice should run one bounded research-to-output case through an authorized adapter, compare results to a manual baseline, and carry a consequential evidence update into a revised artifact. Do that before introducing autonomous execution across more domains.

## Bounded research execution (first local adapter)

The separate `vm.py research` subcommand now performs operator-mediated text capture, exact-excerpt association, evidence auditing, and immutable review-draft generation. See [research capture](RESEARCH_CAPTURE.md) for the commands, limitations and update behavior.

It is recorded as `local-source-capture` in the tool registry with a local draft effect. It does **not** run an agent, fetch a website, verify authenticity or authorize a publication. A composed method plan remains planning-only; the operator chooses and runs the research steps explicitly. An execution receipt and a live adapter binding are future work.
