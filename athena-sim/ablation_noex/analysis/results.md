# graph_noex ablation — results (exploratory; analysis fixed before the runs)

### o3-mini — rename

| condition | source | trials | API errors | primary % [95% CI] | prefix_match % | exact_match % |
|---|---|---|---|---|---|---|
| graph | new | 366 | 0 | 100.0 [99–100] | 100.0 | 86.3 |
| graph_noex | new | 366 | 0 | 95.4 [93–97] | 92.8 | 80.3 |
| none | orig | 366 | 0 | 24.3 [20–29] | 20.3 | 23.0 |
| fulldoc | orig | 366 | 0 | 97.8 [96–99] | 100.0 | 78.4 |
| chunk | orig | 366 | 0 | 62.6 [58–67] | 86.1 | 38.8 |
| graph_orig | orig | 366 | 0 | 100.0 [99–100] | 100.0 | 85.5 |

| comparison | units | better / worse / ties | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|
| E: examples (graph vs graph_noex) | 122 | 8 / 0 / 114 | +4.6 | 0.00781 | 0.0234 |
| S: selection vs chunk (graph_noex vs chunk) | 122 | 50 / 7 / 65 | +32.8 | 4.24e-09 | 1.69e-08 |
| S: selection vs full document (graph_noex vs fulldoc) | 122 | 5 / 8 / 109 | -2.5 | 0.581 | 1 |
| noex vs none (graph_noex vs none) | 122 | 100 / 0 / 22 | +71.0 | 1.58e-30 | 7.89e-30 |
| replication: graph re-run vs original (graph vs graph_orig) | 122 | 0 / 0 / 122 | +0.0 | 1 | 1 |

### o3-mini — comment

| condition | source | trials | API errors | primary % [95% CI] |  |
|---|---|---|---|---|
| graph | new | 36 | 0 | 100.0 [90–100] |  |
| graph_noex | new | 36 | 0 | 100.0 [90–100] |  |
| none | orig | 36 | 0 | 0.0 [0–10] |  |
| fulldoc | orig | 36 | 0 | 88.9 [75–96] |  |
| chunk | orig | 36 | 0 | 80.6 [65–90] |  |
| graph_orig | orig | 36 | 0 | 100.0 [90–100] |  |

| comparison | units | better / worse / ties | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|
| E: examples (graph vs graph_noex) | 12 | 0 / 0 / 12 | +0.0 | 1 | 1 |
| S: selection vs chunk (graph_noex vs chunk) | 12 | 3 / 0 / 9 | +19.4 | 0.25 | 0.75 |
| S: selection vs full document (graph_noex vs fulldoc) | 12 | 4 / 0 / 8 | +11.1 | 0.125 | 0.5 |
| noex vs none (graph_noex vs none) | 12 | 12 / 0 / 0 | +100.0 | 0.000488 | 0.00244 |
| replication: graph re-run vs original (graph vs graph_orig) | 12 | 0 / 0 / 12 | +0.0 | 1 | 1 |

### GPT-6 Luna — rename

| condition | source | trials | API errors | primary % [95% CI] | prefix_match % | exact_match % |
|---|---|---|---|---|---|---|
| graph | new | 366 | 0 | 100.0 [99–100] | 100.0 | 99.5 |
| graph_noex | new | 366 | 0 | 98.6 [97–99] | 97.9 | 92.6 |
| none | orig | 366 | 0 | 46.4 [41–52] | 44.7 | 43.2 |
| fulldoc | orig | 366 | 0 | 99.5 [98–100] | 100.0 | 88.8 |
| chunk | orig | 366 | 0 | 76.8 [72–81] | 92.8 | 56.6 |
| graph_orig | orig | 366 | 0 | 100.0 [99–100] | 100.0 | 99.5 |

| comparison | units | better / worse / ties | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|
| E: examples (graph vs graph_noex) | 122 | 2 / 0 / 120 | +1.4 | 0.5 | 1 |
| S: selection vs chunk (graph_noex vs chunk) | 122 | 34 / 2 / 86 | +21.9 | 1.94e-08 | 7.76e-08 |
| S: selection vs full document (graph_noex vs fulldoc) | 122 | 2 / 2 / 118 | -0.8 | 1 | 1 |
| noex vs none (graph_noex vs none) | 122 | 71 / 0 / 51 | +52.2 | 8.47e-22 | 4.24e-21 |
| replication: graph re-run vs original (graph vs graph_orig) | 122 | 0 / 0 / 122 | +0.0 | 1 | 1 |

### GPT-6 Luna — comment

| condition | source | trials | API errors | primary % [95% CI] |  |
|---|---|---|---|---|
| graph | new | 36 | 0 | 100.0 [90–100] |  |
| graph_noex | new | 36 | 0 | 100.0 [90–100] |  |
| none | orig | 36 | 0 | 0.0 [0–10] |  |
| fulldoc | orig | 36 | 0 | 27.8 [16–44] |  |
| chunk | orig | 36 | 0 | 13.9 [6–29] |  |
| graph_orig | orig | 36 | 0 | 100.0 [90–100] |  |

| comparison | units | better / worse / ties | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|
| E: examples (graph vs graph_noex) | 12 | 0 / 0 / 12 | +0.0 | 1 | 1 |
| S: selection vs chunk (graph_noex vs chunk) | 12 | 12 / 0 / 0 | +86.1 | 0.000488 | 0.00244 |
| S: selection vs full document (graph_noex vs fulldoc) | 12 | 12 / 0 / 0 | +72.2 | 0.000488 | 0.00244 |
| noex vs none (graph_noex vs none) | 12 | 12 / 0 / 0 | +100.0 | 0.000488 | 0.00244 |
| replication: graph re-run vs original (graph vs graph_orig) | 12 | 0 / 0 / 12 | +0.0 | 1 | 1 |

### Gemini 3.1 Flash-Lite — rename

| condition | source | trials | API errors | primary % [95% CI] | prefix_match % | exact_match % |
|---|---|---|---|---|---|---|
| graph | new | 366 | 0 | 100.0 [99–100] | 100.0 | 91.5 |
| graph_noex | new | 366 | 0 | 98.4 [96–99] | 97.5 | 84.7 |
| none | orig | 366 | 0 | 39.1 [34–44] | 38.8 | 37.2 |
| fulldoc | orig | 366 | 0 | 99.2 [98–100] | 100.0 | 91.3 |
| chunk | orig | 366 | 0 | 68.9 [64–73] | 84.4 | 51.4 |
| graph_orig | orig | 366 | 0 | 100.0 [99–100] | 100.0 | 91.0 |

| comparison | units | better / worse / ties | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|
| E: examples (graph vs graph_noex) | 122 | 2 / 0 / 120 | +1.6 | 0.5 | 1 |
| S: selection vs chunk (graph_noex vs chunk) | 122 | 43 / 2 / 77 | +29.5 | 5.89e-11 | 2.36e-10 |
| S: selection vs full document (graph_noex vs fulldoc) | 122 | 2 / 2 / 118 | -0.8 | 1 | 1 |
| noex vs none (graph_noex vs none) | 122 | 81 / 0 / 41 | +59.3 | 8.27e-25 | 4.14e-24 |
| replication: graph re-run vs original (graph vs graph_orig) | 122 | 0 / 0 / 122 | +0.0 | 1 | 1 |

### Gemini 3.1 Flash-Lite — comment

| condition | source | trials | API errors | primary % [95% CI] |  |
|---|---|---|---|---|
| graph | new | 36 | 0 | 100.0 [90–100] |  |
| graph_noex | new | 36 | 0 | 100.0 [90–100] |  |
| none | orig | 36 | 0 | 0.0 [0–10] |  |
| fulldoc | orig | 36 | 0 | 94.4 [82–98] |  |
| chunk | orig | 36 | 0 | 83.3 [68–92] |  |
| graph_orig | orig | 36 | 0 | 100.0 [90–100] |  |

| comparison | units | better / worse / ties | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|
| E: examples (graph vs graph_noex) | 12 | 0 / 0 / 12 | +0.0 | 1 | 1 |
| S: selection vs chunk (graph_noex vs chunk) | 12 | 2 / 0 / 10 | +16.7 | 0.5 | 1 |
| S: selection vs full document (graph_noex vs fulldoc) | 12 | 2 / 0 / 10 | +5.6 | 0.5 | 1 |
| noex vs none (graph_noex vs none) | 12 | 12 / 0 / 0 | +100.0 | 0.000488 | 0.00244 |
| replication: graph re-run vs original (graph vs graph_orig) | 12 | 0 / 0 / 12 | +0.0 | 1 | 1 |

### Gemma 4 26B (hosted API) — rename

| condition | source | trials | API errors | primary % [95% CI] | prefix_match % | exact_match % |
|---|---|---|---|---|---|---|
| graph | new | 366 | 0 | 100.0 [99–100] | 100.0 | 91.3 |
| graph_noex | new | 366 | 0 | 100.0 [99–100] | 100.0 | 88.8 |
| none | new | 366 | 0 | 33.9 [29–39] | 38.0 | 32.2 |
| fulldoc | new | 366 | 0 | 95.9 [93–98] | 100.0 | 91.8 |
| chunk | new | 366 | 0 | 66.9 [62–72] | 86.9 | 51.4 |

| comparison | units | better / worse / ties | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|
| E: examples (graph vs graph_noex) | 122 | 0 / 0 / 122 | +0.0 | 1 | 1 |
| S: selection vs chunk (graph_noex vs chunk) | 122 | 44 / 0 / 78 | +33.1 | 1.14e-13 | 3.41e-13 |
| S: selection vs full document (graph_noex vs fulldoc) | 122 | 8 / 0 / 114 | +4.1 | 0.00781 | 0.0156 |
| noex vs none (graph_noex vs none) | 122 | 88 / 0 / 34 | +66.1 | 6.46e-27 | 3.23e-26 |
| graph vs none (same run) (graph vs none) | 122 | 88 / 0 / 34 | +66.1 | 6.46e-27 | 3.23e-26 |

### Gemma 4 26B (hosted API) — comment

| condition | source | trials | API errors | primary % [95% CI] |  |
|---|---|---|---|---|
| graph | new | 36 | 0 | 100.0 [90–100] |  |
| graph_noex | new | 36 | 0 | 100.0 [90–100] |  |
| none | new | 36 | 0 | 0.0 [0–10] |  |
| fulldoc | new | 36 | 0 | 100.0 [90–100] |  |
| chunk | new | 36 | 0 | 83.3 [68–92] |  |

| comparison | units | better / worse / ties | mean diff (pp) | p | p (Holm) |
|---|---|---|---|---|---|
| E: examples (graph vs graph_noex) | 12 | 0 / 0 / 12 | +0.0 | 1 | 1 |
| S: selection vs chunk (graph_noex vs chunk) | 12 | 2 / 0 / 10 | +16.7 | 0.5 | 1 |
| S: selection vs full document (graph_noex vs fulldoc) | 12 | 0 / 0 / 12 | +0.0 | 1 | 1 |
| noex vs none (graph_noex vs none) | 12 | 12 / 0 / 0 | +100.0 | 0.000488 | 0.00244 |
| graph vs none (same run) (graph vs none) | 12 | 12 / 0 / 0 | +100.0 | 0.000488 | 0.00244 |
