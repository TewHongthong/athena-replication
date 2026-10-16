# Phase 10 results (exploratory; see ADDENDUM.md)

## 10.1a GSCS rename, main runs

| model | comparison | level | n | better/worse/ties | mean diff pp | p | Holm p |
|---|---|---|---|---|---|---|---|
| o3-mini | fulldoc vs none | program | 12 | 12/0/0 | +73.1 | 0.000488 | 0.00146 |
| o3-mini | chunk vs none | program | 12 | 12/0/0 | +38.2 | 0.000488 | 0.00146 |
| o3-mini | graph vs none | program | 12 | 12/0/0 | +75.3 | 0.000488 | 0.00146 |
| o3-mini | graph vs chunk | program | 12 | 12/0/0 | +37.2 | 0.000488 | - |
| o3-mini | graph vs fulldoc | program | 12 | 4/0/8 | +2.3 | 0.125 | - |
| o3-mini | fulldoc vs none | unit | 122 | 103/0/19 | +73.5 | 1.97e-31 | 5.92e-31 |
| o3-mini | chunk vs none | unit | 122 | 73/13/36 | +38.3 | 2.72e-11 | 2.72e-11 |
| o3-mini | graph vs none | unit | 122 | 103/0/19 | +75.7 | 1.97e-31 | 5.92e-31 |
| o3-mini | graph vs chunk | unit | 122 | 52/0/70 | +37.4 | 4.44e-16 | - |
| o3-mini | graph vs fulldoc | unit | 122 | 5/0/117 | +2.2 | 0.0625 | - |
| GPT-6 Luna | fulldoc vs none | program | 12 | 12/0/0 | +53.7 | 0.000488 | 0.00146 |
| GPT-6 Luna | chunk vs none | program | 12 | 11/1/0 | +31.3 | 0.00635 | 0.00635 |
| GPT-6 Luna | graph vs none | program | 12 | 12/0/0 | +54.2 | 0.000488 | 0.00146 |
| GPT-6 Luna | graph vs chunk | program | 12 | 11/0/1 | +22.9 | 0.000977 | - |
| GPT-6 Luna | graph vs fulldoc | program | 12 | 2/0/10 | +0.5 | 0.5 | - |
| GPT-6 Luna | fulldoc vs none | unit | 122 | 72/0/50 | +53.0 | 4.24e-22 | 1.27e-21 |
| GPT-6 Luna | chunk vs none | unit | 122 | 64/18/40 | +30.3 | 3.32e-07 | 3.32e-07 |
| GPT-6 Luna | graph vs none | unit | 122 | 72/0/50 | +53.6 | 4.24e-22 | 1.27e-21 |
| GPT-6 Luna | graph vs chunk | unit | 122 | 34/0/88 | +23.2 | 1.16e-10 | - |
| GPT-6 Luna | graph vs fulldoc | unit | 122 | 2/0/120 | +0.5 | 0.5 | - |
| Qwen3.5-9B | fulldoc vs none | program | 12 | 12/0/0 | +67.4 | 0.000488 | 0.00146 |
| Qwen3.5-9B | chunk vs none | program | 12 | 11/1/0 | +27.1 | 0.00635 | 0.00635 |
| Qwen3.5-9B | graph vs none | program | 12 | 12/0/0 | +73.7 | 0.000488 | 0.00146 |
| Qwen3.5-9B | graph vs chunk | program | 12 | 12/0/0 | +46.6 | 0.000488 | - |
| Qwen3.5-9B | graph vs fulldoc | program | 12 | 7/4/1 | +6.3 | 0.549 | - |
| Qwen3.5-9B | fulldoc vs none | unit | 122 | 102/0/20 | +67.2 | 3.94e-31 | 7.89e-31 |
| Qwen3.5-9B | chunk vs none | unit | 122 | 61/22/39 | +27.3 | 2.18e-05 | 2.18e-05 |
| Qwen3.5-9B | graph vs none | unit | 122 | 109/0/13 | +73.5 | 3.08e-33 | 9.24e-33 |
| Qwen3.5-9B | graph vs chunk | unit | 122 | 73/11/38 | +46.2 | 2.25e-12 | - |
| Qwen3.5-9B | graph vs fulldoc | unit | 122 | 25/13/84 | +6.3 | 0.073 | - |
| Gemini 3.1 Flash-Lite | fulldoc vs none | program | 12 | 12/0/0 | +60.2 | 0.000488 | 0.00146 |
| Gemini 3.1 Flash-Lite | chunk vs none | program | 12 | 12/0/0 | +30.3 | 0.000488 | 0.00146 |
| Gemini 3.1 Flash-Lite | graph vs none | program | 12 | 12/0/0 | +61.2 | 0.000488 | 0.00146 |
| Gemini 3.1 Flash-Lite | graph vs chunk | program | 12 | 11/0/1 | +30.9 | 0.000977 | - |
| Gemini 3.1 Flash-Lite | graph vs fulldoc | program | 12 | 2/0/10 | +1.0 | 0.5 | - |
| Gemini 3.1 Flash-Lite | fulldoc vs none | unit | 122 | 83/0/39 | +60.1 | 2.07e-25 | 6.2e-25 |
| Gemini 3.1 Flash-Lite | chunk vs none | unit | 122 | 60/17/45 | +29.8 | 8.91e-07 | 8.91e-07 |
| Gemini 3.1 Flash-Lite | graph vs none | unit | 122 | 83/0/39 | +60.9 | 2.07e-25 | 6.2e-25 |
| Gemini 3.1 Flash-Lite | graph vs chunk | unit | 122 | 43/0/79 | +31.1 | 2.27e-13 | - |
| Gemini 3.1 Flash-Lite | graph vs fulldoc | unit | 122 | 2/0/120 | +0.8 | 0.5 | - |
| DeepSeek V4 Flash | fulldoc vs none | program | 12 | 12/0/0 | +67.0 | 0.000488 | 0.00146 |
| DeepSeek V4 Flash | chunk vs none | program | 12 | 12/0/0 | +37.8 | 0.000488 | 0.00146 |
| DeepSeek V4 Flash | graph vs none | program | 12 | 12/0/0 | +69.6 | 0.000488 | 0.00146 |
| DeepSeek V4 Flash | graph vs chunk | program | 12 | 11/0/1 | +31.8 | 0.000977 | - |
| DeepSeek V4 Flash | graph vs fulldoc | program | 12 | 4/0/8 | +2.5 | 0.125 | - |
| DeepSeek V4 Flash | fulldoc vs none | unit | 122 | 100/0/22 | +66.1 | 1.58e-30 | 4.73e-30 |
| DeepSeek V4 Flash | chunk vs none | unit | 122 | 76/14/32 | +36.6 | 1.78e-11 | 1.78e-11 |
| DeepSeek V4 Flash | graph vs none | unit | 122 | 101/1/20 | +68.9 | 4.06e-29 | 8.13e-29 |
| DeepSeek V4 Flash | graph vs chunk | unit | 122 | 51/2/69 | +32.2 | 3.18e-13 | - |
| DeepSeek V4 Flash | graph vs fulldoc | unit | 122 | 11/3/108 | +2.7 | 0.0574 | - |
| Gemma 4 26B | fulldoc vs none | program | 12 | 12/0/0 | +60.0 | 0.000488 | 0.00146 |
| Gemma 4 26B | chunk vs none | program | 12 | 11/0/1 | +31.1 | 0.000977 | 0.00146 |
| Gemma 4 26B | graph vs none | program | 12 | 12/0/0 | +64.1 | 0.000488 | 0.00146 |
| Gemma 4 26B | graph vs chunk | program | 12 | 11/0/1 | +33.1 | 0.000977 | - |
| Gemma 4 26B | graph vs fulldoc | program | 12 | 6/0/6 | +4.2 | 0.0312 | - |
| Gemma 4 26B | fulldoc vs none | unit | 122 | 79/0/43 | +60.4 | 3.31e-24 | 6.62e-24 |
| Gemma 4 26B | chunk vs none | unit | 122 | 55/12/55 | +31.4 | 1.03e-07 | 1.03e-07 |
| Gemma 4 26B | graph vs none | unit | 122 | 83/0/39 | +64.2 | 2.07e-25 | 6.2e-25 |
| Gemma 4 26B | graph vs chunk | unit | 122 | 41/0/81 | +32.8 | 9.09e-13 | - |
| Gemma 4 26B | graph vs fulldoc | unit | 122 | 6/0/116 | +3.8 | 0.0312 | - |

## 10.1b Ablation (program level, Holm within model x task)

| model | task | comparison | n | better/worse/ties | mean diff pp | p | Holm p |
|---|---|---|---|---|---|---|---|
| o3-mini | rename | graph vs graph_noex | 12 | 5/0/7 | +4.6 | 0.0625 | 0.188 |
| o3-mini | rename | graph_noex vs chunk | 12 | 12/0/0 | +32.6 | 0.000488 | 0.00244 |
| o3-mini | rename | graph_noex vs fulldoc | 12 | 2/5/5 | -2.3 | 0.453 | 0.906 |
| o3-mini | rename | graph_noex vs none | 12 | 12/0/0 | +70.7 | 0.000488 | 0.00244 |
| o3-mini | rename | graph vs graph_orig | 12 | 0/0/12 | +0.0 | 1 | 1 |
| o3-mini | comment | graph vs graph_noex | 12 | 0/0/12 | +0.0 | 1 | 1 |
| o3-mini | comment | graph_noex vs chunk | 12 | 3/0/9 | +19.4 | 0.25 | 0.75 |
| o3-mini | comment | graph_noex vs fulldoc | 12 | 4/0/8 | +11.1 | 0.125 | 0.5 |
| o3-mini | comment | graph_noex vs none | 12 | 12/0/0 | +100.0 | 0.000488 | 0.00244 |
| o3-mini | comment | graph vs graph_orig | 12 | 0/0/12 | +0.0 | 1 | 1 |
| GPT-6 Luna | rename | graph vs graph_noex | 12 | 2/0/10 | +1.4 | 0.5 | 1 |
| GPT-6 Luna | rename | graph_noex vs chunk | 12 | 10/1/1 | +21.5 | 0.0117 | 0.0469 |
| GPT-6 Luna | rename | graph_noex vs fulldoc | 12 | 2/2/8 | -0.8 | 1 | 1 |
| GPT-6 Luna | rename | graph_noex vs none | 12 | 12/0/0 | +52.8 | 0.000488 | 0.00244 |
| GPT-6 Luna | rename | graph vs graph_orig | 12 | 0/0/12 | +0.0 | 1 | 1 |
| GPT-6 Luna | comment | graph vs graph_noex | 12 | 0/0/12 | +0.0 | 1 | 1 |
| GPT-6 Luna | comment | graph_noex vs chunk | 12 | 12/0/0 | +86.1 | 0.000488 | 0.00244 |
| GPT-6 Luna | comment | graph_noex vs fulldoc | 12 | 12/0/0 | +72.2 | 0.000488 | 0.00244 |
| GPT-6 Luna | comment | graph_noex vs none | 12 | 12/0/0 | +100.0 | 0.000488 | 0.00244 |
| GPT-6 Luna | comment | graph vs graph_orig | 12 | 0/0/12 | +0.0 | 1 | 1 |
| Gemini 3.1 Flash-Lite | rename | graph vs graph_noex | 12 | 2/0/10 | +1.7 | 0.5 | 1 |
| Gemini 3.1 Flash-Lite | rename | graph_noex vs chunk | 12 | 11/0/1 | +29.2 | 0.000977 | 0.00391 |
| Gemini 3.1 Flash-Lite | rename | graph_noex vs fulldoc | 12 | 2/2/8 | -0.6 | 1 | 1 |
| Gemini 3.1 Flash-Lite | rename | graph_noex vs none | 12 | 12/0/0 | +59.5 | 0.000488 | 0.00244 |
| Gemini 3.1 Flash-Lite | rename | graph vs graph_orig | 12 | 0/0/12 | +0.0 | 1 | 1 |
| Gemini 3.1 Flash-Lite | comment | graph vs graph_noex | 12 | 0/0/12 | +0.0 | 1 | 1 |
| Gemini 3.1 Flash-Lite | comment | graph_noex vs chunk | 12 | 2/0/10 | +16.7 | 0.5 | 1 |
| Gemini 3.1 Flash-Lite | comment | graph_noex vs fulldoc | 12 | 2/0/10 | +5.6 | 0.5 | 1 |
| Gemini 3.1 Flash-Lite | comment | graph_noex vs none | 12 | 12/0/0 | +100.0 | 0.000488 | 0.00244 |
| Gemini 3.1 Flash-Lite | comment | graph vs graph_orig | 12 | 0/0/12 | +0.0 | 1 | 1 |
| Gemma 4 26B (endpoint) | rename | graph vs graph_noex | 12 | 0/0/12 | +0.0 | 1 | 1 |
| Gemma 4 26B (endpoint) | rename | graph_noex vs chunk | 12 | 11/0/1 | +33.3 | 0.000977 | 0.00293 |
| Gemma 4 26B (endpoint) | rename | graph_noex vs fulldoc | 12 | 7/0/5 | +4.4 | 0.0156 | 0.0312 |
| Gemma 4 26B (endpoint) | rename | graph_noex vs none | 12 | 12/0/0 | +66.2 | 0.000488 | 0.00244 |
| Gemma 4 26B (endpoint) | rename | graph vs none | 12 | 12/0/0 | +66.2 | 0.000488 | 0.00244 |
| Gemma 4 26B (endpoint) | comment | graph vs graph_noex | 12 | 0/0/12 | +0.0 | 1 | 1 |
| Gemma 4 26B (endpoint) | comment | graph_noex vs chunk | 12 | 2/0/10 | +16.7 | 0.5 | 1 |
| Gemma 4 26B (endpoint) | comment | graph_noex vs fulldoc | 12 | 0/0/12 | +0.0 | 1 | 1 |
| Gemma 4 26B (endpoint) | comment | graph_noex vs none | 12 | 12/0/0 | +100.0 | 0.000488 | 0.00244 |
| Gemma 4 26B (endpoint) | comment | graph vs none | 12 | 12/0/0 | +100.0 | 0.000488 | 0.00244 |

## 10.1c Units per program

comment units per program: {'gscs_cpp_001': 1, 'gscs_cpp_002': 1, 'gscs_cpp_005': 1, 'gscs_cpp_004': 1, 'gscs_java_005': 1, 'gscs_java_002': 1, 'gscs_java_001': 1, 'gscs_java_004': 1, 'gscs_python_001': 1, 'gscs_python_002': 1, 'gscs_python_005': 1, 'gscs_python_004': 1}
rename units per program: {'gscs_cpp_001': 11, 'gscs_cpp_002': 10, 'gscs_cpp_004': 12, 'gscs_cpp_005': 9, 'gscs_java_001': 11, 'gscs_java_002': 11, 'gscs_java_004': 9, 'gscs_java_005': 10, 'gscs_python_001': 11, 'gscs_python_002': 10, 'gscs_python_004': 11, 'gscs_python_005': 7}

## 10.2 Behaviour check accounting

```
{
 "trials": 10248,
 "status": {
  "pass": 8891,
  "wrong_output": 7,
  "not_applied": 1350
 },
 "not_applied_reasons": {
  "no valid answer": 248,
  "same as injected": 1102
 },
 "not_applied_by_model": {
  "Qwen3.5-9B": 36,
  "Gemini 3.1 Flash-Lite": 5,
  "DeepSeek V4 Flash": 215,
  "Gemma 4 26B": 2,
  "linter autofix": 1092
 },
 "exec_cache_entries": 894
}
```
