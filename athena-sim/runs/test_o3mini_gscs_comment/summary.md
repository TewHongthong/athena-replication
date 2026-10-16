# Athena Sim summary

144 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `test_o3mini_gscs_comment` (test split) was started from freeze `frozen_o3mini_gscs_comment.json` (sha256 6416e6167474).

## comment - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | structure ok [95% CI] | labels present | labels filled | delimiter ok | similarity to reference | latency s | tokens in/out |
|---|---|---|---|---|---|---|---|---|---|---|
| openai:openai/o3-mini | none | 36 | 100.0% | 0.0% [0-10] | 0.0% | - | 100.0% | 0.300 | 4.31 | 13128/23348 |
| openai:openai/o3-mini | fulldoc | 36 | 100.0% | 88.9% [75-96] | 98.3% | 96.2% | 100.0% | 0.511 | 5.85 | 65400/29897 |
| openai:openai/o3-mini | chunk | 36 | 97.2% | 80.6% [65-90] | 82.9% | 90.2% | 97.2% | 0.513 | 4.73 | 27183/25892 |
| openai:openai/o3-mini | graph | 36 | 100.0% | 100.0% [90-100] | 100.0% | 87.0% | 100.0% | 0.605 | 4.14 | 22128/22604 |

### By language (structure ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:openai/o3-mini | none | 0.0% [12] | 0.0% [12] | 0.0% [12] |
| openai:openai/o3-mini | fulldoc | 83.3% [12] | 91.7% [12] | 91.7% [12] |
| openai:openai/o3-mini | chunk | 100.0% [12] | 75.0% [12] | 66.7% [12] |
| openai:openai/o3-mini | graph | 100.0% [12] | 100.0% [12] | 100.0% [12] |

### Per-language, per-condition (comment_ok, delimiter_ok, vacuous-check share)

`vacuous (n_checks=0)` is the share of units whose applicable MUST comment rules have no mechanical check today (e.g. Python's plain-line-comment format, most Airbnb JS comment rules) -- comment_ok is trivially true for those regardless of what the model writes.

| backend | condition | language | n | comment_ok [95% CI] [n scored] | delimiter_ok | vacuous (n_checks=0) |
|---|---|---|---|---|---|---|
| openai:openai/o3-mini | none | cpp | 12 | 0.0% [0-24] [12] | 100.0% | 100.0% |
| openai:openai/o3-mini | none | java | 12 | 0.0% [0-24] [12] | 100.0% | 100.0% |
| openai:openai/o3-mini | none | python | 12 | 0.0% [0-24] [12] | 100.0% | 100.0% |
| openai:openai/o3-mini | fulldoc | cpp | 12 | 83.3% [55-95] [12] | 100.0% | 100.0% |
| openai:openai/o3-mini | fulldoc | java | 12 | 91.7% [65-99] [12] | 100.0% | 100.0% |
| openai:openai/o3-mini | fulldoc | python | 12 | 91.7% [65-99] [12] | 100.0% | 100.0% |
| openai:openai/o3-mini | chunk | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:openai/o3-mini | chunk | java | 12 | 75.0% [47-91] [12] | 100.0% | 100.0% |
| openai:openai/o3-mini | chunk | python | 12 | 66.7% [39-86] [12] | 91.7% | 100.0% |
| openai:openai/o3-mini | graph | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:openai/o3-mini | graph | java | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:openai/o3-mini | graph | python | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:openai/o3-mini | fulldoc vs none | comment_ok | 12 | 12 | 0 | 0 | +88.9 | 0.000488 | 0.00146 |
| openai:openai/o3-mini | chunk vs none | comment_ok | 12 | 10 | 0 | 2 | +80.6 | 0.00195 | 0.00195 |
| openai:openai/o3-mini | graph vs none | comment_ok | 12 | 12 | 0 | 0 | +100.0 | 0.000488 | 0.00146 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
