"""Core storage layer for the SL knowledge base.

Notes are stored as markdown files with a YAML front-matter header and indexed
in a SQLite database so they can be searched and listed quickly. The
:class:`KnowledgeBase` owns a directory (``.sl/`` by default) that contains the
notes and the index database.
"""

from __future__ import annotations

import re
import sqlite3
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import yaml

DEFAULT_DIRNAME = ".sl"
NOTES_DIRNAME = "notes"
INDEX_DBNAME = "index.db"

_SLUG_RE = re.compile(r"[^a-z0-9]+")
_FRONT_MATTER_RE = re.compile(r"^---\n(.*?)\n---\n(.*)$", re.DOTALL)


def _slugify(text: str) -> str:
    slug = _SLUG_RE.sub("-", text.lower()).strip("-")
    return slug or "note"


@dataclass
class Note:
    """A single knowledge-base note."""

    id: str
    title: str
    framework: str
    body: str
    tags: list[str] = field(default_factory=list)
    created: str = ""
    path: Path | None = None

    def to_markdown(self) -> str:
        meta = {
            "id": self.id,
            "title": self.title,
            "framework": self.framework,
            "tags": self.tags,
            "created": self.created,
        }
        front = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True).strip()
        return f"---\n{front}\n---\n{self.body}"

    @classmethod
    def from_markdown(cls, text: str, path: Path | None = None) -> Note:
        match = _FRONT_MATTER_RE.match(text)
        if not match:
            raise ValueError("note is missing YAML front-matter")
        meta = yaml.safe_load(match.group(1)) or {}
        body = match.group(2)
        return cls(
            id=str(meta.get("id", "")),
            title=str(meta.get("title", "")),
            framework=str(meta.get("framework", "")),
            tags=list(meta.get("tags", []) or []),
            created=str(meta.get("created", "")),
            body=body,
            path=path,
        )


class KnowledgeBase:
    """A directory-backed knowledge base with a SQLite search index."""

    def __init__(self, root: Path | str = "."):
        self.root = Path(root)
        self.base_dir = self.root / DEFAULT_DIRNAME
        self.notes_dir = self.base_dir / NOTES_DIRNAME
        self.db_path = self.base_dir / INDEX_DBNAME

    @property
    def exists(self) -> bool:
        return self.base_dir.is_dir() and self.db_path.exists()

    def init(self) -> None:
        """Create the knowledge-base directory structure and index database."""
        self.notes_dir.mkdir(parents=True, exist_ok=True)
        conn = self._connect()
        try:
            conn.execute(
                """
                CREATE TABLE IF NOT EXISTS notes (
                    id TEXT PRIMARY KEY,
                    title TEXT NOT NULL,
                    framework TEXT NOT NULL,
                    tags TEXT NOT NULL,
                    created TEXT NOT NULL,
                    body TEXT NOT NULL
                )
                """
            )
            conn.commit()
        finally:
            conn.close()

    def _connect(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

    def _require(self) -> None:
        if not self.exists:
            raise FileNotFoundError(
                f"no knowledge base found at {self.base_dir} (run `sl init` first)"
            )

    def _make_id(self, title: str) -> str:
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S")
        return f"{stamp}-{_slugify(title)}"

    def add_note(
        self,
        title: str,
        framework: str,
        body: str,
        tags: list[str] | None = None,
    ) -> Note:
        self._require()
        note = Note(
            id=self._make_id(title),
            title=title,
            framework=framework,
            body=body,
            tags=list(tags or []),
            created=datetime.now(timezone.utc).isoformat(timespec="seconds"),
            path=None,
        )
        note.path = self.notes_dir / f"{note.id}.md"
        note.path.write_text(note.to_markdown(), encoding="utf-8")
        self._index(note)
        return note

    def _index(self, note: Note) -> None:
        conn = self._connect()
        try:
            conn.execute(
                """
                INSERT INTO notes (id, title, framework, tags, created, body)
                VALUES (?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    title=excluded.title,
                    framework=excluded.framework,
                    tags=excluded.tags,
                    created=excluded.created,
                    body=excluded.body
                """,
                (
                    note.id,
                    note.title,
                    note.framework,
                    ",".join(note.tags),
                    note.created,
                    note.body,
                ),
            )
            conn.commit()
        finally:
            conn.close()

    def get(self, note_id: str) -> Note:
        self._require()
        path = self.notes_dir / f"{note_id}.md"
        if not path.exists():
            raise KeyError(f"no note with id {note_id!r}")
        return Note.from_markdown(path.read_text(encoding="utf-8"), path=path)

    def update_body(self, note_id: str, body: str) -> Note:
        note = self.get(note_id)
        note.body = body
        assert note.path is not None
        note.path.write_text(note.to_markdown(), encoding="utf-8")
        self._index(note)
        return note

    def reindex(self) -> int:
        """Rebuild the search index from the note files on disk.

        Notes are markdown-first and may be edited directly in an editor, so the
        index can drift. This rescans every ``*.md`` file and returns the count.
        """
        self._require()
        conn = self._connect()
        try:
            conn.execute("DELETE FROM notes")
            conn.commit()
        finally:
            conn.close()
        count = 0
        for path in sorted(self.notes_dir.glob("*.md")):
            note = Note.from_markdown(path.read_text(encoding="utf-8"), path=path)
            self._index(note)
            count += 1
        return count

    def list_notes(self) -> list[Note]:
        self._require()
        conn = self._connect()
        try:
            rows = conn.execute(
                "SELECT * FROM notes ORDER BY created DESC"
            ).fetchall()
        finally:
            conn.close()
        return [self._row_to_note(row) for row in rows]

    def search(self, query: str) -> list[Note]:
        self._require()
        like = f"%{query}%"
        conn = self._connect()
        try:
            rows = conn.execute(
                """
                SELECT * FROM notes
                WHERE title LIKE ? OR body LIKE ? OR tags LIKE ?
                ORDER BY created DESC
                """,
                (like, like, like),
            ).fetchall()
        finally:
            conn.close()
        return [self._row_to_note(row) for row in rows]

    def _row_to_note(self, row: sqlite3.Row) -> Note:
        tags = [t for t in str(row["tags"]).split(",") if t]
        return Note(
            id=row["id"],
            title=row["title"],
            framework=row["framework"],
            tags=tags,
            created=row["created"],
            body=row["body"],
            path=self.notes_dir / f"{row['id']}.md",
        )
