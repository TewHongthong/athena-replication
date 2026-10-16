# Athena Sim summary

1200 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `p5x_dsv4f_p5_rename` (test split) was started from freeze `frozen_p5x_dsv4f_p5_rename.json` (sha256 3902c98e63f2).

## rename - pack `public5`

### By condition and backend

| backend | condition | n | parsed | exact match [95% CI] | violated rule ok | all core rules ok [95% CI] | type prefix kept | collision | similarity idx before -> after | retrieval hit | latency s | tokens in/out | cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| openai:deepseek/deepseek-v4-flash | none | 300 | 100.0% | 90.3% [86-93] | 100.0% | 100.0% [99-100] | - | 1.0% | 0.985 -> 0.999 | - | 8.44 | 136484/162360 | 0.2269 |
| openai:deepseek/deepseek-v4-flash | fulldoc | 300 | 99.3% | 91.7% [88-94] | 99.3% | 99.3% [98-100] | - | 1.0% | 0.985 -> 0.999 | - | 10.01 | 563068/155938 | 0.2784 |
| openai:deepseek/deepseek-v4-flash | chunk | 300 | 99.7% | 90.7% [87-93] | 99.7% | 99.7% [98-100] | - | 1.7% | 0.985 -> 0.999 | 90.0% | 9.16 | 193888/166349 | 0.2401 |
| openai:deepseek/deepseek-v4-flash | graph | 300 | 99.7% | 91.7% [88-94] | 99.7% | 99.7% [98-100] | - | 1.0% | 0.985 -> 0.999 | 100.0% | 9.24 | 187446/156486 | 0.2265 |

### By language (all core rules ok; n in brackets)

| backend | condition | csharp | java | javascript | python | typescript |
|---|---|---|---|---|---|---|
| openai:deepseek/deepseek-v4-flash | none | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] |
| openai:deepseek/deepseek-v4-flash | fulldoc | 96.7% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] |
| openai:deepseek/deepseek-v4-flash | chunk | 98.3% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] |
| openai:deepseek/deepseek-v4-flash | graph | 100.0% [60] | 98.3% [60] | 100.0% [60] | 100.0% [60] | 100.0% [60] |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:deepseek/deepseek-v4-flash | fulldoc vs none | core_ok | 100 | 0 | 1 | 99 | -0.7 | 1 | 1 |
| openai:deepseek/deepseek-v4-flash | chunk vs none | core_ok | 100 | 0 | 1 | 99 | -0.3 | 1 | 1 |
| openai:deepseek/deepseek-v4-flash | graph vs none | core_ok | 100 | 0 | 1 | 99 | -0.3 | 1 | 1 |
| openai:deepseek/deepseek-v4-flash | fulldoc vs none | exact_match | 100 | 7 | 4 | 89 | +1.3 | 0.549 | 1 |
| openai:deepseek/deepseek-v4-flash | chunk vs none | exact_match | 100 | 6 | 5 | 89 | +0.3 | 1 | 1 |
| openai:deepseek/deepseek-v4-flash | graph vs none | exact_match | 100 | 6 | 3 | 91 | +1.3 | 0.508 | 1 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
