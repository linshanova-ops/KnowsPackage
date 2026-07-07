import os
from contextlib import contextmanager

from typer.testing import CliRunner

from sl.cli import app
from sl.core import KnowledgeBase

runner = CliRunner()


@contextmanager
def chdir(path):
    prev = os.getcwd()
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(prev)


def _latest_note_id(path):
    return KnowledgeBase(path).list_notes()[0].id


def test_cli_end_to_end(tmp_path):
    with chdir(tmp_path):
        assert runner.invoke(app, ["init"]).exit_code == 0

        result = runner.invoke(
            app, ["new", "literature-note", "--title", "Deep Learning"]
        )
        assert result.exit_code == 0
        assert "Created note" in result.stdout

        list_result = runner.invoke(app, ["list"])
        assert list_result.exit_code == 0
        assert "Deep Learning" in list_result.stdout

        search_result = runner.invoke(app, ["search", "Deep"])
        assert search_result.exit_code == 0
        assert "Deep Learning" in search_result.stdout


def test_cli_frameworks_lists_builtins(tmp_path):
    with chdir(tmp_path):
        result = runner.invoke(app, ["frameworks"])
        assert result.exit_code == 0
        assert "literature-note" in result.stdout


def test_cli_run_executes_code(tmp_path):
    with chdir(tmp_path):
        runner.invoke(app, ["init"])
        runner.invoke(app, ["new", "experiment-log", "--title", "Exp"])
        note_id = _latest_note_id(tmp_path)
        result = runner.invoke(app, ["run", note_id])
        assert result.exit_code == 0
        assert "ok" in result.stdout
