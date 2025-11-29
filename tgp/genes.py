from .models import GeneDefinition

GENES = {
    "MINT_UNBOUNDED": GeneDefinition("MINT_UNBOUNDED","monetary","Mint without cap"),
    "MINT_CAPPED": GeneDefinition("MINT_CAPPED","monetary","Mint with cap"),
    "BURN_ALLOWED": GeneDefinition("BURN_ALLOWED","monetary","Burn function present"),
    "REBASING_SUPPLY": GeneDefinition("REBASING_SUPPLY","monetary","Rebase mechanics"),
    "FEE_BASIC": GeneDefinition("FEE_BASIC","fees","Basic fee/tax found"),
    "FEE_DYNAMIC": GeneDefinition("FEE_DYNAMIC","fees","Settable fee logic"),
    "FEE_HIGH_RISK_PATTERN": GeneDefinition("FEE_HIGH_RISK_PATTERN","fees","Honeypot-like fee pattern"),
    "OWNER_EOA_LIKE": GeneDefinition("OWNER_EOA_LIKE","permissions","EOA-like owner control"),
    "OWNER_RENOUNCE_LOGIC": GeneDefinition("OWNER_RENOUNCE_LOGIC","permissions","Renounce logic found"),
    "BLACKLIST_PRESENT": GeneDefinition("BLACKLIST_PRESENT","permissions","Blacklist detected"),
    "WHITELIST_PRESENT": GeneDefinition("WHITELIST_PRESENT","permissions","Whitelist detected"),
    "TRADING_TOGGLE": GeneDefinition("TRADING_TOGGLE","permissions","Trading enable/disable"),
    "HONEYPOT_LIKE": GeneDefinition("HONEYPOT_LIKE","liquidity","Honeypot-like structure"),
    "MANUAL_PRICE_SETTER": GeneDefinition("MANUAL_PRICE_SETTER","oracle","Manual price setter"),
    "PROXY_UPGRADEABLE": GeneDefinition("PROXY_UPGRADEABLE","upgrade","Proxy upgradeable"),
    "CENTRALIZATION_RISK_HIGH": GeneDefinition("CENTRALIZATION_RISK_HIGH","risk","High centralization risk")
}
