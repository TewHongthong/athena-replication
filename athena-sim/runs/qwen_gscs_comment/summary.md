# Athena Sim summary

144 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `qwen_gscs_comment` (test split) was started from freeze `frozen_qwen_gscs_comment.json` (sha256 d096b8958ea0).

## comment - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | structure ok [95% CI] | labels present | labels filled | delimiter ok | similarity to reference | latency s | tokens in/out |
|---|---|---|---|---|---|---|---|---|---|---|
| openai:Qwen3.5-9B-Q4_K_M | none | 36 | 91.7% | 0.0% [0-10] | 0.0% | - | 86.1% | 0.311 | 13.33 | 14166/8130 |
| openai:Qwen3.5-9B-Q4_K_M | fulldoc | 36 | 100.0% | 86.1% [71-94] | 95.1% | 81.1% | 100.0% | 0.603 | 27.20 | 68742/9505 |
| openai:Qwen3.5-9B-Q4_K_M | chunk | 36 | 100.0% | 83.3% [68-92] | 83.3% | 66.7% | 100.0% | 0.572 | 19.21 | 28827/9218 |
| openai:Qwen3.5-9B-Q4_K_M | graph | 36 | 100.0% | 100.0% [90-100] | 100.0% | 67.6% | 100.0% | 0.643 | 16.79 | 23526/8710 |

### By language (structure ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:Qwen3.5-9B-Q4_K_M | none | 0.0% [12] | 0.0% [12] | 0.0% [12] |
| openai:Qwen3.5-9B-Q4_K_M | fulldoc | 91.7% [12] | 66.7% [12] | 100.0% [12] |
| openai:Qwen3.5-9B-Q4_K_M | chunk | 100.0% [12] | 75.0% [12] | 75.0% [12] |
| openai:Qwen3.5-9B-Q4_K_M | graph | 100.0% [12] | 100.0% [12] | 100.0% [12] |

### Per-language, per-condition (comment_ok, delimiter_ok, vacuous-check share)

`vacuous (n_checks=0)` is the share of units whose applicable MUST comment rules have no mechanical check today (e.g. Python's plain-line-comment format, most Airbnb JS comment rules) -- comment_ok is trivially true for those regardless of what the model writes.

| backend | condition | language | n | comment_ok [95% CI] [n scored] | delimiter_ok | vacuous (n_checks=0) |
|---|---|---|---|---|---|---|
| openai:Qwen3.5-9B-Q4_K_M | none | cpp | 12 | 0.0% [0-24] [12] | 91.7% | 100.0% |
| openai:Qwen3.5-9B-Q4_K_M | none | java | 12 | 0.0% [0-24] [12] | 100.0% | 100.0% |
| openai:Qwen3.5-9B-Q4_K_M | none | python | 12 | 0.0% [0-24] [12] | 66.7% | 100.0% |
| openai:Qwen3.5-9B-Q4_K_M | fulldoc | cpp | 12 | 91.7% [65-99] [12] | 100.0% | 100.0% |
| openai:Qwen3.5-9B-Q4_K_M | fulldoc | java | 12 | 66.7% [39-86] [12] | 100.0% | 100.0% |
| openai:Qwen3.5-9B-Q4_K_M | fulldoc | python | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:Qwen3.5-9B-Q4_K_M | chunk | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:Qwen3.5-9B-Q4_K_M | chunk | java | 12 | 75.0% [47-91] [12] | 100.0% | 100.0% |
| openai:Qwen3.5-9B-Q4_K_M | chunk | python | 12 | 75.0% [47-91] [12] | 100.0% | 100.0% |
| openai:Qwen3.5-9B-Q4_K_M | graph | cpp | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:Qwen3.5-9B-Q4_K_M | graph | java | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |
| openai:Qwen3.5-9B-Q4_K_M | graph | python | 12 | 100.0% [76-100] [12] | 100.0% | 100.0% |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:Qwen3.5-9B-Q4_K_M | fulldoc vs none | comment_ok | 12 | 12 | 0 | 0 | +86.1 | 0.000488 | 0.00146 |
| openai:Qwen3.5-9B-Q4_K_M | chunk vs none | comment_ok | 12 | 10 | 0 | 2 | +83.3 | 0.00195 | 0.00195 |
| openai:Qwen3.5-9B-Q4_K_M | graph vs none | comment_ok | 12 | 12 | 0 | 0 | +100.0 | 0.000488 | 0.00146 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
