# Athena Sim summary

30 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

> Contains mock backends: **mock rows are deterministic stand-ins, not LLM results.**

Split: dev.

## comment - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | structure ok [95% CI] | labels present | labels filled | delimiter ok | similarity to reference | latency s | tokens in/out |
|---|---|---|---|---|---|---|---|---|---|---|
| mock:echo | none | 6 | 100.0% | 0.0% [0-39] | 0.0% | - | 100.0% | 0.058 | 0.00 | 0/0 |
| mock:echo | fulldoc | 6 | 100.0% | 0.0% [0-39] | 0.0% | - | 100.0% | 0.058 | 0.00 | 0/0 |
| mock:echo | chunk | 6 | 100.0% | 0.0% [0-39] | 0.0% | - | 100.0% | 0.058 | 0.00 | 0/0 |
| mock:echo | graph | 6 | 100.0% | 0.0% [0-39] | 0.0% | - | 100.0% | 0.058 | 0.00 | 0/0 |
| mock:echo | graph_noex | 6 | 100.0% | 0.0% [0-39] | 0.0% | - | 100.0% | 0.058 | 0.00 | 0/0 |

### By language (structure ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| mock:echo | none | 0.0% [2] | 0.0% [2] | 0.0% [2] |
| mock:echo | fulldoc | 0.0% [2] | 0.0% [2] | 0.0% [2] |
| mock:echo | chunk | 0.0% [2] | 0.0% [2] | 0.0% [2] |
| mock:echo | graph | 0.0% [2] | 0.0% [2] | 0.0% [2] |
| mock:echo | graph_noex | 0.0% [2] | 0.0% [2] | 0.0% [2] |

### Per-language, per-condition (comment_ok, delimiter_ok, vacuous-check share)

`vacuous (n_checks=0)` is the share of units whose applicable MUST comment rules have no mechanical check today (e.g. Python's plain-line-comment format, most Airbnb JS comment rules) -- comment_ok is trivially true for those regardless of what the model writes.

| backend | condition | language | n | comment_ok [95% CI] [n scored] | delimiter_ok | vacuous (n_checks=0) |
|---|---|---|---|---|---|---|
| mock:echo | none | cpp | 2 | 0.0% [0-66] [2] | 100.0% | 100.0% |
| mock:echo | none | java | 2 | 0.0% [0-66] [2] | 100.0% | 100.0% |
| mock:echo | none | python | 2 | 0.0% [0-66] [2] | 100.0% | 100.0% |
| mock:echo | fulldoc | cpp | 2 | 0.0% [0-66] [2] | 100.0% | 100.0% |
| mock:echo | fulldoc | java | 2 | 0.0% [0-66] [2] | 100.0% | 100.0% |
| mock:echo | fulldoc | python | 2 | 0.0% [0-66] [2] | 100.0% | 100.0% |
| mock:echo | chunk | cpp | 2 | 0.0% [0-66] [2] | 100.0% | 100.0% |
| mock:echo | chunk | java | 2 | 0.0% [0-66] [2] | 100.0% | 100.0% |
| mock:echo | chunk | python | 2 | 0.0% [0-66] [2] | 100.0% | 100.0% |
| mock:echo | graph | cpp | 2 | 0.0% [0-66] [2] | 100.0% | 100.0% |
| mock:echo | graph | java | 2 | 0.0% [0-66] [2] | 100.0% | 100.0% |
| mock:echo | graph | python | 2 | 0.0% [0-66] [2] | 100.0% | 100.0% |
| mock:echo | graph_noex | cpp | 2 | 0.0% [0-66] [2] | 100.0% | 100.0% |
| mock:echo | graph_noex | java | 2 | 0.0% [0-66] [2] | 100.0% | 100.0% |
| mock:echo | graph_noex | python | 2 | 0.0% [0-66] [2] | 100.0% | 100.0% |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| mock:echo | fulldoc vs none | comment_ok | 6 | 0 | 0 | 6 | +0.0 | 1 | 1 |
| mock:echo | chunk vs none | comment_ok | 6 | 0 | 0 | 6 | +0.0 | 1 | 1 |
| mock:echo | graph vs none | comment_ok | 6 | 0 | 0 | 6 | +0.0 | 1 | 1 |
| mock:echo | graph_noex vs none | comment_ok | 6 | 0 | 0 | 6 | +0.0 | 1 | 1 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
