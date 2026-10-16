# Review E analyses K2, K4, K5 - exploratory; see ADDENDUM.md

## K2 section-level hit of the applicable rule, top 3 (GSCS test units)

TF-IDF recomputation vs logged retrieved_ids: 0 mismatches of 122

| retriever | hit % |
|---|---|
| tfidf | 17.2 |
| bm25 | 5.7 |
| bm25_k15 | 5.7 |

by violated rule: {"tfidf": {"GSCS-CONST-UPPER": 9.1, "GSCS-FUNC-RETURN-PREFIX": 100.0, "GSCS-VAR-TYPED-PREFIX": 3.6, "GSCS-TYPE-SUFFIX": 11.1, "GSCS-PROC-VERB-OBJECT": 0.0, "GSCS-BOOL-BLN-PREFIX": 33.3}, "bm25": {"GSCS-CONST-UPPER": 0.0, "GSCS-FUNC-RETURN-PREFIX": 50.0, "GSCS-VAR-TYPED-PREFIX": 0.0, "GSCS-TYPE-SUFFIX": 11.1, "GSCS-PROC-VERB-OBJECT": 0.0, "GSCS-BOOL-BLN-PREFIX": 0.0}, "bm25_k15": {"GSCS-CONST-UPPER": 0.0, "GSCS-FUNC-RETURN-PREFIX": 50.0, "GSCS-VAR-TYPED-PREFIX": 0.0, "GSCS-TYPE-SUFFIX": 11.1, "GSCS-PROC-VERB-OBJECT": 0.0, "GSCS-BOOL-BLN-PREFIX": 0.0}}

## K4 core-rule compliance by violated rule (GSCS test)

| model | condition | GSCS-BOOL-BLN-PREFIX | GSCS-CONST-UPPER | GSCS-FUNC-RETURN-PREFIX | GSCS-PROC-VERB-OBJECT | GSCS-TYPE-SUFFIX | GSCS-VAR-TYPED-PREFIX |
|---|---|---|---|---|---|---|---|
| o3-mini | none | 0.0 | 60.6 | 0.0 | 0.0 | 0.0 | 29.7 |
| o3-mini | fulldoc | 100.0 | 100.0 | 97.2 | 80.6 | 100.0 | 100.0 |
| o3-mini | chunk | 80.6 | 16.7 | 77.8 | 2.8 | 11.1 | 95.2 |
| o3-mini | graph | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| GPT-6 Luna | none | 0.0 | 92.4 | 0.0 | 0.0 | 0.0 | 66.1 |
| GPT-6 Luna | fulldoc | 100.0 | 100.0 | 100.0 | 94.4 | 100.0 | 100.0 |
| GPT-6 Luna | chunk | 100.0 | 19.7 | 97.2 | 61.1 | 37.0 | 100.0 |
| GPT-6 Luna | graph | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Qwen3.5-9B | none | 0.0 | 60.6 | 0.0 | 0.0 | 0.0 | 20.6 |
| Qwen3.5-9B | fulldoc | 97.2 | 95.5 | 80.6 | 38.9 | 88.9 | 93.9 |
| Qwen3.5-9B | chunk | 100.0 | 9.1 | 11.1 | 0.0 | 7.4 | 76.4 |
| Qwen3.5-9B | graph | 100.0 | 100.0 | 100.0 | 97.2 | 96.3 | 87.3 |
| Gemini 3.1 Flash-Lite | none | 0.0 | 77.3 | 0.0 | 0.0 | 0.0 | 55.8 |
| Gemini 3.1 Flash-Lite | fulldoc | 100.0 | 100.0 | 91.7 | 100.0 | 100.0 | 100.0 |
| Gemini 3.1 Flash-Lite | chunk | 97.2 | 15.2 | 86.1 | 16.7 | 18.5 | 100.0 |
| Gemini 3.1 Flash-Lite | graph | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| DeepSeek V4 Flash | none | 0.0 | 54.5 | 0.0 | 0.0 | 0.0 | 45.5 |
| DeepSeek V4 Flash | fulldoc | 100.0 | 98.5 | 97.2 | 80.6 | 96.3 | 98.2 |
| DeepSeek V4 Flash | chunk | 75.0 | 18.2 | 94.4 | 16.7 | 14.8 | 98.2 |
| DeepSeek V4 Flash | graph | 97.2 | 100.0 | 100.0 | 100.0 | 100.0 | 98.8 |
| Gemma 4 26B | none | 0.0 | 63.6 | 0.0 | 0.0 | 0.0 | 53.9 |
| Gemma 4 26B | fulldoc | 100.0 | 100.0 | 72.2 | 88.9 | 100.0 | 100.0 |
| Gemma 4 26B | chunk | 100.0 | 18.2 | 25.0 | 52.8 | 22.2 | 99.4 |
| Gemma 4 26B | graph | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| o3-mini [ablation run] | graph | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| o3-mini [ablation run] | graph_noex | 52.8 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| GPT-6 Luna [ablation run] | graph | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| GPT-6 Luna [ablation run] | graph_noex | 86.1 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Gemini 3.1 Flash-Lite [ablation run] | graph | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Gemini 3.1 Flash-Lite [ablation run] | graph_noex | 83.3 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Gemma 4 26B (endpoint) [ablation run] | none | 0.0 | 59.1 | 0.0 | 0.0 | 0.0 | 51.5 |
| Gemma 4 26B (endpoint) [ablation run] | fulldoc | 100.0 | 98.5 | 75.0 | 86.1 | 100.0 | 100.0 |
| Gemma 4 26B (endpoint) [ablation run] | chunk | 100.0 | 18.2 | 27.8 | 44.4 | 22.2 | 100.0 |
| Gemma 4 26B (endpoint) [ablation run] | graph | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |
| Gemma 4 26B (endpoint) [ablation run] | graph_noex | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 | 100.0 |

units per rule: {"GSCS-CONST-UPPER": 22, "GSCS-FUNC-RETURN-PREFIX": 12, "GSCS-VAR-TYPED-PREFIX": 55, "GSCS-TYPE-SUFFIX": 9, "GSCS-PROC-VERB-OBJECT": 12, "GSCS-BOOL-BLN-PREFIX": 12}

## K4b by language

{"o3-mini": {"chunk|cpp": 64.3, "chunk|java": 60.2, "chunk|python": 63.2, "fulldoc|cpp": 100.0, "fulldoc|java": 99.2, "fulldoc|python": 94.0, "graph|cpp": 100.0, "graph|java": 100.0, "graph|python": 100.0, "none|cpp": 30.2, "none|java": 21.1, "none|python": 21.4}, "GPT-6 Luna": {"chunk|cpp": 79.4, "chunk|java": 77.2, "chunk|python": 73.5, "fulldoc|cpp": 100.0, "fulldoc|java": 100.0, "fulldoc|python": 98.3, "graph|cpp": 100.0, "graph|java": 100.0, "graph|python": 100.0, "none|cpp": 57.9, "none|java": 44.7, "none|python": 35.9}, "Qwen3.5-9B": {"chunk|cpp": 54.0, "chunk|java": 38.2, "chunk|python": 50.4, "fulldoc|cpp": 90.5, "fulldoc|java": 87.0, "fulldoc|python": 84.6, "graph|cpp": 97.6, "graph|java": 91.1, "graph|python": 92.3, "none|cpp": 23.0, "none|java": 22.8, "none|python": 14.5}, "Gemini 3.1 Flash-Lite": {"chunk|cpp": 73.0, "chunk|java": 67.5, "chunk|python": 65.8, "fulldoc|cpp": 100.0, "fulldoc|java": 100.0, "fulldoc|python": 97.4, "graph|cpp": 100.0, "graph|java": 100.0, "graph|python": 100.0, "none|cpp": 43.7, "none|java": 41.5, "none|python": 31.6}, "DeepSeek V4 Flash": {"chunk|cpp": 69.8, "chunk|java": 67.5, "chunk|python": 63.2, "fulldoc|cpp": 97.6, "fulldoc|java": 97.6, "fulldoc|python": 94.0, "graph|cpp": 100.0, "graph|java": 98.4, "graph|python": 99.1, "none|cpp": 31.0, "none|java": 32.5, "none|python": 27.4}, "Gemma 4 26B": {"chunk|cpp": 73.0, "chunk|java": 66.7, "chunk|python": 61.5, "fulldoc|cpp": 99.2, "fulldoc|java": 96.7, "fulldoc|python": 92.3, "graph|cpp": 100.0, "graph|java": 100.0, "graph|python": 100.0, "none|cpp": 36.5, "none|java": 32.5, "none|python": 38.5}, "o3-mini [ablation run]": {"graph|cpp": 100.0, "graph|java": 100.0, "graph|python": 100.0, "graph_noex|cpp": 96.8, "graph_noex|java": 91.9, "graph_noex|python": 97.4}, "GPT-6 Luna [ablation run]": {"graph|cpp": 100.0, "graph|java": 100.0, "graph|python": 100.0, "graph_noex|cpp": 100.0, "graph_noex|java": 95.9, "graph_noex|python": 100.0}, "Gemini 3.1 Flash-Lite [ablation run]": {"graph|cpp": 100.0, "graph|java": 100.0, "graph|python": 100.0, "graph_noex|cpp": 100.0, "graph_noex|java": 95.1, "graph_noex|python": 100.0}, "Gemma 4 26B (endpoint) [ablation run]": {"chunk|cpp": 69.8, "chunk|java": 67.5, "chunk|python": 63.2, "fulldoc|cpp": 99.2, "fulldoc|java": 97.6, "fulldoc|python": 90.6, "graph|cpp": 100.0, "graph|java": 100.0, "graph|python": 100.0, "graph_noex|cpp": 100.0, "graph_noex|java": 100.0, "graph_noex|python": 100.0, "none|cpp": 39.7, "none|java": 33.3, "none|python": 28.2}}

## K5 latency per call (s), GSCS renaming

| model | condition | n | P50 | P95 | mean |
|---|---|---|---|---|---|
| o3-mini | fulldoc | 366 | 4.77 | 7.52 | 4.86 |
| o3-mini | chunk | 366 | 4.77 | 9.07 | 5.37 |
| o3-mini | none | 366 | 5.01 | 8.9 | 5.51 |
| o3-mini | graph | 366 | 3.41 | 8.08 | 4.1 |
| GPT-6 Luna | chunk | 366 | 3.36 | 5.93 | 3.67 |
| GPT-6 Luna | fulldoc | 366 | 3.28 | 4.42 | 3.39 |
| GPT-6 Luna | graph | 366 | 3.02 | 4.24 | 3.1 |
| GPT-6 Luna | none | 366 | 4.68 | 9.67 | 5.56 |
| Qwen3.5-9B | none | 366 | 11.78 | 21.92 | 12.95 |
| Qwen3.5-9B | fulldoc | 366 | 24.12 | 29.89 | 24.38 |
| Qwen3.5-9B | chunk | 366 | 17.17 | 19.57 | 17.45 |
| Qwen3.5-9B | graph | 366 | 13.26 | 14.61 | 13.09 |
| Gemini 3.1 Flash-Lite | graph | 366 | 1.76 | 2.86 | 2.01 |
| Gemini 3.1 Flash-Lite | chunk | 366 | 1.73 | 3.05 | 2.03 |
| Gemini 3.1 Flash-Lite | fulldoc | 366 | 2.1 | 3.09 | 2.17 |
| Gemini 3.1 Flash-Lite | none | 366 | 1.9 | 3.1 | 2.09 |
| DeepSeek V4 Flash | chunk | 366 | 47.92 | 406.69 | 108.35 |
| DeepSeek V4 Flash | graph | 366 | 30.52 | 105.85 | 41.52 |
| DeepSeek V4 Flash | fulldoc | 366 | 41.15 | 157.33 | 59.38 |
| DeepSeek V4 Flash | none | 366 | 197.25 | 443.68 | 220.75 |
| Gemma 4 26B | none | 366 | 2.0 | 3.72 | 2.34 |
| Gemma 4 26B | fulldoc | 366 | 2.54 | 2.89 | 2.52 |
| Gemma 4 26B | chunk | 366 | 2.08 | 3.04 | 2.3 |
| Gemma 4 26B | graph | 366 | 1.88 | 2.12 | 1.89 |
| o3-mini [ablation run] | graph | 366 | 4.96 | 11.65 | 5.72 |
| o3-mini [ablation run] | graph_noex | 366 | 4.97 | 11.94 | 5.81 |
| GPT-6 Luna [ablation run] | graph_noex | 366 | 3.74 | 6.31 | 3.92 |
| GPT-6 Luna [ablation run] | graph | 366 | 3.86 | 6.28 | 4.02 |
| Gemini 3.1 Flash-Lite [ablation run] | graph_noex | 366 | 1.43 | 2.53 | 1.56 |
| Gemini 3.1 Flash-Lite [ablation run] | graph | 366 | 1.46 | 2.18 | 1.53 |
| Gemma 4 26B (endpoint) [ablation run] | graph | 366 | 2.48 | 6.76 | 3.07 |
| Gemma 4 26B (endpoint) [ablation run] | chunk | 366 | 2.92 | 7.57 | 3.7 |
| Gemma 4 26B (endpoint) [ablation run] | graph_noex | 366 | 2.67 | 6.36 | 3.07 |
| Gemma 4 26B (endpoint) [ablation run] | none | 366 | 3.16 | 9.49 | 3.98 |
| Gemma 4 26B (endpoint) [ablation run] | fulldoc | 366 | 2.64 | 7.07 | 3.48 |

Retrieval time of condition (iv) on this machine: 0.0192 ms per call (median over 1,000 passes of the 122 test units)

