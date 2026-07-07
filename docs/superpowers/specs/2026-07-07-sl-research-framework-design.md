# SL — Research Knowledge Management Framework (Design)

Date: 2026-07-07

## Purpose

`SL` is a Python-based CLI and library framework for **research knowledge
management**. It combines a **knowledge base** (capture notes, sources, and
runnable code) with pluggable **research frameworks** (structured templates
that guide how knowledge is recorded and connected). It is designed so that
other tools can be built on top of it, both as a Python library and via a
plugin system for adding new research frameworks.

## Key decision

Python is the **host language**: a single pip-installable package `sl` exposing
both a library API and a `sl` CLI. It can execute **Python and R** code snippets
embedded in notes (R via `Rscript`), keeping R a first-class citizen for
reproducible research without maintaining two parallel libraries.

## Components

- `sl.core` — storage layer. Notes are markdown files with YAML front-matter,
  indexed in SQLite for search and link resolution. A `KnowledgeBase` object
  owns a directory (`.sl/`) containing notes and the index database.
- `sl.frameworks` — plugin system. A research framework is a `Framework` with a
  `name`, `title`, and a `render()` that produces the initial note body/metadata.
  Built-ins: `literature-note`, `experiment-log`, `zettel`. Third parties can
  register frameworks via the `sl.frameworks` entry-point group.
- `sl.exec` — executes fenced code blocks found in a note. Supports `python`
  and `r` languages. Degrades gracefully with a clear error if `Rscript` is
  absent.
- `sl.cli` — Typer CLI: `sl init`, `sl frameworks`, `sl new <framework>`,
  `sl list`, `sl search <query>`, `sl show <id>`, `sl run <id>`.

## Data flow

CLI command → `KnowledgeBase` operation → read/write markdown note + update
SQLite index → optional code execution via `sl.exec` → results shown/stored.

## Testing

`pytest` covers core storage/search, framework rendering, and code execution.
The CLI is tested with Typer's `CliRunner`. Lint via `ruff`.

## Dev environment

Python 3.12 (venv + pip, editable install), `pytest`, `ruff`, and R (`r-base`)
for the R execution feature.

## Hello-world demo

`sl init` → `sl new literature-note` → add a Python and an R fenced code block →
`sl run <id>` captures both outputs → `sl search` finds the note.
