# ADDENDUM — Phase 5 re-analysis (cluster bootstrap CIs; collision and rename-safe)

Written before computing anything in this folder. Post-hoc re-analysis of trials that already exist
(no model is called, no frozen file or score is changed). Everything here is exploratory.

## 5.1 Cluster bootstrap confidence intervals (review feedback B §6)
Wilson intervals treat the 3 repeats of a unit (and correlated units of one snippet) as independent trials.
- Statistic: rate of the primary metric = mean over units of the per-unit mean over its repeats (equals the pooled rate
  when every unit has 3 trials). Primary metric: core-rule compliance for renaming (unparsable answer = failure),
  comment structure ok for comments. Latest record per trial key (DeepSeek re-runs).
- Primary interval: **unit-level cluster bootstrap** — resample units with replacement (each with all its repeats),
  B = 10,000, percentile 95% interval, fixed seed 20261002.
- Sensitivity: **snippet-level cluster bootstrap** (resample snippets with all their units; GSCS has only 12 test
  snippets, so this interval is coarse).
- Degenerate cells (every resample equals the observed rate, i.e. all units at 100% or all at 0%): report the exact
  Clopper–Pearson 95% interval over units instead (k units fully compliant out of n), and say so in the caption.
- Scope: Table 2 (GSCS renaming, 6 LLMs × 4 conditions + rule-based fixer), Table 3 (Public5 renaming, Luna),
  Table 4 (comment structure), Table 6 (ablation, condition v) and CIs quoted in the text.
- Paired sign tests with Holm correction stay as they are. Check: does any conclusion that relies on CIs change?

## 5.2 Collision and rename-safe
- Collision as implemented (`athena/evaluate.py`): the proposed name differs from the injected and the original name
  and occurs as a whole word anywhere in the snippet (not scope-aware; also matches comments and strings), so it is
  an upper bound on real name clashes.
- Report collision rate and **rename-safe = core-rule compliant AND no collision** per model × condition
  (GSCS renaming, Public5 renaming, ablation runs).
- Cross-check against the compile/test results of `semantic_check/` (GSCS, 12 programs): how many behaviour-changing
  renames are flagged as collisions, and how many collisions left behaviour unchanged (false alarms of the
  scope-blind check).
