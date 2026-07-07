import shutil

import pytest

from sl.exec import CodeBlock, extract_code_blocks, run_block, run_note_body


def test_extract_code_blocks_filters_supported():
    body = (
        "```python\nprint(1)\n```\n"
        "```text\nnot code\n```\n"
        "```r\ncat('hi')\n```\n"
    )
    blocks = extract_code_blocks(body)
    langs = [b.lang for b in blocks]
    assert langs == ["python", "r"]


def test_run_python_block_captures_stdout():
    res = run_block(CodeBlock("python", "print('hello from python')"))
    assert res.ok
    assert "hello from python" in res.stdout


def test_run_python_block_reports_failure():
    res = run_block(CodeBlock("python", "raise ValueError('boom')"))
    assert not res.ok
    assert "boom" in res.stderr


def test_run_note_body_runs_all_blocks():
    body = "```python\nprint('a')\n```\n```python\nprint('b')\n```"
    results = run_note_body(body)
    assert [r.stdout.strip() for r in results] == ["a", "b"]


@pytest.mark.skipif(shutil.which("Rscript") is None, reason="R not installed")
def test_run_r_block_captures_stdout():
    res = run_block(CodeBlock("r", "cat('hello from R\\n')"))
    assert res.ok
    assert "hello from R" in res.stdout


@pytest.mark.skipif(shutil.which("Rscript") is not None, reason="R is installed")
def test_run_r_block_without_rscript_reports_error():
    res = run_block(CodeBlock("r", "cat('hi')"))
    assert not res.ok
    assert "Rscript not found" in res.stderr
