---
name: analyzing-global-macro
description: Use when analyzing world-level financial and economic conditions from a day's news — assessing global markets, central bank policy, growth, inflation, or risk sentiment as part of a research pipeline or on request.
---

# Analyzing Global Macro Conditions

## Overview

Turn a verified news log into a world-level situation assessment: what regime are we in, what changed today, and what does it imply.

**Core principle: separate the state from the delta.** Most daily news confirms the existing regime; the analytical value is in identifying the few items that change it. An assessment that treats every item as equally important is noise.

## When to Use

- Stage 2 of the daily briefing pipeline (input: news log from `gathering-financial-news`)
- Standalone "what's going on in global markets/economy?" requests
- NOT for single-company analysis or China domestic analysis (use `analyzing-china-macro`)

## Analysis Framework

Work through four lenses, citing news-log items for every claim:

### 1. Monetary policy & rates
Where are the major central banks (Fed, ECB, BOJ) in their cycle? Did today's news shift expected policy paths? Watch: official communication vs. market pricing gaps, yield-curve shape changes, real-rate moves.

### 2. Growth & inflation
What did today's data say relative to expectations? Beats/misses matter more than levels. Classify each release: confirms trend / breaks trend / ambiguous. One data point never proves a trend has changed — say "if confirmed by [next release]".

### 3. Risk sentiment & flows
Risk-on or risk-off today, and why? Cross-check equities against credit spreads, VIX, gold, JPY, and Treasuries. **Divergences are more informative than confirmations** — e.g., equities up while credit spreads widen is a warning worth flagging; everything moving together is just a mood.

### 4. Cross-border linkages
Dollar strength/weakness and its pressure on EM and commodities; oil as both inflation input and geopolitical thermometer; trade policy shifts; contagion channels from any regional stress.

## Output Format

```markdown
## Global Situation

**Regime:** 1–2 sentences (e.g., "easing cycle priced in, growth cooling but not contracting, risk appetite elevated").

**What changed today:** 2–4 bullets, each citing news-log items. If nothing regime-relevant happened, say so.

**What it implies:** 2–3 conditional statements ("if X continues, expect pressure on Y").

**Tensions/divergences:** anything that doesn't fit the regime story. This section may not be empty-by-default — actively look.
```

## Common Mistakes

- **Narrative laundering** — repeating a journalist's causal story ("stocks fell on rate fears") as your own analysis. Attribute it, or verify it against actual market moves in the log.
- **Level/change confusion** — "unemployment is low" (state) is not news; "unemployment rose 0.3pp unexpectedly" (delta) is.
- **Single-day extrapolation** — one CPI print is not a new inflation regime. Grade conviction accordingly.
- **US-only tunnel vision** — Europe and Japan policy shifts move global rates and FX; check the log covered them.
- **Empty tensions section** — if you found zero divergences, you likely didn't look; scan the cross-asset items again.
