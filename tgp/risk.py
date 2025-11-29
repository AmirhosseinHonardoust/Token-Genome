from typing import Dict, Any
from .genes import GENES
from .models import Genome

# Simple weights per gene. You can tune these later.
RISK_WEIGHTS: Dict[str, int] = {
    "MINT_UNBOUNDED": 4,
    "MINT_CAPPED": 1,
    "BURN_ALLOWED": 1,
    "REBASING_SUPPLY": 2,
    "FEE_BASIC": 1,
    "FEE_DYNAMIC": 2,
    "FEE_HIGH_RISK_PATTERN": 4,
    "OWNER_EOA_LIKE": 2,
    "OWNER_RENOUNCE_LOGIC": -1,   # small reduction if renounce logic exists
    "BLACKLIST_PRESENT": 3,
    "WHITELIST_PRESENT": 2,
    "TRADING_TOGGLE": 2,
    "HONEYPOT_LIKE": 5,
    "MANUAL_PRICE_SETTER": 4,
    "PROXY_UPGRADEABLE": 2,
    "CENTRALIZATION_RISK_HIGH": 4,
}


def compute_risk(genome: Genome) -> Dict[str, Any]:
    """Compute a simple risk score and level from active genes."""
    score = 0
    contrib: Dict[str, int] = {}

    for key, active in genome.genes.items():
        if not active:
            continue
        w = RISK_WEIGHTS.get(key, 0)
        if w != 0:
            score += w
            contrib[key] = w

    if score <= 0:
        level = "NONE"
    elif score <= 4:
        level = "LOW"
    elif score <= 8:
        level = "MEDIUM"
    elif score <= 14:
        level = "HIGH"
    else:
        level = "CRITICAL"

    return {
        "score": score,
        "level": level,
        "contributions": contrib,
    }
