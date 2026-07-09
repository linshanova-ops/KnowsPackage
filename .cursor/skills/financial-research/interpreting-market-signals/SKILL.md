---
name: interpreting-market-signals
description: Use when extracting signals from financial news and analysis — answering "what does this news reveal", identifying early warnings, regime shifts, or second-order implications that headlines don't state directly.
---

# Interpreting Market Signals

## Overview

Convert situation analysis into an explicit, graded list of signals: what today's news *reveals* beyond what it *states*.

**Core principle: a signal is a falsifiable inference, not a vibe.** Every signal must name its evidence, its mechanism (why the evidence implies the conclusion), and what would disprove it. If you can't state what would disprove it, it's not a signal — drop it.

## When to Use

- Stage 4 of the daily briefing pipeline (input: global + China assessments)
- User asks "what does this news mean/reveal/signal?"
- NOT for generating recommendations (that's `generating-actionable-insights` — signals describe the world; suggestions tell the reader what to do)

## Signal Format

```markdown
- **[STRONG|MODERATE|WEAK] Signal name**
  Evidence: news-log items / analysis findings
  Mechanism: why the evidence implies this
  Disproved if: observable condition that would kill the signal
```

## Grading

| Grade | Criteria |
|-------|----------|
| STRONG | Multiple independent evidence items, clear mechanism, market already partially confirming |
| MODERATE | Solid single evidence + mechanism, or multiple weak corroborations |
| WEAK | Plausible inference worth monitoring; single ambiguous data point |

Cap output at ~3–7 signals. Ten signals of which seven are weak is worse than four that matter.

## Where Signals Hide

Systematically check these patterns against the day's analysis — see [references/signal-playbook.md](references/signal-playbook.md) for the detailed catalog with historical examples:

1. **Divergences** — assets that normally move together, splitting (equities vs credit, copper vs oil, A vs H shares)
2. **Non-reactions** — good news that fails to lift a market, or bad news that fails to sink it (positioning is already saturated the other way)
3. **Communication deltas** — what officials *changed* or *stopped saying* versus last statement
4. **Second-order effects** — the headline's downstream consequence (chip export controls → check equipment suppliers, not just the named companies)
5. **Coinciding events** — separate stories forming a pattern (three unrelated funding-stress items in one day = a theme)
6. **Dogs that didn't bark** — expected events that didn't happen (no PBOC response to weak data, a skipped routine operation)

## Common Mistakes

- **Confirmation harvesting** — collecting only signals that support yesterday's view. For each signal, ask: what's the strongest counter-reading of the same evidence? If it's about as strong, downgrade to WEAK or drop.
- **Mechanism-free pattern matching** — "this looks like 2008" without naming the causal channel. Analogies are prompts for investigation, not evidence.
- **Over-reading noise** — daily moves within normal volatility ranges are not signals. A 0.5% index move needs no explanation.
- **Signal inflation** — grading everything STRONG to sound decisive. The grade is a promise about evidence quality; keep it honest.
- **Missing the non-event** — the playbook's non-reactions and dogs-that-didn't-bark checks exist because omission signals are the most commonly skipped.
