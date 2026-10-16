"""Review E analyses K1 (bounds), K2, K4, K5 - see ADDENDUM.md.  Run from athena-sim/review_e:
   python3 -B analyze.py  -> results.json, results.md   (K1 kinds come from k1_kinds.py, run with clang)"""
import collections, json, math, os, sys, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__)); SIM = os.path.dirname(HERE)
sys.path.insert(0, SIM)
from athena.packs import load_pack  # noqa: E402
from athena.retrieval import Retriever, ChunkIndex, words  # noqa: E402

GSCS = {"o3-mini": "runs/test_o3mini_gscs_rename", "GPT-6 Luna": "runs/test_luna_gscs_rename",
        "Qwen3.5-9B": "runs/qwen_gscs_rename", "Gemini 3.1 Flash-Lite": "runs/gemini31fl_gscs_rename",
        "DeepSeek V4 Flash": "runs/dsv4f_gscs_rename", "Gemma 4 26B": "runs/gemma4_gscs_rename"}
ABL = {"o3-mini": "ablation_noex/runs/abl_o3mini_rename", "GPT-6 Luna": "ablation_noex/runs/abl_luna_rename",
       "Gemini 3.1 Flash-Lite": "ablation_noex/runs/abl_gemini31fl_rename", "Gemma 4 26B (endpoint)": "ablation_noex/runs/abl_gemma4or_rename"}
P5 = {"GPT-6 Luna": "runs/test_luna_p5_rename", "Gemini 3.1 Flash-Lite": "p5_extra/runs/p5x_gemini31fl_p5_rename",
      "DeepSeek V4 Flash": "p5_extra/runs/p5x_dsv4f_p5_rename", "Gemma 4 26B (endpoint)": "p5_extra/runs/p5x_gemma4or_p5_rename"}
COND = ["none", "fulldoc", "chunk", "graph", "graph_noex"]


def load(rel):
    latest = {}
    with open(os.path.join(SIM, rel, "trials.jsonl"), encoding="utf-8") as f:
        for line in f:
            t = json.loads(line); latest[t["key"]] = t
    return [t for t in latest.values() if not t.get("error") and t.get("split", "test") == "test"]


def ok(t):
    return 1.0 if (t.get("metrics") or {}).get("core_ok") else 0.0


def pct(x):
    return round(100 * float(np.mean(x)), 1) if len(x) else None


OUT, MD = {}, ["# Review E analyses (K1, K2, K4, K5) - exploratory; see ADDENDUM.md", ""]

# ---------------------------------------------------------------- K1 bounds
K = json.load(open(os.path.join(HERE, "k1_kinds.json")))
agree = {(r["pack"], r["unit_id"]): r for r in K}
k1 = {"gscs": {}, "public5": {}}
for pack, runs in (("gscs", GSCS), ("public5", P5)):
    rows = [r for r in K if r["pack"] == pack]
    k1[pack]["units"] = len(rows)
    k1[pack]["exactA"] = sum(r["predA"] == r["gold"] for r in rows)
    k1[pack]["exactB"] = sum(r["predB"] == r["gold"] for r in rows)
    k1[pack]["agreeA"] = sum(r["agreeA"] for r in rows)
    k1[pack]["agreeB"] = sum(r["agreeB"] for r in rows)
    k1[pack]["confusion"] = collections.Counter(f"{r['language']}:{r['gold']}->{r['predA']}" for r in rows if r["predA"] != r["gold"])
    if pack == "public5":
        k1[pack]["nameDependent"] = sum(r["nameDependent"] for r in rows)
        k1[pack]["unparsedAlone"] = sum(r["before"] is None for r in rows)
        k1[pack]["beforeWrongKind"] = sum(r["before"] is not None and r["before"] != r["gold"] for r in rows)
    k1[pack]["models"] = {}
    for m, rel in runs.items():
        T = [t for t in load(rel) if t["condition"] == "graph"]
        rep = pct([ok(t) for t in T])
        lowA = pct([ok(t) if agree[(pack, t["unit_id"])]["agreeA"] else 0.0 for t in T])
        lowB = pct([ok(t) if agree[(pack, t["unit_id"])]["agreeB"] else 0.0 for t in T])
        row = dict(trials=len(T), reported=rep, lower_A=lowA, lower_B=lowB)
        if pack == "public5":   # only the name-dependent units counted as failures
            row["lower_nameDependent"] = pct([0.0 if agree[(pack, t["unit_id"])]["nameDependent"] else ok(t) for t in T])
        k1[pack]["models"][m] = row
OUT["K1"] = k1
MD += ["## K1 identifier kind inferred without the original name", ""]
for pack in ("gscs", "public5"):
    d = k1[pack]
    MD.append(f"**{pack}**: {d['units']} test units; kind exact A {d['exactA']}, B {d['exactB']}; same core rules A {d['agreeA']}, B {d['agreeB']}"
              + (f"; name-dependent kind changes {d['nameDependent']}; excerpt not analysable alone {d['unparsedAlone']}; "
                 f"excerpt read as another kind before the rename {d['beforeWrongKind']}" if pack == "public5" else ""))
    MD.append(f"confusion (A): {dict(d['confusion'])}")
    MD += ["", "| model | (iv) trials | reported % | lower bound A % | lower bound B % |" + (" name-dependent only % |" if pack == "public5" else ""),
           "|---|---|---|---|---|" + ("---|" if pack == "public5" else "")]
    for m, r in d["models"].items():
        MD.append(f"| {m} | {r['trials']} | {r['reported']} | {r['lower_A']} | {r['lower_B']} |" + (f" {r['lower_nameDependent']} |" if pack == "public5" else ""))
    MD.append("")
json.dump(OUT, open(os.path.join(HERE, "results.json"), "w"), indent=1, default=dict)
open(os.path.join(HERE, "results.md"), "w").write("\n".join(MD) + "\n")
print("\n".join(MD))
