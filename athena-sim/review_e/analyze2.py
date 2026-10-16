"""Review E analyses K2 (BM25 hit rate), K4 (by rule / language), K5 (latency) - see ADDENDUM.md.
   python3 -B analyze2.py -> results2.json, results2.md"""
import collections, json, math, os, sys, time
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); SIM = os.path.dirname(HERE)
sys.path.insert(0, SIM); sys.path.insert(0, HERE)
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


from athena.packs import load_pack  # noqa: E402
from athena.retrieval import Retriever, ChunkIndex, words  # noqa: E402

pack = load_pack("gscs")
units = {u.unit_id: u for u in pack.rename_units() if u.split == "test"}
OUT, MD = {}, ["# Review E analyses K2, K4, K5 - exploratory; see ADDENDUM.md", ""]

# ---------------------------------------------------------------- K2 BM25
chunks = pack.chunks("GSCS")
docs = [words(t) for _, t in chunks]
N = len(docs); avgdl = sum(map(len, docs)) / N
df = collections.Counter(w for d in docs for w in set(d))
tf = [collections.Counter(d) for d in docs]


def bm25_top(q, k=3, k1=1.2, b=0.75):
    sc = []
    for i, d in enumerate(tf):
        s = 0.0
        for w in q:                       # query term frequency counted by repetition, as in the TF-IDF query
            if w in d:
                idf = math.log(1 + (N - df[w] + 0.5) / (df[w] + 0.5))
                s += idf * d[w] * (k1 + 1) / (d[w] + k1 * (1 - b + b * len(docs[i]) / avgdl))
        sc.append((s, i))
    sc.sort(key=lambda x: (-x[0], x[1]))
    return [chunks[i][0] for s, i in sc[:k] if s > 0]


def secs(rid):
    s = pack.ontology.rule(rid).get("sourceSection", "")
    return {x.split(" - ")[0].strip() for x in s.split(";") if x.strip()}


idx = ChunkIndex(chunks)
logged = {}
for t in load(GSCS["o3-mini"]):
    if t["condition"] == "chunk":
        logged[t["unit_id"]] = (t.get("retrieval") or {}).get("retrieved_ids")
res = {"tfidf": [], "bm25": [], "bm25_k15": []}
sanity_bad = 0
per_rule = collections.defaultdict(lambda: collections.defaultdict(list))
for uid, u in units.items():
    q = words(f"{u.language} {u.kind} {u.kind} {u.kind} {u.injected} {u.injected}") + words(u.code_violation)
    core = pack.core_rules(u.language, u.kind)
    need = set().union(*[secs(r) for r in core]) if core else set()
    tf_ids = [chunks[i][0] for i in idx.top(q, 3)]
    if logged.get(uid) is not None and logged[uid] != tf_ids:
        sanity_bad += 1
    for name, ids in (("tfidf", tf_ids), ("bm25", bm25_top(q)), ("bm25_k15", bm25_top(q, k1=1.5))):
        h = bool(need) and need <= set(ids)
        res[name].append(h); per_rule[name][u.rule_id].append(h)
OUT["K2"] = {"units": len(units), "tfidf_sanity_mismatches": sanity_bad,
             "hit_pct": {k: pct(v) for k, v in res.items()},
             "hit_pct_by_rule": {k: {r: pct(v) for r, v in d.items()} for k, d in per_rule.items()}}
MD += ["## K2 section-level hit of the applicable rule, top 3 (GSCS test units)", "",
       f"TF-IDF recomputation vs logged retrieved_ids: {sanity_bad} mismatches of {len(logged)}", "",
       "| retriever | hit % |", "|---|---|"] + [f"| {k} | {pct(v)} |" for k, v in res.items()] + [""]
MD += ["by violated rule: " + json.dumps(OUT["K2"]["hit_pct_by_rule"]), ""]

# ---------------------------------------------------------------- K4 by rule / language ; K5 latency
k4, k5 = {}, {}
for m, rel in list(GSCS.items()) + [(m + " [ablation run]", r) for m, r in ABL.items()]:
    T = load(rel)
    byr = collections.defaultdict(list); byl = collections.defaultdict(list); lat = collections.defaultdict(list)
    for t in T:
        byr[(t["condition"], t["rule_id"])].append(ok(t)); byl[(t["condition"], t["language"])].append(ok(t))
        if t.get("latency_s") is not None:
            lat[t["condition"]].append(t["latency_s"])
    k4[m] = {"by_rule": {f"{c}|{r}": pct(v) for (c, r), v in sorted(byr.items())},
             "by_language": {f"{c}|{l}": pct(v) for (c, l), v in sorted(byl.items())}}
    k5[m] = {c: {"n": len(v), "p50": round(float(np.percentile(v, 50)), 2), "p95": round(float(np.percentile(v, 95)), 2),
                 "mean": round(float(np.mean(v)), 2)} for c, v in lat.items()}
r = Retriever(pack)
ul = list(units.values())
passes = []
for _ in range(1000):
    t0 = time.perf_counter()
    for u in ul:
        r.context("graph", task="rename", standard_id=u.standard_id, language=u.language, kind=u.kind, name=u.injected, code=u.code_violation)
    passes.append((time.perf_counter() - t0) / len(ul))
k5["retrieval_graph_ms_per_call"] = round(1000 * float(np.median(passes)), 4)
OUT["K4"], OUT["K5"] = k4, k5
rules = sorted({u.rule_id for u in ul})
MD += ["## K4 core-rule compliance by violated rule (GSCS test)", "",
       "| model | condition | " + " | ".join(rules) + " |", "|---|---|" + "---|" * len(rules)]
for m, d in k4.items():
    for c in COND if (COND := ["none", "fulldoc", "chunk", "graph", "graph_noex"]) else []:
        vals = [d["by_rule"].get(f"{c}|{r}") for r in rules]
        if any(v is not None for v in vals):
            MD.append(f"| {m} | {c} | " + " | ".join("" if v is None else str(v) for v in vals) + " |")
MD += ["", "units per rule: " + json.dumps(collections.Counter(u.rule_id for u in ul)), "",
       "## K4b by language", "", json.dumps({m: d["by_language"] for m, d in k4.items()}), "",
       "## K5 latency per call (s), GSCS renaming", "", "| model | condition | n | P50 | P95 | mean |", "|---|---|---|---|---|---|"]
for m, d in k5.items():
    if isinstance(d, dict):
        for c, v in d.items():
            MD.append(f"| {m} | {c} | {v['n']} | {v['p50']} | {v['p95']} | {v['mean']} |")
MD += ["", f"Retrieval time of condition (iv) on this machine: {k5['retrieval_graph_ms_per_call']} ms per call (median over 1,000 passes of the 122 test units)", ""]
json.dump(OUT, open(os.path.join(HERE, "results2.json"), "w"), indent=1)
open(os.path.join(HERE, "results2.md"), "w").write("\n".join(MD) + "\n")
print("\n".join(MD))
