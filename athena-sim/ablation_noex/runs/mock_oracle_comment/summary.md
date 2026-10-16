# Athena Sim summary

30 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

> Contains mock backends: **mock rows are deterministic stand-ins, not LLM results.**

Split: dev.

## comment - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | structure ok [95% CI] | labels present | labels filled | delimiter ok | similarity to reference | latency s | tokens in/out |
|---|---|---|---|---|---|---|---|---|---|---|
| mock:oracle | none | 6 | 100.0% | 100.0% [61-100] | 100.0% | 100.0% | 100.0% | 1.000 | 0.00 | 0/0 |
| mock:oracle | fulldoc | 6 | 100.0% | 100.0% [61-100] | 100.0% | 100.0% | 100.0% | 1.000 | 0.00 | 0/0 |
| mock:oracle | chunk | 6 | 100.0% | 100.0% [61-100] | 100.0% | 100.0% | 100.0% | 1.000 | 0.00 | 0/0 |
| mock:oracle | graph | 6 | 100.0% | 100.0% [61-100] | 100.0% | 100.0% | 100.0% | 1.000 | 0.00 | 0/0 |
| mock:oracle | graph_noex | 6 | 100.0% | 100.0% [61-100] | 100.0% | 100.0% | 100.0% | 1.000 | 0.00 | 0/0 |

### By language (structure ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| mock:oracle | none | 100.0% [2] | 100.0% [2] | 100.0% [2] |
| mock:oracle | fulldoc | 100.0% [2] | 100.0% [2] | 100.0% [2] |
| mock:oracle | chunk | 100.0% [2] | 100.0% [2] | 100.0% [2] |
| mock:oracle | graph | 100.0% [2] | 100.0% [2] | 100.0% [2] |
| mock:oracle | graph_noex | 100.0% [2] | 100.0% [2] | 100.0% [2] |

### Per-language, per-condition (comment_ok, delimiter_ok, vacuous-check share)

`vacuous (n_checks=0)` is the share of units whose applicable MUST comment rules have no mechanical check today (e.g. Python's plain-line-comment format, most Airbnb JS comment rules) -- comment_ok is trivially true for those regardless of what the model writes.

| backend | condition | language | n | comment_ok [95% CI] [n scored] | delimiter_ok | vacuous (n_checks=0) |
|---|---|---|---|---|---|---|
| mock:oracle | none | cpp | 2 | 100.0% [34-100] [2] | 100.0% | 100.0% |
| mock:oracle | none | java | 2 | 100.0% [34-100] [2] | 100.0% | 100.0% |
| mock:oracle | none | python | 2 | 100.0% [34-100] [2] | 100.0% | 100.0% |
| mock:oracle | fulldoc | cpp | 2 | 100.0% [34-100] [2] | 100.0% | 100.0% |
| mock:oracle | fulldoc | java | 2 | 100.0% [34-100] [2] | 100.0% | 100.0% |
| mock:oracle | fulldoc | python | 2 | 100.0% [34-100] [2] | 100.0% | 100.0% |
| mock:oracle | chunk | cpp | 2 | 100.0% [34-100] [2] | 100.0% | 100.0% |
| mock:oracle | chunk | java | 2 | 100.0% [34-100] [2] | 100.0% | 100.0% |
| mock:oracle | chunk | python | 2 | 100.0% [34-100] [2] | 100.0% | 100.0% |
| mock:oracle | graph | cpp | 2 | 100.0% [34-100] [2] | 100.0% | 100.0% |
| mock:oracle | graph | java | 2 | 100.0% [34-100] [2] | 100.0% | 100.0% |
| mock:oracle | graph | python | 2 | 100.0% [34-100] [2] | 100.0% | 100.0% |
| mock:oracle | graph_noex | cpp | 2 | 100.0% [34-100] [2] | 100.0% | 100.0% |
| mock:oracle | graph_noex | java | 2 | 100.0% [34-100] [2] | 100.0% | 100.0% |
| mock:oracle | graph_noex | python | 2 | 100.0% [34-100] [2] | 100.0% | 100.0% |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| mock:oracle | fulldoc vs none | comment_ok | 6 | 0 | 0 | 6 | +0.0 | 1 | 1 |
| mock:oracle | chunk vs none | comment_ok | 6 | 0 | 0 | 6 | +0.0 | 1 | 1 |
| mock:oracle | graph vs none | comment_ok | 6 | 0 | 0 | 6 | +0.0 | 1 | 1 |
| mock:oracle | graph_noex vs none | comment_ok | 6 | 0 | 0 | 6 | +0.0 | 1 | 1 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
