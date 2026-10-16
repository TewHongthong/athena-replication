"""Post-hoc descriptive check (see ADDENDUM, recorded after the first computation)."""
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); SIM = os.path.dirname(HERE)
GSCS = {"o3-mini": "runs/test_o3mini_gscs_rename", "GPT-6 Luna": "runs/test_luna_gscs_rename",
        "Qwen3.5-9B": "runs/qwen_gscs_rename", "Gemini 3.1 Flash-Lite": "runs/gemini31fl_gscs_rename",
        "DeepSeek V4 Flash": "runs/dsv4f_gscs_rename", "Gemma 4 26B": "runs/gemma4_gscs_rename"}
PFX = re.compile(r"^(i|f|d|str|bln|c|l|s|b|arr|lst|ch|n)_", re.I)
tot_f = tot_p = 0; out = []
for m, rel in GSCS.items():
    latest = {}
    for l in open(os.path.join(SIM, rel, "trials.jsonl"), encoding="utf-8"):
        t = json.loads(l); latest[t["key"]] = t
    T = [t for t in latest.values() if not t.get("error") and t["rule_id"] == "GSCS-CONST-UPPER" and t["condition"] == "chunk"]
    F = [t for t in T if not (t.get("metrics") or {}).get("core_ok")]
    P = [t for t in F if PFX.match(str((t.get("metrics") or {}).get("suggested") or ""))]
    tot_f += len(F); tot_p += len(P)
    out.append(f"| {m} | {len(T)} | {len(F)} | {len(P)} |")
md = ["# Post-hoc: chunk-condition failures on GSCS constants that carry a type prefix", "",
      "| model | chunk trials on constants | failures | failures with a type prefix |", "|---|---|---|---|"] + out + ["", f"total: {tot_p} of {tot_f} failures"]
open(os.path.join(HERE, "const_prefix.md"), "w").write("\n".join(md) + "\n"); print("\n".join(md))
