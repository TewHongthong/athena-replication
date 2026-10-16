# Athena Sim summary

480 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

> Contains mock backends: **mock rows are deterministic stand-ins, not LLM results.**

Split: dev, test.

> **This report mixes dev and test trials. Do not quote the pooled numbers; report the splits separately.**

## comment - pack `public5`

### By condition and backend

| backend | condition | n | parsed | structure ok [95% CI] | labels present | labels filled | delimiter ok | similarity to reference | latency s | tokens in/out |
|---|---|---|---|---|---|---|---|---|---|---|
| mock:echo | none | 120 | 100.0% | 33.9% [26-43] | - | - | 100.0% | 0.110 | 0.00 | 0/0 |
| mock:echo | fulldoc | 120 | 100.0% | 33.9% [26-43] | - | - | 100.0% | 0.110 | 0.00 | 0/0 |
| mock:echo | chunk | 120 | 100.0% | 33.9% [26-43] | - | - | 100.0% | 0.110 | 0.00 | 0/0 |
| mock:echo | graph | 120 | 100.0% | 33.9% [26-43] | - | - | 100.0% | 0.110 | 0.00 | 0/0 |

### By language (structure ok; n in brackets)

| backend | condition | csharp | java | javascript | python | typescript |
|---|---|---|---|---|---|---|
| mock:echo | none | 0.0% [30] | 0.0% [20] | 100.0% [5] | 100.0% [34] | 0.0% [26] |
| mock:echo | fulldoc | 0.0% [30] | 0.0% [20] | 100.0% [5] | 100.0% [34] | 0.0% [26] |
| mock:echo | chunk | 0.0% [30] | 0.0% [20] | 100.0% [5] | 100.0% [34] | 0.0% [26] |
| mock:echo | graph | 0.0% [30] | 0.0% [20] | 100.0% [5] | 100.0% [34] | 0.0% [26] |

### Per-language, per-condition (comment_ok, delimiter_ok, vacuous-check share)

`vacuous (n_checks=0)` is the share of units whose applicable MUST comment rules have no mechanical check today (e.g. Python's plain-line-comment format, most Airbnb JS comment rules) -- comment_ok is trivially true for those regardless of what the model writes.

| backend | condition | language | n | comment_ok [95% CI] [n scored] | delimiter_ok | vacuous (n_checks=0) |
|---|---|---|---|---|---|---|
| mock:echo | none | csharp | 30 | 0.0% [0-11] [30] | 100.0% | 0.0% |
| mock:echo | none | java | 20 | 0.0% [0-16] [20] | 100.0% | 0.0% |
| mock:echo | none | javascript | 6 | 100.0% [57-100] [5] | 100.0% | 100.0% |
| mock:echo | none | python | 37 | 100.0% [90-100] [34] | 100.0% | 100.0% |
| mock:echo | none | typescript | 27 | 0.0% [0-13] [26] | 100.0% | 3.7% |
| mock:echo | fulldoc | csharp | 30 | 0.0% [0-11] [30] | 100.0% | 0.0% |
| mock:echo | fulldoc | java | 20 | 0.0% [0-16] [20] | 100.0% | 0.0% |
| mock:echo | fulldoc | javascript | 6 | 100.0% [57-100] [5] | 100.0% | 100.0% |
| mock:echo | fulldoc | python | 37 | 100.0% [90-100] [34] | 100.0% | 100.0% |
| mock:echo | fulldoc | typescript | 27 | 0.0% [0-13] [26] | 100.0% | 3.7% |
| mock:echo | chunk | csharp | 30 | 0.0% [0-11] [30] | 100.0% | 0.0% |
| mock:echo | chunk | java | 20 | 0.0% [0-16] [20] | 100.0% | 0.0% |
| mock:echo | chunk | javascript | 6 | 100.0% [57-100] [5] | 100.0% | 100.0% |
| mock:echo | chunk | python | 37 | 100.0% [90-100] [34] | 100.0% | 100.0% |
| mock:echo | chunk | typescript | 27 | 0.0% [0-13] [26] | 100.0% | 3.7% |
| mock:echo | graph | csharp | 30 | 0.0% [0-11] [30] | 100.0% | 0.0% |
| mock:echo | graph | java | 20 | 0.0% [0-16] [20] | 100.0% | 0.0% |
| mock:echo | graph | javascript | 6 | 100.0% [57-100] [5] | 100.0% | 100.0% |
| mock:echo | graph | python | 37 | 100.0% [90-100] [34] | 100.0% | 100.0% |
| mock:echo | graph | typescript | 27 | 0.0% [0-13] [26] | 100.0% | 3.7% |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| mock:echo | fulldoc vs none | comment_ok | 115 | 0 | 0 | 115 | +0.0 | 1 | 1 |
| mock:echo | chunk vs none | comment_ok | 115 | 0 | 0 | 115 | +0.0 | 1 | 1 |
| mock:echo | graph vs none | comment_ok | 115 | 0 | 0 | 115 | +0.0 | 1 | 1 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
