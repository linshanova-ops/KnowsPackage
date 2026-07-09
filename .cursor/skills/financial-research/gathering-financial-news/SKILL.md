---
name: gathering-financial-news
description: Use when collecting the latest daily financial, market, or economic news from global and China sources — before any analysis or report writing, or when the user asks "what happened in markets today".
---

# Gathering Financial News

## Overview

Systematically sweep the day's financial news into a structured, verifiable news log. The log — not raw search results — is the input to all downstream analysis.

**Core principle: an undated item is an unusable item.** Financial news loses meaning without a timestamp; always verify publication dates and mark each item with one.

## Sweep Checklist

Search each category explicitly — don't rely on one generic "financial news today" query, which surfaces only the loudest story. Include today's date in queries to force recency.

Timing note: a "daily" sweep run during Asian morning hours should treat the prior US session as today's news.

1. **Central banks & rates** — Fed, ECB, BOJ, PBOC, BOE: decisions, speeches, minutes, unexpected operations
2. **Macro data releases** — inflation, employment, PMI, GDP, trade, retail sales (note actual vs. consensus when available)
3. **Equity markets** — major index moves (S&P 500, Nasdaq, Stoxx, Nikkei, CSI 300, Hang Seng), notable sector or single-name moves with market-wide implications
4. **Rates, credit & FX** — Treasury yields, yield-curve moves, credit spreads, DXY, CNY, JPY, EUR
5. **Commodities** — oil, gold, copper, agricultural staples; supply/demand news
6. **China-specific** — policy announcements, regulator statements, property sector, local government debt, major SOE/tech news, capital flows (Stock Connect)
7. **Geopolitics & trade** — conflicts, sanctions, tariffs, elections with market relevance
8. **Corporate/systemic** — earnings or corporate events large enough to move markets or reveal macro information (a mega-cap guidance cut is macro news; a small-cap beat is not)

For source quality tiers and go-to outlets per category, see [references/sources.md](references/sources.md).

## Verification Rules

- **Date every item.** If a search result has no visible date, open the article or find a second source. Discard if unverifiable.
- **Triangulate market-moving claims.** Any item that would drive a signal downstream needs 2+ independent sources, or must be marked `single-source`. Two outlets carrying the same wire story (e.g. both republishing Reuters) count as one source; independence means separately reported. A `single-source` item may still drive a signal if nothing contradicts it — carry the flag through to the report's caveats section rather than dropping the item.
- **Numbers over adjectives.** Record "CPI 3.2% y/y vs 3.0% expected", not "inflation came in hot". Capture the actual figures.
- **Separate fact from interpretation.** The log records what happened; opinions from the article go in a separate `commentary` note or are dropped.

## News Log Format

One entry per item:

```markdown
- [CATEGORY] [DATE] Headline-style summary with key numbers.
  Source: Outlet1, Outlet2. Confidence: confirmed | single-source.
  Note: (optional — consensus vs actual, context, commentary flag)
```

## Common Mistakes

- **Trusting search-snippet dates.** Snippets often show index dates, not publication dates. Verify.
- **Recency bias toward US hours.** Asia and Europe sessions produce news too — sweep all regions, especially for China coverage.
- **Logging stale "evergreen" articles.** Explainers and week-old analysis pieces rank well in search but aren't today's news.
- **Stopping at 5 items.** A proper sweep of 8 categories typically yields 15–30 items on a normal day. Thin results usually mean the sweep was incomplete, not that nothing happened.
