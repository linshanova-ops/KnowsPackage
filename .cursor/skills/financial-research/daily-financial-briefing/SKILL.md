---
name: daily-financial-briefing
description: Use when the user asks for a daily financial briefing, market report, morning brief, 财经日报, or wants today's financial news gathered, analyzed, and turned into a report with practical suggestions. Entry point that orchestrates the full research pipeline.
---

# Daily Financial Briefing (Pipeline Orchestrator)

## Overview

Produces one daily report from raw news: gather → analyze (world + China) → extract signals → derive suggestions → write. Each stage has a dedicated skill; this skill defines the order, hand-offs, and quality gates.

**Core principle: no stage consumes what the previous stage didn't verify.** Analysis only uses dated, sourced news items. Suggestions only reference signals identified in analysis. The report contains nothing that can't be traced back to a gathered item.

## Pipeline

Run stages in order. Read each stage's skill before executing it.

| Stage | Skill | Output |
|-------|-------|--------|
| 1. Gather | `gathering-financial-news` | Structured news log (dated, sourced, categorized items) |
| 2. World analysis | `analyzing-global-macro` | Global situation assessment |
| 3. China analysis | `analyzing-china-macro` | China situation assessment |
| 4. Signals | `interpreting-market-signals` | Graded signal list |
| 5. Suggestions | `generating-actionable-insights` | Prioritized watch-list with triggers |
| 6. Report | `writing-daily-financial-report` | Final report document |

## Quality Gates (check before advancing)

- **After stage 1:** Every item has a publication date from the last 24–48 hours and a named source. Discard undated or stale items — do not carry them forward "for context" unless explicitly labeled as background.
- **After stages 2–3:** Every claim in the assessment cites a news-log item. No claims from memory of "how things usually are."
- **After stage 4:** Every signal is graded (strong/moderate/weak) with reasoning. Ungraded observations stay out of the suggestions stage.
- **After stage 5:** Max 5 suggestions, each with a trigger and an invalidator.
- **After stage 6:** Report follows the template; disclaimer present.

## Defaults (override only if user specifies)

- Coverage window: last 24 hours (weekend/Monday: last 72 hours)
- Scope: global + China (both always; user may narrow)
- Language: match the user's request language
- Report length: readable in ~5 minutes (~1,000–1,500 words)

## Common Mistakes

- **Skipping the news log and writing analysis directly from search snippets.** Snippets lack dates and get facts wrong; build the log first.
- **Letting the report drift from the analysis.** If you discover something new while writing, go back and add it to the log and analysis, then update the report.
- **Padding thin news days.** A quiet day is a valid finding — say so briefly instead of inflating minor items into signals.
