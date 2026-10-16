# ADDENDUM — ablation `graph_noex` (revision plan Phase 3.1)

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
