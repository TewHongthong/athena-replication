# Athena Sim summary

1464 successful trials, 0 trial keys with only errors. Rates are per trial; repeats of the same unit are pooled (treat CIs and p-values as exploratory).

Split: test.

> Run `gemini31fl_gscs_rename` (test split) was started from freeze `frozen_gemini31fl_gscs_rename.json` (sha256 eba42de44a0f).

## rename - pack `gscs`

### By condition and backend

| backend | condition | n | parsed | exact match [95% CI] | violated rule ok | all core rules ok [95% CI] | type prefix kept | collision | similarity idx before -> after | retrieval hit | latency s | tokens in/out | cost USD |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| openai:google/gemini-3.1-flash-lite | none | 366 | 99.7% | 37.2% [32-42] | 39.1% | 39.1% [34-44] | 38.8% | 3.0% | 0.990 -> 0.993 | - | 2.09 | 189274/50799 | 0.1235 |
| openai:google/gemini-3.1-flash-lite | fulldoc | 366 | 100.0% | 91.3% [88-94] | 99.2% | 99.2% [98-100] | 100.0% | 0.0% | 0.990 -> 0.999 | - | 2.17 | 761461/46325 | 0.2599 |
| openai:google/gemini-3.1-flash-lite | chunk | 366 | 99.7% | 51.4% [46-56] | 68.9% | 68.9% [64-73] | 84.4% | 0.0% | 0.990 -> 0.992 | - | 2.03 | 355901/47257 | 0.1599 |
| openai:google/gemini-3.1-flash-lite | graph | 366 | 100.0% | 91.0% [88-94] | 100.0% | 100.0% [99-100] | 100.0% | 0.0% | 0.990 -> 0.999 | 100.0% | 2.01 | 237929/48434 | 0.1321 |

### By language (all core rules ok; n in brackets)

| backend | condition | cpp | java | python |
|---|---|---|---|---|
| openai:google/gemini-3.1-flash-lite | none | 43.7% [126] | 41.5% [123] | 31.6% [117] |
| openai:google/gemini-3.1-flash-lite | fulldoc | 100.0% [126] | 100.0% [123] | 97.4% [117] |
| openai:google/gemini-3.1-flash-lite | chunk | 73.0% [126] | 67.5% [123] | 65.8% [117] |
| openai:google/gemini-3.1-flash-lite | graph | 100.0% [126] | 100.0% [123] | 100.0% [117] |

### Paired comparison against `none` (per unit, repeats averaged; exact two-sided sign test)

| backend | comparison | metric | units | better | worse | tied | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|---|---|---|---|
| openai:google/gemini-3.1-flash-lite | fulldoc vs none | core_ok | 122 | 83 | 0 | 39 | +60.1 | 2.07e-25 | 1.24e-24 |
| openai:google/gemini-3.1-flash-lite | chunk vs none | core_ok | 122 | 60 | 17 | 45 | +29.8 | 8.91e-07 | 1.78e-06 |
| openai:google/gemini-3.1-flash-lite | graph vs none | core_ok | 122 | 83 | 0 | 39 | +60.9 | 2.07e-25 | 1.24e-24 |
| openai:google/gemini-3.1-flash-lite | fulldoc vs none | exact_match | 122 | 76 | 1 | 45 | +54.1 | 1.03e-21 | 3.1e-21 |
| openai:google/gemini-3.1-flash-lite | chunk vs none | exact_match | 122 | 41 | 20 | 61 | +14.2 | 0.00985 | 0.00985 |
| openai:google/gemini-3.1-flash-lite | graph vs none | exact_match | 122 | 79 | 0 | 43 | +53.8 | 3.31e-24 | 1.32e-23 |

`better`/`worse` count units. `p (Holm)` corrects for all comparisons in this table; only hypotheses written in HYPOTHESES.md before the test run are confirmatory.
