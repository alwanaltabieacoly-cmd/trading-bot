"""Validation and overfitting protection.

A backtest that finds the best of many parameter sets will always find
something that looks great. That is a property of the search, not of the
market. Three guards here:

1. HOLDOUT IS SACRED. Candidates are selected using data up to TRAIN_END.
   The holdout window is only used to give a final verdict on the handful
   of survivors. It is never used to choose between candidates.

2. DEFlated Sharpe Ratio. Bailey and Lopez de Prado's correction for the
   fact that the best of N trials has an inflated Sharpe ratio by chance.
   Without this, a search of 200 parameter sets will always "discover" a
   winner. The DSR subtracts the expected maximum Sharpe under a null of
   no skill, given the number of trials tried.

3. CONSISTENCY. A real edge shows up across assets. A lucky parameter set
   shows up on one and nowhere else.
"""
import math

import numpy as np

from . import config


# --------------------------------------------------------------------------
# Deflated Sharpe Ratio
# --------------------------------------------------------------------------


def _norm_cdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def deflated_sharpe(sharpe_annual, n_trials, n_obs, periods_per_year, skew=0.0, kurt=3.0):
    """Probability the observed Sharpe exceeds what pure luck would produce.

    sharpe_annual   : observed ANNUALISED Sharpe ratio
    n_trials        : how many strategy candidates were tried
    n_obs           : number of return observations (bars) used
    periods_per_year: bars per year, to annualise/unannualise

    Follows Lo ("The Statistics of Sharpe Ratios", 2nd ed.): the expected
    maximum Sharpe across N independent trials, then the probability that
    the observed Sharpe clears that bar.

    Units matter here. The expected maximum is a multiple of the STANDARD
    ERROR of the Sharpe estimate, not an absolute number - getting that
    wrong makes every strategy look like noise.
    """
    if n_trials <= 1 or n_obs <= 2 or not np.isfinite(sharpe_annual):
        return 0.5 if n_trials <= 1 else 0.0

    euler = 0.5772156649015329

    # per-observation Sharpe (the units the trial-count maths assumes)
    sr = sharpe_annual / math.sqrt(periods_per_year)

    # variance of the Sharpe estimate (Skew/Kurt correction)
    var_sharpe = (
        1.0
        + (0.5 * skew * sr)
        + ((kurt - 3.0) / 8.0) * (sr ** 2 - 1.0)
    ) / (n_obs - 1)
    se = math.sqrt(max(var_sharpe, 1e-12))

    # expected maximum Sharpe across n_trials independent trials, in SE units
    expected_max = se * (
        (1 - euler) * _norm_cdf_inv(1 - 1.0 / n_trials)
        + euler * _norm_cdf_inv(1 - 1.0 / (n_trials * math.e))
    )

    z = (sr - expected_max) / se
    return _norm_cdf(z)


def _norm_cdf_inv(p):
    """Inverse normal CDF via rational approximation (Acklam)."""
    if p <= 0:
        return -8.0
    if p >= 1:
        return 8.0
    a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
         1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
         6.680131188771972e+01, -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
         -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00,
         3.754408661907416e+00]
    plow, phigh = 0.02425, 1 - 0.02425
    if p < plow:
        q = math.sqrt(-2 * math.log(p))
        return (((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / \
               ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    if p > phigh:
        q = math.sqrt(-2 * math.log(1 - p))
        return -(((((c[0] * q + c[1]) * q + c[2]) * q + c[3]) * q + c[4]) * q + c[5]) / \
               ((((d[0] * q + d[1]) * q + d[2]) * q + d[3]) * q + 1)
    q = p - 0.5
    r = q * q
    return (((((a[0] * r + a[1]) * r + a[2]) * r + a[3]) * r + a[4]) * r + a[5]) * q / \
           (((((b[0] * r + b[1]) * r + b[2]) * r + b[3]) * r + b[4]) * r + 1)


# --------------------------------------------------------------------------
# promotion gate
# --------------------------------------------------------------------------


def passes_basic(candidate):
    """Rules a strategy must clear to even be considered.

    These are about making money and being consistent - not about
    beating a statistical bar.
    """
    reasons = []
    ok = True

    if candidate["train_cagr"] <= 0:
        ok = False
        reasons.append(f"train CAGR {candidate['train_cagr']:.1f}% <= 0")
    if candidate["holdout_cagr"] <= 0:
        ok = False
        reasons.append(f"holdout CAGR {candidate['holdout_cagr']:.1f}% <= 0")
    if candidate["assets_positive"] < config.MIN_ASSET_CONSISTENCY:
        ok = False
        reasons.append(
            f"only {candidate['assets_positive']}/{candidate['assets_tested']} assets "
            f"positive < {config.MIN_ASSET_CONSISTENCY}"
        )
    if candidate["train_dd"] < -60:
        ok = False
        reasons.append(f"train drawdown {candidate['train_dd']:.1f}% too deep")
    return ok, reasons


def passes_gate(candidate):
    """Everything a challenger must clear to be promoted.

    On top of the basic rules, the deflated Sharpe probability must be
    high enough that the result cannot be explained by having tried a lot
    of parameter combinations.
    """
    ok, reasons = passes_basic(candidate)
    if candidate["dsr"] < config.MIN_DEFLATED_SHARPE:
        ok = False
        reasons.append(
            f"deflated Sharpe prob {candidate['dsr']:.3f} < {config.MIN_DEFLATED_SHARPE}"
        )
    if candidate["train_cagr"] < config.MIN_TRAIN_CAGR_PCT:
        ok = False
        reasons.append(
            f"train CAGR {candidate['train_cagr']:.1f}% < {config.MIN_TRAIN_CAGR_PCT}%"
        )
    return ok, reasons


def beats_champion(candidate_holdout_cagr, champion_holdout_cagr):
    if champion_holdout_cagr is None:
        return True
    return candidate_holdout_cagr > (
        champion_holdout_cagr + config.MIN_IMPROVEMENT_OVER_CHAMPION_PCT
    )
