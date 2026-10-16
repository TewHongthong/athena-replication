# Athena Sim summary

480 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

> Contains mock backends: **mock rows are deterministic stand-ins, not LLM results.**

Split: dev, test.

> **This report mixes dev and test trials. Do not quote the pooled numbers; report the splits separately.**

## comment - pack `public5`

### By condition and backend

| backend | condition | n | parsed | structure ok [95% CI] | labels present | labels filled | delimiter ok | similarity to reference | latency s | tokens in/out |
|---|---|---|---|---|---|---|---|---|---|---|
| mock:oracle | none | 120 | 100.0% | 86.1% [79-91] | - | - | 100.0% | 1.000 | 0.00 | 0/0 |
| mock:oracle | fulldoc | 120 | 100.0% | 86.1% [79-91] | - | - | 100.0% | 1.000 | 0.00 | 0/0 |
| mock:oracle | chunk | 120 | 100.0% | 86.1% [79-91] | - | - | 100.0% | 1.000 | 0.00 | 0/0 |
| mock:oracle | graph | 120 | 100.0% | 86.1% [79-91] | - | - | 100.0% | 1.000 | 0.00 | 0/0 |

### By language (structure ok; n in brackets)

| backend | condition | csharp | java | javascript | python | typescript |
|---|---|---|---|---|---|---|
| mock:oracle | none | 83.3% [30] | 45.0% [20] | 100.0% [5] | 100.0% [34] | 100.0% [26] |
| mock:oracle | fulldoc | 83.3% [30] | 45.0% [20] | 100.0% [5] | 100.0% [34] | 100.0% [26] |
| mock:oracle | chunk | 83.3% [30] | 45.0% [20] | 100.0% [5] | 100.0% [34] | 100.0% [26] |
| mock:oracle | graph | 83.3% [30] | 45.0% [20] | 100.0% [5] | 100.0% [34] | 100.0% [26] |

### Per-language, per-condition (comment_ok, delimiter_ok, vacuous-check share)

`vacuous (n_checks=0)` is the share of units whose applicable MUST comment rules have no mechanical check today (e.g. Python's plain-line-comment format, most Airbnb JS comment rules) -- comment_ok is trivially true for those regardless of what the model writes.

| backend | condition | language | n | comment_ok [95% CI] [n scored] | delimiter_ok | vacuous (n_checks=0) |
|---|---|---|---|---|---|---|
| mock:oracle | none | csharp | 30 | 83.3% [66-93] [30] | 100.0% | 0.0% |
| mock:oracle | none | java | 20 | 45.0% [26-66] [20] | 100.0% | 0.0% |
| mock:oracle | none | javascript | 6 | 100.0% [57-100] [5] | 100.0% | 100.0% |
| mock:oracle | none | python | 37 | 100.0% [90-100] [34] | 100.0% | 100.0% |
| mock:oracle | none | typescript | 27 | 100.0% [87-100] [26] | 100.0% | 3.7% |
| mock:oracle | fulldoc | csharp | 30 | 83.3% [66-93] [30] | 100.0% | 0.0% |
| mock:oracle | fulldoc | java | 20 | 45.0% [26-66] [20] | 100.0% | 0.0% |
| mock:oracle | fulldoc | javascript | 6 | 100.0% [57-100] [5] | 100.0% | 100.0% |
| mock:oracle | fulldoc | python | 37 | 100.0% [90-100] [34] | 100.0% | 100.0% |
| mock:oracle | fulldoc | typescript | 27 | 100.0% [87-100] [26] | 100.0% | 3.7% |
| mock:oracle | chunk | csharp | 30 | 83.3% [66-93] [30] | 100.0% | 0.0% |
| mock:oracle | chunk | java | 20 | 45.0% [26-66] [20] | 100.0% | 0.0% |
| mock:oracle | chunk | javascript | 6 | 100.0% [57-100] [5] | 100.0% | 100.0% |
| mock:oracle | chunk | python | 37 | 100.0% [90-100] [34] | 100.0% | 100.0% |
| mock:oracle | chunk | typescript | 27 | 100.0% [87-100] [26] | 100.0% | 3.7% |
| mock:oracle | graph | csharp | 30 | 83.3% [66-93] [30] | 100.0% | 0.0% |
| mock:oracle | graph | java | 20 | 45.0% [26-66] [20] | 100.0% | 0.0% |
| mock:oracle | graph | javascript | 6 | 100.0% [57-100] [5] | 100.0% | 100.0% |
| mock:oracle | graph | python | 37 | 100.0% [90-100] [34] | 100.0% | 100.0% |
| mock:oracle | graph | typescript | 27 | 100.0% [87-100] [26] | 100.0% | 3.7% |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| mock:oracle | fulldoc vs none | comment_ok | 115 | 0 | 0 | 115 | +0.0 | 1 | 1 |
| mock:oracle | chunk vs none | comment_ok | 115 | 0 | 0 | 115 | +0.0 | 1 | 1 |
| mock:oracle | graph vs none | comment_ok | 115 | 0 | 0 | 115 | +0.0 | 1 | 1 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
