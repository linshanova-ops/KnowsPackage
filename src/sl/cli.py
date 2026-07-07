"""Typer-based command-line interface for SL."""

from __future__ import annotations

import typer
from rich.console import Console
from rich.table import Table

from sl.core import KnowledgeBase
from sl.exec import run_note_body
from sl.frameworks import available_frameworks, get_framework

app = typer.Typer(help="SL — research knowledge management framework.")
console = Console()


def _kb() -> KnowledgeBase:
    return KnowledgeBase(".")


@app.command()
def init() -> None:
    """Initialise a knowledge base in the current directory."""
    kb = _kb()
    if kb.exists:
        console.print(f"Knowledge base already exists at [bold]{kb.base_dir}[/].")
        raise typer.Exit(0)
    kb.init()
    console.print(f"Initialised knowledge base at [bold green]{kb.base_dir}[/].")


@app.command()
def frameworks() -> None:
    """List available research frameworks."""
    table = Table(title="Research frameworks")
    table.add_column("name", style="cyan")
    table.add_column("title")
    table.add_column("description")
    for fw in available_frameworks().values():
        table.add_row(fw.name, fw.title, fw.description)
    console.print(table)


@app.command()
def new(
    framework: str = typer.Argument(..., help="Framework name, e.g. literature-note."),
    title: str = typer.Option(..., "--title", "-t", help="Note title / topic."),
    tag: list[str] = typer.Option(None, "--tag", help="Extra tag (repeatable)."),
) -> None:
    """Create a new note from a research framework."""
    kb = _kb()
    try:
        fw = get_framework(framework)
    except KeyError:
        names = ", ".join(available_frameworks())
        console.print(f"[red]Unknown framework '{framework}'.[/] Available: {names}")
        raise typer.Exit(1) from None
    body, tags = fw.render(title)
    tags.extend(tag or [])
    note = kb.add_note(title=title, framework=framework, body=body, tags=tags)
    console.print(f"Created note [bold green]{note.id}[/] ({fw.title}).")
    console.print(f"File: {note.path}")


@app.command(name="list")
def list_notes() -> None:
    """List all notes."""
    kb = _kb()
    notes = kb.list_notes()
    if not notes:
        console.print("No notes yet. Create one with [bold]sl new[/].")
        return
    table = Table(title=f"Notes ({len(notes)})")
    table.add_column("id", style="cyan", no_wrap=True)
    table.add_column("framework")
    table.add_column("title")
    table.add_column("tags")
    for note in notes:
        table.add_row(note.id, note.framework, note.title, ", ".join(note.tags))
    console.print(table)


@app.command()
def reindex() -> None:
    """Rebuild the search index from note files (run after editing notes)."""
    kb = _kb()
    count = kb.reindex()
    console.print(f"Reindexed [bold green]{count}[/] note(s).")


@app.command()
def search(query: str = typer.Argument(..., help="Text to search for.")) -> None:
    """Search notes by title, body, or tags."""
    kb = _kb()
    results = kb.search(query)
    if not results:
        console.print(f"No notes match [bold]{query!r}[/].")
        return
    table = Table(title=f"Matches for {query!r} ({len(results)})")
    table.add_column("id", style="cyan", no_wrap=True)
    table.add_column("title")
    for note in results:
        table.add_row(note.id, note.title)
    console.print(table)


@app.command()
def show(note_id: str = typer.Argument(..., help="Note id.")) -> None:
    """Print a note's contents."""
    kb = _kb()
    try:
        note = kb.get(note_id)
    except KeyError:
        console.print(f"[red]No note with id '{note_id}'.[/]")
        raise typer.Exit(1) from None
    console.print(note.to_markdown())


@app.command()
def run(note_id: str = typer.Argument(..., help="Note id.")) -> None:
    """Execute the python/R code blocks embedded in a note."""
    kb = _kb()
    try:
        note = kb.get(note_id)
    except KeyError:
        console.print(f"[red]No note with id '{note_id}'.[/]")
        raise typer.Exit(1) from None
    results = run_note_body(note.body)
    if not results:
        console.print("No runnable code blocks found in this note.")
        return
    failures = 0
    for i, res in enumerate(results, start=1):
        status = "[green]ok[/]" if res.ok else "[red]failed[/]"
        console.print(f"[bold]Block {i}[/] ({res.lang}) — {status}")
        if res.stdout:
            console.print(res.stdout.rstrip())
        if res.stderr:
            console.print(f"[yellow]{res.stderr.rstrip()}[/]")
        if not res.ok:
            failures += 1
    if failures:
        raise typer.Exit(1)


if __name__ == "__main__":
    app()
