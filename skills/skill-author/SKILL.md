---
name: skill-author
description: "Create, adapt and evaluate reusable agent skills, rather than accumulating prompt fragments. Use when: No suitable skill exists, a skill underperforms, a method changes or a specialized domain procedure must be encoded."
---
# Skill Author

**Purpose:** Create, adapt and evaluate reusable agent skills, rather than accumulating prompt fragments.

## When to use

No suitable skill exists, a skill underperforms, a method changes or a specialized domain procedure must be encoded.

## Inputs

User goal, allowed tools, input/output contracts, known examples, failure modes, baseline skill or no-skill condition.

## Method

1. Identify a narrow repeatable capability with measurable success and a clear activation boundary.
2. Draft SKILL.md with explicit inputs, procedure, outputs, quality gates and references; avoid vendor-exclusive syntax in core.
3. Create realistic positive, negative, edge and ambiguity test cases, including confidentiality and injection cases.
4. Compare a skill-enabled agent against a baseline on the same tasks, using independent outcome grading where possible.
5. Record version, license, upstream source and SHA; promote only with demonstrated improvement and no safety regression.

## Outputs

Candidate skill directory, eval fixture, measurable rubric, version metadata, benchmark comparison and approval record.

## Quality gates

- Do not install or execute unfamiliar third-party scripts without review.
- Do not claim improved performance unless baseline evaluations were run.
- Do not import third-party text without compatible rights and attribution.
- Label observations, sourced third-party assertions, analysis and recommendations separately.
- If required information is absent, disclose it and propose next checks; never fabricate completion.
- Prefer the shortest defensible workflow appropriate to the stakes.

## Handoff contract

Include engagement ID, objective, references to source IDs and claim IDs, unresolved issues, recommended next action, and approval owner.

## Evaluation

Use `evals/skill-author.json` to test relevance, factual discipline and output usefulness against a no-skill baseline.
