# Hypotheses and analysis plan (written before running the real models)

Written before any LLM was called. This file is included in the `freeze` hash; if it is edited after a freeze, the test run is refused.
The aim is that results in which Athena wins (if it really wins) are protected against hindsight, and that results in which Athena does not win are reported just as completely.

*Translation note: the original of this file was written in Thai; this version is a wording-only English translation for the public replication package. No hypothesis, rule, number or procedure was changed. The hashes stored in `frozen/*.json` refer to earlier versions of this file (see README, "Anonymization"); the Thai original is in the git history.*

**Revision 1 (made before the freeze and before any test run):** the actual models and the scope under the budget were specified (plan A); see §2, §5 and §6. Before this revision, only a smoke test of 5 units on the dev split had been run, with o3-mini and gpt-6-luna, to check the pipeline and the cost. No run on the test split had been made and no test result had been looked at.

## 1. Data and split

| pack | dev (used for tuning) | test (used for reporting, once) |
|---|---|---|
| `gscs` (the standard in the docx, hand-written seed) | 6 snippets (`*_003`, `*_006` of Java/Python/C++): 58 rename, 6 comment | 12 snippets: 122 rename, 12 comment |
| `public5` (PEP 8, Google Java, .NET, Google TS, Airbnb JS) | ~30% of snippets (hash of the id, fixed) | the remaining ~70% |

The split is made by snippet (all violations of the same snippet fall on the same side) and was fixed before any model was run.

## 2. Hypotheses

The main model `openai:openai/o3-mini` (as in the pilot, called through a hosted API) is used on `gscs` only (H1-H5). The second model `openai:openai/gpt-6-luna` (through a hosted API, knowledge cutoff 2026-05-18, before the corpus cutoff date of 2026-06-01) is run on both `gscs` (replication, exploratory) and `public5` (H6), because of budget limits. No cross-model comparison is stated as a hypothesis. The main task is `rename`; the conditions compared are `none`, `fulldoc`, `chunk` and `graph` (= Athena, ontology-guided).
The primary metric is `core_ok` = the name proposed by the model passes every core rule for that language / identifier kind (unparseable = fail).

| # | Hypothesis | Status | Expected reason |
|---|---|---|---|
| H1 | `gscs` / test: `graph` has higher `core_ok` than `none` | **primary (confirmatory)** | GSCS is an organization-specific standard that the model cannot recall (prefixes `i_`, `f_`, `bln_`, suffix `_Type`); condition `none` receives no rules at all |
| H2 | `gscs` / test: `graph` has higher `core_ok` than `chunk` | secondary | chunk retrieves by lexical similarity and may pick the wrong section |
| H3 | `gscs` / test: `graph` is **not worse than** `fulldoc` (a clear win is not expected) | secondary | the document is very short (~1 page), so putting the whole document in the prompt should work well; the advantage of graph should lie in a shorter prompt (see tokens) |
| H4 | `gscs` / test: `graph` has higher `type prefix kept` than `fulldoc` and `chunk` | exploratory | the examples retrieved with each rule help choose the right prefix for the data type |
| H5 | `gscs` / test, `comment` task: `graph` has higher `structure ok` than `none` | exploratory | only 12 units, so the test has low power; reported as a case study |
| H6 | `public5` / test (model `gpt-6-luna`): `graph` **does not differ much** from `none` (expected difference of at most ±5 percentage points) | exploratory | the model already knows PEP 8 / Google style (ceiling effect) |

**If H3 does not hold** (graph clearly loses to fulldoc) or **H6 holds**, write it up accordingly: the ontology helps when the standard is organization-specific and when a short prompt is wanted;
it does not help correctness when the model already knows the standard.

## 3. Rules that apply in every case

- Report every condition and every metric in `summary.md`; do not drop units, do not drop languages, and do not change the checker after seeing test results.
- Results that cannot be parsed count as failures; trials with an API error are re-run until complete (not discarded).
- **The tuning budget is equal for all conditions**: every condition gets the same number of variants tried on dev (for example, if graph is tuned with `--examples` 0/1/2/3, chunk must be tuned with `--chunk-k` 1/2/3/5, and fulldoc with the same number of prompt wordings).
- What may be tuned on dev: `--examples`, `--top-k`, `--chunk-k`, the wording in `prompts.py` (the prompt structure must be identical across conditions), temperature / reasoning effort / max tokens.
- What must not be changed after seeing results: the seed and the split, the rules in the ontology, the `CORE` table, the rule checker, the metric definitions, and this list of hypotheses.
- If a bug in the simulator is found after the freeze: fix it, freeze again, re-run, and report both runs (the ledger keeps the history).
- Results on dev are not the main results of the paper; they are used only to describe the tuning process.

## 4. Analysis plan

- The unit of analysis is one unit (the mean of `--repeats` per unit); conditions are compared pairwise against `none` on the same unit with an exact two-sided sign test (equivalent to McNemar when repeats = 1), α = 0.05.
- The whole table is corrected for p-values with Holm; **only H1 is a confirmatory test**, and everything else is reported as secondary / exploratory.
- Report effect sizes (mean difference in percentage points) and the Wilson 95% CI of the rate per condition.
- Secondary metrics: `exact_match`, `type prefix kept`, collision, Similarity Index before/after, tokens and cost.
- Use `--repeats 3` to see the variance of the model.

## 5. Limitations that must be written in the paper

- The `gscs` seed and the GSCS ontology were written by the same person who designed the Sim, so there is a risk that the examples favor graph; others are advised to review the seed and the rules.
- Units in the same snippet are correlated (test has only 12 snippets), so p-values that treat units as independent are biased toward overconfidence.
- The `core_ok` checker checks the form of the prefix, not whether the data type is correct (hence `type prefix kept` as a secondary metric).
- The violations are injected artificially into short code; they are not real programmer mistakes.
- H1-H5 use o3-mini only (Luna replicates on GSCS, exploratory). H6 (public5) uses Luna only; o3-mini was not tested on public5 because of budget. Results for other models must be replicated; `public5` rename samples 20 units per language (fixed seed) from 2,157 test units; the models are called through a hosted API, so requests may be routed to different downstream providers.
- `none` is not the same as the "default documentation" of the original Athena.
- The `comment` task checks only the structure of the header.

## 6. Procedure

```bash
# A. Tune on dev (any number of rounds; the same budget for every condition)
python athena_sim.py run --pack gscs --backend openai:openai/o3-mini --split dev --per-language 0 --repeats 3 --run-id dev_v1

# B. When satisfied, freeze (use the same options that will be used for the test run)
python athena_sim.py freeze --pack gscs --backend openai:openai/o3-mini --per-language 0 --repeats 3 --out-file frozen_gscs_rename.json --note "describe what was tuned on dev"

# C. Run the test once
python athena_sim.py run --pack gscs --backend openai:openai/o3-mini --split test --per-language 0 --repeats 3 --frozen frozen_gscs_rename.json --run-id test_gscs_rename

# D. Repeat for --task comment and for --pack public5; keep frozen_*.json, *.ledger.jsonl and runs/ as evidence
# E. The actual runs of plan A were made through run_all.py (--base-url <OPENAI_BASE_URL> --max-tokens 8192 --repeats 3, public5 rename --per-language 20, no tuning on dev)
```

---

## ADDENDUM — ablation `graph_noex` (revision plan Phase 3.1)

Written before any LLM call in this folder. Post-hoc to the original freeze, so every result here is
exploratory. Motivation (review feedback): condition (iv) supplies the applicable rules *and* up to two examples per
rule, so the original design cannot separate the effect of rule selection from that of the few-shot examples.

## Harness
- `ablation_noex/` is a copy of `athena-sim/` so the original frozen runs stay verifiable. Differences:
  `retrieval.py` (new condition `graph_noex` = the graph block with no examples), `runner.py` (retrieval hit also for
  graph_noex), `report.py` (column order), `llm.py` = the Gemini/DeepSeek version (sha 257bc553…) plus two env-gated
  options: `ATHENA_EXTRA_BODY` (JSON merged into the request; used for hosted API provider/reasoning settings) and
  `ATHENA_LOG_PROVIDER=1` (serving provider appended to the logged model id). HYPOTHESES.md here = the original + this addendum.
- `regression_check.py` (run before this addendum): the four original conditions reproduce the logged o3-mini and
  GPT-6 Luna GSCS test prompts character for character; graph_noex = graph minus its example lines for all 134 test
  units → PASS (`regression_check.txt`). Mock checks on dev: oracle 100%, echo 0% under graph_noex.

## Design
- Pack GSCS, test split: rename 122 units, comment 12 units; 3 repeats; no tuning (dev used only for a 1-unit smoke test).
- Hosted models, conditions `graph` + `graph_noex` (graph re-run in the same run), settings identical to their original test runs:
  - o3-mini `openai/o3-mini` (reasoning model: no temperature), max_tokens 8192
  - GPT-6 Luna `openai/gpt-6-luna`, temperature 0.2, max_tokens 8192
  - Gemini 3.1 Flash-Lite `google/gemini-3.1-flash-lite`, temperature omitted (ATHENA_OMIT_TEMP=1), max_tokens 8192
- Gemma 4 26B A4B via a hosted OpenAI-compatible API `google/gemma-4-26b-a4b-it` (the local machine is not available), ALL five conditions
  (none, fulldoc, chunk, graph, graph_noex), because this serving (bf16 providers, reasoning effort "none") differs from
  the local 4-bit run: temperature 0.2, max_tokens 2048, `{"reasoning":{"effort":"none"}}`, serving provider logged. Reported as a separate configuration, not merged with the local run.
- All via a hosted OpenAI-compatible API, run by the author with `run_ablation.py` (budget guard $4).

## Comparisons (paired by unit, repeats averaged; exact two-sided sign test; Holm within each model × task)
- E, effect of examples: graph vs graph_noex (same run).
- S, effect of rule selection: graph_noex vs chunk and graph_noex vs fulldoc (none of the three has examples).
  Gemma via a hosted OpenAI-compatible API: within the same run. Hosted models: against chunk/fulldoc of their original frozen test runs
  (different run date — stated as a caveat).
- Also: graph_noex vs none; graph (re-run) vs graph (original) as run-to-run variation.
- Metrics: core-rule compliance (primary), type prefix kept (H4), exact match, Similarity Index; comment structure ok;
  input tokens, latency, cost. Failures counted as in Section 4.3.

## Expectations (stated before running)
- S > 0 on renaming for every model (graph_noex above chunk), because selection by identifier kind is what supplies
  the companion rules that chunk retrieval misses (Section 5.5).
- E small on core-rule compliance where graph is at ceiling, possibly larger on type prefix kept and exact match;
  on comments E may matter more for GPT-6 Luna (graph 100% vs full document 27.8%).
- Whatever the outcome, results are reported in full and RQ3 is revised to say which part of the gain comes from selection.
