# Public5 renaming with further models — results note (after the runs)

Runs (local machine), in this order: Gemini 3.1 Flash-Lite, Gemma 4 26B endpoint,
DeepSeek V4 Flash. 1,200 trials each, 0 API errors, 0 unparsable lines. Recorded cost (price args):
Gemini $0.49, Gemma $0.08, DeepSeek $0.97 (DeepSeek prices are a rough estimate). DeepSeek was interrupted after
3 trials (Ctrl+C / window closed) and resumed under the same run id and freeze with --workers 16 (parallelism only;
prompts and settings unchanged). Gemma and DeepSeek requests were spread over several serving providers (logged).

Results (analysis/results.md; analyze_p5_extra.py unchanged since written):
- Core-rule compliance without the standard: Luna 99.7, Gemini 100.0, Gemma 100.0, DeepSeek 100.0.
- All conditions 98.0–100.0; graph − none: Luna +0.3, Gemini 0.0, Gemma −0.3, DeepSeek −0.3 pp; every sign test
  p = 1 (at most 2 units differ). Valid answers 99.3–100%; under none 100% for every model.
- Expectations E1 (Gemini, Gemma) and E2 (DeepSeek, on valid answers) both met.
- DeepSeek: no invalid answer and no token-limit hit under none (mean 541 output tokens), against 4,760 and 128/366
  limit hits on the GSCS case study — long outputs arise with the unfamiliar convention, not from the task.
- Exact match 80.7–91.7%; collision flags 0.0–1.7%; collision-screened compliance 97.0–100.0%.
