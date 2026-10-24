# Positioning, copy and voice | reusable working method

These are six **first-party, review-stage Agent Skills**, adapted from five open-source skill references and April Dunford's alternative-first positioning process. Each works individually; do not turn this into a compulsory six-agent chain.

## The job determines selection

| User task | Minimum sequence |
| --- | --- |
| New company/service positioning | `marketing-context` -> `competitive-positioning`; add `brand-architecture` for entity architecture |
| New homepage, agency profile, service page or outreach copy | Load existing `marketing-context`; verify `competitive-positioning`; `marketing-copywriting` |
| Polish a strong existing draft | `brand-voice-preservation` or `copy-editing` as needed; never rebuild positioning by default |
| Copy sounds formulaic or artificial but argument is sound | `human-writing-audit` only |
| Repeated owner correction | Record restriction in canonical context; update only the affected copy; rerun narrow editorial check |
| Enterprise claim, market claim or client proof disputed | `evidence-audit` then the relevant editor |

## Source-of-truth contract
- **Host owned:** the consuming project owns the canonical marketing context. Venture Method ships a reusable template, not its clients' private context.
- **Existing file first:** read previous accepted copy, actual owner's language, market evidence, approval status and explicit rejections before generating.
- **Location:** use an established project context path; for new projects suggest `.agents/product-marketing.md`.
- **Version:** change the version and append a dated reason for any material update; preserve decision history and retired/rejected wording.
- **Authority:** owner-approved > provisional proposal; verified evidence > unsourced speculation for factual claims; the user may choose a creative style without inventing customer proof.
- **Current task:** narrow editing requests are not permission to change the commercial thesis.

## Positioning method
Apply the sequence: **alternatives -> comparative capabilities -> customer value -> best-fit customer -> market category**. The ordering follows April Dunford's published account. The actual competitors are the options customers weigh, including internal implementation and delaying. A public description of a vendor does not prove that a prospective buyer considers it an alternative.

## Drafting and review
Write the strongest supportable commercial argument. Preserve true distinctive terms. Treat website, Upwork, cold outreach and founder writing as separate channels. After drafting, check claims and author fidelity, then remove formulaic language. Changing punctuation or synonyms cannot repair unsupported positioning.

## Test before trusting
See `evals/{marketing-context,competitive-positioning,marketing-copywriting,brand-voice-preservation,copy-editing,human-writing-audit}.json`.
Run paired agent trials on the exact same input, compare results blind where possible, and measure claim retention, forbidden-language recurrence, buyer understanding, minimal-edit compliance and factual accuracy. Fixtures are not executed benchmarks.

## External study and attribution
Original Venture Method instructions are not forks or copy-pasted third-party skills:
- Corey Haines, Marketingskills (MIT): [product-marketing](https://github.com/coreyhaines31/marketingskills/blob/main/skills/product-marketing/SKILL.md), [copywriting](https://github.com/coreyhaines31/marketingskills/blob/main/skills/copywriting/SKILL.md), [copy-editing](https://github.com/coreyhaines31/marketingskills/blob/main/skills/copy-editing/SKILL.md)
- Microsoft CAT skill: [brand-voice-pass](https://github.com/microsoft/cat-agent-skills/blob/main/submissions/brand-voice-pass/SKILL.md), referenced as method, not vendored
- blader (MIT): [humanizer](https://github.com/blader/humanizer/blob/main/SKILL.md)
- April Dunford, [A Quickstart Guide to Positioning](https://www.aprildunford.com/post/a-quickstart-guide-to-positioning), method attributed, original templates not redistributed.

All upstream links may change; verify licenses, versions and exact commit before vendoring code or reproducing substantial protected material. No outside scripts, packages, agent plugins or network permissions are installed.
