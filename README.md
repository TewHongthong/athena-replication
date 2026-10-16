# Athena: replication package

Code, benchmark and recorded results for the manuscript *Athena: Ontology-Guided Rule Retrieval and Mechanical
Validation for User-Defined Coding Standards with Large Language Models*. The package contains the pipeline evaluated
in the paper (ontology, rule retriever, prompt builder, output validator), the evaluation harness, the benchmark, every
recorded trial of the reported runs, and the analyses added after the pre-registered protocol. Every number in the
results tables can be recomputed from the recorded trials without calling any model.

## Layout

```
README.md  LICENSE  LICENSE-DATA.md  THIRD_PARTY_NOTICES.md  CHECKSUMS.sha256

athena-sim/                      evaluation harness, recorded runs and analyses (Python 3.9+)
  -- harness --------------------------------------------------------------------------------------
  athena_sim.py                  command line: run / report / prompts / show / packs / freeze
  athena/                        ontology, packs, retrieval (conditions none, fulldoc, chunk, graph, graph_noex),
                                 prompts, LLM clients, evaluation, reports, freeze
  vendor/output_validator.py     mechanical naming / comment rule checker
  packs/gscs/                    case-study standard: extracted rules, ontology, 18 seeds, benchmark units
  tests/                         unit and end-to-end tests (no key, no network)
  run_all.py                     driver of the o3-mini and GPT-6 Luna runs
  HYPOTHESES.md                  hypotheses and analysis plan written before any model was called
  -- main experiment (case study GSCS, public standards) ---------------------------------------------
  frozen/                        frozen configurations and run ledgers of the reported test runs
  runs/<run_id>/                 config.json, trials.jsonl (every prompt, raw answer and metric), trials.csv, summary.md
  -- further experiments, each with its own frozen files, runs and analysis ------------------------
  ablation_noex/                 rule selection without the few-shot examples (condition graph_noex)
  p5_extra/                      public-standard renaming with three further models
  -- exploratory analyses of the recorded trials (each folder has an ADDENDUM.md written before scoring) --
  semantic_check/                compile-and-run check of every applied rename on the case-study programs
  scope_check/                   scope-aware name-conflict check of the applied renames
  judge_rubric/                  rubric rating of generated comments by two LLM judges
  judge_rubric_mask/             the same rating with author/date label values masked (sensitivity)
  lookup_check/                  graph retrieval compared with a flat lookup table
  phase5_stats/                  cluster-bootstrap intervals; collision / rename-safe accounting
  phase9_stats/                  retrieval load, Similarity Index and invalid answers, MUST-only sensitivity,
                                 repository-level bootstrap
  phase10_stats/                 program-level paired tests, behaviour-check accounting
  review_e/                      identifier kind inferred without the original name, constant-prefix and
                                 further robustness analyses (K1, K2, K4, K5)

athena-corpus/                   public-standards benchmark
  corpus/                        792 source files from 40 public repositories (MIT or Apache-2.0, created after 2026-06-01)
  benchmark/                     500 snippets, 2,957 injected violations, 120 comment units, curation report
  curation/                      curation scripts, rule tables and the public-standards ontology (curation/pipeline/)
  corpus_repos.tsv, corpus_index.tsv   repository list with pinned commits; per-file index with git blob hashes
```

## Quick check (no API key)

```bash
cd athena-sim
python -m unittest discover -s tests          # 40 tests; 12 are skipped (see "Withheld material")
python athena_sim.py packs
python athena_sim.py show --pack gscs --condition graph          # the prompt an LLM receives
python athena_sim.py run --pack gscs --backend mock:oracle --conditions none,graph --per-language 0   # 100%
python athena_sim.py run --pack gscs --backend mock:echo   --conditions none,graph --per-language 0   # 0%
```

## Where each reported result comes from

Regenerate the summary of any run from its recorded trials with `python athena_sim.py report <run folder>`
(for example `runs/qwen_gscs_rename` or `ablation_noex/runs/abl_luna_rename`).

| Result in the paper | Run(s) or file |
|---|---|
| Identifier renaming, case study (GSCS), six LLMs x four conditions | `runs/test_o3mini_gscs_rename`, `runs/test_luna_gscs_rename`, `runs/gemini31fl_gscs_rename`, `runs/dsv4f_gscs_rename`, `runs/qwen_gscs_rename`, `runs/gemma4_gscs_rename` |
| Identifier renaming, five public standards, GPT-6 Luna | `runs/test_luna_p5_rename` |
| Identifier renaming, five public standards, three further models | `p5_extra/runs/p5x_*`, `p5_extra/analysis/results.md` |
| Comment structure | `runs/*_gscs_comment`, `runs/test_luna_p5_comment` |
| Rule-based fixer baseline (deterministic, no LLM) | `runs/test_autofix_gscs_rename`, `runs/test_autofix_gscs_comment` |
| Pipeline checks: developer comments as answers (oracle) and empty answers (echo) | `runs/cm_oracle`, `runs/cm_echo`, `ablation_noex/runs/mock_*` |
| Ablation: rule selection with and without examples | `ablation_noex/runs/abl_*`, `ablation_noex/analysis/results.md` |
| Graph retrieval compared with a flat lookup | `lookup_check/results.md`, `lookup_check/results_allmodels.md` |
| Compile-and-run check of renames | `semantic_check/results/semantic_summary.md` |
| Scope-aware name-conflict check | `scope_check/results/results.md` |
| Rubric rating of comment content | `judge_rubric/results/rubric_summary.md`; masked sensitivity `judge_rubric_mask/results/mask_summary.md` |
| Confidence intervals, collision and rename-safe accounting | `phase5_stats/results_ci.md`, `phase5_stats/results_collision.md` |
| Retrieval load, Similarity Index, MUST-only sensitivity, repository-level bootstrap | `phase9_stats/results.md` |
| Program-level paired tests, behaviour-check accounting | `phase10_stats/results.md` |
| Identifier kind inferred without the original name, constant prefix | `review_e/results.md`, `review_e/results2.md`, `review_e/k1_kinds.json`, `review_e/const_prefix.md` |

Each `summary.md` reports, per condition, the compliance rate with its Wilson 95% interval, exact match, Similarity
Index before and after renaming, collisions, tokens, latency and cost, followed by paired exact sign tests on per-unit
means with Holm correction. `trials.jsonl` holds one record per trial: unit, condition, repeat, prompt, raw answer,
parsed answer, token counts, latency and every metric.

Analysis scripts are run from their own folder, for example `cd athena-sim/phase5_stats && python -B phase5.py`,
`cd athena-sim/ablation_noex && python -B analyze_ablation.py`, `cd athena-sim/p5_extra && python -B analyze_p5_extra.py`.
Scripts that rebuild the full-document and chunk prompts of the case study (`ablation_noex/regression_check.py`,
`review_e/analyze2.py`, section 9.5 of `phase9_stats/phase9.py`) need the withheld GSCS document (see below).

## Models and settings of the reported runs

Hosted models were called through an OpenAI-compatible API; Qwen3.5-9B and the local Gemma 4 26B run were served
locally through an OpenAI-compatible server. Model identifiers are those recorded in each run's `config.json`. All
runs used the test split, three repeats per unit, and the frozen configuration stored next to the run.

| Model | Backend id | Temperature | Max output tokens | Switch (environment variable) |
|---|---|---|---|---|
| o3-mini | `openai:openai/o3-mini` | not sent (reasoning model) | 8,192 | none |
| GPT-6 Luna | `openai:openai/gpt-6-luna` | 0.2 | 8,192 | none |
| Gemini 3.1 Flash-Lite | `openai:google/gemini-3.1-flash-lite` | vendor default | 8,192 | `ATHENA_OMIT_TEMP=1` |
| DeepSeek V4 Flash | `openai:deepseek/deepseek-v4-flash` | vendor default | 8,192 | `ATHENA_OMIT_TEMP=1` |
| Qwen3.5-9B, Q4_K_M | `openai:Qwen3.5-9B-Q4_K_M` | 0.2 | 1,024 | `ATHENA_NO_THINK=1` (thinking off) |
| Gemma 4 26B-A4B, Q4_K_M (local) | `openai:gemma4:26b` | 0.2 | 2,048 | `ATHENA_EXTRA_BODY='{"reasoning_effort":"none"}'` (thinking off) |
| Gemma 4 26B-A4B (hosted, ablation and `p5_extra`) | `openai:google/gemma-4-26b-a4b-it` | 0.2 | 2,048 | `ATHENA_EXTRA_BODY='{"reasoning":{"effort":"none"}}'` |

`athena/llm.py` contains all switches (including `ATHENA_LOG_PROVIDER`, which appends the serving host to the logged
model id; the host names were removed from the recorded trials). Each switch is off unless its variable is set, so one
file reproduces every run. `athena/` is the version used for the ablation and `p5_extra` runs; it differs from the version used for the main runs only in `llm.py` (environment switches), `retrieval.py` (the new
condition `graph_noex`), `runner.py` and `report.py` (retrieval-hit bookkeeping and column order). All scoring code (`evaluate.py`, `prompts.py`, `packs.py`,
`vendor/output_validator.py`) is identical, and `ablation_noex/regression_check.py` and
`p5_extra/regression_check_p5.py` show that it regenerates the logged prompts of the earlier runs character for
character.

To call a model:

```bash
export OPENAI_BASE_URL=<your OpenAI-compatible endpoint>   # e.g. https://api.openai.com/v1
export OPENAI_API_KEY=<key>
python athena_sim.py run --pack gscs --task rename --backend openai:<model> --conditions none,graph \
       --per-language 0 --repeats 3 --split dev
```

The harness enforces the protocol of the study: tuning on the dev split, `freeze`, then one run on the test split
with `--frozen`. The files in `frozen/` record hashes of the code and data as they were when each test run started.
The edits described under "Anonymization" changed some of those files, so a new test run needs a new `freeze`, and is
a new run rather than a replay. `ablation_noex/run_ablation.py` and `p5_extra/run_p5_extra.py` are the drivers of the
two further experiments; they call the shared `athena_sim.py` one level up.

## Pre-registration and addenda

- `athena-sim/HYPOTHESES.md` (written before any model call; its hash is stored in every frozen file).
  H1 (confirmatory): on the case study, graph retrieval gives higher compliance than no standard. H2: graph above
  similarity-based chunk retrieval. H3: graph not worse than the full document. H4 (exploratory): graph keeps the
  data-type prefix more often than full document and chunk. H5 (exploratory): comment structure, graph above none.
  H6 (exploratory, GPT-6 Luna): on the public standards graph differs from none by at most +-5 points.
- Every analysis and experiment added after the freeze has an `ADDENDUM.md` written before its results were computed;
  all of them are exploratory.
- Runs not reported: besides the runs listed above, one attempted test run with another Gemini model stopped after 16
  trials on an API quota error; its results were not analysed.

## Withheld material

The case-study standard is an organization's internal document. Its text is not distributed. The package includes
the rules extracted from it (`packs/gscs/gscs_standard.json`, `packs/gscs/gscs_ontology.json`), the seeds and the
benchmark units. In the recorded trials, the document text inside full-document and chunk prompts is replaced by a
marker giving the length and SHA-256 prefix of the removed text, for example
`[GSCS document text withheld from the replication package: 7031 characters, sha256 ...]`; answers and metrics are
unchanged. Without the document, the harness runs the `none` and `graph` conditions on the case study; `fulldoc` and
`chunk` need the file `packs/gscs/gscs_source.txt`, and two tests that use it are skipped. The ten other skipped tests
need the tree-sitter library used during curation (`athena-corpus/curation/tools/build_treesitter.sh`).

## Anonymization

Local paths, host names and endpoint URLs were replaced (`<OPENAI_BASE_URL>`), the names of the serving and routing
services were removed from configuration records, notes and code comments, the serving host was removed from the
model identifier logged for each trial, and the judges' host-selection settings and per-call host field were removed
from the judge configuration and records. These edits do not change any prompt, answer or metric: every summary
regenerated from the cleaned trials matches the summary written when the run finished (the only difference is the
model identifier of the local Qwen run, which no longer contains a local file path). The compile-and-run summary, the
rubric summaries and the other analysis outputs are the files produced at analysis time.

## Requirements

- Harness, reports and tests: Python 3.9 or later, standard library only.
- Statistical re-analyses (`phase5_stats`, `phase9_stats`, `review_e`, `p5_extra/analyze_p5_extra.py`): numpy.
- Compile-and-run check (`semantic_check`, modes `prepare` and `run`): g++ (C++17), JDK 11 and Python 3; mode `report`
  needs only the cached results.
- Scope-aware check (`scope_check`): clang 18 (C++ AST), a JDK (Java), Python 3.
- Rubric judging (`judge_rubric/judge.py`, `judge_rubric_mask/judge.py`): an OpenAI-compatible endpoint in
  `JUDGE_BASE_URL` and a key in `JUDGE_API_KEY`.

## Licenses

Code: MIT (`LICENSE`). Ontologies, seeds, benchmark annotations and results: CC BY 4.0 (`LICENSE-DATA.md`). The files in
`athena-corpus/corpus/` and the code inside `athena-corpus/benchmark/` come from third-party repositories and remain
under their original licenses (`THIRD_PARTY_NOTICES.md`).
