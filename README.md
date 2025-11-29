# **Token Genome Project, Extended Technical README**

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python_3.10+-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/Solidity-0.8.x-363636?style=for-the-badge&logo=solidity">
  <img src="https://img.shields.io/badge/Focus-Token%20Genomics-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Analysis-Economic%20Behavior-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Project-Research--Grade-blueviolet?style=for-the-badge">
  <img src="https://img.shields.io/badge/Risk-Scoring%20Engine-green?style=for-the-badge">
</p>


### *A Research-Grade Framework for Genetic Classification of Tokenomics, On-Chain Behavior, and Smart Contract Economic Structures*

---

# Introduction

Smart contract tokens, especially ERC-20 derivatives, have evolved from simple fixed-supply assets to **complex economic organisms** with dynamic behavior, intricate control structures, embedded incentive systems, and sometimes malicious intent. The token ecosystem contains **thousands of mutations, forks, adaptations, and design patterns**.

The **Token Genome Project (TGP)** introduces a new analytical paradigm:

> **Treat each token as an organism, and extract its "genetic" code.**

These “genes” are not biological; they are **behavioral, economic, and structural features** that define what a token *can do*, *is allowed to do*, or *is capable of becoming*.

This README explains:

* **the theory behind token genomics**
* **why genes matter**
* **how the classification system is constructed**
* **what risk tells us about "organism fitness"**
* **how TGP extracts genetic traits**
* **how to extend the taxonomy**
* **how to use the tool effectively**
* **the broader implications for DeFi, auditing, and research**

This is not just a tool.
It is a **new lens**.

---

# Project Structure

```
token-genome-project/
│
├── tgp/
│   ├── cli.py           # unified scan + compare CLI
│   ├── extractor.py     # genome inference engine
│   ├── genes.py         # gene definitions + metadata
│   ├── loader.py        # Solidity loader
│   ├── models.py        # Genome & Gene models
│   ├── risk.py          # scoring engine
│   ├── report.py        # HTML report generator
│
├── examples/            # curated token examples
│   ├── simple_token.sol
│   ├── unlimited_mint_token.sol
│   ├── capped_mint_token.sol
│   ├── blacklist_tax.sol
│   ├── rebase_token.sol
│   ├── … etc
│
├── genomes/             # generated JSON/HTML outputs (auto-created)
│
├── README.md
└── pyproject.toml
```

---

# 1. The Theory: What Is Token Genomics?

## 1.1 Tokens behave like evolving species

Token codebases mutate and fork:

* ERC-20 → Reflection Tokens (e.g., SafeMoon species)
* ERC-20 → Tax Tokens → honeypot variants
* ERC-20 → Rebase species (OHM forks, AMPL forks)
* ERC-20 → Proxy mutating species (upgradeable, UUPS)
* ERC-20 → Algorithmic stablecoin species
* ERC-20 → Anti-whale / Anti-bot species
* ERC-20 → Blacklist-regulated governance species

These are not just code differences, they are **predictable evolutionary branches**.

## 1.2 Genes are behavioral feature markers

A "gene" is a binary/categorical feature that influences economic behavior.

Examples:

* **MINT_UNBOUNDED** → infinite inflation potential
* **FEE_DYNAMIC** → admin can alter financial properties after launch
* **BLACKLIST_PRESENT** → admin can selectively disable trading
* **HONEYPOT_LIKE** → potential buy-allow / sell-block
* **PROXY_UPGRADEABLE** → token can mutate in the future
* **MANUAL_PRICE_SETTER** → admin manually defines price values
* **CENTRALIZATION_RISK_HIGH** → excessive admin privileges

These traits directly correspond to real-world behaviors.

## 1.3 Why classify tokens genetically?

This approach answers questions like:

* What species does this token belong to?
* What class of risks does it inherently carry?
* How similar are token A and token B?
* Which features evolved first?
* Are dangerous mutations emerging?
* What behavioral patterns dominate new launches?

---

# 2. Genome Terminology

To make genomics systematic, TGP uses formal definitions:

### **Genome**

A mapping of gene → boolean/number.

### **Gene**

A detectable feature with:

* key
* category
* description
* (optional) weight
* (optional) risk contribution

### **Gene Category**

Genes are grouped by logical taxonomy:

| Category        | Meaning                             |
| --------------- | ----------------------------------- |
| monetary_policy | supply, inflation, burn, rebase     |
| fees            | taxes, reflections, adjustable fees |
| permissions     | ownership, blacklist, whitelist     |
| liquidity       | honeypot behavior, LP control       |
| oracle          | price manipulation vectors          |
| upgradeability  | proxy mutation potential            |
| risk            | centralization, admin power         |

### **Risk Score**

Aggregated gene-weight metric representing "dangerous potential".

### **Species**

Informal classification (future ML clustering). Examples:

* Tax Predator Species
* Rebase Species
* Proxy Mutant Species
* Oracle-Controlled Species
* Blacklist-Regulated Species
* Infinite-Mint Species
* Legitimate Simple Species

---

# 3. How the Genome Extractor Works

TGP uses **heuristic static analysis**:

### 3.1 Pattern detection

The extractor scans for patterns like:

* `mint(`
* `setFee(`
* `setBlacklist(`
* `renounceOwnership`
* `delegatecall` / `implementation`
* `_transfer(` logic complexity
* `price =` or `setPrice()`
* `rebase()`
* fee/tax keywords (`fee`, `tax`, `reflection`, `redistribute`)

### 3.2 Ownership models

Detect EOA-like owner patterns:

* OpenZeppelin Ownable
* custom onlyOwner patterns
* multiple owner-gated functions
* renounceOwnership logic

This determines centralization genes.

### 3.3 Control surfaces

The tool detects:

* selective transfer control
* dynamic fee switching
* trading toggles
* blacklists/whitelists
* admin drain functions
* kill-switches
* LP unlockers

### 3.4 Structural mutations

Proxy detection:

* presence of implementation storage
* delegatecall
* upgrade function
* admin-only upgrade logic

---

# 4. Gene Categories and Deep Explanations

Below is a detailed breakdown of each gene category.

---

## 4.1 Monetary Policy Genes

### **MINT_UNBOUNDED**

Indicates the token has minting without a supply cap.

**Risks:**

* Admin can inflate supply infinitely.
* Price can be destroyed instantly.
* Perfect rug-pull tool.

**Found in:**
Scams, rug tokens, "infinite mint predators".

---

### **MINT_CAPPED**

Minting exists but is bound by a max supply or cap variable.

**Interpretation:**
Potentially trustworthy but needs scrutiny.

---

### **BURN_ALLOWED**

Token can reduce supply via user burn.

**Interpretation:**
Neutral. Sometimes used for deflationary models.

---

### **REBASING_SUPPLY**

Supply adjusts algorithmically (positive or negative).

**Implications:**

* Price and supply correlate inversely.
* Balances may change automatically.
* Not suitable for regular wallets.
* Associated with AMPL/OHM forks.

---

## 4.2 Fee Genes

### **FEE_BASIC**

Simple tax or transfer fee.

### **FEE_DYNAMIC**

Admin can modify fee levels.

**Interpretation:**

* Useful for treasury protocols
* Dangerous for scams (admin -> 100% fee)

---

### **FEE_HIGH_RISK_PATTERN**

Combination of:

* fee-based tokenomics
* owner control
* tax functions
* often seen in honeypots

**Meaning:**
This token is structurally similar to known scams.

---

## 4.3 Permissions

### **OWNER_EOA_LIKE**

Single externally-owned account has high privileges.

**Risk:**
If compromised = total compromise.

---

### **BLACKLIST_PRESENT**

Admin can disable trading for specific addresses.

**Interpretation:**
Often used in:

* honeypots
* rug tokens
* censorship-based control tokens

---

### **WHITELIST_PRESENT**

Trading is allowed only for approved addresses.

**Used by:**

* presale tokens
* launchpad tokens
* early-stage scams to block sells

---

### **TRADING_TOGGLE**

Admin can globally pause/unpause trading.

**High control gene.**

---

## 4.4 Liquidity Genes

### **HONEYPOT_LIKE**

Combined conditions:

* blacklist present
* trading toggle
* fees
  = strong pattern for buy-allowed / sell-blocked scams.

This is a **dangerous gene**.

---

## 4.5 Oracle Genes

### **MANUAL_PRICE_SETTER**

Admin can set price manually.

**Dangers:**

* price manipulation
* liquidation manipulation
* front-running attackers
* stablecoin depegs by admin decision

---

## 4.6 Upgradeability

### **PROXY_UPGRADEABLE**

Token can mutate after deployment.

**Risk spectrum:**

* legitimate upgradable tokens (safe)
* malicious upgrade scripts (rug potential)

Context determines interpretation.

---

## 4.7 Global Risk Gene

### **CENTRALIZATION_RISK_HIGH**

Fires when:

* many admin-only functions
* dynamic powers
* mint + fee control
* oracles + price control

**Meaning:**
The admin is the "god mode" of the token.

---

# 5. Risk Scoring, Detailed Interpretation

TGP uses a weighted score.
Weights are based on:

* historical exploit patterns
* audit findings in real world
* typical scam strategies
* DeFi economic behavior

Weights approximate:

### 1–4: LOW

Minor centralization but no severe vectors.

### 5–8: MEDIUM

Some dangerous patterns, but not fatal.

### 9–14: HIGH

Multiple vectors combine to form a real threat.

### 15+: CRITICAL

This is a ticking time bomb.

---

# 6. HTML Report Format Explained

Each report includes:

### 6.1 Header

Token, risk level, score.

### 6.2 Active Gene Table

For each gene:

* Name
* Category
* Risk Weight
* Description

### 6.3 Interpretation Section *(coming soon)*

Planned features:

* Narrative summary
* Risk explanation paragraphs
* Power mapping (ownership/lp/oracle)

---

# 7. CLI Usage with Full Explanations

### **Scan a folder**

```
tgp-scan examples
```

This:

* loads all `.sol` files
* runs gene extractor
* computes risk
* saves genome JSON
* saves HTML reports
* prints human-readable summary

### **Compare two tokens**

```
tgp-scan --mode compare tokenA.sol --other tokenB.sol
```

This prints:

* shared active genes
* genes unique to A
* genes unique to B
* structural and economic differences

Useful for:

* mutation detection
* fork analysis
* audit differential review
* identifying scam clones

---

# 8. Example Full Output Interpretation

Given:

```
=== unlimited_mint_token.sol ===
Risk: HIGH (score=10)
MINT_UNBOUNDED      ACTIVE  Mint without cap
OWNER_EOA_LIKE      ACTIVE  EOA-like owner control
```

Meaning:

1. **MINT_UNBOUNDED**
   admin can create infinite supply
   → inflation risk + rug capability.

2. **OWNER_EOA_LIKE**
   one person controls the entire token.

3. HIGH score =
   → token belongs to “Infinite Mint Predator” species.
   → not suitable for public trading.

---

# 9. Example: Genetic Difference Between Two Tokens

```
tgp-scan --mode compare unlimited_mint.sol --other capped_mint.sol
```

Output:

```
Shared active genes:
  OWNER_EOA_LIKE

Active only in unlimited_mint:
  MINT_UNBOUNDED

Active only in capped_mint:
  MINT_CAPPED
```

Interpretation:

* Both tokens are centrally controlled (bad).
* One has unlimited inflation (very bad).
* One has capped inflation (acceptable).

---

# 10. Extending the Genome

You can add new genes easily in `tgp/genes.py`.

Potential expansions:

### 10.1 Liquidity Genes

* LIQUIDITY_LOCKED
* LIQUIDITY_UNLOCKABLE
* AUTO_LP_ADD
* REMOVE_LP_ADMIN

### 10.2 Trading Rules

* ANTI_WHALE
* COOL_DOWN
* MAX_SELL_TOKENS

### 10.3 Governance

* TOKEN_VOTING
* TIMELOCK_CONTROLLER
* PAUSABLE_GOV

### 10.4 Advanced Risk

* RUG_DRAIN_VECTOR
* PRICE_MANIPULATION_VECTOR

This can grow into a **200+ gene ecosystem**.

---

# 11. Future Research Directions (Deep Section)

### 11.1 Token Species Evolution

Use clustering to identify:

* evolutionary branches
* signatures of scam evolution
* decentralized vs. centralized species groups
* tokenomic hybrid models

### 11.2 Phylogenetic Tree

Construct token evolution trees similar to biological genealogy.

### 11.3 Gene Drift

Analyze which features drift over time in DeFi cycles.

### 11.4 Dominant Mutations

During bull markets, certain genes dominate (reflection, tax).
During bear markets, others dominate (rebase, stablecoins).

### 11.5 Anomaly Detection

Detect outlier behavior patterns.

### 11.6 On-Chain ML Genome Classifiers

Train models to classify scam species using genetic vectors.

---

# 12. Why This Project Matters

* Allows **scientific understanding** of token ecosystems.
* Helps auditors detect malicious behavior fast.
* Helps researchers map tokenomic evolution.
* Helps analysts compare forks.
* Helps developers avoid dangerous patterns.
* Helps the community identify rug-pull species.

The Token Genome Project is the first step toward **systematic cryptoeconomic taxonomy**.

---

# 13. Final Notes

This project treats tokenomics as a **living ecosystem**.
Each contract is a creature.
Each feature is a gene.
Each combination is a species.

TGP gives you tools to map, classify, evaluate, and compare those organisms.

The deeper you go, the more insights you uncover.
