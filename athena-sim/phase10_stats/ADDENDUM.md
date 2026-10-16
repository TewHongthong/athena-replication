# ADDENDUM — Phase 10 re-analysis (review feedback D)

Written before running phase10.py. Post-hoc, exploratory re-analysis of existing trials (no model is called,
no frozen file or score is changed). Disclosure: while answering the review, the program-level comparison graph vs none
(GSCS rename, 6 models) was already computed once: graph better on 12/12 programs for every model (p = 0.00049).

## 10.1 Program-level paired tests on GSCS (review D #2)
The 122 renaming units of the GSCS test split are nested in 12 programs (snippet_id). Per model and condition: unit
result = mean over repeats (unparsable = failure; latest record per trial key; API errors excluded as before); program
result = mean over its units. Paired exact two-sided sign test across the 12 programs.
- Main runs (6 models): (ii), (iii), (iv) vs (i), Holm within model (the registered family, now at program level);
  exploratory: (iv) vs (iii), (iv) vs (ii), raw p.
- Ablation runs (4 models): the same pairs as analyze_ablation.py (examples, selection vs chunk, selection vs full
  document, noex vs none, replication / graph vs none), Holm within model x task, program level.
- Comment units: check that each program holds exactly one comment unit (then unit- and program-level tests coincide).
The registered unit-level tests are kept as a sensitivity analysis.

## 10.2 Behaviour check accounting (review D #18)
From semantic_check/results/trial_results.csv: trials, applied renames, not applied (by reason where derivable),
distinct programs built and run.

## 10.3 Reproducibility facts (review D #7, #8, #16)
Similarity Index and comment similarity as implemented in athena/evaluate.py; model identifiers as requested from the
APIs and run dates from each run's config.json.
