# Live host comparison protocol

Use \`scenarios.json\` as the published canonical task set, then supply real sanitized project artifacts and permission manifest per run. Preserve two independent host runtimes and versions. For each case, run the same task with an isolated baseline and with a pinned Venture Method skill; no shared agent memory or transcript between arms.

Write \`runs.json\` with \`schema_version\`, \`host_runtimes\` (two actual runtime names), \`executor_ids\`, and \`cases\`. Every case lists \`id\`, \`baseline_branch\` (A or B), and runs A/B with \`runtime\`, \`model\`, \`version\`, \`executor_id\`, \`input_sha256\`, \`output_sha256\`. Keep raw outputs at \`<case>/A/response.md\` and \`<case>/B/response.md\`. A blinded independent reviewer must score both arms in \`review.json\` under \`ratings[case][A|B]\` on integer 0..4 for \`accuracy\`, \`usefulness\`, \`method_fidelity\`, \`traceability\`, \`authority\`, \`efficiency\`. Reviewer ID must differ from the named run executors.

Run \`python -m src.va.portable_eval PATH\` for structural checks and a quantitative paired summary. A complete structure is not authenticated empirical evidence. Publish no confidential host material; if a user authorizes publication, strip identifying information and archive permission details securely.

Gate requires an average improvement >=0.5 rubric points, no accuracy or authority regression in any case, and independent review of actual transcripts. These are provisional thresholds subject to expert sign-off. Avoid presenting any generated fixture as a real-world benchmark.
