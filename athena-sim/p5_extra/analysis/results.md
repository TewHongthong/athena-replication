# Public5 renaming with further models (exploratory; see ADDENDUM.md)

| Model | Condition | trials | valid % | core-rule % [95% CI] | core-rule % of valid | exact match % | collision-screened % | SI char after |
|---|---|---|---|---|---|---|---|---|
| GPT-6 Luna (frozen run) | none | 300 | 100.0 | 99.7 [99–100] | 99.7 | 89.0 | 98.0 | 0.9985 |
| GPT-6 Luna (frozen run) | fulldoc | 300 | 100.0 | 100.0† [96–100] | 100.0 | 87.0 | 99.0 | 0.9982 |
| GPT-6 Luna (frozen run) | chunk | 300 | 100.0 | 99.0 [97–100] | 99.0 | 86.0 | 98.0 | 0.9982 |
| GPT-6 Luna (frozen run) | graph | 300 | 100.0 | 100.0† [96–100] | 100.0 | 88.0 | 99.0 | 0.9981 |
| Gemini 3.1 Flash-Lite | none | 300 | 100.0 | 100.0† [96–100] | 100.0 | 80.7 | 99.3 | 0.9973 |
| Gemini 3.1 Flash-Lite | fulldoc | 300 | 100.0 | 100.0† [96–100] | 100.0 | 88.3 | 100.0 | 0.9982 |
| Gemini 3.1 Flash-Lite | chunk | 300 | 100.0 | 100.0† [96–100] | 100.0 | 82.7 | 100.0 | 0.9974 |
| Gemini 3.1 Flash-Lite | graph | 300 | 100.0 | 100.0† [96–100] | 100.0 | 86.0 | 100.0 | 0.9975 |
| Gemma 4 26B (endpoint) | none | 300 | 100.0 | 100.0† [96–100] | 100.0 | 87.7 | 99.0 | 0.9983 |
| Gemma 4 26B (endpoint) | fulldoc | 300 | 100.0 | 100.0† [96–100] | 100.0 | 90.0 | 99.0 | 0.9983 |
| Gemma 4 26B (endpoint) | chunk | 300 | 100.0 | 98.0 [95–100] | 98.0 | 88.7 | 97.0 | 0.9983 |
| Gemma 4 26B (endpoint) | graph | 300 | 99.7 | 99.7 [99–100] | 100.0 | 91.3 | 98.7 | 0.9988 |
| DeepSeek V4 Flash | none | 300 | 100.0 | 100.0† [96–100] | 100.0 | 90.3 | 99.0 | 0.9987 |
| DeepSeek V4 Flash | fulldoc | 300 | 99.3 | 99.3 [98–100] | 100.0 | 91.7 | 98.3 | 0.9987 |
| DeepSeek V4 Flash | chunk | 300 | 99.7 | 99.7 [99–100] | 100.0 | 90.7 | 98.0 | 0.9987 |
| DeepSeek V4 Flash | graph | 300 | 99.7 | 99.7 [99–100] | 100.0 | 91.7 | 98.7 | 0.9987 |

† every unit complies in every repeat; exact Clopper–Pearson interval over units.

## Paired exact sign tests on per-unit means (graph vs other condition), Holm within model

| Model | graph vs | diff (pp) | units better | units worse | p | Holm p |
|---|---|---|---|---|---|---|
| GPT-6 Luna (frozen run) | none | +0.3 | 1 | 0 | 1 | 1 |
| GPT-6 Luna (frozen run) | fulldoc | +0.0 | 0 | 0 | 1 | 1 |
| GPT-6 Luna (frozen run) | chunk | +1.0 | 1 | 0 | 1 | 1 |
| Gemini 3.1 Flash-Lite | none | +0.0 | 0 | 0 | 1 | 1 |
| Gemini 3.1 Flash-Lite | fulldoc | +0.0 | 0 | 0 | 1 | 1 |
| Gemini 3.1 Flash-Lite | chunk | +0.0 | 0 | 0 | 1 | 1 |
| Gemma 4 26B (endpoint) | none | -0.3 | 0 | 1 | 1 | 1 |
| Gemma 4 26B (endpoint) | fulldoc | -0.3 | 0 | 1 | 1 | 1 |
| Gemma 4 26B (endpoint) | chunk | +1.7 | 2 | 1 | 1 | 1 |
| DeepSeek V4 Flash | none | -0.3 | 0 | 1 | 1 | 1 |
| DeepSeek V4 Flash | fulldoc | +0.3 | 1 | 1 | 1 | 1 |
| DeepSeek V4 Flash | chunk | +0.0 | 1 | 1 | 1 | 1 |

## Core-rule % by language

| Model | Condition | csharp | java | javascript | python | typescript |
|---|---|---|---|---|---|---|
| GPT-6 Luna (frozen run) | none | 100.0 | 100.0 | 98.3 | 100.0 | 100.0 |
| GPT-6 Luna (frozen run) | fulldoc | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| GPT-6 Luna (frozen run) | chunk | 100.0 | 95.0 | 100.0 | 100.0 | 100.0 |
| GPT-6 Luna (frozen run) | graph | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Gemini 3.1 Flash-Lite | none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Gemini 3.1 Flash-Lite | fulldoc | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Gemini 3.1 Flash-Lite | chunk | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Gemini 3.1 Flash-Lite | graph | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Gemma 4 26B (endpoint) | none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Gemma 4 26B (endpoint) | fulldoc | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Gemma 4 26B (endpoint) | chunk | 100.0 | 90.0 | 100.0 | 100.0 | 100.0 |
| Gemma 4 26B (endpoint) | graph | 98.3 | 100.0 | 100.0 | 100.0 | 100.0 |
| DeepSeek V4 Flash | none | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| DeepSeek V4 Flash | fulldoc | 96.7 | 100.0 | 100.0 | 100.0 | 100.0 |
| DeepSeek V4 Flash | chunk | 98.3 | 100.0 | 100.0 | 100.0 | 100.0 |
| DeepSeek V4 Flash | graph | 100.0 | 98.3 | 100.0 | 100.0 | 100.0 |

## Expectations (ADDENDUM.md)

- GPT-6 Luna (frozen run): none 99.7% (valid only 99.7%), graph − none +0.3 pp overall, +0.3 pp on valid answers; invalid under none 0.0%
- Gemini 3.1 Flash-Lite: none 100.0% (valid only 100.0%), graph − none +0.0 pp overall, +0.0 pp on valid answers; invalid under none 0.0%
- Gemma 4 26B (endpoint): none 100.0% (valid only 100.0%), graph − none -0.3 pp overall, +0.0 pp on valid answers; invalid under none 0.0%
- DeepSeek V4 Flash: none 100.0% (valid only 100.0%), graph − none -0.3 pp overall, +0.0 pp on valid answers; invalid under none 0.0%

