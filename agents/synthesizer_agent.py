"""Synthesizer: merges analyst + critic + risk + session + news into a final decision."""
from . import common


def analyze(asof, market_report, risk_report, analyst_rec, critic_rec, round_num):
    """Produce a blackboard entry + a normalized decision dict.

    Returns (entry, decision_pairs) where decision_pairs is pair->decision dict.
    """
    size_cap = risk_report.get("size_cap", 0.0) if isinstance(risk_report, dict) else 0.0
    pairs = list((analyst_rec or {}).keys()) or list((critic_rec or {}).keys())
    decision_pairs = {}
    blockers_all = []
    claims = []
    for pair in pairs:
        a = (analyst_rec or {}).get(pair, {})
        c = (critic_rec or {}).get(pair, {})
        a_action = a.get("action", "block")
        c_action = c.get("action", "block") if isinstance(c, dict) else "block"
        # Convergence rule: allow only if BOTH analyst and critic allow
        if a_action == "allow" and c_action == "allow" and size_cap > 0:
            action = "allow"
            size = min(float(a.get("size", size_cap)), size_cap)
            rationale = "synthesizer: analyst+critic agree allow"
        else:
            action = "block"
            size = 0.0
            reasons = []
            if a_action != "allow":
                reasons.append(f"analyst={a_action}")
            if c_action != "allow":
                reasons.append(f"critic={c_action}")
            if size_cap <= 0:
                reasons.append("size_cap=0")
            rationale = "synthesizer: blocked (" + ", ".join(reasons or ["n/a"]) + ")"
        if action == "block":
            blockers_all.append(f"{pair}: {rationale}")
        confidence = min(
            float(a.get("confidence", 0.5)), float(c.get("confidence", 0.5)) if isinstance(c, dict) else 0.5
        )
        decision_pairs[pair] = {
            "action": action,
            "size": common.rnd(size),
            "confidence": common.rnd(confidence),
            "rationale": rationale,
        }
        claims.append({
            "text": f"{pair}: {action} size={size}",
            "evidence": [
                f"analyst_action={a_action}",
                f"critic_action={c_action}",
                f"size_cap={size_cap}",
            ],
        })
    recommendation = "block" if all(v["action"] == "block" for v in decision_pairs.values()) else "allow"
    entry = {
        "agent": "synthesizer",
        "round": round_num,
        "claims": claims if claims else [{"text": "no pairs", "evidence": ["n/a"]}],
        "recommendation": recommendation,
        "confidence": common.rnd(sum(v["confidence"] for v in decision_pairs.values()) / max(1, len(decision_pairs))),
        "blockers": blockers_all,
        "pair_recommendations": {p: decision_pairs[p]["action"] for p in decision_pairs},
    }
    return entry, decision_pairs
