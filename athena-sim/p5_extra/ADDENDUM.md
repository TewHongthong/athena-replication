# ADDENDUM — Public5 renaming with further models (review feedback, reviewer 3 item 4)

Written before any LLM call in this folder. Post-hoc to the original freeze, so every result
here is exploratory. Motivation: the public-standard result (H6, ceiling effect) rests on one model, GPT-6 Luna.

## Design (no dev tuning; nothing changed after seeing results)
- Pack public5, task rename, test split, the same 100 units as the frozen GPT-6 Luna run (--per-language 20,
  --seed 42), conditions none, fulldoc, chunk, graph, 3 repeats -> 1,200 trials per model. Comments are not run
  (their content would need the LLM-judge rubric again).
- Models, in priority order, each with the settings of its own earlier test run:
  1. Gemini 3.1 Flash-Lite (google/gemini-3.1-flash-lite): temperature omitted (vendor default, ATHENA_OMIT_TEMP=1),
     max_tokens 8192, as in gemini31fl/.
  2. Gemma 4 26B A4B served through the same endpoint as the hosted models (google/gemma-4-26b-a4b-it):
     temperature 0.2, max_tokens 2048, reasoning off and bf16 providers only (ATHENA_EXTRA_BODY), as in the
     ablation run (not the local 4-bit run).
  3. DeepSeek V4 Flash (deepseek/deepseek-v4-flash, 0423 snapshot): temperature omitted, max_tokens 8192,
     provider-default reasoning, as in dsv4f_v2/.
- Harness: copy of ablation_noex/ (athena/, athena_sim.py, vendor/). regression_check_p5.py: the sampled units equal
  the 100 units of the Luna run and the prompts of all four conditions equal the logged Luna prompts character for
  character (1,200/1,200) -> PASS (regression_check_p5.txt). HYPOTHESES.md here = the original + this addendum.
- Per model: 1-unit smoke test on the dev split, then freeze, then the test split once (run_p5_extra.py).

## Expectations (H6-style, stated before the runs)
- E1 (Gemini, Gemma): core-rule compliance without the standard is at least 95%, and graph differs from none by at
  most 5 percentage points.
- E2 (DeepSeek): on GSCS this model often returned no valid answer without the standard (43.4% of trials), so
  overall compliance under none may be lower for that reason alone. The expectation is stated on valid answers:
  compliance among valid answers under none is at least 95%, and graph differs from none by at most 5 points on
  valid answers. A larger gap in overall compliance driven by invalid answers is reported as such.

## Analysis (analyze_p5_extra.py, written before the runs; GPT-6 Luna recomputed from ../runs/test_luna_p5_rename)
- Per model x condition: trials; valid answers %; core-rule compliance % (invalid = failure) with a unit-level
  cluster-bootstrap 95% CI (B = 10,000, seed 20261002; exact Clopper-Pearson over units when every unit complies);
  compliance among valid answers; exact match; collision-screened compliance; Similarity Index (character) after.
- Per model: paired exact two-sided sign tests on per-unit means over the 3 repeats, graph vs none, fulldoc and
  chunk, Holm within model (3 tests). Unit-level, as for the public standards in the paper.
- Per language core-rule compliance (descriptive). All models and conditions are reported, whatever the outcome.
- Checks before any LLM call: run_p5_extra.py --dry-run shows the plan; a mock:oracle run on the dev split (4 units,
  written outside this folder) scores 20/20; analyze_p5_extra.py reproduces Table 3 of the paper from the frozen
  Luna run (99.7 [99–100], 100.0† [96–100], 99.0 [97–100], 100.0† [96–100]; collision-screened 98.0–99.0).
