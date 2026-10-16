# Phase 9 results (exploratory; see ADDENDUM.md)

## 9.1a Settings used (frozen configs)

| run | task | conditions | top_k | chunk_k | examples | temperature | max_tokens | repeats |
|---|---|---|---|---|---|---|---|---|
| o3-mini | rename | none,fulldoc,chunk,graph | None | 3 | 2 | 0.2 | 8192 | 3 |
| o3-mini | comment | none,fulldoc,chunk,graph | None | 3 | 2 | 0.2 | 8192 | 3 |
| GPT-6 Luna | rename | none,fulldoc,chunk,graph | None | 3 | 2 | 0.2 | 8192 | 3 |
| GPT-6 Luna | comment | none,fulldoc,chunk,graph | None | 3 | 2 | 0.2 | 8192 | 3 |
| GPT-6 Luna (Public5) | rename | none,fulldoc,chunk,graph | None | 3 | 2 | 0.2 | 8192 | 3 |
| GPT-6 Luna (Public5) | comment | none,fulldoc,chunk,graph | None | 3 | 2 | 0.2 | 8192 | 3 |
| Qwen3.5-9B | rename | none,fulldoc,chunk,graph | None | 3 | 2 | 0.2 | 1024 | 3 |
| Qwen3.5-9B | comment | none,fulldoc,chunk,graph | None | 3 | 2 | 0.2 | 1024 | 3 |
| Gemini 3.1 Flash-Lite | rename | none,fulldoc,chunk,graph | None | 3 | 2 | 0.2 | 8192 | 3 |
| Gemini 3.1 Flash-Lite | comment | none,fulldoc,chunk,graph | None | 3 | 2 | 0.2 | 8192 | 3 |
| DeepSeek V4 Flash | rename | none,fulldoc,chunk,graph | None | 3 | 2 | 0.2 | 8192 | 3 |
| DeepSeek V4 Flash | comment | none,fulldoc,chunk,graph | None | 3 | 2 | 0.2 | 8192 | 3 |
| Gemma 4 26B | rename | none,fulldoc,chunk,graph | None | 3 | 2 | 0.2 | 2048 | 3 |
| Gemma 4 26B | comment | none,fulldoc,chunk,graph | None | 3 | 2 | 0.2 | 2048 | 3 |
| ablation o3-mini | rename | graph,graph_noex | None | 3 | 2 | 0.2 | 8192 | 3 |
| ablation o3-mini | comment | graph,graph_noex | None | 3 | 2 | 0.2 | 8192 | 3 |
| ablation Luna | rename | graph,graph_noex | None | 3 | 2 | 0.2 | 8192 | 3 |
| ablation Luna | comment | graph,graph_noex | None | 3 | 2 | 0.2 | 8192 | 3 |
| ablation Gemini | rename | graph,graph_noex | None | 3 | 2 | 0.2 | 8192 | 3 |
| ablation Gemini | comment | graph,graph_noex | None | 3 | 2 | 0.2 | 8192 | 3 |
| ablation Gemma (endpoint) | rename | none,fulldoc,chunk,graph,graph_noex | None | 3 | 2 | 0.2 | 2048 | 3 |
| ablation Gemma (endpoint) | comment | none,fulldoc,chunk,graph,graph_noex | None | 3 | 2 | 0.2 | 2048 | 3 |

## 9.1b Retrieved items per trial and prompt tokens

| family | task | model | condition | trials | items mean | min | max | prompt tokens |
|---|---|---|---|---|---|---|---|---|
| GSCS | rename | o3-mini | none | 366 | 0.00 | 0 | 0 | 467.1 |
| GSCS | rename | o3-mini | fulldoc | 366 | 1.00 | 1 | 1 | 1919.1 |
| GSCS | rename | o3-mini | chunk | 366 | 3.00 | 3 | 3 | 884.3 |
| GSCS | rename | o3-mini | graph | 366 | 1.00 | 1 | 1 | 594.6 |
| GSCS | rename | GPT-6 Luna | none | 366 | 0.00 | 0 | 0 | 467.1 |
| GSCS | rename | GPT-6 Luna | fulldoc | 366 | 1.00 | 1 | 1 | 1919.1 |
| GSCS | rename | GPT-6 Luna | chunk | 366 | 3.00 | 3 | 3 | 884.3 |
| GSCS | rename | GPT-6 Luna | graph | 366 | 1.00 | 1 | 1 | 594.6 |
| GSCS | rename | Qwen3.5-9B | none | 366 | 0.00 | 0 | 0 | 503.1 |
| GSCS | rename | Qwen3.5-9B | fulldoc | 366 | 1.00 | 1 | 1 | 2019.1 |
| GSCS | rename | Qwen3.5-9B | chunk | 366 | 3.00 | 3 | 3 | 941.8 |
| GSCS | rename | Qwen3.5-9B | graph | 366 | 1.00 | 1 | 1 | 633.0 |
| GSCS | rename | Gemini 3.1 Flash-Lite | none | 366 | 0.00 | 0 | 0 | 518.6 |
| GSCS | rename | Gemini 3.1 Flash-Lite | fulldoc | 366 | 1.00 | 1 | 1 | 2080.5 |
| GSCS | rename | Gemini 3.1 Flash-Lite | chunk | 366 | 3.00 | 3 | 3 | 975.1 |
| GSCS | rename | Gemini 3.1 Flash-Lite | graph | 366 | 1.00 | 1 | 1 | 650.1 |
| GSCS | rename | DeepSeek V4 Flash | none | 366 | 0.00 | 0 | 0 | 549.1 |
| GSCS | rename | DeepSeek V4 Flash | fulldoc | 366 | 1.00 | 1 | 1 | 2037.1 |
| GSCS | rename | DeepSeek V4 Flash | chunk | 366 | 3.00 | 3 | 3 | 979.3 |
| GSCS | rename | DeepSeek V4 Flash | graph | 366 | 1.00 | 1 | 1 | 686.0 |
| GSCS | rename | Gemma 4 26B | none | 366 | 0.00 | 0 | 0 | 531.5 |
| GSCS | rename | Gemma 4 26B | fulldoc | 366 | 1.00 | 1 | 1 | 2093.5 |
| GSCS | rename | Gemma 4 26B | chunk | 366 | 3.00 | 3 | 3 | 987.9 |
| GSCS | rename | Gemma 4 26B | graph | 366 | 1.00 | 1 | 1 | 663.1 |
| GSCS | comment | o3-mini | none | 36 | 0.00 | 0 | 0 | 364.7 |
| GSCS | comment | o3-mini | fulldoc | 36 | 1.00 | 1 | 1 | 1816.7 |
| GSCS | comment | o3-mini | chunk | 36 | 3.00 | 3 | 3 | 755.1 |
| GSCS | comment | o3-mini | graph | 36 | 1.00 | 1 | 1 | 614.7 |
| GSCS | comment | GPT-6 Luna | none | 36 | 0.00 | 0 | 0 | 364.7 |
| GSCS | comment | GPT-6 Luna | fulldoc | 36 | 1.00 | 1 | 1 | 1816.7 |
| GSCS | comment | GPT-6 Luna | chunk | 36 | 3.00 | 3 | 3 | 755.1 |
| GSCS | comment | GPT-6 Luna | graph | 36 | 1.00 | 1 | 1 | 614.7 |
| GSCS | comment | Qwen3.5-9B | none | 36 | 0.00 | 0 | 0 | 393.5 |
| GSCS | comment | Qwen3.5-9B | fulldoc | 36 | 1.00 | 1 | 1 | 1909.5 |
| GSCS | comment | Qwen3.5-9B | chunk | 36 | 3.00 | 3 | 3 | 800.8 |
| GSCS | comment | Qwen3.5-9B | graph | 36 | 1.00 | 1 | 1 | 653.5 |
| GSCS | comment | Gemini 3.1 Flash-Lite | none | 36 | 0.00 | 0 | 0 | 407.7 |
| GSCS | comment | Gemini 3.1 Flash-Lite | fulldoc | 36 | 1.00 | 1 | 1 | 1970.3 |
| GSCS | comment | Gemini 3.1 Flash-Lite | chunk | 36 | 3.00 | 3 | 3 | 831.2 |
| GSCS | comment | Gemini 3.1 Flash-Lite | graph | 36 | 1.00 | 1 | 1 | 664.3 |
| GSCS | comment | DeepSeek V4 Flash | none | 36 | 0.00 | 0 | 0 | 426.1 |
| GSCS | comment | DeepSeek V4 Flash | fulldoc | 36 | 1.00 | 1 | 1 | 1900.8 |
| GSCS | comment | DeepSeek V4 Flash | chunk | 36 | 3.00 | 3 | 3 | 813.7 |
| GSCS | comment | DeepSeek V4 Flash | graph | 36 | 1.00 | 1 | 1 | 683.7 |
| GSCS | comment | Gemma 4 26B | none | 36 | 0.00 | 0 | 0 | 420.3 |
| GSCS | comment | Gemma 4 26B | fulldoc | 36 | 1.00 | 1 | 1 | 1982.3 |
| GSCS | comment | Gemma 4 26B | chunk | 36 | 3.00 | 3 | 3 | 844.2 |
| GSCS | comment | Gemma 4 26B | graph | 36 | 1.00 | 1 | 1 | 677.3 |
| Public5 | rename | GPT-6 Luna | none | 300 | 0.00 | 0 | 0 | 422.9 |
| Public5 | rename | GPT-6 Luna | fulldoc | 300 | 1.00 | 1 | 1 | 1797.7 |
| Public5 | rename | GPT-6 Luna | chunk | 300 | 3.00 | 3 | 3 | 609.7 |
| Public5 | rename | GPT-6 Luna | graph | 300 | 1.37 | 1 | 3 | 583.7 |
| Public5 | comment | GPT-6 Luna | none | 267 | 0.00 | 0 | 0 | 417.0 |
| Public5 | comment | GPT-6 Luna | fulldoc | 267 | 1.00 | 1 | 1 | 1798.0 |
| Public5 | comment | GPT-6 Luna | chunk | 267 | 3.00 | 3 | 3 | 615.4 |
| Public5 | comment | GPT-6 Luna | graph | 267 | 1.22 | 0 | 3 | 607.2 |
| Ablation | rename | o3-mini | graph | 366 | 1.00 | 1 | 1 | 594.6 |
| Ablation | rename | o3-mini | graph_noex | 366 | 1.00 | 1 | 1 | 555.4 |
| Ablation | rename | GPT-6 Luna | graph | 366 | 1.00 | 1 | 1 | 594.6 |
| Ablation | rename | GPT-6 Luna | graph_noex | 366 | 1.00 | 1 | 1 | 555.4 |
| Ablation | rename | Gemini 3.1 Flash-Lite | graph | 366 | 1.00 | 1 | 1 | 650.1 |
| Ablation | rename | Gemini 3.1 Flash-Lite | graph_noex | 366 | 1.00 | 1 | 1 | 608.4 |
| Ablation | rename | Gemma 4 26B (endpoint) | none | 366 | 0.00 | 0 | 0 | 531.5 |
| Ablation | rename | Gemma 4 26B (endpoint) | fulldoc | 366 | 1.00 | 1 | 1 | 2093.5 |
| Ablation | rename | Gemma 4 26B (endpoint) | chunk | 366 | 3.00 | 3 | 3 | 987.9 |
| Ablation | rename | Gemma 4 26B (endpoint) | graph | 366 | 1.00 | 1 | 1 | 663.1 |
| Ablation | rename | Gemma 4 26B (endpoint) | graph_noex | 366 | 1.00 | 1 | 1 | 621.4 |
| Ablation | comment | o3-mini | graph | 36 | 1.00 | 1 | 1 | 614.7 |
| Ablation | comment | o3-mini | graph_noex | 36 | 1.00 | 1 | 1 | 471.7 |
| Ablation | comment | GPT-6 Luna | graph | 36 | 1.00 | 1 | 1 | 614.7 |
| Ablation | comment | GPT-6 Luna | graph_noex | 36 | 1.00 | 1 | 1 | 471.7 |
| Ablation | comment | Gemini 3.1 Flash-Lite | graph | 36 | 1.00 | 1 | 1 | 664.3 |
| Ablation | comment | Gemini 3.1 Flash-Lite | graph_noex | 36 | 1.00 | 1 | 1 | 519.3 |
| Ablation | comment | Gemma 4 26B (endpoint) | none | 36 | 0.00 | 0 | 0 | 420.3 |
| Ablation | comment | Gemma 4 26B (endpoint) | fulldoc | 36 | 1.00 | 1 | 1 | 1982.3 |
| Ablation | comment | Gemma 4 26B (endpoint) | chunk | 36 | 3.00 | 3 | 3 | 844.2 |
| Ablation | comment | Gemma 4 26B (endpoint) | graph | 36 | 1.00 | 1 | 1 | 677.3 |
| Ablation | comment | Gemma 4 26B (endpoint) | graph_noex | 36 | 1.00 | 1 | 1 | 532.3 |

## 9.2 Similarity Index (character) and invalid answers

| family | model | condition | trials | provider errors | invalid (%) | SI before | SI reported | SI valid only | invalid at SI=1 |
|---|---|---|---|---|---|---|---|---|---|
| GSCS | o3-mini | none | 366 | 0 | 0 (0.0) | 0.9901 | 0.9883 | 0.9883 | 0 |
| GSCS | o3-mini | fulldoc | 366 | 0 | 0 (0.0) | 0.9901 | 0.9971 | 0.9971 | 0 |
| GSCS | o3-mini | chunk | 366 | 0 | 0 (0.0) | 0.9901 | 0.9897 | 0.9897 | 0 |
| GSCS | o3-mini | graph | 366 | 0 | 0 (0.0) | 0.9901 | 0.9977 | 0.9977 | 0 |
| GSCS | GPT-6 Luna | none | 366 | 0 | 0 (0.0) | 0.9901 | 0.9962 | 0.9962 | 0 |
| GSCS | GPT-6 Luna | fulldoc | 366 | 0 | 0 (0.0) | 0.9901 | 0.9993 | 0.9993 | 0 |
| GSCS | GPT-6 Luna | chunk | 366 | 0 | 0 (0.0) | 0.9901 | 0.9932 | 0.9932 | 0 |
| GSCS | GPT-6 Luna | graph | 366 | 0 | 0 (0.0) | 0.9901 | 1.0000 | 1.0000 | 0 |
| GSCS | Qwen3.5-9B | none | 366 | 0 | 9 (2.5) | 0.9901 | 0.9873 | 0.9872 | 0 |
| GSCS | Qwen3.5-9B | fulldoc | 366 | 0 | 14 (3.8) | 0.9901 | 0.9941 | 0.9942 | 0 |
| GSCS | Qwen3.5-9B | chunk | 366 | 0 | 5 (1.4) | 0.9901 | 0.9885 | 0.9884 | 0 |
| GSCS | Qwen3.5-9B | graph | 366 | 0 | 1 (0.3) | 0.9901 | 0.9967 | 0.9967 | 0 |
| GSCS | Gemini 3.1 Flash-Lite | none | 366 | 0 | 1 (0.3) | 0.9901 | 0.9931 | 0.9932 | 0 |
| GSCS | Gemini 3.1 Flash-Lite | fulldoc | 366 | 0 | 0 (0.0) | 0.9901 | 0.9989 | 0.9989 | 0 |
| GSCS | Gemini 3.1 Flash-Lite | chunk | 366 | 0 | 1 (0.3) | 0.9901 | 0.9921 | 0.9921 | 0 |
| GSCS | Gemini 3.1 Flash-Lite | graph | 366 | 0 | 0 (0.0) | 0.9901 | 0.9989 | 0.9989 | 0 |
| GSCS | DeepSeek V4 Flash | none | 366 | 0 | 159 (43.4) | 0.9901 | 0.9938 | 0.9975 | 0 |
| GSCS | DeepSeek V4 Flash | fulldoc | 366 | 0 | 11 (3.0) | 0.9901 | 0.9992 | 0.9994 | 0 |
| GSCS | DeepSeek V4 Flash | chunk | 366 | 0 | 42 (11.5) | 0.9901 | 0.9931 | 0.9930 | 0 |
| GSCS | DeepSeek V4 Flash | graph | 366 | 0 | 3 (0.8) | 0.9901 | 0.9991 | 0.9992 | 0 |
| GSCS | Gemma 4 26B | none | 366 | 0 | 1 (0.3) | 0.9901 | 0.9936 | 0.9936 | 0 |
| GSCS | Gemma 4 26B | fulldoc | 366 | 0 | 0 (0.0) | 0.9901 | 0.9991 | 0.9991 | 0 |
| GSCS | Gemma 4 26B | chunk | 366 | 0 | 1 (0.3) | 0.9901 | 0.9921 | 0.9921 | 0 |
| GSCS | Gemma 4 26B | graph | 366 | 0 | 0 (0.0) | 0.9901 | 0.9991 | 0.9991 | 0 |
| Public5 | GPT-6 Luna | none | 300 | 0 | 0 (0.0) | 0.9847 | 0.9985 | 0.9985 | 0 |
| Public5 | GPT-6 Luna | fulldoc | 300 | 0 | 0 (0.0) | 0.9847 | 0.9982 | 0.9982 | 0 |
| Public5 | GPT-6 Luna | chunk | 300 | 0 | 0 (0.0) | 0.9847 | 0.9982 | 0.9982 | 0 |
| Public5 | GPT-6 Luna | graph | 300 | 0 | 0 (0.0) | 0.9847 | 0.9981 | 0.9981 | 0 |

## 9.3 MUST-only sensitivity (Public5, Luna, rename)

units 100; core set contains SHOULD/MAY: 17; core set has no MUST rule: 15; no core rule: 0; recompute mismatches vs recorded core_ok: 0; GSCS naming-rule severities: {'MUST': 6}

| condition | units (all core) | core-rule % (recorded definition) | units (MUST only) | MUST-only % |
|---|---|---|---|---|
| none | 100 | 99.7 | 85 | 99.6 |
| fulldoc | 100 | 100.0 | 85 | 100.0 |
| chunk | 100 | 99.0 | 85 | 98.8 |
| graph | 100 | 100.0 | 85 | 100.0 |

## 9.4 Repository-level cluster bootstrap (Public5, Luna)

| task | statistic | value | unit bootstrap 95% | repository bootstrap 95% | units | repos |
|---|---|---|---|---|---|---|
| rename | none | 99.7 | 99.0–100.0 | 98.8–100.0 | 100 | 29 |
| rename | fulldoc | 100.0 | 100.0–100.0 | 100.0–100.0 | 100 | 29 |
| rename | chunk | 99.0 | 97.0–100.0 | 96.5–100.0 | 100 | 29 |
| rename | graph | 100.0 | 100.0–100.0 | 100.0–100.0 | 100 | 29 |
| rename | graph - none (pp) | 0.3 | 0.0–1.0 | 0.0–1.2 | 100 | 29 |
| rename | graph - chunk (pp) | 1.0 | 0.0–3.0 | 0.0–3.4 | 100 | 29 |
| rename | graph - fulldoc (pp) | 0.0 | 0.0–0.0 | 0.0–0.0 | 100 | 29 |
| comment | none | 99.6 | 98.8–100.0 | 98.8–100.0 | 86 | 21 |
| comment | fulldoc | 98.8 | 96.9–100.0 | 97.1–100.0 | 86 | 21 |
| comment | chunk | 99.6 | 98.8–100.0 | 98.7–100.0 | 86 | 21 |
| comment | graph | 99.6 | 98.8–100.0 | 98.7–100.0 | 86 | 21 |
| comment | graph - none (pp) | 0.0 | -1.2–1.2 | -1.1–1.1 | 86 | 21 |
| comment | graph - chunk (pp) | 0.0 | 0.0–0.0 | 0.0–0.0 | 86 | 21 |
| comment | graph - fulldoc (pp) | 0.8 | 0.0–1.9 | 0.0–1.7 | 86 | 21 |

## 9.5 GSCS chunk retrieval: section-level hit (exploratory; ADDENDUM 9.5)

| model | chunk trials | section hit % | core-rule % when hit (n) | core-rule % when missed (n) |
|---|---|---|---|---|
| o3-mini | 366 | 17.2 | 87.3 (63) | 57.4 (303) |
| GPT-6 Luna | 366 | 17.2 | 98.4 (63) | 72.3 (303) |
| Qwen3.5-9B | 366 | 17.2 | 47.6 (63) | 47.5 (303) |
| Gemini 3.1 Flash-Lite | 366 | 17.2 | 92.1 (63) | 64.0 (303) |
| DeepSeek V4 Flash | 366 | 17.2 | 93.7 (63) | 61.4 (303) |
| Gemma 4 26B | 366 | 17.2 | 57.1 (63) | 69.3 (303) |
