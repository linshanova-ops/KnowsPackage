# SL

**SL** is a CLI + library framework for **research knowledge management**. It
combines a **knowledge base** (markdown notes indexed in SQLite) with pluggable
**research frameworks** (structured templates for how you capture and connect
knowledge), and can execute **Python and R** code embedded in your notes.

## Install (development)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

R is optional but required to run `r` code blocks (`sudo apt-get install -y r-base-core`).

## Usage

```bash
sl init                                   # create a knowledge base (./.sl)
sl frameworks                             # list available research frameworks
sl new literature-note --title "A Paper"  # create a note from a framework
sl list                                   # list all notes
sl search attention                       # full-text search
sl show <note-id>                         # print a note
sl run <note-id>                          # run python/R code blocks in a note
```

## Extending

New research frameworks are registered via the `sl.frameworks` entry-point
group, so other packages can add frameworks the same way the built-ins are
declared in `pyproject.toml`.

## Development

```bash
ruff check .        # lint
pytest              # tests
```

See `docs/superpowers/specs/` for the design document.
