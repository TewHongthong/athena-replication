"""Analysis for Public5 renaming with further models (see ADDENDUM.md; written before the runs).
Run from p5_extra/:  python -B analyze_p5_extra.py   -> analysis/results.md, analysis/results.json"""
import collections, json, math, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
B, SEED = 10_000, 20261002
RUNS = {"GPT-6 Luna (frozen run)": os.path.join(HERE, "..", "runs", "test_luna_p5_rename"),
        "Gemini 3.1 Flash-Lite": os.path.join(HERE, "runs", "p5x_gemini31fl_p5_rename"),
        "Gemma 4 26B (endpoint)": os.path.join(HERE, "runs", "p5x_gemma4or_p5_rename"),
        "DeepSeek V4 Flash": os.path.join(HERE, "runs", "p5x_dsv4f_p5_rename")}
CONDS = ["none", "fulldoc", "chunk", "graph"]


def load(d):
    p = os.path.join(d, "trials.jsonl")
    if not os.path.exists(p):
        return None
    latest = {}
    for line in open(p, encoding="utf-8"):
        t = json.loads(line); latest[t["key"]] = t
    return [t for t in latest.values() if not t.get("error")]


def m(t, k):
    return (t.get("metrics") or {}).get(k)


def core(t):
    return 1.0 if m(t, "core_ok") else 0.0


def valid(t):
    return bool(m(t, "valid_identifier"))


def per_unit(T, f):
    d = collections.defaultdict(list)
    for t in T:
        d[t["unit_id"]].append(f(t))
    return {u: sum(v) / len(v) for u, v in d.items()}


def boot_ci(units, rng):
    x = np.array([units[u] for u in sorted(units)]); n = len(x)
    bs = x[rng.integers(0, n, size=(B, n))].mean(axis=1) * 100
    if bs.min() == bs.max():
        if x.mean() == 1.0:
            return (100 * 0.025 ** (1 / n), 100.0), True
        if x.mean() == 0.0:
            return (0.0, 100 * (1 - 0.025 ** (1 / n))), True
    return tuple(np.percentile(bs, [2.5, 97.5])), False


def sign_test(a, b):
    """exact two-sided sign test on paired per-unit means (ties dropped)."""
    plus = sum(1 for u in a if a[u] > b[u]); minus = sum(1 for u in a if a[u] < b[u]); n = plus + minus
    if n == 0:
        return plus, minus, 1.0
    k = min(plus, minus)
    p = min(1.0, 2 * sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n)
    return plus, minus, p


def holm(ps):
    order = sorted(range(len(ps)), key=lambda i: ps[i]); out = [0.0] * len(ps); run = 0.0
    for r, i in enumerate(order):
        run = max(run, min(1.0, (len(ps) - r) * ps[i])); out[i] = run
    return out


def main():
    rng = np.random.default_rng(SEED)
    res, L = {}, ["# Public5 renaming with further models (exploratory; see ADDENDUM.md)", ""]
    L += ["| Model | Condition | trials | valid % | core-rule % [95% CI] | core-rule % of valid | exact match % | collision-screened % | SI char after |",
          "|---|---|---|---|---|---|---|---|---|"]
    tests, langs, prov = [], [], {}
    for model, d in RUNS.items():
        T = load(d)
        if T is None:
            L.append(f"| {model} | (not run) | | | | | | | |"); continue
        prov[model] = dict(collections.Counter(str(t.get("model")) for t in T))
        units_by_c = {}
        for c in CONDS:
            Tc = [t for t in T if t["condition"] == c]
            if not Tc:
                continue
            u = per_unit(Tc, core); units_by_c[c] = u
            (lo, hi), deg = boot_ci(u, rng)
            V = [t for t in Tc if valid(t)]
            row = dict(trials=len(Tc), units=len(u), valid=100 * len(V) / len(Tc), core=100 * sum(map(core, Tc)) / len(Tc),
                       ci=(lo, hi), exact_ci=deg, core_valid=(100 * sum(map(core, V)) / len(V)) if V else None,
                       exact=100 * sum(1 for t in Tc if m(t, "exact_match")) / len(Tc),
                       screened=100 * sum(1 for t in Tc if m(t, "core_ok") and not m(t, "collision")) / len(Tc),
                       si=float(np.mean([m(t, "sim_char_after") for t in Tc])))
            res[f"{model}|{c}"] = row
            cv = f"{row['core_valid']:.1f}" if row["core_valid"] is not None else "-"
            L.append(f"| {model} | {c} | {row['trials']} | {row['valid']:.1f} | {row['core']:.1f}{'†' if deg else ''} [{lo:.0f}–{hi:.0f}] | "
                     f"{cv} | {row['exact']:.1f} | {row['screened']:.1f} | {row['si']:.4f} |")
            byl = collections.defaultdict(list)
            for t in Tc:
                byl[t["language"]].append(core(t))
            langs.append((model, c, {k: 100 * sum(v) / len(v) for k, v in sorted(byl.items())}))
        if "graph" in units_by_c:
            ps, rows = [], []
            for c in ("none", "fulldoc", "chunk"):
                if c in units_by_c:
                    plus, minus, p = sign_test(units_by_c["graph"], units_by_c[c])
                    diff = 100 * (np.mean(list(units_by_c["graph"].values())) - np.mean(list(units_by_c[c].values())))
                    rows.append([model, c, diff, plus, minus, p]); ps.append(p)
            for r, h in zip(rows, holm(ps)):
                tests.append(r + [h])
    L += ["", "† every unit complies in every repeat; exact Clopper–Pearson interval over units.", "",
          "## Paired exact sign tests on per-unit means (graph vs other condition), Holm within model", "",
          "| Model | graph vs | diff (pp) | units better | units worse | p | Holm p |", "|---|---|---|---|---|---|---|"]
    for r in tests:
        L.append(f"| {r[0]} | {r[1]} | {r[2]:+.1f} | {r[3]} | {r[4]} | {r[5]:.3g} | {r[6]:.3g} |")
    L += ["", "## Core-rule % by language", "", "| Model | Condition | " + " | ".join(sorted(langs[0][2])) + " |",
          "|---|---|" + "---|" * len(langs[0][2])]
    for model, c, d in langs:
        L.append(f"| {model} | {c} | " + " | ".join(f"{v:.1f}" for v in d.values()) + " |")
    L += ["", "## Expectations (ADDENDUM.md)", ""]
    for model in RUNS:
        n, g = res.get(f"{model}|none"), res.get(f"{model}|graph")
        if not (n and g):
            continue
        L.append(f"- {model}: none {n['core']:.1f}% (valid only {n['core_valid'] if n['core_valid'] is None else round(n['core_valid'], 1)}%), "
                 f"graph − none {g['core'] - n['core']:+.1f} pp overall, "
                 f"{(g['core_valid'] or 0) - (n['core_valid'] or 0):+.1f} pp on valid answers; invalid under none {100 - n['valid']:.1f}%")
    os.makedirs(os.path.join(HERE, "analysis"), exist_ok=True)
    open(os.path.join(HERE, "analysis", "results.md"), "w", encoding="utf-8").write("\n".join(L) + "\n")
    json.dump(dict(rows=res, tests=tests, languages=langs), open(os.path.join(HERE, "analysis", "results.json"), "w"), indent=1)
    print("\n".join(L))


if __name__ == "__main__":
    main()
