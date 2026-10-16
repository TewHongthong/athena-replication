# Data license

The following material created for this study is licensed under the Creative Commons Attribution 4.0 International
License (CC BY 4.0, https://creativecommons.org/licenses/by/4.0/legalcode):

- the coding-standard ontologies and rule tables (`athena-corpus/curation/pipeline/athena_ontology.json`,
  `athena-corpus/curation/rules.py` rule data, `athena-sim/packs/gscs/gscs_standard.json`,
  `athena-sim/packs/gscs/gscs_ontology.json`);
- the case-study seed programs and units (`athena-sim/packs/gscs/`);
- the benchmark annotations: snippet boundaries, target identifiers, injected violations, comment-unit metadata
  (`athena-corpus/benchmark/`);
- the recorded trials, summaries, judge ratings and analysis results (`athena-sim/runs/`, `athena-sim/frozen/`, and the
  run, result and analysis folders of `ablation_noex`, `p5_extra`, `semantic_check`, `scope_check`, `judge_rubric`,
  `judge_rubric_mask`, `lookup_check`, `phase5_stats`, `phase9_stats`, `phase10_stats` and `review_e`).

Rules in the ontologies paraphrase the public style guides they cite (PEP 8, Google Java and TypeScript style guides,
.NET naming guidelines, Airbnb JavaScript Style Guide); those guides remain under their own terms.

Source code taken from third-party repositories (`athena-corpus/corpus/` and the code fields inside
`athena-corpus/benchmark/`) is not covered by this license; see `THIRD_PARTY_NOTICES.md`.

Model outputs recorded in `trials.jsonl` and in the judge records are included for verification of the reported
results.
