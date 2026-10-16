# Review E analyses (K1, K2, K4, K5) - exploratory; see ADDENDUM.md

## K1 identifier kind inferred without the original name

**gscs**: 122 test units; kind exact A 114, B 122; same core rules A 114, B 122
confusion (A): {'python:constant->variable': 8}

| model | (iv) trials | reported % | lower bound A % | lower bound B % |
|---|---|---|---|---|
| o3-mini | 366 | 100.0 | 93.4 | 100.0 |
| GPT-6 Luna | 366 | 100.0 | 93.4 | 100.0 |
| Qwen3.5-9B | 366 | 93.7 | 87.2 | 93.7 |
| Gemini 3.1 Flash-Lite | 366 | 100.0 | 93.4 | 100.0 |
| DeepSeek V4 Flash | 366 | 99.2 | 92.6 | 99.2 |
| Gemma 4 26B | 366 | 100.0 | 93.4 | 100.0 |

**public5**: 100 test units; kind exact A 81, B 81; same core rules A 81, B 81; name-dependent kind changes 7; excerpt not analysable alone 11; excerpt read as another kind before the rename 1
confusion (A): {'csharp:method->None': 1, 'java:parameter->None': 2, 'java:method->None': 3, 'java:variable->None': 3, 'javascript:method->None': 2, 'python:field->constant': 3, 'python:constant->field': 3, 'python:method->function': 1, 'typescript:variable->constant': 1}

| model | (iv) trials | reported % | lower bound A % | lower bound B % | name-dependent only % |
|---|---|---|---|---|---|
| GPT-6 Luna | 300 | 100.0 | 81.0 | 81.0 | 93.0 |
| Gemini 3.1 Flash-Lite | 300 | 100.0 | 81.0 | 81.0 | 93.0 |
| DeepSeek V4 Flash | 300 | 99.7 | 80.7 | 80.7 | 92.7 |
| Gemma 4 26B (endpoint) | 300 | 99.7 | 80.7 | 80.7 | 92.7 |

