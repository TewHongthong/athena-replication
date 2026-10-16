# Addendum (post-freeze, exploratory): rubric rating of generated comments (RQ2, part A)

Written after all frozen comment runs finished and before any judge was run.
Not part of the frozen HYPOTHESES.md; exploratory; re-scores existing outputs only (no generator is called again).
No human rater is used (advisor recommendation): two open-weight LLMs act as judges.

## Items
- GSCS test, 12 units: comments from o3-mini, GPT-6 Luna, Qwen3.5-9B, Gemini 3.1 Flash-Lite, DeepSeek V4 Flash,
  Gemma 4 26B (4 conditions x 3 repeats = 144 trials each), the linter-autofix baseline (floor anchor) and the
  12 seed reference comments (ceiling anchor).
- Public5 test, 89 units: GPT-6 Luna comments (1,068 trials) and the 89 developer-written reference comments.
- Trials without a parsable comment are not sent to the judges; they score 1 on every criterion in the
  all-trials analysis (consistent with "unanswered counts as failure") and are excluded in the answered-only analysis.
- Identical comment texts for the same unit are judged once and the score is shared.
- Blinding: the judge sees the language, element kind and name, the applicable comment rules, the code without its
  comment and the comment. It never sees the model, the condition, or whether the item is a reference or baseline.
  Items are shuffled with a fixed seed (20261001).

## Rubric (each criterion 1-5; anchors are in the judge prompt, judge.py)
1. accuracy: everything the comment says is true of the code; nothing invented.
2. completeness: purpose, each parameter, return value and thrown exceptions that the code has and the rules require.
3. clarity: concise, readable and informative rather than restating the code or the name.
4. conformance: the applicable rules followed beyond syntax: required elements/labels present and filled with
   meaningful content, right comment style. Labels whose content cannot be known from the code (author, dates,
   revision history) may hold placeholders without penalty.
Overall = mean of the four criteria.

## Judges and settings
- Judge 1: Gemma 4 26B (gemma4:26b). Judge 2: Qwen3.8-27B (UD-Q4_K_M GGUF). Both served locally.
- temperature 0, seed 0, thinking disabled, context 8,192 tokens, at most 400 output tokens, JSON output.
- Each item is rated once per judge. Unparsable judge output: one retry; if still unparsable, recorded as missing
  and reported.

## Known bias and how it is handled
Gemma 4 26B is also one of the generators, and Qwen3.8-27B shares a family with the Qwen3.5-9B generator
(self-preference risk). The main comparison is between conditions WITHIN one generator, where a judge's preference
for a generator applies equally to all four conditions. Sensitivity analysis: for Gemma 4 26B outputs use only the
Qwen judge, and for Qwen3.5-9B outputs use only the Gemma judge; report whether conclusions change.

## Validity checks (reported, decided before judging)
- Agreement between judges on unique items: quadratic-weighted Cohen's kappa per criterion, exact and within-1 agreement.
- Discrimination: reference comments must score higher overall than the linter-autofix floor (empty template).
  If they do not, the judges are reported as unable to discriminate and the rubric results are not interpreted.

## Analysis
- Per model x condition: mean of the two judges per criterion and overall, all trials and answered only.
- Exact two-sided sign test on per-unit means of the overall score: graph vs none and graph vs fulldoc for each
  GSCS model (12 tests) and for Luna on Public5 (2 tests); Holm correction across these 14 tests.
- GSCS has 12 units only, so its tests have low power; all results are exploratory.

## Frozen before any judge call
Pipeline smoke-tested with a deterministic mock judge outside the results folder (no real judge output exists yet). 1,962 unique items from 2,177 rows; 22 rows have no parsable comment.
```
f4ce8f4cc7747de0  build_items.py
2ca5e1191eb25a2a  items.jsonl
9b3f8078692887fa  item_map.jsonl
2d2db08793b8eeca  judge.py
58c4e7ad15c03822  aggregate.py
```
judges.json is not hashed because the Qwen model tag is filled in after download; the settings in it must stay as written (temperature 0, seed 0, num_ctx 8192, num_predict 400, think false).

## Revision before any judge call
Judges replaced to remove self-preference: Gemma 4 26B is a generator and Qwen3.8-27B shares the Qwen3.5-9B generator's family.
- Judge 1: IBM Granite 4.2 30B, local model tag granite4.2:30b-q4_K_M (released 25 Aug 2026, Apache 2.0, built on IBM's Granite 4.0).
- Judge 2: Meta Muse Glimmer 30B, local model tag muse-glimmer:30b-q4_K_M (released 10 Aug 2026, Apache 2.0, distilled from Meta's larger Muse model);
  system prompt "Reasoning strength: low" (the vendor's reasoning control); the think flag is dropped automatically if the model rejects it.
- Neither judge shares a provider or family with the six generators (OpenAI, Google/Gemma, DeepSeek, Qwen). Both were trained partly on
  synthetic data from undisclosed sources, so indirect influence from generator families cannot be fully excluded (stated as a limitation).
- The self-family sensitivity analysis is no longer needed; aggregate.py skips it automatically when no judge family matches a generator.
- num_ctx 8192 -> 4096 so a 30B Q4 model fits in 20 GB VRAM; the longest prompt is about 1,900 tokens plus at most 400 output tokens.
  If the local server shows partial CPU offload, the quantization may be lowered (e.g. Granite q4_K_S) before the full run; the tag actually used
  is recorded in results/judge_<key>_info.json.
- Unchanged: rubric, prompt, items, blinding, temperature 0, seed 0, num_predict 400, analysis plan, validity checks.
- judge.py now supports an optional system message per judge; tested with a mock HTTP layer (request bodies, think fallback, parsing).
```
07f9c2012ccbf93b  judge.py
2625a368852a8fa0  aggregate.py
19ca50d3a6520639  judges.json
4cda183b20520962  run_all.cmd
2ca5e1191eb25a2a  items.jsonl
9b3f8078692887fa  item_map.jsonl
```

## Revision 2 before any judge call
Local hosting failed (the local machine ran out of disk space while downloading). Judges moved to a hosted API (budget USD 10).
Granite 4.2 30B is not offered by the hosted API, so it is replaced.
- Judge 1: Meta Muse Glimmer 30B, `meta/muse-glimmer-30b`, pinned to a single host serving bf16 weights, no fallback;
  reasoning effort low, excluded from the reply; max_tokens 2000 because reasoning tokens count toward the output budget; seed 0.
  The "Reasoning strength: low" system prompt of revision 1 is not used (the API's reasoning parameter replaces it).
- Judge 2: Anthropic Claude Haiku 4.5, `anthropic/claude-haiku-4.5`, provider Anthropic (other hosts of the same model allowed
  as fallback); no reasoning; max_tokens 400; the API takes no seed.
- Neither shares a provider or family with the six generators. Muse Glimmer is open-weight; Haiku 4.5 is a versioned closed model.
- Output constrained by a strict JSON schema; the 1-5 range is still checked by parse().
- Cost recorded per call; caps USD 2.5 (Muse) and USD 5.0 (Haiku). Estimated total about USD 4-5.
- Unchanged: prompt (rendering verified byte-identical for all 1,962 items), items, rubric, temperature 0, analysis plan.
- Tested with a fake HTTP layer: request bodies, 429 backoff, resume, cost cap, fatal stop on HTTP 402 / missing API key.
```
1b18ec66b773c653  judge.py
054479dc700386d2  judges.json
ef59f5244fa02e93  run_all.cmd
2625a368852a8fa0  aggregate.py
2ca5e1191eb25a2a  items.jsonl
9b3f8078692887fa  item_map.jsonl
```

## Revision before any judge call: hosted API
Local serving was abandoned: the local machine ran out of disk space while downloading the first model, and no judge output was produced.
Judges are now called through a hosted API (budget USD 10):
- `muse`: Meta Muse Glimmer 30B (`meta/muse-glimmer-30b`), pinned to a single host serving bf16 weights with no fallback, reasoning effort low
  with reasoning text excluded, max_tokens 2000 (room for reasoning tokens), seed 0. The system prompt "Reasoning strength: low" is
  no longer sent; the API's reasoning parameter is used instead.
- `haiku`: Anthropic Claude Haiku 4.5 (`anthropic/claude-haiku-4.5`), Anthropic first with fallback to other hosts of the same model,
  max_tokens 400, no seed (not supported). Closed-weight: reproducibility rests on the pinned model id (limitation).
- Granite 4.2 30B is not offered by the hosted API, so it was replaced by Haiku. Neither judge shares a family with the six generators.
- Output: strict JSON schema (scores as enum 1-5); if a provider rejects the schema, that judge falls back to JSON mode; the format used,
  the serving provider, the served model and the cost are recorded per call.
- Prompt and items unchanged: all 1,962 prompts verified byte-identical to the frozen judge.py. temperature 0. Cost caps per judge:
  USD 3 (muse), USD 5 (haiku). 8 parallel requests; rate-limit and server errors retried with backoff.
- Tested with a mocked HTTP layer: request bodies and headers, 429 retry, schema fallback, cost-cap stop, resume, parallel writes.
```
3ce4f634b2a42116  judge.py
2625a368852a8fa0  aggregate.py
c172906be8855bf2  judges.json
d7e4672a0ce7814b  run_all.cmd
2ca5e1191eb25a2a  items.jsonl
9b3f8078692887fa  item_map.jsonl
```
