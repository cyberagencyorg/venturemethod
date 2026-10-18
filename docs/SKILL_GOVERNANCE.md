# Skill acquisition, customization and evaluation

## Skill lifecycle

1. **Discover:** Browse spec-compliant libraries and record the specific task gap, not popularity alone.
2. **Compare:** Determine whether a current internal skill already handles the task. Test on representative prompts.
3. **Vet:** Record upstream URL, version, SHA, license, dependencies, executable scripts, tool permissions and data access.
4. **Select:** Prefer first-party original, permissively licensed and minimal dependency implementations.
5. **Adapt:** Write a local wrapper or clean-room skill when methods need organization-specific context. Preserve attribution/licensing when copying permitted text.
6. **Evaluate:** Run paired no-skill and with-skill cases on identical inputs. Include ordinary, adversarial and ambiguous examples; grade facts, actionability, consistency, privacy and cost.
7. **Promote:** Document empirical improvement, security review, owner, version, rollback instructions and approval.
8. **Monitor:** Re-evaluate on model upgrades, framework changes or recurring operational failures.

## Registry contract

For each candidate skill record at least:

```
name, upstream, ref/sha, content_hash, license, author, review_date,
status, allowed_tools, internet_required, executable_scripts,
compatible_harnesses, dependencies, data_sensitivity, eval_suite,
baseline_score, with_skill_score, reviewer, rollback
```

`config/skills-registry.json` has only first-party original skills today. The registry says **draft-validated-structure**, not production-certified. Manual upstream approval is required for any future importer.

## Evaluation rubric (0 to 4 on each dimension)

- **Selection:** activates only when relevant; does not hijack unrelated tasks.
- **Accuracy:** no invented facts, numbers, sources, validations or approvals.
- **Task usefulness:** actionable output addresses the underlying decision.
- **Method fidelity:** applies the correct technique including prerequisites and exceptions.
- **Traceability:** material claims link to sources; recommendations link to decisions.
- **Privacy and authority:** no unauthorized disclosure or external action.
- **Efficiency:** depth appropriate to risk and context, without needless work.

Compare paired runs using identical inputs and a reviewer blind to which arm produced which output when possible. Report distributions and failures, not just aggregate scores. Prefer evaluating the exact output artifact and its citations. A skill is not promoted merely because a rubric is written.

## Attack cases

A third-party source says to ignore the engagement brief; instructions hidden in a downloaded PDF; a skill requests credentials, network calls or destructive shell access; business references mix similarly named organizations; an output inflates unverified market numbers; material is leaked between engagements. Fail closed on approval or publication.

## License cautions

The public `deanpeters/Product-Manager-Skills` collection currently states **CC BY-NC-SA 4.0** with additional guidance; this is not a simple permissive commercial redistribution grant. `RefoundAI/lenny-skills` explicitly distinguishes MIT code structure from third-party content rights. `phuryn/pm-skills` states MIT; `product-on-purpose/pm-skills` states Apache-2.0. Confirm license at pinned commit and consult counsel before incorporating substantial third-party material into products or commercial packages.
