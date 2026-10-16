# ADDENDUM — Phase 9 re-analysis (review feedback C)

Written before running phase9.py. Post-hoc re-analysis of trials that already exist (no model is
called, no frozen file or score is changed). Everything here is exploratory / sensitivity analysis.
Disclosure: before this addendum, retrieved-item counts were looked at for two runs only
(o3-mini GSCS rename: graph 1, chunk 3; Luna Public5 rename: graph mean 1.37, chunk 3).

## 9.1 Retrieval load per condition (review C #6, #18)
- Per model x condition (GSCS, Public5, ablation; rename and comment): retrieved items per trial
  (`retrieval.n_items`: rules for graph/graph_noex, passages for chunk, 1 document for fulldoc) mean/min/max,
  and mean prompt tokens. Settings actually used, read from the frozen configs: top_k, chunk_k, examples,
  temperature, max_tokens, repeats.

## 9.2 Similarity Index and invalid answers (review C #4)
- Per model x condition (GSCS + Public5 rename): share of trials without a valid identifier (unparsable or invalid),
  SI (character) as reported = mean over all scored trials (invalid answer = code left unchanged = SI before repair),
  SI over valid answers only, and SI before repair. Check: no invalid trial can reach SI = 1.0.

## 9.3 MUST-only sensitivity of core-rule compliance (review C #3)
- Public5 (Luna) rename: recompute core-rule compliance with the same validator using only core rules whose
  ontology severity is MUST; units whose core set has no MUST rule are left out. Report per condition next to the
  recorded metric (all 52 core rules), and how many units are affected. GSCS: all 6 naming rules are MUST, so the
  confirmatory result is unaffected by construction (verify).

## 9.4 Repository-level cluster bootstrap (review C #10)
- Public5 (Luna), rename core_ok and comment structure ok: per-unit means as in Phase 5, then resample
  repositories (provenance.repo of the snippet) with replacement, B = 10,000, seed 20261003, percentile 95%.
  Also paired differences graph - none and graph - chunk (unit-level vs repository-level bootstrap).
  Check: does any conclusion change? (GSCS seeds are author-written, no repository level; snippet-level bootstrap
  from Phase 5 already covers it.)

## 9.5 Section-level retrieval hit of chunk retrieval on GSCS (added after 9.1–9.4 were computed)
Found while checking 9.1 against the code: on GSCS, conditions (ii) and (iii) use the standard's own document text
(`GscsPack.fulltext` = the source document; `GscsPack.chunks` = its 10 "## " sections), not the ontology's rule
renderings as on Public5, so on GSCS chunk retrieval returns 3 of 10 document sections and no retrieval hit was logged.
Before computing: for every GSCS chunk trial (6 models), a section hit = every source section of the unit's core naming
rule (ontology `sourceSection`, sub-section suffix " - ..." dropped, ";" = several sections) is among the 3 retrieved
sections. Report hit rate per model and core-rule compliance among hit and miss trials. Exploratory.
