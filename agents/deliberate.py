"""Deliberative orchestrator: blackboard + critic + auditor + synthesizer.

Wraps decision_agent.decide() outputs into a structured multi-agent
deliberation. Keeps the existing decide() as the data-gathering/LLM step,
then adds red-team + audit + synthesis on top.
"""
from . import common, decision_agent, critic_agent, auditor_agent, synthesizer_agent, blackboard as bb


def run(pairs, asof, use_llm=True, api_url=None, live_orderbook=False, anonymize=False):
    asof_dt = common.parse_utc(asof) if not hasattr(asof, "tzinfo") else asof
    # Gather reports + LLM decision via existing pipeline
    decision = decision_agent.decide(
        pairs, asof_dt, use_llm=use_llm, api_url=api_url,
        live_orderbook=live_orderbook, anonymize=anonymize,
    )
    reports = decision["reports"]
    market = reports["market"]
    risk = reports["risk"]
    analyst_rec = decision["pairs"]  # treat LLM output as analyst recommendation
    b = bb.Blackboard(common.iso_utc(asof_dt), pairs)

    # Round 1: analyst (from decide()) + risk + critic
    analyst_entry = {
        "agent": "analyst",
        "round": 1,
        "claims": [{"text": f"LLM decision source={decision['source']}", "evidence": ["decision.pairs"]}],
        "recommendation": "allow" if any(v.get("action") == "allow" for v in analyst_rec.values()) else "block",
        "confidence": common.rnd(sum(v.get("confidence", 0.0) for v in analyst_rec.values()) / max(1, len(analyst_rec))),
        "blockers": [],
        "pair_recommendations": {p: v.get("action", "block") for p, v in analyst_rec.items()},
    }
    risk_entry = {
        "agent": "risk",
        "round": 1,
        "claims": [{"text": f"size_cap={risk.get('size_cap')}", "evidence": [f"drawdown={risk.get('drawdown')}", f"reasons={risk.get('reasons')}"]}],
        "recommendation": "allow" if risk.get("size_cap", 0) > 0 else "block",
        "confidence": 0.9,
        "blockers": risk.get("reasons", []),
        "pair_recommendations": {},
    }
    critic_raw = critic_agent.analyze(asof_dt, market, analyst_rec)
    critic_raw["round"] = 1
    b.add(analyst_entry)
    b.add(risk_entry)
    b.add(critic_raw)

    # Round 2: synthesizer + auditor
    synth_entry, decision_pairs = synthesizer_agent.analyze(
        asof_dt, market, risk, analyst_rec, critic_raw.get("pair_recommendations", {}), 2
    )
    synth_entry["round"] = 2
    audit_raw = auditor_agent.analyze(asof_dt, b.round_entries(1))
    audit_raw["round"] = 2
    b.add(synth_entry)
    b.add(audit_raw)

    # If auditor blocks, force block all
    if audit_raw["recommendation"] == "block":
        for p in decision_pairs:
            decision_pairs[p]["action"] = "block"
            decision_pairs[p]["size"] = 0.0
            decision_pairs[p]["rationale"] = "auditor veto: " + "; ".join(audit_raw["blockers"])

    b.convergence = b.converged()
    # override convergence if auditor blocked
    if audit_raw["recommendation"] == "block":
        b.convergence = False

    decision["pairs"] = decision_pairs
    decision["deliberation"] = b.to_dict()
    return decision, b
