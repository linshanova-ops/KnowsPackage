import pytest

from sl.frameworks import available_frameworks, get_framework


def test_builtin_frameworks_present():
    names = set(available_frameworks())
    assert {"literature-note", "experiment-log", "zettel"} <= names


def test_render_returns_body_and_tags():
    fw = get_framework("literature-note")
    body, tags = fw.render("Some Paper")
    assert "Some Paper" in body
    assert "literature" in tags


def test_experiment_log_has_runnable_block():
    body, _ = get_framework("experiment-log").render("Exp 1")
    assert "```python" in body


def test_unknown_framework_raises():
    with pytest.raises(KeyError):
        get_framework("does-not-exist")
