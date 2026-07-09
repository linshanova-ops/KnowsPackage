---
name: generating-actionable-insights
description: Use when converting financial signals and analysis into practical suggestions — what the reader should pay attention to, monitor, or prepare for. Applies whenever a report needs a "so what" section.
---

# Generating Actionable Insights

## Overview

Turn graded signals into a short, prioritized list of things the reader should *do* — where "do" means watch, verify, prepare, or reassess. This is a research product, not investment advice: suggest attention and preparation, never specific trades, position sizes, or "buy X".

**Core principle: every suggestion needs a trigger and an invalidator.** "Pay attention to inflation" is unfalsifiable filler. "Watch Thursday's CPI; a third consecutive upside surprise breaks the disinflation narrative — if it comes in at/below consensus, this concern drops off the list" tells the reader exactly what to look for and when to stop looking.

## When to Use

- Stage 5 of the daily briefing pipeline (input: graded signal list from `interpreting-market-signals`)
- User asks "what should I focus on / watch / do about this?"

## Suggestion Format

```markdown
1. **[Priority: HIGH|MEDIUM|LOW] Imperative headline**
   - Why: link to signal(s) driving this
   - Watch: the specific observable — data release (with date if known), price level, official statement, flow metric
   - Trigger: what reading/event escalates this
   - Invalidator: what reading/event retires this
   - Horizon: days / weeks / quarter
```

## Rules

- **Max 5 suggestions.** Rank by (impact if signal is right) × (signal grade). A list of 12 watchpoints is a list of zero.
- **Traceability:** every suggestion cites at least one signal; no suggestions from general knowledge with no basis in today's analysis.
- **Specific observables only:** name the release, the level, the spread, the meeting date. "Monitor the situation" is banned phrasing.
- **Carry state across days** when prior reports are available: mark each item as new / continuing / escalated / retired, and explicitly retire items whose invalidators hit. A watch-list that only grows is not being maintained.
- **Include one contrarian check when warranted:** if the day's signals all point one way, add a suggestion for what would indicate the consensus reading is wrong.
- **No trade recommendations.** Allowed: "elevated risk for X assets", "conditions favor reviewing exposure to Y". Not allowed: "buy/sell/short Z", target prices, allocations.

## Priority Guide

| Priority | Meaning |
|----------|---------|
| HIGH | STRONG signal with broad market impact, or MODERATE signal with imminent trigger (≤1 week) |
| MEDIUM | MODERATE signal, or STRONG signal with slow-burn horizon |
| LOW | WEAK signal worth one line; include at most one or two |

## Common Mistakes

- **Horoscope suggestions** — advice vague enough to always be right ("stay diversified", "volatility may continue"). If it would be equally valid on any day, delete it.
- **Suggestion inflation** — turning every signal into a suggestion. Weak signals usually deserve zero suggestions.
- **Missing the invalidator** — a watchpoint without an exit condition becomes permanent noise.
- **Smuggling in trades** — "watch for entry points in tech" is a trade call wearing a watch-list costume. Rephrase to the observable ("watch whether the Nasdaq holds its 50-day average after the earnings cluster") or drop.
- **Ignoring the reader's stated interests** — if the user has told you their focus areas (e.g., China equities, FX), weight priorities accordingly and say so.
