# Contributing to Venture Method

The goal is a small number of genuinely useful, rigorous capabilities that compose well. Please resist adding large collections of framework names or prompt files without evidence of practical value.

## Good contributions

- An improvement to an existing method, with a credible reference and a clear explanation of where it applies.
- A working capability that addresses a documented gap and adds appropriate tests.
- A realistic, permission-cleared benchmark or anonymized example showing both success and failure cases.
- A correction to a misleading claim, omitted limitation, or unsafe assumption.
- A better knowledge revision, provenance, privacy or review workflow.

## Quality requirements

For a new method or skill, document:

1. **Question and intended user:** What decision or task does this improve?
2. **Distinction:** Why isn't an existing method or skill sufficient?
3. **Inputs and prerequisites:** What data or expertise is actually required?
4. **Procedure and expected outputs:** What specific, inspectable work occurs?
5. **Failure modes:** When is the method inappropriate or easy to misuse?
6. **Evidence and credit:** Primary references, attribution, licenses and version pins.
7. **Evaluation:** Baseline comparison, adversarial cases and professional review criteria.
8. **Knowledge lifecycle:** What becomes stale, what can change, and what downstream work depends on it?

Structural tests are necessary but insufficient. A model's assertion that it did good work is not an independent evaluation.

## Working rules

- Make focused branches and reviewable pull requests. Keep code, method definition and test changes connected.
- Keep confidential engagements out of commits. They live under ignored `engagements/` by default.
- Do not import third-party skill material without checking the license for each component and retaining required notices.
- Do not let agents auto-update trusted skills or execute unreviewed scripts.
- Do not imply that interviews, financial figures, legal conclusions, approvals or external research occurred when they did not.
- Run `python -m unittest discover -s tests -v` and `python vm.py skills check` before proposing a change.

## License and publication status

**This working repository does not currently carry an open-source redistribution license.** An owner-approved license and a third-party attribution review must precede public distribution and external code contributions. Repository visibility alone does not grant adaptation or commercial reuse rights. This note does not restrict reading or discussing the project.

See [ABOUT](ABOUT.md), [method selection](docs/METHOD_SELECTION.md), and [skill governance](docs/SKILL_GOVERNANCE.md).
