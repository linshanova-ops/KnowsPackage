# AGENTS.md

## Cursor Cloud specific instructions

`SL` is a Python **CLI + library** for research knowledge management (no
long-running server/service — commands run and exit). Standard usage, install,
and extension notes live in `README.md`; the design is in
`docs/superpowers/specs/`.

Environment / running notes for future agents (dependencies are already
installed by the startup update script):

- Use the project virtualenv at `.venv` (created by the update script). Either
  activate it (`source .venv/bin/activate`) or call tools directly
  (`.venv/bin/pytest`, `.venv/bin/ruff`, `.venv/bin/sl`). The package is
  installed editable, so source edits take effect without reinstalling.
- Commands: lint `ruff check .`; test `pytest`; run the app via the `sl` entry
  point (e.g. `sl init`, `sl new`, `sl run`).
- **R is required** to execute `r` code blocks (`sl run`). `Rscript` (r-base) is
  provided by the VM snapshot, not the update script. If it is ever missing,
  `sl run` degrades gracefully (reports the error) rather than crashing, and the
  R-specific pytest is auto-skipped via `shutil.which("Rscript")`.
- **Search uses a SQLite index, not the files.** Notes are markdown-first and
  can be edited directly on disk; the index does not auto-refresh on manual
  edits. Run `sl reindex` after editing note files so `sl search` stays
  accurate. (`sl run` reads the file directly, so it is always current.)
- A knowledge base lives in a `.sl/` directory in the current working
  directory; `.sl/` is git-ignored.
