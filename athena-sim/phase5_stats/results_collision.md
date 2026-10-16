# 5.2 Collision and rename-safe (exploratory; see ADDENDUM.md)

collision = proposed name occurs as a whole word elsewhere in the snippet (scope-blind upper bound); rename-safe = core-rule compliant AND no collision. Rates over all trials.

| family | model | condition | trials | core-rule % | collision % (n) | rename-safe % |
|---|---|---|---|---|---|---|
| GSCS | o3-mini | none | 366 | 24.3 | 2.2 (8) | 24.3 |
| GSCS | o3-mini | fulldoc | 366 | 97.8 | 0.0 (0) | 97.8 |
| GSCS | o3-mini | chunk | 366 | 62.6 | 0.8 (3) | 62.6 |
| GSCS | o3-mini | graph | 366 | 100.0 | 0.0 (0) | 100.0 |
| GSCS | GPT-6 Luna | none | 366 | 46.4 | 3.0 (11) | 46.2 |
| GSCS | GPT-6 Luna | fulldoc | 366 | 99.5 | 0.0 (0) | 99.5 |
| GSCS | GPT-6 Luna | chunk | 366 | 76.8 | 0.0 (0) | 76.8 |
| GSCS | GPT-6 Luna | graph | 366 | 100.0 | 0.0 (0) | 100.0 |
| GSCS | Qwen3.5-9B | none | 366 | 20.2 | 4.6 (17) | 20.2 |
| GSCS | Qwen3.5-9B | fulldoc | 366 | 87.4 | 1.1 (4) | 86.3 |
| GSCS | Qwen3.5-9B | chunk | 366 | 47.5 | 2.2 (8) | 46.7 |
| GSCS | Qwen3.5-9B | graph | 366 | 93.7 | 0.0 (0) | 93.7 |
| GSCS | Gemini 3.1 Flash-Lite | none | 366 | 39.1 | 3.0 (11) | 39.1 |
| GSCS | Gemini 3.1 Flash-Lite | fulldoc | 366 | 99.2 | 0.0 (0) | 99.2 |
| GSCS | Gemini 3.1 Flash-Lite | chunk | 366 | 68.9 | 0.0 (0) | 68.9 |
| GSCS | Gemini 3.1 Flash-Lite | graph | 366 | 100.0 | 0.0 (0) | 100.0 |
| GSCS | DeepSeek V4 Flash | none | 366 | 30.3 | 1.4 (5) | 30.3 |
| GSCS | DeepSeek V4 Flash | fulldoc | 366 | 96.4 | 0.0 (0) | 96.4 |
| GSCS | DeepSeek V4 Flash | chunk | 366 | 66.9 | 0.0 (0) | 66.9 |
| GSCS | DeepSeek V4 Flash | graph | 366 | 99.2 | 0.0 (0) | 99.2 |
| GSCS | Gemma 4 26B | none | 366 | 35.8 | 3.8 (14) | 35.8 |
| GSCS | Gemma 4 26B | fulldoc | 366 | 96.2 | 0.0 (0) | 96.2 |
| GSCS | Gemma 4 26B | chunk | 366 | 67.2 | 0.0 (0) | 67.2 |
| GSCS | Gemma 4 26B | graph | 366 | 100.0 | 0.0 (0) | 100.0 |
| GSCS | rule-based fixer | none | 366 | 25.4 | 0.0 (0) | 25.4 |
| GSCS | rule-based fixer | fulldoc | 366 | 25.4 | 0.0 (0) | 25.4 |
| GSCS | rule-based fixer | chunk | 366 | 25.4 | 0.0 (0) | 25.4 |
| GSCS | rule-based fixer | graph | 366 | 25.4 | 0.0 (0) | 25.4 |
| Public5 | GPT-6 Luna (Public5) | none | 300 | 99.7 | 1.7 (5) | 98.0 |
| Public5 | GPT-6 Luna (Public5) | fulldoc | 300 | 100.0 | 1.0 (3) | 99.0 |
| Public5 | GPT-6 Luna (Public5) | chunk | 300 | 99.0 | 1.0 (3) | 98.0 |
| Public5 | GPT-6 Luna (Public5) | graph | 300 | 100.0 | 1.0 (3) | 99.0 |
| Ablation (GSCS) | o3-mini (ablation) | graph | 366 | 100.0 | 0.0 (0) | 100.0 |
| Ablation (GSCS) | o3-mini (ablation) | graph_noex | 366 | 95.4 | 0.0 (0) | 95.4 |
| Ablation (GSCS) | GPT-6 Luna (ablation) | graph | 366 | 100.0 | 0.0 (0) | 100.0 |
| Ablation (GSCS) | GPT-6 Luna (ablation) | graph_noex | 366 | 98.6 | 0.0 (0) | 98.6 |
| Ablation (GSCS) | Gemini 3.1 Flash-Lite (ablation) | graph | 366 | 100.0 | 0.0 (0) | 100.0 |
| Ablation (GSCS) | Gemini 3.1 Flash-Lite (ablation) | graph_noex | 366 | 98.4 | 0.0 (0) | 98.4 |
| Ablation (GSCS) | Gemma 4 26B via endpoint (ablation) | none | 366 | 33.9 | 3.6 (13) | 33.9 |
| Ablation (GSCS) | Gemma 4 26B via endpoint (ablation) | fulldoc | 366 | 95.9 | 0.0 (0) | 95.9 |
| Ablation (GSCS) | Gemma 4 26B via endpoint (ablation) | chunk | 366 | 66.9 | 0.0 (0) | 66.9 |
| Ablation (GSCS) | Gemma 4 26B via endpoint (ablation) | graph | 366 | 100.0 | 0.0 (0) | 100.0 |
| Ablation (GSCS) | Gemma 4 26B via endpoint (ablation) | graph_noex | 366 | 100.0 | 0.0 (0) | 100.0 |

## Collision flag vs compile/test outcome (GSCS, applied renames)

| collision flagged | behaviour unchanged | behaviour changed |
|---|---|---|
| True | 74 | 7 |
| False | 8817 | 0 |
| None | 0 | 0 |

Behaviour-changing trials:
- ('Qwen3.5-9B', 'gscs_cpp_004__str_new_name__strip_prefix', 'fulldoc', 0) -> str_student_name (wrong_output; collision=True)
- ('Qwen3.5-9B', 'gscs_cpp_004__str_new_name__strip_prefix', 'fulldoc', 1) -> str_student_name (wrong_output; collision=True)
- ('Qwen3.5-9B', 'gscs_cpp_004__str_new_name__strip_prefix', 'chunk', 1) -> str_student_name (wrong_output; collision=True)
- ('Qwen3.5-9B', 'gscs_python_005__str_price_text__camel_no_prefix', 'fulldoc', 1) -> f_price (wrong_output; collision=True)
- ('Qwen3.5-9B', 'gscs_python_005__str_price_text__camel_no_prefix', 'chunk', 1) -> f_price (wrong_output; collision=True)
- ('Qwen3.5-9B', 'gscs_python_005__str_price_text__camel_no_prefix', 'fulldoc', 2) -> f_price (wrong_output; collision=True)
- ('Qwen3.5-9B', 'gscs_python_005__str_price_text__camel_no_prefix', 'chunk', 2) -> f_price (wrong_output; collision=True)
