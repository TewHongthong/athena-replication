"""Phase 5 re-analysis (see ADDENDUM.md): cluster bootstrap CIs (5.1) and collision / rename-safe (5.2).
Run from athena-sim/phase5_stats:  python -B phase5.py   -> results_ci.md, results_collision.md, results.json
"""
import collections, csv, json, math, os
import numpy as np

SIM = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))
B, SEED = 10_000, 20261002
GSCS = {"o3-mini": "runs/test_o3mini_gscs_{t}", "GPT-6 Luna": "runs/test_luna_gscs_{t}",
        "Qwen3.5-9B": "runs/qwen_gscs_{t}", "Gemini 3.1 Flash-Lite": "runs/gemini31fl_gscs_{t}",
        "DeepSeek V4 Flash": "runs/dsv4f_gscs_{t}", "Gemma 4 26B": "runs/gemma4_gscs_{t}",
        "rule-based fixer": "runs/test_autofix_gscs_{t}"}
P5 = {"GPT-6 Luna (Public5)": "runs/test_luna_p5_{t}"}
ABL = {"o3-mini (ablation)": "ablation_noex/runs/abl_o3mini_{t}", "GPT-6 Luna (ablation)": "ablation_noex/runs/abl_luna_{t}",
       "Gemini 3.1 Flash-Lite (ablation)": "ablation_noex/runs/abl_gemini31fl_{t}",
       "Gemma 4 26B via endpoint (ablation)": "ablation_noex/runs/abl_gemma4or_{t}"}
COND = ["none", "fulldoc", "chunk", "graph", "graph_noex"]
METRIC = {"rename": "core_ok", "comment": "comment_ok"}


def load(rel):
    p = os.path.join(SIM, rel, "trials.jsonl")
    latest = {}
    with open(p, encoding="utf-8") as f:
        for line in f:
            t = json.loads(line); latest[t["key"]] = t
    return [t for t in latest.values() if not t.get("error")]


def val(t, metric):
    """core_ok: missing / unparsable = failure. comment_ok: None (nothing checkable) is left out, as in Table 4."""
    v = (t.get("metrics") or {}).get(metric)
    if v is None and metric == "comment_ok":
        return None
    return 1.0 if v else 0.0


def wilson(k, n, z=1.96):
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return 100 * (c - h) / d, 100 * (c + h) / d


def boot(units, snip_of, rng):
    """units: dict unit -> per-unit mean. Returns (unit-level CI, snippet-level CI, degenerate flag)."""
    ids = sorted(units); x = np.array([units[u] for u in ids]); n = len(x)
    idx = rng.integers(0, n, size=(B, n)); bs = x[idx].mean(axis=1) * 100
    u_ci = tuple(np.percentile(bs, [2.5, 97.5]))
    sn = collections.defaultdict(list)
    for u in ids:
        sn[snip_of[u]].append(units[u])
    ss = list(sn.values()); m = len(ss)
    sums = np.array([sum(s) for s in ss]); cnts = np.array([len(s) for s in ss])
    j = rng.integers(0, m, size=(B, m)); sb = sums[j].sum(axis=1) / cnts[j].sum(axis=1) * 100
    s_ci = tuple(np.percentile(sb, [2.5, 97.5]))
    degenerate = bs.min() == bs.max()
    if degenerate:                     # all units at 100% or 0%: exact Clopper-Pearson over units
        if x.mean() == 1.0:
            u_ci = (100 * 0.025 ** (1 / n), 100.0)
        else:
            u_ci = (0.0, 100 * (1 - 0.025 ** (1 / n)))
    return u_ci, s_ci, degenerate, n, m


def ci_table(rng):
    rows = []
    for fam, mapping in (("GSCS", GSCS), ("Public5", P5), ("Ablation (GSCS)", ABL)):
        for task in ("rename", "comment"):
            for model, rel in mapping.items():
                try:
                    tr = load(rel.format(t=task))
                except FileNotFoundError:
                    continue
                for c in COND:
                    T = [t for t in tr if t["condition"] == c]
                    if not T:
                        continue
                    per = collections.defaultdict(list); snip = {}
                    vals = [(t, val(t, METRIC[task])) for t in T]
                    vals = [(t, v) for t, v in vals if v is not None]
                    for t, v in vals:
                        per[t["unit_id"]].append(v); snip[t["unit_id"]] = t["snippet_id"]
                    units = {u: sum(v) / len(v) for u, v in per.items()}
                    k = sum(v for _, v in vals); n = len(vals)
                    u_ci, s_ci, deg, nu, ns = boot(units, snip, rng)
                    rows.append(dict(family=fam, task=task, model=model, condition=c, trials=n, units=nu, snippets=ns,
                                     rate=100 * k / n, wilson=wilson(k, n), unit_boot=u_ci, snippet_boot=s_ci,
                                     degenerate=bool(deg)))
    return rows


def collision_table():
    rows = []
    for fam, mapping in (("GSCS", GSCS), ("Public5", P5), ("Ablation (GSCS)", ABL)):
        for model, rel in mapping.items():
            try:
                tr = load(rel.format(t="rename"))
            except FileNotFoundError:
                continue
            for c in COND:
                T = [t for t in tr if t["condition"] == c]
                if not T:
                    continue
                m = [(t.get("metrics") or {}) for t in T]
                coll = sum(1 for x in m if x.get("collision")); core = sum(1 for x in m if x.get("core_ok"))
                safe = sum(1 for x in m if x.get("core_ok") and not x.get("collision"))
                rows.append(dict(family=fam, model=model, condition=c, trials=len(T), core_ok=100 * core / len(T),
                                 collision=100 * coll / len(T), collision_n=coll, rename_safe=100 * safe / len(T)))
    return rows


def cross_semantic():
    """GSCS: collision flag vs compile/test outcome (semantic_check/results/trial_results.csv)."""
    flags = {}
    for model, rel in GSCS.items():
        for t in load(rel.format(t="rename")):
            flags[(model, t["unit_id"], t["condition"], int(t["repeat"]))] = bool((t.get("metrics") or {}).get("collision"))
    name = {"linter autofix": "rule-based fixer"}
    tab = collections.Counter(); examples = []
    with open(os.path.join(SIM, "semantic_check", "results", "trial_results.csv"), encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if r["status"] == "not_applied":
                continue
            key = (name.get(r["model"], r["model"]), r["unit"], r["cond"], int(r["rep"]))
            col = flags.get(key)
            ok = r["status"] == "pass"
            tab[(col, ok)] += 1
            if col and not ok or (not col and not ok):
                examples.append((key, r["suggested"], r["status"], col))
    return tab, examples


def main():
    rng = np.random.default_rng(SEED)
    ci = ci_table(rng); col = collision_table(); tab, ex = cross_semantic()
    json.dump(dict(ci=ci, collision=col, cross={f"collision={k[0]} behaviour_ok={k[1]}": v for k, v in tab.items()},
                   failures=[list(map(str, e)) for e in ex]),
              open(os.path.join(HERE, "results.json"), "w", encoding="utf-8"), indent=1)
    L = ["# 5.1 Cluster bootstrap 95% CIs (exploratory; see ADDENDUM.md)", "",
         f"B = {B}, seed {SEED}. unit = resample units with their repeats (primary); snippet = resample snippets (sensitivity). "
         "† degenerate bootstrap (all units at ceiling/floor) → exact Clopper–Pearson over units.", ""]
    for fam in ("GSCS", "Public5", "Ablation (GSCS)"):
        for task in ("rename", "comment"):
            R = [r for r in ci if r["family"] == fam and r["task"] == task]
            if not R:
                continue
            L += [f"## {fam} — {task} ({METRIC[task]})", "",
                  "| model | condition | trials | units | snippets | rate % | Wilson (trials) | unit bootstrap | snippet bootstrap |",
                  "|---|---|---|---|---|---|---|---|---|"]
            for r in R:
                f = lambda c: f"{c[0]:.1f}–{c[1]:.1f}"
                L.append(f"| {r['model']} | {r['condition']} | {r['trials']} | {r['units']} | {r['snippets']} | {r['rate']:.1f} | "
                         f"{f(r['wilson'])} | {f(r['unit_boot'])}{' †' if r['degenerate'] else ''} | {f(r['snippet_boot'])} |")
            L.append("")
    open(os.path.join(HERE, "results_ci.md"), "w", encoding="utf-8").write("\n".join(L))
    C = ["# 5.2 Collision and rename-safe (exploratory; see ADDENDUM.md)", "",
         "collision = proposed name occurs as a whole word elsewhere in the snippet (scope-blind upper bound); "
         "rename-safe = core-rule compliant AND no collision. Rates over all trials.", "",
         "| family | model | condition | trials | core-rule % | collision % (n) | rename-safe % |", "|---|---|---|---|---|---|---|"]
    for r in col:
        C.append(f"| {r['family']} | {r['model']} | {r['condition']} | {r['trials']} | {r['core_ok']:.1f} | "
                 f"{r['collision']:.1f} ({r['collision_n']}) | {r['rename_safe']:.1f} |")
    C += ["", "## Collision flag vs compile/test outcome (GSCS, applied renames)", "",
          "| collision flagged | behaviour unchanged | behaviour changed |", "|---|---|---|"]
    for flag in (True, False, None):
        C.append(f"| {flag} | {tab.get((flag, True), 0)} | {tab.get((flag, False), 0)} |")
    C += ["", "Behaviour-changing trials:"] + [f"- {e[0]} -> {e[1]} ({e[2]}; collision={e[3]})" for e in ex]
    open(os.path.join(HERE, "results_collision.md"), "w", encoding="utf-8").write("\n".join(C) + "\n")
    print("\n".join(L[:4])); print("written results_ci.md, results_collision.md, results.json")


if __name__ == "__main__":
    main()
