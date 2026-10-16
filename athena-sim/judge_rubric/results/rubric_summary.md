# Rubric rating of generated comments (exploratory; see ADDENDUM.md)

Judges: muse (1962/1962 items rated), haiku (1962/1962 items rated)

## Agreement between muse and haiku (1962 items)

| Criterion | weighted kappa | exact % | within 1 % |
|---|---|---|---|
| accuracy | 0.23 | 87.4 | 97.4 |
| completeness | 0.54 | 51.3 | 88.8 |
| clarity | 0.49 | 72.4 | 99.2 |
| conformance | 0.78 | 59.9 | 89.2 |
| overall | 0.52 | 61.7 | 99.2 |

- muse: unparsed/failed judge calls recorded: 0
- haiku: unparsed/failed judge calls recorded: 0
- Discrimination check (GSCS): reference overall 4.79 vs linter-autofix floor 1.81 -> PASS

No judge shares a model family with any generator, so the self-family sensitivity analysis is not needed.

## All judges

Rows not yet rated by any judge: 0

| Pack | Source | Condition | n | answered | accuracy | completeness | clarity | conformance | overall (all) | overall (answered) |
|---|---|---|---|---|---|---|---|---|---|---|
| gscs | DeepSeek V4 Flash | none | 36 | 28 | 4.08 | 2.93 | 4.03 | 1.04 | 3.02 | 3.60 |
| gscs | DeepSeek V4 Flash | fulldoc | 36 | 33 | 4.67 | 4.32 | 4.49 | 3.90 | 4.34 | 4.65 |
| gscs | DeepSeek V4 Flash | chunk | 36 | 36 | 5.00 | 4.31 | 4.82 | 3.54 | 4.42 | 4.42 |
| gscs | DeepSeek V4 Flash | graph | 36 | 33 | 4.62 | 4.19 | 4.53 | 3.96 | 4.33 | 4.63 |
| gscs | GPT-6 Luna | none | 36 | 36 | 5.00 | 3.54 | 4.90 | 1.00 | 3.61 | 3.61 |
| gscs | GPT-6 Luna | fulldoc | 36 | 36 | 5.00 | 3.94 | 4.76 | 2.49 | 4.05 | 4.05 |
| gscs | GPT-6 Luna | chunk | 36 | 36 | 5.00 | 3.56 | 4.83 | 2.18 | 3.89 | 3.89 |
| gscs | GPT-6 Luna | graph | 36 | 36 | 4.94 | 4.61 | 4.88 | 3.93 | 4.59 | 4.59 |
| gscs | Gemini 3.1 Flash-Lite | none | 36 | 35 | 4.89 | 3.17 | 4.64 | 1.00 | 3.42 | 3.49 |
| gscs | Gemini 3.1 Flash-Lite | fulldoc | 36 | 34 | 4.72 | 4.61 | 4.68 | 4.42 | 4.61 | 4.82 |
| gscs | Gemini 3.1 Flash-Lite | chunk | 36 | 36 | 4.97 | 4.54 | 4.96 | 4.00 | 4.62 | 4.62 |
| gscs | Gemini 3.1 Flash-Lite | graph | 36 | 36 | 4.94 | 4.57 | 4.97 | 4.35 | 4.71 | 4.71 |
| gscs | Gemma 4 26B | none | 36 | 36 | 5.00 | 3.19 | 4.71 | 1.00 | 3.48 | 3.48 |
| gscs | Gemma 4 26B | fulldoc | 36 | 36 | 5.00 | 4.96 | 4.99 | 4.88 | 4.95 | 4.95 |
| gscs | Gemma 4 26B | chunk | 36 | 36 | 4.97 | 4.39 | 4.81 | 3.76 | 4.48 | 4.48 |
| gscs | Gemma 4 26B | graph | 36 | 36 | 4.88 | 4.60 | 4.92 | 4.31 | 4.67 | 4.67 |
| gscs | Qwen3.5-9B | none | 36 | 33 | 4.53 | 2.89 | 4.54 | 1.00 | 3.24 | 3.44 |
| gscs | Qwen3.5-9B | fulldoc | 36 | 36 | 4.93 | 4.71 | 4.99 | 4.17 | 4.70 | 4.70 |
| gscs | Qwen3.5-9B | chunk | 36 | 36 | 5.00 | 4.18 | 4.88 | 3.60 | 4.41 | 4.41 |
| gscs | Qwen3.5-9B | graph | 36 | 36 | 4.82 | 4.10 | 4.68 | 3.71 | 4.33 | 4.33 |
| gscs | linter autofix | none | 36 | 36 | 3.00 | 1.00 | 1.00 | 2.25 | 1.81 | 1.81 |
| gscs | linter autofix | fulldoc | 36 | 36 | 3.00 | 1.00 | 1.00 | 2.25 | 1.81 | 1.81 |
| gscs | linter autofix | chunk | 36 | 36 | 3.00 | 1.00 | 1.00 | 2.25 | 1.81 | 1.81 |
| gscs | linter autofix | graph | 36 | 36 | 3.00 | 1.00 | 1.00 | 2.25 | 1.81 | 1.81 |
| gscs | o3-mini | none | 36 | 36 | 4.99 | 3.51 | 4.78 | 1.03 | 3.58 | 3.58 |
| gscs | o3-mini | fulldoc | 36 | 36 | 4.99 | 4.86 | 4.85 | 4.35 | 4.76 | 4.76 |
| gscs | o3-mini | chunk | 36 | 35 | 4.89 | 4.40 | 4.69 | 3.71 | 4.42 | 4.52 |
| gscs | o3-mini | graph | 36 | 36 | 4.97 | 4.60 | 4.88 | 4.39 | 4.71 | 4.71 |
| gscs | reference | reference | 12 | 12 | 4.79 | 4.96 | 4.92 | 4.50 | 4.79 | 4.79 |
| public5 | GPT-6 Luna | none | 267 | 266 | 4.91 | 4.28 | 4.80 | 4.49 | 4.62 | 4.63 |
| public5 | GPT-6 Luna | fulldoc | 267 | 267 | 4.87 | 4.43 | 4.80 | 4.69 | 4.70 | 4.70 |
| public5 | GPT-6 Luna | chunk | 267 | 267 | 4.87 | 4.31 | 4.80 | 4.58 | 4.64 | 4.64 |
| public5 | GPT-6 Luna | graph | 267 | 267 | 4.90 | 4.21 | 4.77 | 4.60 | 4.62 | 4.62 |
| public5 | reference | reference | 89 | 89 | 4.42 | 2.96 | 4.42 | 3.39 | 3.80 | 3.80 |

Paired exact sign tests, per-unit mean overall score, graph vs other (Holm within this table):

| Pack | Source | graph vs | mean diff | units better | units worse | p | Holm p |
|---|---|---|---|---|---|---|---|
| gscs | DeepSeek V4 Flash | none | +1.31 | 10 | 2 | 0.0386 | 0.193 |
| gscs | DeepSeek V4 Flash | fulldoc | -0.02 | 6 | 6 | 1 | 1 |
| gscs | GPT-6 Luna | none | +0.98 | 12 | 0 | 0.000488 | 0.00684 |
| gscs | GPT-6 Luna | fulldoc | +0.54 | 12 | 0 | 0.000488 | 0.00684 |
| gscs | Gemini 3.1 Flash-Lite | none | +1.28 | 12 | 0 | 0.000488 | 0.00684 |
| gscs | Gemini 3.1 Flash-Lite | fulldoc | +0.10 | 4 | 6 | 0.754 | 1 |
| gscs | Gemma 4 26B | none | +1.20 | 12 | 0 | 0.000488 | 0.00684 |
| gscs | Gemma 4 26B | fulldoc | -0.28 | 0 | 11 | 0.000977 | 0.00781 |
| gscs | Qwen3.5-9B | none | +1.09 | 12 | 0 | 0.000488 | 0.00684 |
| gscs | Qwen3.5-9B | fulldoc | -0.37 | 1 | 11 | 0.00635 | 0.0381 |
| gscs | o3-mini | none | +1.13 | 12 | 0 | 0.000488 | 0.00684 |
| gscs | o3-mini | fulldoc | -0.05 | 3 | 8 | 0.227 | 0.906 |
| public5 | GPT-6 Luna | none | +0.01 | 39 | 43 | 0.741 | 1 |
| public5 | GPT-6 Luna | fulldoc | -0.08 | 28 | 54 | 0.00544 | 0.0381 |

