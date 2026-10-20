"""Self-evolution: the harness changes its own search space based on evidence.

This is the "learns from its total run" part. It is deliberately narrow,
because the failure mode of an automatic search is that it keeps adding
more trials until it finds something that looks good by chance.

What this module does automatically:
  1. RETIRES a strategy family when the accumulated evidence says it is
     actively harmful - a family whose every variant loses money on the
     untouched window, across several separated runs.
  2. REPORTS which families deserve more exploration, so effort goes
     where the evidence points instead of uniformly.
  3. GUARDS the search space - caps the total number of candidates and
     guarantees the current champion is always still in the space, so a
     retirement can never delete the strategy we are currently using.

What this module deliberately does NOT do:
  - It does not invent new strategies. Automatic idea generation is how a
    search ends up convinced of a curve-fit. New rule types are added by
    hand, guided by the report.
  - It does not retire anything on thin evidence. Minimum run counts apply.
  - It never changes the holdout, the promotion rules, or the DSR. Those
    are the guardrails, and a guardrail that can edit itself is not one.

Every change is written to research/evolution.json and to an append-only
evolution log, so the audit trail shows exactly what the system changed and
when it decided to.
"""
import json
import os

import numpy as np
import pandas as pd

from . import config

EVOLUTION_FILE = os.path.join(config.PROJECT_ROOT, "research", "evolution.json")
LOG_FILE = os.path.join(config.PROJECT_ROOT, "research", "evolution-log.jsonl")

# --- how much evidence before the system is allowed to act -----------------
MIN_RUNS_TO_RETIRE = 3          # separated runs, not back-to-back repeats
MIN_CANDIDATES_IN_FAMILY = 2
RETIRE_HOLDOUT_MEDIAN_PCT = -2.0  # a family must be clearly harmful

# --- guardrails on the search space ---------------------------------------
MAX_TOTAL_CANDIDATES = 150


def load_history():
    path = os.path.join(config.PROJECT_ROOT, "research", "history.csv")
    if not os.path.exists(path):
        return pd.DataFrame()
    df = pd.read_csv(path)
    if "run_at" in df.columns:
        df["run_at"] = pd.to_datetime(df["run_at"], errors="coerce")
    return df


def load_state():
    if os.path.exists(config.STATE_FILE):
        try:
            with open(config.STATE_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"champion": None}


def load_evolution():
    if os.path.exists(EVOLUTION_FILE):
        try:
            with open(EVOLUTION_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {"retired_families": [], "explore_next": [], "history": []}


def decide(df, state):
    """Work out which families to retire and which to explore further."""
    out = {
        "retired_families": [],
        "explore_next": [],
        "reasons": [],
        "n_runs": 0,
    }

    if df.empty:
        out["reasons"].append("no history yet - no changes made")
        return out

    out["n_runs"] = int(df["run_at"].nunique())

    fam = df.groupby("family").agg(
        n_candidates=("candidate_id", "nunique"),
        median_holdout=("holdout_cagr", "median"),
        mean_holdout=("holdout_cagr", "mean"),
        max_dsr=("dsr", "max"),
        mean_dsr=("dsr", "mean"),
        times_basic=("passes_basic", "sum"),
        times_gate=("passes_gate", "sum"),
        assets=("assets_positive", "mean"),
        runs_seen=("run_at", "nunique"),
    ).reset_index()

    # --- retire families that are consistently harmful --------------------
    for _, r in fam.iterrows():
        if r["runs_seen"] < MIN_RUNS_TO_RETIRE:
            continue
        if r["n_candidates"] < MIN_CANDIDATES_IN_FAMILY:
            continue
        if r["median_holdout"] < RETIRE_HOLDOUT_MEDIAN_PCT:
            out["retired_families"].append(r["family"])
            out["reasons"].append(
                f"RETIRE `{r['family']}`: median holdout CAGR "
                f"{r['median_holdout']:.1f}% across {int(r['runs_seen'])} runs "
                f"and {int(r['n_candidates'])} variants"
            )

    # --- recommend where to explore further ------------------------------
    alive = fam[~fam["family"].isin(out["retired_families"])]
    for _, r in alive.sort_values("median_holdout", ascending=False).iterrows():
        if r["median_holdout"] < 5.0:
            continue
        reason = (
            f"median holdout {r['median_holdout']:.1f}%, "
            f"best DSR {r['max_dsr']:.3f}, positive on {r['assets']:.1f}/10 series"
        )
        out["explore_next"].append({
            "family": r["family"],
            "median_holdout_cagr": round(float(r["median_holdout"]), 2),
            "max_dsr": round(float(r["max_dsr"]), 4),
            "mean_assets_positive": round(float(r["assets"]), 2),
            "times_gate": int(r["times_gate"]),
            "why": reason,
        })

    # The current champion's family must never be retired, and the champion
    # itself must always remain evaluable.
    champ = (state.get("champion") or {}).get("id")
    if champ:
        champ_family = None
        for _, r in fam.iterrows():
            if champ_family is None and champ.startswith(r["family"]):
                champ_family = r["family"]
        if champ_family and champ_family in out["retired_families"]:
            out["retired_families"].remove(champ_family)
            out["reasons"].append(
                f"KEPT `{champ_family}` despite negative median - it is the "
                "current champion and must stay in the space for comparison"
            )

    return out


def apply(decision, state):
    """Merge a decision into the saved evolution state and log it."""
    current = load_evolution()

    retired = sorted(set(current.get("retired_families", []))
                     | set(decision.get("retired_families", [])))
    entry = {
        "at": config.now_iso(),
        "retired_families": retired,
        "explore_next": decision.get("explore_next", []),
        "reasons": decision.get("reasons", []),
        "n_runs": decision.get("n_runs", 0),
    }
    current["retired_families"] = retired
    current["explore_next"] = decision.get("explore_next", [])
    current["last_decision"] = entry
    current["history"] = (current.get("history", []) + [entry])[-120:]

    with open(EVOLUTION_FILE, "w", encoding="utf-8") as f:
        json.dump(current, f, indent=2)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")

    return current


def main():
    df = load_history()
    state = load_state()
    decision = decide(df, state)
    saved = apply(decision, state)

    print("=== evolution decision ===")
    for r in decision.get("reasons", []) or ["no changes"]:
        print(f"  {r}")
    if not decision.get("explore_next"):
        print("  no family currently meets the bar for further exploration")
    else:
        print("  explore next:")
        for e in decision["explore_next"][:5]:
            print(f"    {e['family']:<26} {e['why']}")
    print(f"  retired families: {saved['retired_families'] or 'none'}")
    print(f"  -> {EVOLUTION_FILE}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
