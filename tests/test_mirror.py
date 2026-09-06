from __future__ import annotations

from pathlib import Path
import shutil

import pytest

from iqa import mirror


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).parent / "fixtures"


def _make_content_tree(tmp_path: Path, fixture_names: list[str]) -> Path:
    """A single-language (en) content tree built from tests/fixtures/statuses/*.md.

    Single-language avoids tripping the bilingual `reconciled_with` cross-check in
    the model - mirror.py does not require both languages to exist, only
    tools/iqa/validate.py's lang-files-exist gate does.
    """
    content = tmp_path / "content"
    section_dir = content / "en" / "python" / "concurrency-and-gil"
    section_dir.mkdir(parents=True)
    for name in fixture_names:
        shutil.copy(FIXTURES / "statuses" / f"{name}.md", section_dir / f"{name}-fixture.md")
    return content


def _question_stems(out: Path) -> set[str]:
    """Stems of the question pages only.

    The mirror also writes index pages (home, track, section) that carry the
    navigation, and those are all named `index.md`. Question pages are the ones
    under `{lang}/q/`, so select on that rather than on "not directly in the
    locale directory", which stopped meaning the same thing.
    """
    return {path.stem for path in out.rglob("*.md") if "q" in path.relative_to(out).parts}


def test_title_inline_code_is_stripped_for_text_and_rendered_for_the_heading() -> None:
    """One title, two shapes: plain text where markup cannot go, `<code>` where it can.

    Starlight puts `title` into the browser `<title>`, `og:title` and the
    sidebar, none of which can hold markup - so the backticks used to show up
    there literally. The heading can hold markup, and the section index already
    rendered the same titles with `<code>`, so leaving the heading as plain text
    made one title look formatted in the list and raw on its own page.
    """
    title = "Спроєктуйте object з узгодженими `__eq__` та `__hash__`"

    assert mirror.title_text(title) == "Спроєктуйте object з узгодженими __eq__ та __hash__"
    assert mirror.title_markup(title) == (
        "Спроєктуйте object з узгодженими <code>__eq__</code> та <code>__hash__</code>"
    )


def test_title_markup_escapes_everything_it_did_not_generate() -> None:
    # The result is injected with `set:html`, so anything the author wrote must
    # arrive as text - inside the code span as well as outside it.
    title = "Why does `a < b & c` differ from <script>?"

    assert mirror.title_markup(title) == (
        "Why does <code>a &lt; b &amp; c</code> differ from &lt;script&gt;?"
    )
    assert mirror.title_text(title) == "Why does a < b & c differ from <script>?"


def test_unwritten_sections_are_not_rendered_at_all(tmp_path: Path) -> None:
    """A `TODO` section leaves no trace on the page.

    The skeleton keeps every required heading in `content/` because the contract
    demands it, but rendering them produced up to nine "not written yet" notices
    on a single page. The gaps are data now - `dist/export/progress.{json,csv}`
    and `/status/` - rather than noise repeated down every page.
    """
    content = _make_content_tree(tmp_path, ["partial"])
    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", preview=False, root=ROOT)

    body = next(out.rglob("partial-fixture.md")).read_text(encoding="utf-8").split("---", 2)[2]
    headings = [line[3:].strip() for line in body.splitlines() if line.startswith("## ")]

    # The fixture has Short answer written, Detailed explanation `TODO`, Sources.
    assert "TODO" not in body
    assert headings == ["Short answer", "Sources"]


def test_production_excludes_draft_and_review(tmp_path: Path) -> None:
    content = _make_content_tree(tmp_path, ["draft", "review", "published", "withdrawn"])
    out = tmp_path / "out"
    count = mirror.generate(content, out, "/interview-qa", preview=False, root=ROOT)

    mirrored_ids = _question_stems(out)
    assert "draft-fixture" not in mirrored_ids
    assert "review-fixture" not in mirrored_ids
    assert "published-fixture" in mirrored_ids
    assert "withdrawn-fixture" in mirrored_ids
    assert count == 2


def test_preview_includes_draft_and_review(tmp_path: Path) -> None:
    content = _make_content_tree(tmp_path, ["draft", "review", "published", "withdrawn"])
    out = tmp_path / "out"
    count = mirror.generate(content, out, "/interview-qa", preview=True, root=ROOT)

    mirrored_ids = _question_stems(out)
    assert mirrored_ids == {"draft-fixture", "review-fixture", "published-fixture", "withdrawn-fixture"}
    assert count == 4


def test_withdrawn_renders_tombstone_not_full_body(tmp_path: Path) -> None:
    content = _make_content_tree(tmp_path, ["withdrawn"])
    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", preview=False, root=ROOT)

    mirrored = next(out.rglob("withdrawn-fixture.md")).read_text(encoding="utf-8")
    assert "withdrawn" in mirrored.lower() or "вилучено" in mirrored
    assert "This answer is written" not in mirrored  # the fixture's real body must not leak


def test_citations_become_links_into_the_sources_list(tmp_path: Path) -> None:
    """A citation is a superscript link to its entry in `Sources`, and no raw

    token survives. Markdown footnotes are deliberately not used: the renderer
    appends its own footnote block below `Sources`, which put every cited source
    on the page twice."""
    content = _make_content_tree(tmp_path, ["published"])
    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", preview=False, root=ROOT)

    mirrored = next(out.rglob("published-fixture.md")).read_text(encoding="utf-8")
    assert '<sup class="iqa-cite"><a href="#source-fixture-source">1</a></sup>' in mirrored
    assert '<li id="source-fixture-source">' in mirrored
    # no raw token and no footnote definition is left for the renderer to expand
    import re

    assert re.search(r"\[\^[a-z0-9-]+\]", mirrored) is None
    assert re.search(r"(?m)^\[\^[a-z0-9-]+\]:", mirrored) is None


def test_sources_section_is_rendered_not_the_placeholder_comment(tmp_path: Path) -> None:
    content = _make_content_tree(tmp_path, ["published"])
    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", preview=False, root=ROOT)

    mirrored = next(out.rglob("published-fixture.md")).read_text(encoding="utf-8")
    assert "generated from frontmatter" not in mirrored
    assert (
        '<li id="source-fixture-source">'
        '<a href="https://example.com/reference">Fixture source</a></li>' in mirrored
    )


def test_english_page_shows_english_headings(tmp_path: Path) -> None:
    content = tmp_path / "content"
    section_dir = content / "en" / "python" / "concurrency-and-gil"
    section_dir.mkdir(parents=True)
    shutil.copy(FIXTURES / "valid" / "base-en.md", section_dir / "base-fixture.md")
    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", preview=False, root=ROOT)

    mirrored = next(out.rglob("base-fixture.md")).read_text(encoding="utf-8")
    assert "## Short answer" in mirrored
    assert "## Detailed explanation" in mirrored
    assert "## Evaluation guide" in mirrored
    assert "### Expected signals" in mirrored
    assert "### Red flags" in mirrored
    assert "### Level-up follow-up" in mirrored


def test_ukrainian_content_shows_ukrainian_headings(tmp_path: Path) -> None:
    content = tmp_path / "content"
    section_dir = content / "uk" / "python" / "concurrency-and-gil"
    section_dir.mkdir(parents=True)
    # A Ukrainian-language fixture: same structural (English) headings in the
    # source, per meta/questions.md section 4 - "headings are identifiers,
    # not text" - but reconciled_with must point at "en", not "uk", to satisfy
    # the model's own-language exclusion rule.
    text = (FIXTURES / "statuses" / "published.md").read_text(encoding="utf-8")
    text = text.replace("reconciled_with: {uk: 1}", "reconciled_with: {en: 1}")
    (section_dir / "published-fixture.md").write_text(text, encoding="utf-8")

    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", preview=False, root=ROOT)

    mirrored = next(out.rglob("published-fixture.md")).read_text(encoding="utf-8")
    assert "## Short answer" not in mirrored
    assert "## Коротка відповідь" in mirrored
    assert "## Detailed explanation" not in mirrored
    assert "## Розгорнуте пояснення" in mirrored


def test_qid_token_resolves_to_a_resolver_url(tmp_path: Path) -> None:
    content = tmp_path / "content"
    section_dir = content / "en" / "python" / "concurrency-and-gil"
    section_dir.mkdir(parents=True)
    base_text = (FIXTURES / "statuses" / "published.md").read_text(encoding="utf-8")

    # The linking question keeps id py-gil-9202 (the fixture default) and points
    # at a second question with a distinct id, py-gil-9299.
    linking_text = base_text.replace(
        "This explanation is written.[^fixture-source]",
        "This explanation is written.[^fixture-source] See also qid:py-gil-9299.",
    )
    (section_dir / "source-fixture.md").write_text(linking_text, encoding="utf-8")
    target_text = base_text.replace("id: py-gil-9202", "id: py-gil-9299")
    (section_dir / "target-fixture.md").write_text(target_text, encoding="utf-8")

    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", preview=False, root=ROOT)
    mirrored = next(out.rglob("source-fixture.md")).read_text(encoding="utf-8")
    assert "/interview-qa/en/q/py-gil-9299/" in mirrored
    assert "qid:" not in mirrored


def test_unknown_qid_target_raises(tmp_path: Path) -> None:
    content = tmp_path / "content"
    section_dir = content / "en" / "python" / "concurrency-and-gil"
    section_dir.mkdir(parents=True)
    base_text = (FIXTURES / "statuses" / "published.md").read_text(encoding="utf-8")
    text = base_text.replace(
        "This explanation is written.[^fixture-source]",
        "This explanation is written.[^fixture-source] See also qid:py-gil-0000.",
    )
    (section_dir / "broken-fixture.md").write_text(text, encoding="utf-8")

    out = tmp_path / "out"
    with pytest.raises(ValueError, match="unknown qid target"):
        mirror.generate(content, out, "/interview-qa", preview=False, root=ROOT)
