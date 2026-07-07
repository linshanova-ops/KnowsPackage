"""Execute fenced code blocks embedded in a note.

Supports ``python`` and ``r`` code fences. Each block is run in a subprocess and
its captured output is returned. R execution requires ``Rscript`` on the PATH;
if it is missing, the corresponding block returns a clear error instead of
crashing.
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path

_FENCE_RE = re.compile(r"```([A-Za-z0-9_+-]+)\n(.*?)```", re.DOTALL)

_SUPPORTED = {"python", "py", "r"}


@dataclass
class CodeBlock:
    lang: str
    code: str


@dataclass
class ExecResult:
    lang: str
    code: str
    stdout: str
    stderr: str
    returncode: int

    @property
    def ok(self) -> bool:
        return self.returncode == 0


def extract_code_blocks(body: str) -> list[CodeBlock]:
    """Return supported (python/r) fenced code blocks from ``body`` in order."""
    blocks: list[CodeBlock] = []
    for match in _FENCE_RE.finditer(body):
        lang = match.group(1).lower()
        if lang in _SUPPORTED:
            blocks.append(CodeBlock(lang=lang, code=match.group(2)))
    return blocks


def _run(cmd: list[str], timeout: int) -> tuple[str, str, int]:
    proc = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return proc.stdout, proc.stderr, proc.returncode


def run_block(block: CodeBlock, timeout: int = 30) -> ExecResult:
    """Execute a single code block and capture its output."""
    if block.lang in ("python", "py"):
        with tempfile.NamedTemporaryFile(
            "w", suffix=".py", delete=False, encoding="utf-8"
        ) as fh:
            fh.write(block.code)
            script = fh.name
        try:
            out, err, rc = _run([sys.executable, script], timeout)
        finally:
            Path(script).unlink(missing_ok=True)
        return ExecResult("python", block.code, out, err, rc)

    if block.lang == "r":
        rscript = shutil.which("Rscript")
        if not rscript:
            return ExecResult(
                "r",
                block.code,
                "",
                "Rscript not found on PATH; install R to run R code blocks.",
                127,
            )
        with tempfile.NamedTemporaryFile(
            "w", suffix=".R", delete=False, encoding="utf-8"
        ) as fh:
            fh.write(block.code)
            script = fh.name
        try:
            out, err, rc = _run([rscript, "--vanilla", script], timeout)
        finally:
            Path(script).unlink(missing_ok=True)
        return ExecResult("r", block.code, out, err, rc)

    raise ValueError(f"unsupported language: {block.lang}")


def run_note_body(body: str, timeout: int = 30) -> list[ExecResult]:
    """Run every supported code block in ``body`` and return the results."""
    return [run_block(block, timeout=timeout) for block in extract_code_blocks(body)]
