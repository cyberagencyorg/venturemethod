# Research capture and evidence brief

The first executable research capability in Venture Method is deliberately modest. It handles operator-provided UTF-8 source material. It does not scrape websites, independently authenticate a publisher, analyze a market with AI, or turn a quotation into a verified fact.

The distinction matters: a content hash establishes what bytes were stored, while a real investigation must still establish whether the source is accurate, representative, current, and relevant to the question.

## Run it

Create a scoped engagement or use one you already have:

```bash
python vm.py new "Example Assessment" --type company --industry logistics --mode quick
python vm.py intake example-assessment --objective "Assess whether customer demand is sufficient for a pilot" --approval-owner "Engagement owner"
```

Save a source you have the right to use as a local UTF-8 `.txt`, `.md`, `.csv`, or `.tsv` file. Preserve the source URL or other locator, and don't substitute an AI-generated summary for original evidence.

```bash
python vm.py research import example-assessment \
  --file /path/to/permitted-source.txt \
  --title "Quarterly industry bulletin" \
  --locator "https://publisher.example/industry/quarterly-bulletin" \
  --kind report --publisher "Publisher name"
```

The command returns `source_id` and a SHA-256 snapshot digest. The locator is a reference, **not** an instruction to fetch the URL. The bytes are copied to `engagements/<slug>/research/snapshots/`, which is ignored by Git.

Add an interpretation only when you can point to an exact passage in the captured source:

```bash
python vm.py research claim example-assessment \
  --source SRC-0001 \
  --text "The publisher reports an increase in customer inquiries" \
  --excerpt "exact phrase copied from source"
```

The excerpt must occur verbatim in the captured file. A match proves that the text exists in the snapshot, **not** that the statement is accurate. Claims remain explicitly unrated and unknown.

Generate a private working evidence brief and inspect source integrity:

```bash
python vm.py research audit example-assessment
python vm.py research brief example-assessment --question "What evidence exists about customer demand?"
```

The brief includes operator-written interpretations, exact excerpts, source IDs, locators and SHA-256 hashes, unresolved review questions, and a reproducible evidence version. It is not a finished commercial recommendation and cannot be published automatically.

## When new research arrives

Import new material under the **same locator**. If the captured content differs, Venture Method creates a separate source record and reports the earlier source's recorded dependents, including connected claims, decisions and evidence briefs.

Nothing is automatically declared superseded. Documents may change because of editorial corrections, formatting, or an entirely new publication. Human review must determine what changed and whether an old conclusion still holds.

`python vm.py research audit <engagement>` checks the journal, captured files, excerpt bindings, artifact hashes, and reports evidence briefs based on older snapshots as candidates for review. Existing drafts remain immutable. Creating a new brief produces a new source-linked version without rewriting the earlier one.

## Boundaries and limitations

- Only local plain UTF-8 text is accepted; maximum 512 KiB per captured file.
- Symlink source files and symlinked research directories are rejected. Files stay under one gitignored engagement.
- The publisher and locator fields are operator assertions. A source may be inaccurate, fabricated, or legally restricted despite passing hash and excerpt checks.
- The system does not verify publication rights or permission to redistribute a source. Never commit confidential sources or distribute captured third-party text without appropriate rights.
- It does not infer unsupported claims, conduct interviews, execute agents, or make outbound network calls.
- Journal and content hashes are tamper-*evident relative to recorded state*, not independently signed audit evidence. Local single-writer assumptions still apply.
- Evidence briefs need human assessment for relevance, source independence, quantitative accuracy, contradictory evidence and consequent recommendations.

## Restricted public HTTPS capture

You can retrieve **one public HTML or plain UTF-8 source at a time** when you explicitly authorize its exact hostname:

```bash
python vm.py research fetch example-assessment \
  --url 'https://www.example.org/public-report' \
  --allow-host www.example.org \
  --title 'Published research report' \
  --publisher 'Publisher claimed on page'
```

The adapter refuses HTTP, wildcard hosts, IP-literal URLs, private or mixed private/public DNS responses, credentials, unapproved ports, redirects, compressed responses, unsupported MIME types, oversized content and non-UTF-8 input. It connects to the validated public IP through TLS with certificate checking. It never crawls linked pages or sends cookies and browser credentials.

Both the original response bytes and the extracted text are preserved inside the private engagement, with separate hashes. `research audit` detects changes to either copy. HTML extraction is basic; it is not a JavaScript browser, general PDF parser, or publisher authentication system. TLS confirms the server connection, **not the truth of the content**. No actual publication rights are inferred.

Security tests exercise DNS and transport using mocked responses. A separate live-network compatibility test and independent security review are still needed before broad deployment. This is an operator-initiated read, never autonomous crawling.

## Independent comparative research review

Produce two Markdown research reports about the same question (for example, a manual baseline and a framework-assisted version), then prepare anonymous A/B packets:

```bash
python vm.py research-benchmark prepare \
  --engagement example-assessment \
  --baseline /path/to/baseline.md \
  --candidate /path/to/candidate.md \
  --question 'Is the evidence sufficient to justify a limited pilot?'
```

Share **A.md, B.md, review.json** with the independent reviewer, but keep **key.json** out of their view until they have completed the scores. The scoring dimensions are source fidelity, reasoning, alternatives, decision usefulness, uncertainty, quantitative rigor and practicality. The reviewer supplies 0–4 scores and written explanations.

```bash
python vm.py research-benchmark summarize \
  --workspace engagements/example-assessment/benchmarks/comparison-<id>
```

The default result is `incomplete`. The tool cannot run the baseline or candidate model, fabricate timings, enforce reviewer anonymity, authenticate a reviewer, or declare the winner before a review. Scores are human assessments, not independent proof of factual correctness.
