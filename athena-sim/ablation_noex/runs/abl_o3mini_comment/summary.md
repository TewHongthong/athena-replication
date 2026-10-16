# Athena Sim summary

72 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `abl_o3mini_comment` (test split) was started from freeze `frozen_abl_o3mini_comment.json` (sha256 fce515a70693).

## comment - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | structure ok [95% CI] | labels present | labels filled | delimiter ok | similarity to reference | latency s | tokens in/out |
|---|---|---|---|---|---|---|---|---|---|---|
| openai:openai/o3-mini | graph | 36 | 100.0% | 100.0% [90-100] | 100.0% | 86.1% | 100.0% | 0.597 | 5.52 | 22128/22448 |
| openai:openai/o3-mini | graph_noex | 36 | 100.0% | 100.0% [90-100] | 100.0% | 93.5% | 100.0% | 0.574 | 5.72 | 16980/24026 |

### By language (structure ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:openai/o3-mini | graph | 100.0% [12] | 100.0% [12] | 100.0% [12] |
| openai:openai/o3-mini | graph_noex | 100.0% [12] | 100.0% [12] | 100.0% [12] |

### Per-language, per-condition (comment_ok, delimiter_ok, vacuous-check share)

`vacuous (n_checks=0)` is the share of units whose applicable MUST comment rules have no mechanical check today (e.g. Python's plain-line-comment format, most Airbnb JS comment rules) -- comment_ok is trivially true for those regardless of what the model writes.

| backend | condition | language | n | comment_ok [95% CI] [n scored] | delimiter_ok | vacuous (n_checks=0) |
|---|---|---|---|---|---|---|
| openai:openai/o3-mini | graph | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:openai/o3-mini | graph | java | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:openai/o3-mini | graph | python | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:openai/o3-mini | graph_noex | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:openai/o3-mini | graph_noex | java | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:openai/o3-mini | graph_noex | python | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |

### Paired comparison against `graph` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:openai/o3-mini | graph_noex vs graph | comment_ok | 12 | 0 | 0 | 12 | +0.0 | 1 | 1 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
