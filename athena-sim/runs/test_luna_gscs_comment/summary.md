# Athena Sim summary

144 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `test_luna_gscs_comment` (test split) was started from freeze `frozen_luna_gscs_comment.json` (sha256 72db35d36b91).

## comment - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | structure ok [95% CI] | labels present | labels filled | delimiter ok | similarity to reference | latency s | tokens in/out |
|---|---|---|---|---|---|---|---|---|---|---|
| openai:openai/gpt-6-luna | none | 36 | 100.0% | 0.0% [0-10] | 0.0% | - | 100.0% | 0.308 | 7.46 | 13128/20620 |
| openai:openai/gpt-6-luna | fulldoc | 36 | 100.0% | 27.8% [16-44] | 63.9% | 92.7% | 100.0% | 0.545 | 6.03 | 65400/16986 |
| openai:openai/gpt-6-luna | chunk | 36 | 100.0% | 13.9% [6-29] | 48.3% | 93.8% | 100.0% | 0.491 | 5.06 | 27183/14729 |
| openai:openai/gpt-6-luna | graph | 36 | 100.0% | 100.0% [90-100] | 100.0% | 74.5% | 100.0% | 0.637 | 4.87 | 22128/13797 |

### By language (structure ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:openai/gpt-6-luna | none | 0.0% [12] | 0.0% [12] | 0.0% [12] |
| openai:openai/gpt-6-luna | fulldoc | 33.3% [12] | 16.7% [12] | 33.3% [12] |
| openai:openai/gpt-6-luna | chunk | 33.3% [12] | 8.3% [12] | 0.0% [12] |
| openai:openai/gpt-6-luna | graph | 100.0% [12] | 100.0% [12] | 100.0% [12] |

### Per-language, per-condition (comment_ok, delimiter_ok, vacuous-check share)

`vacuous (n_checks=0)` is the share of units whose applicable MUST comment rules have no mechanical check today (e.g. Python's plain-line-comment format, most Airbnb JS comment rules) -- comment_ok is trivially true for those regardless of what the model writes.

| backend | condition | language | n | comment_ok [95% CI] [n scored] | delimiter_ok | vacuous (n_checks=0) |
|---|---|---|---|---|---|---|
| openai:openai/gpt-6-luna | none | cpp | 12 | 0.0% [0-24] [12] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | none | java | 12 | 0.0% [0-24] [12] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | none | python | 12 | 0.0% [0-24] [12] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | fulldoc | cpp | 12 | 33.3% [14-61] [12] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | fulldoc | java | 12 | 16.7% [5-45] [12] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | fulldoc | python | 12 | 33.3% [14-61] [12] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | chunk | cpp | 12 | 33.3% [14-61] [12] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | chunk | java | 12 | 8.3% [1-35] [12] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | chunk | python | 12 | 0.0% [0-24] [12] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | graph | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | graph | java | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:openai/gpt-6-luna | graph | python | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:openai/gpt-6-luna | fulldoc vs none | comment_ok | 12 | 7 | 0 | 5 | +27.8 | 0.0156 | 0.0312 |
| openai:openai/gpt-6-luna | chunk vs none | comment_ok | 12 | 4 | 0 | 8 | +13.9 | 0.125 | 0.125 |
| openai:openai/gpt-6-luna | graph vs none | comment_ok | 12 | 12 | 0 | 0 | +100.0 | 0.000488 | 0.00146 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
