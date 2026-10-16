# 5.1 Cluster bootstrap 95% CIs (exploratory; see ADDENDUM.md)

B = 10000, seed 20261002. unit = resample units with their repeats (primary); snippet = resample snippets (sensitivity). † degenerate bootstrap (all units at ceiling/floor) → exact Clopper–Pearson over units.

## GSCS — rename (core_ok)

| model | condition | trials | units | snippets | rate % | Wilson (trials) | unit bootstrap | snippet bootstrap |
|---|---|---|---|---|---|---|---|---|
| o3-mini | none | 366 | 122 | 12 | 24.3 | 20.2–29.0 | 17.8–31.4 | 14.8–34.9 |
| o3-mini | fulldoc | 366 | 122 | 12 | 97.8 | 95.7–98.9 | 95.6–99.5 | 95.3–99.7 |
| o3-mini | chunk | 366 | 122 | 12 | 62.6 | 57.5–67.4 | 54.1–70.5 | 54.4–71.0 |
| o3-mini | graph | 366 | 122 | 12 | 100.0 | 99.0–100.0 | 97.0–100.0 † | 100.0–100.0 |
| GPT-6 Luna | none | 366 | 122 | 12 | 46.4 | 41.4–51.6 | 37.7–55.2 | 35.9–57.2 |
| GPT-6 Luna | fulldoc | 366 | 122 | 12 | 99.5 | 98.0–99.9 | 98.6–100.0 | 98.7–100.0 |
| GPT-6 Luna | chunk | 366 | 122 | 12 | 76.8 | 72.2–80.8 | 69.4–83.6 | 72.1–82.6 |
| GPT-6 Luna | graph | 366 | 122 | 12 | 100.0 | 99.0–100.0 | 97.0–100.0 † | 100.0–100.0 |
| Qwen3.5-9B | none | 366 | 122 | 12 | 20.2 | 16.4–24.6 | 14.8–26.2 | 15.3–25.6 |
| Qwen3.5-9B | fulldoc | 366 | 122 | 12 | 87.4 | 83.6–90.4 | 82.2–92.1 | 82.1–92.6 |
| Qwen3.5-9B | chunk | 366 | 122 | 12 | 47.5 | 42.5–52.7 | 39.3–55.5 | 40.2–53.4 |
| Qwen3.5-9B | graph | 366 | 122 | 12 | 93.7 | 90.7–95.8 | 90.2–96.7 | 91.0–96.1 |
| Gemini 3.1 Flash-Lite | none | 366 | 122 | 12 | 39.1 | 34.2–44.2 | 31.1–47.3 | 30.0–48.6 |
| Gemini 3.1 Flash-Lite | fulldoc | 366 | 122 | 12 | 99.2 | 97.6–99.7 | 97.8–100.0 | 97.7–100.0 |
| Gemini 3.1 Flash-Lite | chunk | 366 | 122 | 12 | 68.9 | 63.9–73.4 | 60.9–76.8 | 63.6–75.5 |
| Gemini 3.1 Flash-Lite | graph | 366 | 122 | 12 | 100.0 | 99.0–100.0 | 97.0–100.0 † | 100.0–100.0 |
| DeepSeek V4 Flash | none | 366 | 122 | 12 | 30.3 | 25.8–35.2 | 23.5–37.4 | 19.7–41.3 |
| DeepSeek V4 Flash | fulldoc | 366 | 122 | 12 | 96.4 | 94.0–97.9 | 94.3–98.4 | 94.2–98.6 |
| DeepSeek V4 Flash | chunk | 366 | 122 | 12 | 66.9 | 62.0–71.6 | 59.3–74.3 | 60.7–74.3 |
| DeepSeek V4 Flash | graph | 366 | 122 | 12 | 99.2 | 97.6–99.7 | 98.1–100.0 | 98.4–100.0 |
| Gemma 4 26B | none | 366 | 122 | 12 | 35.8 | 31.1–40.8 | 27.6–44.0 | 26.0–46.3 |
| Gemma 4 26B | fulldoc | 366 | 122 | 12 | 96.2 | 93.7–97.7 | 92.6–98.9 | 93.4–98.7 |
| Gemma 4 26B | chunk | 366 | 122 | 12 | 67.2 | 62.2–71.8 | 58.7–75.4 | 60.1–74.8 |
| Gemma 4 26B | graph | 366 | 122 | 12 | 100.0 | 99.0–100.0 | 97.0–100.0 † | 100.0–100.0 |
| rule-based fixer | none | 366 | 122 | 12 | 25.4 | 21.2–30.1 | 18.0–32.8 | 20.3–29.2 |
| rule-based fixer | fulldoc | 366 | 122 | 12 | 25.4 | 21.2–30.1 | 18.0–33.6 | 20.4–29.1 |
| rule-based fixer | chunk | 366 | 122 | 12 | 25.4 | 21.2–30.1 | 18.0–33.6 | 20.3–29.1 |
| rule-based fixer | graph | 366 | 122 | 12 | 25.4 | 21.2–30.1 | 18.0–33.6 | 20.5–29.1 |

## GSCS — comment (comment_ok)

| model | condition | trials | units | snippets | rate % | Wilson (trials) | unit bootstrap | snippet bootstrap |
|---|---|---|---|---|---|---|---|---|
| o3-mini | none | 36 | 12 | 12 | 0.0 | 0.0–9.6 | 0.0–26.5 † | 0.0–0.0 |
| o3-mini | fulldoc | 36 | 12 | 12 | 88.9 | 74.7–95.6 | 80.6–97.2 | 80.6–97.2 |
| o3-mini | chunk | 36 | 12 | 12 | 80.6 | 65.0–90.2 | 55.6–100.0 | 58.3–100.0 |
| o3-mini | graph | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
| GPT-6 Luna | none | 36 | 12 | 12 | 0.0 | 0.0–9.6 | 0.0–26.5 † | 0.0–0.0 |
| GPT-6 Luna | fulldoc | 36 | 12 | 12 | 27.8 | 15.8–44.0 | 13.9–44.4 | 13.9–41.7 |
| GPT-6 Luna | chunk | 36 | 12 | 12 | 13.9 | 6.1–28.7 | 2.8–27.8 | 2.8–27.8 |
| GPT-6 Luna | graph | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
| Qwen3.5-9B | none | 36 | 12 | 12 | 0.0 | 0.0–9.6 | 0.0–26.5 † | 0.0–0.0 |
| Qwen3.5-9B | fulldoc | 36 | 12 | 12 | 86.1 | 71.3–93.9 | 72.2–97.2 | 72.2–97.2 |
| Qwen3.5-9B | chunk | 36 | 12 | 12 | 83.3 | 68.1–92.1 | 58.3–100.0 | 58.3–100.0 |
| Qwen3.5-9B | graph | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
| Gemini 3.1 Flash-Lite | none | 36 | 12 | 12 | 0.0 | 0.0–9.6 | 0.0–26.5 † | 0.0–0.0 |
| Gemini 3.1 Flash-Lite | fulldoc | 36 | 12 | 12 | 94.4 | 81.9–98.5 | 86.1–100.0 | 86.1–100.0 |
| Gemini 3.1 Flash-Lite | chunk | 36 | 12 | 12 | 83.3 | 68.1–92.1 | 58.3–100.0 | 58.3–100.0 |
| Gemini 3.1 Flash-Lite | graph | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
| DeepSeek V4 Flash | none | 36 | 12 | 12 | 0.0 | 0.0–9.6 | 0.0–26.5 † | 0.0–0.0 |
| DeepSeek V4 Flash | fulldoc | 36 | 12 | 12 | 86.1 | 71.3–93.9 | 77.8–94.4 | 77.8–94.4 |
| DeepSeek V4 Flash | chunk | 36 | 12 | 12 | 77.8 | 61.9–88.3 | 55.6–97.2 | 55.6–97.2 |
| DeepSeek V4 Flash | graph | 36 | 12 | 12 | 91.7 | 78.2–97.1 | 83.3–100.0 | 83.3–100.0 |
| Gemma 4 26B | none | 36 | 12 | 12 | 0.0 | 0.0–9.6 | 0.0–26.5 † | 0.0–0.0 |
| Gemma 4 26B | fulldoc | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
| Gemma 4 26B | chunk | 36 | 12 | 12 | 83.3 | 68.1–92.1 | 58.3–100.0 | 58.3–100.0 |
| Gemma 4 26B | graph | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
| rule-based fixer | none | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
| rule-based fixer | fulldoc | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
| rule-based fixer | chunk | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
| rule-based fixer | graph | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |

## Public5 — rename (core_ok)

| model | condition | trials | units | snippets | rate % | Wilson (trials) | unit bootstrap | snippet bootstrap |
|---|---|---|---|---|---|---|---|---|
| GPT-6 Luna (Public5) | none | 300 | 100 | 83 | 99.7 | 98.1–99.9 | 99.0–100.0 | 98.9–100.0 |
| GPT-6 Luna (Public5) | fulldoc | 300 | 100 | 83 | 100.0 | 98.7–100.0 | 96.4–100.0 † | 100.0–100.0 |
| GPT-6 Luna (Public5) | chunk | 300 | 100 | 83 | 99.0 | 97.1–99.7 | 97.0–100.0 | 96.9–100.0 |
| GPT-6 Luna (Public5) | graph | 300 | 100 | 83 | 100.0 | 98.7–100.0 | 96.4–100.0 † | 100.0–100.0 |

## Public5 — comment (comment_ok)

| model | condition | trials | units | snippets | rate % | Wilson (trials) | unit bootstrap | snippet bootstrap |
|---|---|---|---|---|---|---|---|---|
| GPT-6 Luna (Public5) | none | 258 | 86 | 86 | 99.6 | 97.8–99.9 | 98.8–100.0 | 98.8–100.0 |
| GPT-6 Luna (Public5) | fulldoc | 258 | 86 | 86 | 98.8 | 96.6–99.6 | 96.9–100.0 | 96.9–100.0 |
| GPT-6 Luna (Public5) | chunk | 258 | 86 | 86 | 99.6 | 97.8–99.9 | 98.8–100.0 | 98.8–100.0 |
| GPT-6 Luna (Public5) | graph | 258 | 86 | 86 | 99.6 | 97.8–99.9 | 98.8–100.0 | 98.8–100.0 |

## Ablation (GSCS) — rename (core_ok)

| model | condition | trials | units | snippets | rate % | Wilson (trials) | unit bootstrap | snippet bootstrap |
|---|---|---|---|---|---|---|---|---|
| o3-mini (ablation) | graph | 366 | 122 | 12 | 100.0 | 99.0–100.0 | 97.0–100.0 † | 100.0–100.0 |
| o3-mini (ablation) | graph_noex | 366 | 122 | 12 | 95.4 | 92.7–97.1 | 91.8–98.4 | 91.6–98.6 |
| GPT-6 Luna (ablation) | graph | 366 | 122 | 12 | 100.0 | 99.0–100.0 | 97.0–100.0 † | 100.0–100.0 |
| GPT-6 Luna (ablation) | graph_noex | 366 | 122 | 12 | 98.6 | 96.8–99.4 | 96.4–100.0 | 96.7–100.0 |
| Gemini 3.1 Flash-Lite (ablation) | graph | 366 | 122 | 12 | 100.0 | 99.0–100.0 | 97.0–100.0 † | 100.0–100.0 |
| Gemini 3.1 Flash-Lite (ablation) | graph_noex | 366 | 122 | 12 | 98.4 | 96.5–99.2 | 95.9–100.0 | 95.9–100.0 |
| Gemma 4 26B via endpoint (ablation) | none | 366 | 122 | 12 | 33.9 | 29.2–38.9 | 26.2–42.1 | 23.8–44.8 |
| Gemma 4 26B via endpoint (ablation) | fulldoc | 366 | 122 | 12 | 95.9 | 93.3–97.5 | 92.3–98.6 | 93.0–98.3 |
| Gemma 4 26B via endpoint (ablation) | chunk | 366 | 122 | 12 | 66.9 | 62.0–71.6 | 58.7–74.9 | 60.5–74.2 |
| Gemma 4 26B via endpoint (ablation) | graph | 366 | 122 | 12 | 100.0 | 99.0–100.0 | 97.0–100.0 † | 100.0–100.0 |
| Gemma 4 26B via endpoint (ablation) | graph_noex | 366 | 122 | 12 | 100.0 | 99.0–100.0 | 97.0–100.0 † | 100.0–100.0 |

## Ablation (GSCS) — comment (comment_ok)

| model | condition | trials | units | snippets | rate % | Wilson (trials) | unit bootstrap | snippet bootstrap |
|---|---|---|---|---|---|---|---|---|
| o3-mini (ablation) | graph | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
| o3-mini (ablation) | graph_noex | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
| GPT-6 Luna (ablation) | graph | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
| GPT-6 Luna (ablation) | graph_noex | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
| Gemini 3.1 Flash-Lite (ablation) | graph | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
| Gemini 3.1 Flash-Lite (ablation) | graph_noex | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
| Gemma 4 26B via endpoint (ablation) | none | 36 | 12 | 12 | 0.0 | 0.0–9.6 | 0.0–26.5 † | 0.0–0.0 |
| Gemma 4 26B via endpoint (ablation) | fulldoc | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
| Gemma 4 26B via endpoint (ablation) | chunk | 36 | 12 | 12 | 83.3 | 68.1–92.1 | 58.3–100.0 | 58.3–100.0 |
| Gemma 4 26B via endpoint (ablation) | graph | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
| Gemma 4 26B via endpoint (ablation) | graph_noex | 36 | 12 | 12 | 100.0 | 90.4–100.0 | 73.5–100.0 † | 100.0–100.0 |
