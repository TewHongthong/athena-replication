"""Analysis of the graph_noex ablation, fixed BEFORE the runs (see ADDENDUM.md). Run from ablation_noex/:

  python -B analyze_ablation.py              # writes analysis/results.md + analysis/results.json
  python -B analyze_ablation.py --selftest   # code check on mock runs, prints only

Per model x task: rates per condition (Wilson 95% CI) and paired comparisons by unit (repeats averaged; exact two-sided
sign test; Holm across the comparisons of that model x task). Trials with an API error are excluded and counted;
unparsable answers count as failures (Section 4.3). Primary metric: core-rule compliance (rename), comment structure ok
(comment). Type prefix kept and exact match are reported descriptively.
"""
import argparse, json, math, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.dirname(HERE)
ORIG = {"o3mini": "runs/test_o3mini_gscs_{t}", "luna": "runs/test_luna_gscs_{t}",
        "gemini31fl": "runs/gemini31fl_gscs_{t}"}
MODELS = ["o3mini", "luna", "gemini31fl", "gemma4or"]
LABEL = {"o3mini": "o3-mini", "luna": "GPT-6 Luna", "gemini31fl": "Gemini 3.1 Flash-Lite", "gemma4or": "Gemma 4 26B (hosted API)"}
PRIMARY = {"rename": "core_ok", "comment": "comment_ok"}
EXTRA = {"rename": ["prefix_match", "exact_match"], "comment": []}


def load(path):
    p = os.path.join(path, "trials.jsonl")
    if not os.path.exists(p):
        return None
    out = []
    with open(p, encoding="utf-8") as f:
        for line in f:
            try:
                out.append(json.loads(line))
            except ValueError:
                pass
    return out


def per_unit(trials, cond, metric):
    """unit -> mean of metric over repeats (latest record per trial key; API errors excluded)."""
    latest = {}
    for t in trials:
        if t["condition"] == cond:
            latest[t["key"]] = t
    vals, errors = defaultdict(list), 0
    for t in latest.values():
        if t.get("error"):
            errors += 1
            continue
        v = (t.get("metrics") or {}).get(metric)
        if v is None and metric == PRIMARY.get(t["task"]):
            v = False                                   # unparsable answer = failure
        if v is not None:
            vals[t["unit_id"]].append(1.0 if v else 0.0)
    return {u: sum(v) / len(v) for u, v in vals.items()}, sum(len(v) for v in vals.values()), errors


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"),) * 2
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (c - h) / d, (c + h) / d


def sign_test(a, b):
    units = sorted(set(a) & set(b))
    better = sum(a[u] > b[u] for u in units); worse = sum(a[u] < b[u] for u in units); n = better + worse
    p = 1.0 if n == 0 else min(1.0, 2 * sum(math.comb(n, i) for i in range(0, min(better, worse) + 1)) / 2 ** n)
    diff = 100 * sum(a[u] - b[u] for u in units) / len(units) if units else float("nan")
    return dict(n_units=len(units), better=better, worse=worse, ties=len(units) - n, mean_diff_pp=diff, p=p)


def holm(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i]); out = [0.0] * len(ps); run = 0.0
    for r, i in enumerate(order):
        run = max(run, min(1.0, (len(ps) - r) * ps[i])); out[i] = run
    return out


def analyse(model, task, new, orig):
    """new/orig: trial lists. Returns dict with rates and comparisons."""
    src = {}
    for c in ("graph", "graph_noex", "none", "fulldoc", "chunk"):
        if any(t["condition"] == c for t in new):
            src[c] = ("new", new)
        elif orig is not None and any(t["condition"] == c for t in orig):
            src[c] = ("orig", orig)
    if orig is not None and any(t["condition"] == "graph" for t in orig):
        src["graph_orig"] = ("orig", orig)
    res = {"model": model, "task": task, "rates": {}, "extra": {}, "comparisons": []}
    pm = PRIMARY[task]; unit = {}
    for c, (where, tr) in src.items():
        cond = "graph" if c == "graph_orig" else c
        u, n, err = per_unit(tr, cond, pm)
        k = sum(1 for t in tr if t["condition"] == cond and not t.get("error") and (t.get("metrics") or {}).get(pm))
        lo, hi = wilson(k, n)
        res["rates"][c] = dict(source=where, n_trials=n, api_errors=err, rate=100 * k / n if n else float("nan"),
                               ci=[100 * lo, 100 * hi])
        unit[c] = u
        for m in EXTRA[task]:
            um, nm, _ = per_unit(tr, cond, m)
            res["extra"].setdefault(m, {})[c] = 100 * sum(um.values()) / len(um) if um else float("nan")
    pairs = [("graph", "graph_noex", "E: examples"), ("graph_noex", "chunk", "S: selection vs chunk"),
             ("graph_noex", "fulldoc", "S: selection vs full document"), ("graph_noex", "none", "noex vs none")]
    pairs.append(("graph", "graph_orig", "replication: graph re-run vs original") if "graph_orig" in unit
                 else ("graph", "none", "graph vs none (same run)"))
    comps = [dict(a=a, b=b, label=l, **sign_test(unit[a], unit[b])) for a, b, l in pairs if a in unit and b in unit]
    for c, ph in zip(comps, holm([c["p"] for c in comps])):
        c["p_holm"] = ph
    res["comparisons"] = comps
    return res


def fmt(res):
    L = [f"### {LABEL.get(res['model'], res['model'])} — {res['task']}", "",
         "| condition | source | trials | API errors | primary % [95% CI] | " + " | ".join(f"{m} %" for m in res["extra"]) + " |",
         "|---|---|---|---|---|" + "---|" * len(res["extra"])]
    for c, r in res["rates"].items():
        L.append(f"| {c} | {r['source']} | {r['n_trials']} | {r['api_errors']} | {r['rate']:.1f} [{r['ci'][0]:.0f}–{r['ci'][1]:.0f}] | "
                 + " | ".join(f"{res['extra'][m].get(c, float('nan')):.1f}" for m in res["extra"]) + " |")
    L += ["", "| comparison | units | better / worse / ties | mean diff (pp) | p | p (Holm) |", "|---|---|---|---|---|---|"]
    for c in res["comparisons"]:
        L.append(f"| {c['label']} ({c['a']} vs {c['b']}) | {c['n_units']} | {c['better']} / {c['worse']} / {c['ties']} | "
                 f"{c['mean_diff_pp']:+.1f} | {c['p']:.3g} | {c['p_holm']:.3g} |")
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--selftest", action="store_true"); a = ap.parse_args()
    if a.selftest:
        new = load(os.path.join(HERE, "runs", "mock_oracle_rename"))
        orig = load(os.path.join(SIM, ORIG["luna"].format(t="rename")))
        print(fmt(analyse("selftest(mock new vs Luna orig, dev vs test units)", "rename", new, orig)))
        return
    out, md = [], ["# graph_noex ablation — results (exploratory; analysis fixed before the runs)", ""]
    for m in MODELS:
        for t in ("rename", "comment"):
            new = load(os.path.join(HERE, "runs", f"abl_{m}_{t}"))
            if new is None:
                md.append(f"*{LABEL[m]} {t}: run not found*\n"); continue
            orig = load(os.path.join(SIM, ORIG[m].format(t=t))) if m in ORIG else None
            r = analyse(m, t, new, orig); out.append(r); md.append(fmt(r))
    os.makedirs(os.path.join(HERE, "analysis"), exist_ok=True)
    json.dump(out, open(os.path.join(HERE, "analysis", "results.json"), "w", encoding="utf-8"), indent=1)
    open(os.path.join(HERE, "analysis", "results.md"), "w", encoding="utf-8").write("\n".join(md))
    print("\n".join(md))


if __name__ == "__main__":
    main()
