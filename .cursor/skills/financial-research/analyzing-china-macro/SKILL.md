---
name: analyzing-china-macro
description: Use when analyzing China's economic and financial situation from a day's news — PBOC policy, Chinese macro data, property sector, A-shares/H-shares, CNY, regulatory moves, or China-global linkages.
---

# Analyzing China Macro Conditions

## Overview

Produce a China-level situation assessment from a verified news log. China requires a separate analytical lens: policy is the dominant driver, official communication is deliberately coded, and data must be read with structural context.

**Core principle: in China analysis, policy intent leads and data follows.** Ask "what is the policy stance and is it shifting?" before "what do the numbers say?"

## When to Use

- Stage 3 of the daily briefing pipeline (input: news log from `gathering-financial-news`)
- Standalone questions about China's economy, markets, or policy direction
- NOT for world-level analysis (use `analyzing-global-macro`)

## Analysis Framework

### 1. Policy stance (the anchor)
- PBOC: MLF/LPR/RRR moves, open-market operation volumes, and the daily CNY fix (a fix persistently stronger/weaker than model estimates is itself a policy signal)
- Fiscal: special bond issuance, consumption subsidies, tax measures
- Regulatory: statements from CSRC, NFRA, MIIT; Politburo/State Council meeting readouts
- **Read official language as code.** Phrase changes matter: 适度宽松 vs 稳健 (moderately loose vs prudent) monetary policy, appearance of 化解风险 (defusing risk), removal of 房住不炒 (housing is for living, not speculation). Compare today's wording with the previous statement — the delta is the signal.

### 2. Growth engines & drags
- Property: new/secondary home prices, developer funding news, land sales — still the biggest drag channel; assess whether stabilization measures are gaining traction
- Consumption vs. investment vs. exports: which is policy leaning on this quarter?
- Local government debt: LGFV refinancing news, debt-swap programs
- Data caveat: cross-check official data against independent proxies when available (Caixin PMI vs official PMI, freight volumes, excavator sales) and flag divergences

### 3. Markets & flows
- A-shares (CSI 300, ChiNext) and H-shares (Hang Seng, HSCEI) — divergence between them often reflects foreign vs domestic sentiment split
- Northbound/southbound Stock Connect flows as foreign-appetite gauges
- CNY/CNH spread: widening = offshore depreciation pressure
- CGB yields: falling long yields despite stimulus = domestic pessimism / asset famine (资产荒)

### 4. External linkages
- US-China: tariffs, export controls (semis, critical minerals), entity-list actions, delisting risk
- China as global demand: commodity import trends (copper, iron ore, oil) as real-time activity proxies
- Supply-chain shift news (relocation to Vietnam/India/Mexico) as structural context

## Output Format

```markdown
## China Situation

**Policy stance:** 1–2 sentences on current stance and today's shift, if any.

**What changed today:** 2–4 bullets citing news-log items.

**What it implies:** 2–3 conditional statements.

**Divergences to watch:** official vs proxy data, A/H gap, CNY fix vs market, onshore/offshore sentiment split.
```

## Common Mistakes

- **Taking announcement = implementation.** Chinese policy announcements are directional; scale and execution often follow slowly. Note when a measure lacks size or timeline.
- **Reading China with a Western central-bank lens.** PBOC targets multiple objectives (growth, FX stability, leverage) simultaneously; a single-rate cut isn't the whole stance.
- **Ignoring the fix.** The daily CNY central parity is one of the most reliable daily policy signals available and rarely makes headlines.
- **Treating stimulus headlines as automatically bullish.** Large stimulus can signal that conditions are worse than official data shows — note both readings.
- **Only using English sources.** Key details often appear in Chinese-language outlets hours earlier; see the sources reference in `gathering-financial-news`.
