import base64
import json

import requests

from . import common


def _btc_regime(asof):
    df = common.load_candles("BTC/USDT", "1d", asof)
    if df is None or len(df) < 2:
        return {"available": False}
    close = df["close"]
    ema200 = close.ewm(span=200, adjust=False).mean()
    last_close = float(close.iloc[-1])
    last_ema200 = float(ema200.iloc[-1])
    return {
        "available": True,
        "close": common.rnd(last_close),
        "ema200": common.rnd(last_ema200),
        "below_ema200": bool(last_close < last_ema200),
    }


def _headers():
    try:
        with open(common.PRIVATE_CONFIG_PATH, encoding="utf-8") as fh:
            cfg = json.load(fh)
        api = cfg.get("api_server", {})
        user = api.get("username")
        password = api.get("password")
        if user is None or password is None:
            return None
        token = base64.b64encode(f"{user}:{password}".encode("utf-8")).decode("ascii")
        return {"Authorization": f"Basic {token}"}
    except Exception:
        return None


def _get(api_url, path, headers):
    try:
        resp = requests.get(api_url.rstrip("/") + path, headers=headers, timeout=15)
        resp.raise_for_status()
        return resp.json()
    except Exception:
        return None


def _account(api_url):
    headers = _headers()
    result = {
        "max_drawdown": None,
        "open_trades": None,
        "profit_all_coin": None,
        "stake_currency": None,
    }
    profit = _get(api_url, "/profit", headers)
    if isinstance(profit, dict):
        result["max_drawdown"] = profit.get("max_drawdown")
        result["profit_all_coin"] = profit.get("profit_all_coin")
        result["stake_currency"] = profit.get("stake_currency")
    status = _get(api_url, "/status", headers)
    if isinstance(status, list):
        result["open_trades"] = len(
            [t for t in status if isinstance(t, dict) and t.get("pair")]
        )
    elif isinstance(status, dict) and isinstance(status.get("trades"), list):
        result["open_trades"] = len(status["trades"])
    return result


def analyze(asof, api_url=None):
    asof_dt = common.parse_utc(asof)
    btc = _btc_regime(asof_dt)
    account = _account(api_url) if api_url else None
    drawdown = account.get("max_drawdown") if account else None
    reasons = []
    if drawdown is not None and drawdown > 0.10:
        size_cap = 0.0
        reasons.append("max drawdown > 10%")
    elif btc.get("below_ema200") is True:
        size_cap = 0.5
        reasons.append("BTC below EMA200")
    else:
        size_cap = 1.0
    return {
        "asof": common.iso_utc(asof_dt),
        "btc": btc,
        "account": account,
        "drawdown": drawdown,
        "size_cap": size_cap,
        "reasons": reasons,
    }
