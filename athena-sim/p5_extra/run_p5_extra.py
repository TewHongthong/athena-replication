#!/usr/bin/env python3
"""Public5 renaming with further models (see ADDENDUM.md). Run from this folder in PowerShell:

  $env:OPENAI_API_KEY = "<your hosted API key>"
  python run_p5_extra.py --dry-run          # show the plan, write nothing
  python run_p5_extra.py --budget 6         # real run (asks "Start? [y/N]")

For every model: 1-unit smoke test on the DEV split (stops if the API call fails), then freeze, then the TEST split once
(3 repeats, the same 100 units as the GPT-6 Luna run). Safe to run again: finished sets are skipped, an interrupted set
resumes under the same run id. Log: runs/run_p5_extra.log.  Nothing outside this folder is written.
"""
import argparse, datetime, json, os, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
RUNS = os.path.join(HERE, "runs")
LOG = os.path.join(RUNS, "run_p5_extra.log")
CORPUS = os.path.normpath(os.path.join(HERE, "..", "..", "athena-corpus"))
BASE_URL = os.environ.get("OPENAI_BASE_URL", "")
REPEATS = 3
CONDS = "none,fulldoc,chunk,graph"
GEMMA_EXTRA = os.environ.get("ATHENA_GEMMA_EXTRA_BODY") or json.dumps(
    {"reasoning": {"effort": "none"}})

MODELS = {   # settings identical to each model's earlier test run (gemini31fl/, ablation_noex/ Gemma endpoint, dsv4f_v2/)
    "gemini31fl": dict(backend="openai:google/gemini-3.1-flash-lite", price_in=0.25, price_out=1.5, max_tokens=8192,
                       env={"ATHENA_OMIT_TEMP": "1"},
                       note="Gemini 3.1 Flash-Lite, temperature omitted (ATHENA_OMIT_TEMP=1), max_tokens 8192, no dev tuning"),
    "gemma4or": dict(backend="openai:google/gemma-4-26b-a4b-it", price_in=0.042, price_out=0.22, max_tokens=2048,
                     env={"ATHENA_EXTRA_BODY": GEMMA_EXTRA},
                     note="Gemma 4 26B A4B endpoint (as in the ablation, not the local 4-bit run), temperature 0.2, max_tokens 2048, extra body " + GEMMA_EXTRA),
    "dsv4f": dict(backend="openai:deepseek/deepseek-v4-flash", price_in=0.14, price_out=1.28, max_tokens=8192,
                  env={"ATHENA_OMIT_TEMP": "1"},
                  note="DeepSeek V4 Flash (0423), temperature omitted (ATHENA_OMIT_TEMP=1), provider-default reasoning, max_tokens 8192; prices are a rough estimate for the budget guard only"),
}
# (model, estimated USD) -- order = priority; task is always Public5 rename
PLAN = [("gemini31fl", 0.7), ("gemma4or", 0.15), ("dsv4f", 4.5)]


def now():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def emit(msg, dry=False):
    line = "[%s] %s" % (now(), msg)
    print(line, flush=True)
    if not dry:
        os.makedirs(RUNS, exist_ok=True)
        with open(LOG, "a", encoding="utf-8") as f:
            f.write(line + "\n")


def trials(run_id):
    p = os.path.join(RUNS, run_id, "trials.jsonl")
    if not os.path.exists(p):
        return []
    out = []
    with open(p, encoding="utf-8") as f:
        for line in f:
            try:
                out.append(json.loads(line))
            except ValueError:
                pass
    return out


def run_cost(run_id):
    return sum(float(t.get("cost_usd") or 0) for t in trials(run_id))


def is_done(frozen_path, run_id):
    p = frozen_path + ".ledger.jsonl"
    done = False
    if os.path.exists(p):
        with open(p, encoding="utf-8") as f:
            for line in f:
                try:
                    e = json.loads(line)
                except ValueError:
                    continue
                if e.get("run_id") == run_id and e.get("event") == "end":
                    done = e.get("status") == "complete" and not e.get("trials_error")
    return done


def call(cmd, env_extra, dry):
    emit("$ " + " ".join("%s=%s" % kv for kv in env_extra.items()) + " " + subprocess.list2cmdline(cmd), dry)
    if dry:
        return 0
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8", PYTHONDONTWRITEBYTECODE="1",
               ATHENA_LOG_PROVIDER="1", **env_extra)
    p = subprocess.Popen(cmd, cwd=HERE, env=env, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         text=True, encoding="utf-8", errors="replace")
    with open(LOG, "a", encoding="utf-8") as lf:
        for line in p.stdout:
            line = line.rstrip("\n")
            print(line, flush=True)
            lf.write("    " + line + "\n")
    return p.wait()


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--budget", type=float, default=6.0, help="stop starting new sets when spent + estimate > budget (USD)")
    ap.add_argument("--workers", type=int, default=4)
    ap.add_argument("--only", help="run one set, e.g. gemini31fl_p5_rename")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--yes", action="store_true")
    a = ap.parse_args()

    entries = []
    for model, est in PLAN:
        sid = "%s_p5_rename" % model
        entries.append(dict(id=sid, model=model, task="rename", conds=CONDS, est=est, run_id="p5x_" + sid,
                            frozen=os.path.join(HERE, "frozen_p5x_%s.json" % sid), **MODELS[model]))
    if a.only:
        entries = [e for e in entries if e["id"] == a.only] or sys.exit("unknown set " + a.only)
    if not a.dry_run and not os.environ.get("OPENAI_API_KEY"):
        sys.exit("OPENAI_API_KEY is not set in this window (put your hosted API key in it first).")

    spent = sum(run_cost(e["run_id"]) for e in entries)
    print("\nPublic5 rename, further models   budget $%.2f   already spent $%.4f\n" % (a.budget, spent))
    print("%-20s %-40s %-36s %-7s %s" % ("set", "backend", "conditions", "est.$", "state"))
    for e in entries:
        state = "DONE" if is_done(e["frozen"], e["run_id"]) else ("resume" if os.path.isdir(os.path.join(RUNS, e["run_id"])) else "new")
        print("%-20s %-40s %-36s %-7.2f %s" % (e["id"], e["backend"], e["conds"], e["est"], state))
    print()
    if not a.dry_run and not a.yes and input("Start? [y/N] ").strip().lower() != "y":
        sys.exit("cancelled")

    smoked, skipped = set(), []
    try:
        for e in entries:
            rid, fz = e["run_id"], e["frozen"]
            if is_done(fz, rid):
                emit("SKIP %s: already complete" % e["id"], a.dry_run)
                continue
            remaining = max(e["est"] - run_cost(rid), 0.0)
            if spent + remaining > a.budget:
                emit("SKIP %s: spent $%.2f + est. $%.2f > budget $%.2f" % (e["id"], spent, remaining, a.budget), a.dry_run)
                skipped.append(e["id"])
                continue
            base = ["--pack", "public5", "--corpus", CORPUS, "--backend", e["backend"], "--per-language", "20",
                    "--seed", "42", "--max-tokens", str(e["max_tokens"]), "--base-url", BASE_URL]
            if e["model"] not in smoked and not os.path.exists(fz):          # smoke once per model, before its freeze
                srid = "smoke_" + e["model"]
                rc = call([sys.executable, "-B", os.path.join(os.path.dirname(HERE), "athena_sim.py"), "run"] + base +
                          ["--task", "rename", "--conditions", e["conds"], "--split", "dev", "--limit", "1", "--repeats", "1",
                           "--run-id", srid, "--max-errors", "2"], e["env"], a.dry_run)
                errs = [t for t in trials(srid) if t.get("error")]
                if not a.dry_run and (rc or errs):
                    emit("STOP: smoke test for %s failed (rc=%s, %d API errors). First error: %s\n"
                         "Send this message to Claude; nothing was frozen or run on the test split."
                         % (e["model"], rc, len(errs), (errs[0]["error"] if errs else "-")[:400]))
                    sys.exit(1)
                if not a.dry_run:
                    served = sorted({t.get("model") for t in trials(srid)})
                    emit("smoke OK for %s; served by: %s" % (e["model"], ", ".join(map(str, served))))
                smoked.add(e["model"])
            common = base + ["--task", e["task"], "--conditions", e["conds"], "--repeats", str(REPEATS)]
            if not os.path.exists(fz):
                rc = call([sys.executable, "-B", os.path.join(os.path.dirname(HERE), "athena_sim.py"), "freeze"] + common +
                          ["--out-file", fz, "--note", "Public5 further models (ADDENDUM.md): " + e["note"]], e["env"], a.dry_run)
                if rc:
                    sys.exit("freeze failed for %s (rc=%s)" % (e["id"], rc))
            emit("START %s (run id %s)" % (e["id"], rid), a.dry_run)
            rc = call([sys.executable, "-B", os.path.join(os.path.dirname(HERE), "athena_sim.py"), "run"] + common +
                      ["--split", "test", "--workers", str(a.workers), "--max-errors", "10",
                       "--price-in", str(e["price_in"]), "--price-out", str(e["price_out"]),
                       "--frozen", fz, "--run-id", rid], e["env"], a.dry_run)
            spent = sum(run_cost(x["run_id"]) for x in entries)
            emit("END %s rc=%s   this set $%.4f   total spent $%.4f" % (e["id"], rc, run_cost(rid), spent), a.dry_run)
            if rc:
                emit("FAILED %s - fix, then run this script again to resume" % e["id"], a.dry_run)
                sys.exit(1)
    except KeyboardInterrupt:
        emit("INTERRUPTED - progress is saved; run this script again to resume", a.dry_run)
        sys.exit(130)
    emit("SUMMARY total spent $%.4f of budget $%.2f; skipped: %s" % (spent, a.budget, ", ".join(skipped) or "none"), a.dry_run)


if __name__ == "__main__":
    main()
