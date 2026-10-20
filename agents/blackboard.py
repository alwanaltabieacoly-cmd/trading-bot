"""Structured blackboard for deliberative multi-agent decisions.

Every agent writes a typed artifact per round. Artifacts must carry evidence
citations (numbers/paths) so the Auditor can reject unsupported claims.
"""
import json
from datetime import datetime, timezone


REQUIRED_FIELDS = ("agent", "round", "claims", "recommendation", "confidence", "blockers")
CLAIM_REQUIRED = ("text", "evidence")


class BlackboardError(ValueError):
    pass


def _validate_claim(claim):
    if not isinstance(claim, dict):
        raise BlackboardError("claim must be a dict")
    for f in CLAIM_REQUIRED:
        if f not in claim:
            raise BlackboardError(f"claim missing required field: {f}")
    if not isinstance(claim["evidence"], list) or not claim["evidence"]:
        raise BlackboardError("claim.evidence must be a non-empty list")
    if not isinstance(claim["text"], str) or not claim["text"].strip():
        raise BlackboardError("claim.text must be a non-empty string")


def _validate_entry(entry):
    if not isinstance(entry, dict):
        raise BlackboardError("entry must be a dict")
    for f in REQUIRED_FIELDS:
        if f not in entry:
            raise BlackboardError(f"entry missing required field: {f}")
    if not isinstance(entry["round"], int) or entry["round"] < 1:
        raise BlackboardError("entry.round must be a positive int")
    if not isinstance(entry["claims"], list):
        raise BlackboardError("entry.claims must be a list")
    for c in entry["claims"]:
        _validate_claim(c)
    if entry["recommendation"] not in ("allow", "block", "abstain"):
        raise BlackboardError("entry.recommendation must be allow/block/abstain")
    if not isinstance(entry["confidence"], (int, float)):
        raise BlackboardError("entry.confidence must be numeric")
    if not (0.0 <= float(entry["confidence"]) <= 1.0):
        raise BlackboardError("entry.confidence must be in [0,1]")
    if not isinstance(entry["blockers"], list):
        raise BlackboardError("entry.blockers must be a list")


class Blackboard:
    def __init__(self, asof, pairs):
        self.asof = asof
        self.pairs = list(pairs)
        self.rounds = {}
        self.history = []
        self.convergence = None

    def add(self, entry):
        _validate_entry(entry)
        r = entry["round"]
        self.rounds.setdefault(r, {})
        self.rounds[r][entry["agent"]] = entry
        self.history.append(entry)

    def round_entries(self, r):
        return dict(self.rounds.get(r, {}))

    def agents_in_round(self, r):
        return list(self.rounds.get(r, {}).keys())

    def latest_by_agent(self, agent):
        out = None
        for e in self.history:
            if e["agent"] == agent:
                out = e
        return out

    def converged(self, threshold=0.15):
        if len(self.rounds) < 2:
            return False
        rs = sorted(self.rounds.keys())
        prev, cur = self.rounds[rs[-2]], self.rounds[rs[-1]]
        if not prev or not cur:
            return False

        def recs(entries):
            out = {}
            for e in entries.values():
                pr = e.get("pair_recommendations", {})
                for pair in self.pairs:
                    if pair in pr:
                        out.setdefault(pair, []).append(pr[pair])
            return out

        r_prev = recs(prev)
        r_cur = recs(cur)
        if not r_prev or not r_cur:
            return False

        def maj(xs):
            allows = sum(1 for x in xs if x == "allow")
            return "allow" if allows > len(xs) / 2 else "block"

        agreed = 0
        total = 0
        for pair in self.pairs:
            a = r_prev.get(pair, [])
            b = r_cur.get(pair, [])
            if not a or not b:
                continue
            total += 1
            if maj(a) == maj(b):
                agreed += 1
        if total == 0:
            return False
        return (agreed / total) >= (1.0 - threshold)

    def to_dict(self):
        return {
            "asof": self.asof,
            "pairs": self.pairs,
            "rounds": {str(k): v for k, v in self.rounds.items()},
            "convergence": self.convergence,
        }

    def dump(self, path):
        from pathlib import Path
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(self.to_dict(), fh, indent=2, default=str)
