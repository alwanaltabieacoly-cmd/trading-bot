import sys
import os
import json
import logging
from datetime import datetime, timezone
from pathlib import Path

sys.path.append(os.path.dirname(__file__))

from TrendAdx1hRegime import TrendAdx1hRegime

logger = logging.getLogger(__name__)


class TrendAdx1hRegimeVeto(TrendAdx1hRegime):
    _decision_cache_ttl = 60

    _decision = None
    _decision_ts = None

    def _load_decision(self) -> dict:
        now = datetime.now(timezone.utc)
        if (
            self._decision_ts is not None
            and (now - self._decision_ts).total_seconds() < self._decision_cache_ttl
        ):
            return self._decision

        path = Path(self.config["user_data_dir"]) / "decisions" / "latest.json"
        try:
            with open(path, "r", encoding="utf-8") as fh:
                decision = json.load(fh)
        except (OSError, ValueError) as exc:
            logger.info("Regime veto: decision file unavailable (%s): %s", path, exc)
            decision = None

        self._decision = decision
        self._decision_ts = now
        return decision

    @staticmethod
    def _parse_generated_at(value):
        if not isinstance(value, str):
            return None
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return None
        if parsed.tzinfo is None:
            parsed = parsed.replace(tzinfo=timezone.utc)
        return parsed

    def confirm_trade_entry(
        self,
        pair: str,
        order_type: str,
        amount: float,
        rate: float,
        time_in_force: str,
        current_time: datetime,
        entry_tag,
        side: str,
        **kwargs,
    ) -> bool:
        if self.dp.runmode.value not in ("dry_run", "live"):
            return True

        decision = self._load_decision()
        if not isinstance(decision, dict):
            logger.info("Regime veto: blocking %s, decision file missing or unparseable", pair)
            return False

        generated_at = self._parse_generated_at(decision.get("generated_at"))
        if generated_at is None:
            logger.info("Regime veto: blocking %s, invalid generated_at", pair)
            return False

        age = datetime.now(timezone.utc) - generated_at
        if age.total_seconds() > 26 * 3600:
            logger.info("Regime veto: blocking %s, decision stale (age %s)", pair, age)
            return False

        pairs = decision.get("pairs")
        entry = pairs.get(pair) if isinstance(pairs, dict) else None
        if not isinstance(entry, dict):
            logger.info("Regime veto: blocking %s, pair not present in decision", pair)
            return False

        action = entry.get("action")
        size = entry.get("size")
        if action != "allow":
            logger.info("Regime veto: blocking %s, action=%s", pair, action)
            return False
        if not isinstance(size, (int, float)) or size <= 0:
            logger.info("Regime veto: blocking %s, size=%s", pair, size)
            return False

        return True

    def custom_stake_amount(
        self,
        pair: str,
        current_time: datetime,
        current_rate: float,
        proposed_stake: float,
        min_stake,
        max_stake: float,
        leverage: float,
        entry_tag,
        side: str,
        **kwargs,
    ) -> float:
        if self.dp.runmode.value not in ("dry_run", "live"):
            return proposed_stake

        decision = self._load_decision()
        if not isinstance(decision, dict):
            return proposed_stake

        pairs = decision.get("pairs")
        entry = pairs.get(pair) if isinstance(pairs, dict) else None
        if not isinstance(entry, dict):
            return proposed_stake

        size = entry.get("size")
        if not isinstance(size, (int, float)):
            return proposed_stake

        size = max(0.0, min(1.0, float(size)))
        stake = proposed_stake * size
        if size > 0 and min_stake is not None and stake < min_stake:
            stake = min_stake
        return stake
