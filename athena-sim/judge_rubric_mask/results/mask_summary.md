# Rubric sensitivity: non-inferable label values masked (GSCS; exploratory, see ADDENDUM.md)

Re-rated items: 404; rated so far: {'muse': 404, 'haiku': 404}; rows missing a score: 0

Judge agreement on re-rated items (overall, quadratic-weighted kappa): 0.67 (n = 404)

Discrimination check (masked): reference 4.68 vs rule-based fixer template 2.18 -> PASS

| Source | Condition | n | overall original | overall masked | diff | conformance orig -> masked | completeness orig -> masked |
|---|---|---|---|---|---|---|---|
| o3-mini | none | 36 | 3.58 | 3.58 | +0.00 | 1.03 -> 1.03 | 3.51 -> 3.51 |
| o3-mini | fulldoc | 36 | 4.76 | 4.74 | -0.02 | 4.35 -> 4.22 | 4.86 -> 4.92 |
| o3-mini | chunk (not re-rated) | 36 | 4.42 | 4.42 | +0.00 | 3.71 -> 3.71 | 4.40 -> 4.40 |
| o3-mini | graph | 36 | 4.71 | 4.84 | +0.13 | 4.39 -> 4.69 | 4.60 -> 4.96 |
| GPT-6 Luna | none | 36 | 3.61 | 3.61 | +0.00 | 1.00 -> 1.00 | 3.54 -> 3.54 |
| GPT-6 Luna | fulldoc | 36 | 4.05 | 4.12 | +0.07 | 2.49 -> 2.71 | 3.94 -> 4.01 |
| GPT-6 Luna | chunk (not re-rated) | 36 | 3.89 | 3.89 | +0.00 | 2.18 -> 2.18 | 3.56 -> 3.56 |
| GPT-6 Luna | graph | 36 | 4.59 | 4.84 | +0.25 | 3.93 -> 4.53 | 4.61 -> 4.93 |
| Qwen3.5-9B | none | 36 | 3.24 | 3.24 | +0.00 | 1.00 -> 1.00 | 2.89 -> 2.89 |
| Qwen3.5-9B | fulldoc | 36 | 4.70 | 4.84 | +0.14 | 4.17 -> 4.61 | 4.71 -> 4.86 |
| Qwen3.5-9B | chunk (not re-rated) | 36 | 4.41 | 4.41 | +0.00 | 3.60 -> 3.60 | 4.18 -> 4.18 |
| Qwen3.5-9B | graph | 36 | 4.33 | 4.40 | +0.07 | 3.71 -> 3.88 | 4.10 -> 4.17 |
| Gemini 3.1 Flash-Lite | none | 36 | 3.42 | 3.42 | +0.00 | 1.00 -> 1.00 | 3.17 -> 3.17 |
| Gemini 3.1 Flash-Lite | fulldoc | 36 | 4.61 | 4.68 | +0.07 | 4.42 -> 4.57 | 4.61 -> 4.69 |
| Gemini 3.1 Flash-Lite | chunk (not re-rated) | 36 | 4.62 | 4.62 | +0.00 | 4.00 -> 4.00 | 4.54 -> 4.54 |
| Gemini 3.1 Flash-Lite | graph | 36 | 4.71 | 4.89 | +0.18 | 4.35 -> 4.64 | 4.57 -> 4.94 |
| DeepSeek V4 Flash | none | 36 | 3.02 | 3.02 | +0.00 | 1.04 -> 1.04 | 2.93 -> 2.93 |
| DeepSeek V4 Flash | fulldoc | 36 | 4.34 | 4.52 | +0.18 | 3.90 -> 4.35 | 4.32 -> 4.56 |
| DeepSeek V4 Flash | chunk (not re-rated) | 36 | 4.42 | 4.42 | +0.00 | 3.54 -> 3.54 | 4.31 -> 4.31 |
| DeepSeek V4 Flash | graph | 36 | 4.33 | 4.53 | +0.20 | 3.96 -> 4.44 | 4.19 -> 4.54 |
| Gemma 4 26B | none | 36 | 3.48 | 3.48 | +0.00 | 1.00 -> 1.00 | 3.19 -> 3.19 |
| Gemma 4 26B | fulldoc | 36 | 4.95 | 4.95 | -0.01 | 4.88 -> 4.89 | 4.96 -> 4.94 |
| Gemma 4 26B | chunk (not re-rated) | 36 | 4.48 | 4.48 | +0.00 | 3.76 -> 3.76 | 4.39 -> 4.39 |
| Gemma 4 26B | graph | 36 | 4.67 | 4.90 | +0.23 | 4.31 -> 4.79 | 4.60 -> 4.93 |
| linter autofix | none | 36 | 1.81 | 2.18 | +0.36 | 2.25 -> 2.71 | 1.00 -> 1.00 |
| linter autofix | fulldoc | 36 | 1.81 | 2.18 | +0.36 | 2.25 -> 2.71 | 1.00 -> 1.00 |
| linter autofix | chunk (not re-rated) | 36 | 1.81 | 2.18 | +0.36 | 2.25 -> 2.71 | 1.00 -> 1.00 |
| linter autofix | graph | 36 | 1.81 | 2.18 | +0.36 | 2.25 -> 2.71 | 1.00 -> 1.00 |
| reference | reference | 12 | 4.79 | 4.68 | -0.11 | 4.50 -> 4.29 | 4.96 -> 4.79 |

## Paired sign tests, original scores (per-unit mean overall; Holm across these 12 GSCS tests)

| Model | graph vs | mean diff | units better | units worse | p | Holm p |
|---|---|---|---|---|---|---|
| o3-mini | none | +1.13 | 12 | 0 | 0.000488 | 0.00586 |
| o3-mini | fulldoc | -0.05 | 3 | 8 | 0.227 | 0.68 |
| GPT-6 Luna | none | +0.98 | 12 | 0 | 0.000488 | 0.00586 |
| GPT-6 Luna | fulldoc | +0.54 | 12 | 0 | 0.000488 | 0.00586 |
| Qwen3.5-9B | none | +1.09 | 12 | 0 | 0.000488 | 0.00586 |
| Qwen3.5-9B | fulldoc | -0.37 | 1 | 11 | 0.00635 | 0.0317 |
| Gemini 3.1 Flash-Lite | none | +1.28 | 12 | 0 | 0.000488 | 0.00586 |
| Gemini 3.1 Flash-Lite | fulldoc | +0.10 | 4 | 6 | 0.754 | 1 |
| DeepSeek V4 Flash | none | +1.31 | 10 | 2 | 0.0386 | 0.154 |
| DeepSeek V4 Flash | fulldoc | -0.02 | 6 | 6 | 1 | 1 |
| Gemma 4 26B | none | +1.20 | 12 | 0 | 0.000488 | 0.00586 |
| Gemma 4 26B | fulldoc | -0.28 | 0 | 11 | 0.000977 | 0.00586 |

## Paired sign tests, masked scores (per-unit mean overall; Holm across these 12 GSCS tests)

| Model | graph vs | mean diff | units better | units worse | p | Holm p |
|---|---|---|---|---|---|---|
| o3-mini | none | +1.26 | 12 | 0 | 0.000488 | 0.00586 |
| o3-mini | fulldoc | +0.10 | 7 | 2 | 0.18 | 0.719 |
| GPT-6 Luna | none | +1.23 | 12 | 0 | 0.000488 | 0.00586 |
| GPT-6 Luna | fulldoc | +0.72 | 12 | 0 | 0.000488 | 0.00586 |
| Qwen3.5-9B | none | +1.16 | 12 | 0 | 0.000488 | 0.00586 |
| Qwen3.5-9B | fulldoc | -0.44 | 1 | 11 | 0.00635 | 0.0381 |
| Gemini 3.1 Flash-Lite | none | +1.46 | 12 | 0 | 0.000488 | 0.00586 |
| Gemini 3.1 Flash-Lite | fulldoc | +0.20 | 6 | 4 | 0.754 | 1 |
| DeepSeek V4 Flash | none | +1.51 | 10 | 2 | 0.0386 | 0.193 |
| DeepSeek V4 Flash | fulldoc | +0.01 | 5 | 5 | 1 | 1 |
| Gemma 4 26B | none | +1.43 | 12 | 0 | 0.000488 | 0.00586 |
| Gemma 4 26B | fulldoc | -0.05 | 3 | 5 | 0.727 | 1 |

