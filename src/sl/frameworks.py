"""Research frameworks: structured templates for capturing knowledge.

A framework produces the initial body and tags for a new note. Built-in
frameworks are registered as entry points in the ``sl.frameworks`` group so
that third-party packages can add their own frameworks in exactly the same way.
"""

from __future__ import annotations

from importlib.metadata import entry_points


class Framework:
    """Base class for a research framework template."""

    name: str = ""
    title: str = ""
    description: str = ""

    def render(self, topic: str) -> tuple[str, list[str]]:
        """Return the initial ``(body, tags)`` for a new note on ``topic``."""
        raise NotImplementedError


class LiteratureNote(Framework):
    name = "literature-note"
    title = "Literature Note"
    description = "Summarise a paper or source: citation, summary, takeaways."

    def render(self, topic: str) -> tuple[str, list[str]]:
        body = (
            f"# {topic}\n\n"
            "## Citation\n\n"
            "> Author, Title, Year, Venue.\n\n"
            "## Summary\n\n"
            "What is the core contribution?\n\n"
            "## Key Takeaways\n\n"
            "- \n\n"
            "## Questions & Follow-ups\n\n"
            "- \n"
        )
        return body, ["literature"]


class ExperimentLog(Framework):
    name = "experiment-log"
    title = "Experiment Log"
    description = "Record a hypothesis, method, results, and conclusion."

    def render(self, topic: str) -> tuple[str, list[str]]:
        body = (
            f"# {topic}\n\n"
            "## Hypothesis\n\n"
            "What do you expect and why?\n\n"
            "## Method\n\n"
            "Describe the setup. Embed runnable code below.\n\n"
            "```python\nprint('replace with your experiment')\n```\n\n"
            "## Results\n\n"
            "## Conclusion\n"
        )
        return body, ["experiment"]


class Zettel(Framework):
    name = "zettel"
    title = "Zettelkasten Note"
    description = "One atomic idea, densely linked to others."

    def render(self, topic: str) -> tuple[str, list[str]]:
        body = (
            f"# {topic}\n\n"
            "One atomic idea, in your own words.\n\n"
            "## Links\n\n"
            "- Related: \n"
        )
        return body, ["zettel"]


_BUILTINS: dict[str, type[Framework]] = {
    LiteratureNote.name: LiteratureNote,
    ExperimentLog.name: ExperimentLog,
    Zettel.name: Zettel,
}


def available_frameworks() -> dict[str, Framework]:
    """Return all registered frameworks keyed by name.

    Built-ins are always present; any frameworks advertised via the
    ``sl.frameworks`` entry-point group are merged in and can override them.
    """
    frameworks: dict[str, Framework] = {
        name: cls() for name, cls in _BUILTINS.items()
    }
    try:
        eps = entry_points(group="sl.frameworks")
    except TypeError:  # pragma: no cover - very old importlib API
        eps = entry_points().get("sl.frameworks", [])  # type: ignore[assignment]
    for ep in eps:
        try:
            cls = ep.load()
        except Exception:  # pragma: no cover - defensive against bad plugins
            continue
        instance = cls()
        frameworks[instance.name or ep.name] = instance
    return frameworks


def get_framework(name: str) -> Framework:
    frameworks = available_frameworks()
    if name not in frameworks:
        raise KeyError(name)
    return frameworks[name]
