"""Deep analysis across all accumulated research runs.

The daily report answers "what happened today". This answers the harder
questions:

  - Is the search even working? (rank correlation between train and holdout)
  - Which strategy families are actually good, consistently?
  - Which candidates are classic overfits? (great on train, bad on holdout)
  - What should we try NEXT?

The last one matters most. It is derived from the evidence, not guessed:
families that survive repeatedly get promoted into the search space with
new parameters, and families that never survive get retired.
"""
import json
import os
from collections import defaultdict

import numpy as np
import pandas as pd

from . import config


def _rank_corr(a, b):
    """Spearman rank correlation - is train rank predictive of holdout rank?"""
    a = pd.Series(a).rank()
    b = pd.Series(b).rank()
    if len(a) < 3 or a.std() == 0 or b.std() == 0:
        return float("nan")
    return float(a.corr(b))


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
    return {"champion": None, "challenger": None, "history": []}


def analyse(df, state):
    out = {}

    if df.empty:
        out["error"] = "no history yet"
        return out

    runs = sorted(df["run_at"].dropna().unique())
    out["n_runs"] = int(len(runs))
    out["n_candidates_per_run"] = int(df.groupby("run_at").size().median())
    out["cumulative_candidates"] = int(len(df))
    out["first_run"] = str(runs[0]) if runs else None
    out["last_run"] = str(runs[-1]) if runs else None

    # --- is the search working? ------------------------------------------
    # If train rank does not predict holdout rank, the search is noise.
    per_run_corr = []
    for run_at, g in df.groupby("run_at"):
        g = g.dropna(subset=["train_cagr", "holdout_cagr"])
        if len(g) >= 5:
            c = _rank_corr(g["train_cagr"], g["holdout_cagr"])
            if np.isfinite(c):
                per_run_corr.append(c)
    out["selection_efficiency"] = {
        "mean_rank_correlation": round(float(np.mean(per_run_corr)), 4)
        if per_run_corr else None,
        "min": round(float(np.min(per_run_corr)), 4) if per_run_corr else None,
        "max": round(float(np.max(per_run_corr)), 4) if per_run_corr else None,
        "n_runs_measured": len(per_run_corr),
        "verdict": (
            "search is informative" if per_run_corr and np.mean(per_run_corr) > 0.3
            else "search is weakly informative" if per_run_corr and np.mean(per_run_corr) > 0.1
            else "search is mostly noise" if per_run_corr
            else "not enough runs to judge"
        ),
    }

    # --- family level ----------------------------------------------------
    fam = df.groupby("family").agg(
        runs=("candidate_id", "nunique"),
        mean_holdout_cagr=("holdout_cagr", "mean"),
        median_holdout_cagr=("holdout_cagr", "median"),
        mean_train_cagr=("train_cagr", "mean"),
        mean_holdout_dd=("holdout_dd", "mean"),
        mean_dsr=("dsr", "mean"),
        max_dsr=("dsr", "max"),
        times_basic=("passes_basic", "sum"),
        times_gate=("passes_gate", "sum"),
        mean_assets_positive=("assets_positive", "mean"),
    ).sort_values("median_holdout_cagr", ascending=False)
    out["families"] = fam.reset_index().to_dict("records")

    # --- consistency across runs -----------------------------------------
    # A strategy that is good in EVERY run is far more interesting than one
    # that is good in the single best run.
    per_cand = df.groupby("candidate_id").agg(
        runs_seen=("run_at", "nunique"),
        mean_holdout_cagr=("holdout_cagr", "mean"),
        min_holdout_cagr=("holdout_cagr", "min"),
        worst_holdout_cagr=("holdout_cagr", "min"),
        positive_runs=("holdout_cagr", lambda s: int((s > 0).sum())),
        mean_dsr=("dsr", "mean"),
        max_dsr=("dsr", "max"),
        times_basic=("passes_basic", "sum"),
        times_gate=("passes_gate", "sum"),
        mean_assets_positive=("assets_positive", "mean"),
        family=("family", "first"),
    ).reset_index()

    consistent = per_cand[
        (per_cand["runs_seen"] >= 2) & (per_cand["min_holdout_cagr"] > 0)
    ].sort_values("mean_holdout_cagr", ascending=False)
    out["consistent_winners"] = consistent.head(10).to_dict("records")

    # --- overfits ---------------------------------------------------------
    # Great on train, bad on holdout, repeatedly.
    overfit_rows = df[
        (df["train_cagr"] > df["holdout_cagr"] + 5) & (df["holdout_cagr"] < 0)
    ]
    overfits = overfit_rows.groupby("candidate_id").agg(
        times=("run_at", "nunique"),
        mean_train=("train_cagr", "mean"),
        mean_holdout=("holdout_cagr", "mean"),
    ).sort_values("times", ascending=False)
    out["overfits"] = overfits.head(10).reset_index().to_dict("records")

    # --- champion timeline ------------------------------------------------
    champ_hist = []
    for run_at, g in df.groupby("run_at"):
        c = state.get("champion")
        if not c:
            continue
        row = g[g["candidate_id"] == c.get("id")]
        if len(row):
            champ_hist.append({
                "run_at": str(run_at),
                "id": c.get("id"),
                "holdout_cagr": float(row["holdout_cagr"].iloc[0]),
                "holdout_dd": float(row["holdout_dd"].iloc[0]),
            })
    out["champion_timeline"] = champ_hist

    # --- what to try next ------------------------------------------------
    suggestions = []
    for _, r in consistent.head(5).iterrows():
        suggestions.append(
            f"KEEP: `{r['candidate_id']}` was positive in "
            f"{int(r['positive_runs'])}/{int(r['runs_seen'])} runs "
            f"(mean holdout {r['mean_holdout_cagr']:.1f}%, worst "
            f"{r['worst_holdout_cagr']:.1f}%, mean DSR {r['mean_dsr']:.3f})"
        )
    for _, r in fam.head(4).iterrows():
        suggestions.append(
            f"FAMILY `{r.name}` has the best median holdout CAGR "
            f"({r['median_holdout_cagr']:.1f}%) - add more parameters to it"
        )
    if out["selection_efficiency"].get("mean_rank_correlation") is not None:
        c = out["selection_efficiency"]["mean_rank_correlation"]
        if c <= 0.1:
            suggestions.append(
                "WARNING: train rank barely predicts holdout rank "
                f"(rho={c:.2f}). The search space may be too noisy to be "
                "useful - consider fewer, more distinct rules rather than "
                "more parameter combinations."
            )
    out["suggestions"] = suggestions

    return out


def render(report):
    if report.get("error"):
        return f"# Deep report\n\n{report['error']}\n"
    L = []
    L.append("# Deep research report")
    L.append("")
    L.append(f"- Runs analysed: **{report['n_runs']}**")
    L.append(f"- Candidates per run: ~{report['n_candidates_per_run']}")
    L.append(f"- Cumulative candidates evaluated: **{report['cumulative_candidates']:,}**")
    L.append(f"- Window: {report['first_run']} -> {report['last_run']}")
    L.append("")

    se = report["selection_efficiency"]
    L.append("## Is the search actually working?")
    L.append("")
    L.append(f"- Train-vs-holdout rank correlation: **{se['mean_rank_correlation']}** "
             f"(min {se['min']}, max {se['max']}, over {se['n_runs_measured']} runs)")
    L.append(f"- Verdict: **{se['verdict']}**")
    L.append("")
    L.append("> A correlation near 0 means the backtest ranking carries no "
             "information about future performance - the search is noise. "
             "Above 0.3 means the search genuinely finds something.")
    L.append("")

    L.append("## Strategy families")
    L.append("")
    L.append("| family | mean holdout CAGR | median | mean DD | mean DSR | max DSR | times basic | times gate |")
    L.append("|---|---|---|---|---|---|---|---|")
    for r in report["families"]:
        L.append(f"| `{r['family']}` | {r['mean_holdout_cagr']:.1f}% | "
                 f"{r['median_holdout_cagr']:.1f}% | {r['mean_holdout_dd']:.1f}% | "
                 f"{r['mean_dsr']:.3f} | {r['max_dsr']:.3f} | "
                 f"{int(r['times_basic'])} | {int(r['times_gate'])} |")
    L.append("")

    L.append("## Consistent winners (positive in every run seen)")
    L.append("")
    if report["consistent_winners"]:
        L.append("| strategy | runs | positive | mean holdout | worst holdout | mean DSR | assets+ |")
        L.append("|---|---|---|---|---|---|---|")
        for r in report["consistent_winners"]:
            L.append(f"| `{r['candidate_id']}` | {int(r['runs_seen'])} | "
                     f"{int(r['positive_runs'])} | {r['mean_holdout_cagr']:.1f}% | "
                     f"{r['worst_holdout_cagr']:.1f}% | {r['mean_dsr']:.3f} | "
                     f"{r['mean_assets_positive']:.1f} |")
    else:
        L.append("None yet - not enough runs, or nothing survives every window.")
    L.append("")

    L.append("## Repeat overfits")
    L.append("")
    L.append("| strategy | times | mean train | mean holdout |")
    L.append("|---|---|---|---|")
    if report["overfits"]:
        for r in report["overfits"]:
            L.append(f"| `{r['candidate_id']}` | {int(r['times'])} | "
                     f"{r['mean_train']:.1f}% | {r['mean_holdout']:.1f}% |")
    else:
        L.append("| none | - | - | - |")
    L.append("")

    L.append("## What to try next")
    L.append("")
    for s in report["suggestions"]:
        L.append(f"- {s}")
    L.append("")
    return "\n".join(L) + "\n"


def main():
    df = load_history()
    state = load_state()
    report = analyse(df, state)

    out_dir = os.path.join(config.PROJECT_ROOT, "research")
    json_path = os.path.join(out_dir, "deep-report.json")
    md_path = os.path.join(out_dir, "deep-report.md")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, default=str)
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(render(report))
    print(f"deep report -> {md_path}")
    if report.get("error"):
        print(report["error"])
    else:
        se = report["selection_efficiency"]
        print(f"runs: {report['n_runs']}  candidates: {report['cumulative_candidates']}")
        print(f"selection efficiency (rank corr): {se['mean_rank_correlation']} "
              f"-> {se['verdict']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
