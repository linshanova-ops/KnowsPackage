# Daily Financial Insights

Cursor Agent Skills for the full daily financial research pipeline — from gathering the latest global and China financial news to a finished briefing with practical suggestions.

**Entry point:** ask the agent for a "daily financial briefing" (or invoke `/daily-financial-briefing`). It orchestrates the stages below in order.

| Skill | Stage | Purpose |
|-------|-------|---------|
| `daily-financial-briefing` | Orchestrator | Runs the pipeline end-to-end with quality gates between stages |
| `gathering-financial-news` | 1 | Sweeps 8 news categories into a dated, sourced news log (+ source-quality reference) |
| `analyzing-global-macro` | 2 | World-level situation assessment: policy, growth/inflation, risk sentiment, linkages |
| `analyzing-china-macro` | 3 | China-level assessment: policy stance decoding, property, markets, external links |
| `interpreting-market-signals` | 4 | Extracts graded, falsifiable signals (+ signal playbook with divergences, non-reactions, second-order effects) |
| `generating-actionable-insights` | 5 | Converts signals into ≤5 prioritized watchpoints, each with a trigger and an invalidator |
| `writing-daily-financial-report` | 6 | Assembles everything into the final report (+ report template) |

Each stage skill also works standalone (e.g. "what does this news signal?" triggers `interpreting-market-signals` directly).

## Setup

Clone this repo into your project (or copy `.cursor/skills/financial-research/` into an existing project's `.cursor/skills/` directory). Cursor discovers skills automatically from `.cursor/skills/`.

## Usage

```
Give me today's daily financial briefing
```

Or invoke individual stages:

```
What does today's PBOC statement signal?
Analyze China's macro situation from today's news
```

All output is research synthesis, not investment advice.
