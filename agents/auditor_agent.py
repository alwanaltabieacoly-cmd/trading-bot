"""Auditor agent: checks that claims are supported by evidence; rejects unsupported."""
from . import common


def analyze(asof, blackboard_round_entries):
    """Return a blackboard entry for the auditor.

    Inspects all entries in the given round; rejects any claim lacking
    non-empty evidence or any agent that issued a recommendation without claims.
    """
    blockers = []
    claims = []
    for agent, entry in (blackboard_round_entries or {}).items():
        ecs = entry.get("claims", [])
        if not ecs:
            blockers.append(f"{agent}: recommendation without any claims")
            claims.append({"text": f"{agent} has no claims", "evidence": ["blackboard"]})
            continue
        for c in ecs:
            ev = c.get("evidence")
            if not (isinstance(ev, list) and ev):
                blockers.append(f"{agent}: claim without evidence: {c.get('text','?')}")
            else:
                claims.append({
                    "text": f"verified {agent} claim: {c.get('text','')}",
                    "evidence": ev,
                })
    recommendation = "block" if blockers else "allow"
    return {
        "agent": "auditor",
        "round": None,
        "claims": claims if claims else [{"text": "no claims to audit", "evidence": ["blackboard"]}],
        "recommendation": recommendation,
        "confidence": 0.9 if not blockers else 0.4,
        "blockers": blockers,
        "pair_recommendations": {},
    }
