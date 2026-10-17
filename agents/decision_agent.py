import json

from . import common, market_agent, news_agent, risk_agent, session_agent

INSTRUCTION = (
    "You are a risk veto layer for a crypto spot trading bot (Bybit, USDT pairs). "
    "Every number below is precomputed by deterministic Python agents; your job is only to interpret them. "
    "You may only ALLOW or BLOCK entries per pair and optionally shrink the position size. "
    "You can never place, modify or close orders. "
    "When in doubt, block. "
    "Respond with ONLY one JSON object and nothing else, no prose and no code fences, using exactly this schema: "
    '{"pairs": {"<PAIR>": {"action": "allow" or "block", "size": <0.0-1.0>, '
    '"confidence": <0.0-1.0>, "rationale": "<short text>"}}, "followups": ["<question>", "..."]}. '
    "Include one entry for every requested pair. size is a fraction of the normal stake. "
    "followups may be an empty list if no further data is needed."
)


def _build_prompt(pairs, asof, reports):
    payload = {
        "asof": reports["market"]["asof"],
        "pairs": list(pairs),
        "market": reports["market"],
        "news": reports["news"],
        "session": reports["session"],
        "risk": reports["risk"],
    }
    return (
        INSTRUCTION
        + "\nDATA: "
        + json.dumps(payload, default=str)
        + "\nReturn only the JSON object now."
    )


def _followup_prompt(base_prompt, followups, reports):
    detail = {
        "market": reports["market"],
        "session": reports["session"],
    }
    return (
        base_prompt
        + "\nFOLLOW-UP QUESTIONS: "
        + json.dumps(list(followups), default=str)
        + "\nFULL MARKET AND SESSION DETAIL: "
        + json.dumps(detail, default=str)
        + "\nAnswer again with the same JSON schema and only that JSON."
    )


def _validate_pair(item, size_cap):
    if not isinstance(item, dict):
        return {
            "action": "block",
            "size": 0.0,
            "confidence": 0.0,
            "rationale": "missing or invalid entry",
        }
    action = item.get("action")
    if action not in ("allow", "block"):
        action = "block"
    try:
        size = float(item.get("size"))
    except (TypeError, ValueError):
        size = 0.0
    if size < 0.0:
        size = 0.0
    if size > size_cap:
        size = size_cap
    if action == "block" or size_cap <= 0:
        action = "block"
        size = 0.0
    try:
        confidence = float(item.get("confidence"))
    except (TypeError, ValueError):
        confidence = 0.0
    confidence = min(1.0, max(0.0, confidence))
    rationale = item.get("rationale")
    if not isinstance(rationale, str):
        rationale = ""
    return {
        "action": action,
        "size": common.rnd(size),
        "confidence": common.rnd(confidence),
        "rationale": rationale,
    }


def _normalize(obj, pairs, size_cap):
    raw_pairs = obj.get("pairs") if isinstance(obj, dict) else None
    if not isinstance(raw_pairs, dict):
        raw_pairs = {}
    return {pair: _validate_pair(raw_pairs.get(pair), size_cap) for pair in pairs}


def _fallback(pairs, size_cap, market):
    result = {}
    for pair in pairs:
        timeframes = market.get("pairs", {}).get(pair, {}).get("timeframes", {})
        regime_1h = timeframes.get("1h", {}).get("regime")
        regime_4h = timeframes.get("4h", {}).get("regime")
        if size_cap > 0 and regime_1h == "bull" and regime_4h == "bull":
            result[pair] = {
                "action": "allow",
                "size": common.rnd(size_cap),
                "confidence": 0.5,
                "rationale": "fallback rule: 1h and 4h regime bull",
            }
        else:
            result[pair] = {
                "action": "block",
                "size": 0.0,
                "confidence": 0.5,
                "rationale": (
                    f"fallback rule: 1h regime={regime_1h}, 4h regime={regime_4h}, "
                    f"size_cap={size_cap}"
                ),
            }
    return result


def decide(pairs, asof, use_llm=True, api_url=None, live_orderbook=False):
    asof_dt = common.parse_utc(asof)
    reports = {
        "market": market_agent.analyze(pairs, asof_dt, live_orderbook=live_orderbook),
        "news": news_agent.analyze(asof_dt),
        "session": session_agent.analyze(pairs, asof_dt),
        "risk": risk_agent.analyze(asof_dt, api_url=api_url),
    }
    size_cap = reports["risk"].get("size_cap", 0.0)
    prompts = []
    raws = []
    followups = []
    best = None
    model_used = None
    if use_llm:
        prompt = _build_prompt(pairs, asof_dt, reports)
        prompts.append(prompt)
        for round_index in range(3):
            obj, raw, model = common.call_llm(prompt, timeout=300)
            raws.append(raw)
            if model:
                model_used = model
            if obj is None:
                break
            best = obj
            followups = obj.get("followups")
            if not isinstance(followups, list):
                followups = []
            followups = [f for f in followups if isinstance(f, str) and f.strip()]
            if not followups or round_index >= 2:
                break
            prompt = _followup_prompt(prompt, followups, reports)
            prompts.append(prompt)
    if best is not None:
        source = "llm"
        decision_pairs = _normalize(best, pairs, size_cap)
    else:
        source = "fallback"
        model_used = None
        decision_pairs = _fallback(pairs, size_cap, reports["market"])
    return {
        "asof": common.iso_utc(asof_dt),
        "source": source,
        "model": model_used,
        "pairs": decision_pairs,
        "followups": followups,
        "reports": reports,
        "prompts": prompts,
        "raw": raws,
    }
