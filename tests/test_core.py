from sl.core import KnowledgeBase, Note


def test_init_creates_structure(tmp_path):
    kb = KnowledgeBase(tmp_path)
    assert not kb.exists
    kb.init()
    assert kb.exists
    assert kb.notes_dir.is_dir()
    assert kb.db_path.exists()


def test_add_and_get_note(tmp_path):
    kb = KnowledgeBase(tmp_path)
    kb.init()
    note = kb.add_note(
        title="Attention Is All You Need",
        framework="literature-note",
        body="# body\n",
        tags=["nlp"],
    )
    assert note.path.exists()
    fetched = kb.get(note.id)
    assert fetched.title == "Attention Is All You Need"
    assert fetched.framework == "literature-note"
    assert "nlp" in fetched.tags


def test_search_matches_title_body_and_tags(tmp_path):
    kb = KnowledgeBase(tmp_path)
    kb.init()
    kb.add_note("Transformers", "zettel", "self-attention idea", tags=["dl"])
    kb.add_note("Gradient Descent", "zettel", "optimisation", tags=["math"])

    assert len(kb.search("attention")) == 1
    assert len(kb.search("optimisation")) == 1
    assert len(kb.search("dl")) == 1
    assert kb.search("nonexistent") == []


def test_list_notes_orders_newest_first(tmp_path):
    kb = KnowledgeBase(tmp_path)
    kb.init()
    kb.add_note("First", "zettel", "a")
    kb.add_note("Second", "zettel", "b")
    titles = [n.title for n in kb.list_notes()]
    assert set(titles) == {"First", "Second"}
    assert len(titles) == 2


def test_reindex_picks_up_direct_edits(tmp_path):
    kb = KnowledgeBase(tmp_path)
    kb.init()
    note = kb.add_note("Note", "zettel", "original body")
    assert kb.search("appended") == []

    # Simulate the user editing the markdown file directly in an editor.
    note.path.write_text(
        note.path.read_text(encoding="utf-8") + "\nappended text\n",
        encoding="utf-8",
    )
    assert kb.search("appended") == []  # index is stale until reindex

    assert kb.reindex() == 1
    assert len(kb.search("appended")) == 1


def test_markdown_roundtrip():
    note = Note(
        id="20260101T000000-x",
        title="X",
        framework="zettel",
        body="hello\n",
        tags=["a", "b"],
        created="2026-01-01T00:00:00+00:00",
    )
    parsed = Note.from_markdown(note.to_markdown())
    assert parsed.id == note.id
    assert parsed.title == note.title
    assert parsed.tags == note.tags
    assert parsed.body == note.body
