# KnowsPackage

Investment research workspace with [AI Berkshire](https://github.com/xbtlin/ai-berkshire) skills for Cursor.

## Setup

```bash
git submodule update --init --recursive
./scripts/install-ai-berkshire.sh
```

## Usage

Ask Cursor to use a skill by name, for example:

- "Use investment-research to analyze Tencent"
- "Use investment-checklist on Moutai, NVIDIA, Apple"
- "Use industry-research on nuclear power"

Available skills live in `.cursor/skills/` (20 investment research workflows).
