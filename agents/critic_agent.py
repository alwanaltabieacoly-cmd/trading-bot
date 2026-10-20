"""Critic agent: red-teams the Analyst candidate. Must attempt to falsify."""
from . import common


def _evidence_for(market, candidate_pair):
    tf = market.get("pairs", {}).get(candidate_pair, {}).get("timeframes", {})
    return [
        f"regime_1h={tf.get('1h', {}).get('regime')}",
        f"regime_4h={tf.get('4h', {}).get('regime')}",
        f"atr_pct_1h={tf.get('1h', {}).get('atr_pct_14')}",
        f"dist_to_high20_1h={tf.get('1h', {}).get('dist_to_high20_pct')}",
    ]


def analyze(asof, market_report, analyst_recommendation):
    """Return a blackboard entry for the critic.

    analyst_recommendation: dict pair-> {action,size,confidence,rationale}
    """
    claims = []
    blockers = []
    pair_recs = {}
    for pair, rec in (analyst_recommendation or {}).items():
        action = rec.get("action", "block")
        ev = _evidence_for(market_report, pair)
        # Red-team checks
        issues = []
        tf = market_report.get("pairs", {}).get(pair, {}).get("timeframes", {})
        r1 = tf.get("1h", {}).get("regime")
        r4 = tf.get("4h", {}).get("regime")
        if action == "allow" and r1 != "bull":
            issues.append("1h regime not bull while allowing entry")
        if action == "allow" and r4 != "bull":
            issues.append("4h regime not bull while allowing entry")
        atr = tf.get("1h", {}).get("atr_pct_14")
        if atr is not None and atr > 5.0:
            issues.append(f"1h ATR {atr}% high -> slippage risk")
        if issues:
            rec_out = "block"
            blockers.extend(issues)
            rationale = "critic veto: " + "; ".join(issues)
        else:
            rec_out = action
            rationale = "critic: no falsifying evidence found after checking regime + ATR"
        claims.append({
            "text": f"Red-teamed {pair}: {rationale}",
            "evidence": ev,
        })
        pair_recs[pair] = rec_out

    recommendation = "block" if blockers else "allow"
    confidence = 0.6 if blockers else 0.7
    return {
        "agent": "critic",
        "round": None,  # caller sets
        "claims": claims if claims else [{"text": "no pairs to critique", "evidence": ["n/a"]}],
        "recommendation": recommendation,
        "confidence": confidence,
        "blockers": blockers,
        "pair_recommendations": pair_recs,
    }
