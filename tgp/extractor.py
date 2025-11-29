from .genes import GENES
from .models import Genome

def extract_genes(name, src):
    low = src.lower()
    g = {}

    if "mint(" in low and "cap" not in low and "max" not in low:
        g["MINT_UNBOUNDED"] = True
    if "mint(" in low and ("cap" in low or "max" in low):
        g["MINT_CAPPED"] = True
    if "burn(" in low:
        g["BURN_ALLOWED"] = True
    if "rebase" in low:
        g["REBASING_SUPPLY"] = True

    if any(x in low for x in ["fee","tax","redistribute"]) and "transfer" in low:
        g["FEE_BASIC"] = True
    if "setfee" in low or "settax" in low:
        g["FEE_DYNAMIC"] = True
    if g.get("FEE_BASIC") and "onlyowner" in low:
        g["FEE_HIGH_RISK_PATTERN"] = True

    if "onlyowner" in low:
        g["OWNER_EOA_LIKE"] = True
    if "renounceownership" in low:
        g["OWNER_RENOUNCE_LOGIC"] = True
    if "blacklist" in low:
        g["BLACKLIST_PRESENT"] = True
    if "whitelist" in low:
        g["WHITELIST_PRESENT"] = True
    if "tradingenabled" in low or "enabletrading" in low:
        g["TRADING_TOGGLE"] = True

    if g.get("BLACKLIST_PRESENT") and g.get("TRADING_TOGGLE"):
        g["HONEYPOT_LIKE"] = True

    if "setprice" in low or "updateprice" in low:
        g["MANUAL_PRICE_SETTER"] = True

    if "proxy" in low or ("implementation" in low and "delegatecall" in low):
        g["PROXY_UPGRADEABLE"] = True

    if low.count("onlyowner") >= 3:
        g["CENTRALIZATION_RISK_HIGH"] = True

    for k in GENES:
        g.setdefault(k, False)

    return Genome(name, g)
