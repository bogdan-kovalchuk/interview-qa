from __future__ import annotations

import json
from pathlib import Path
import re
import shutil

import pytest
import yaml

from iqa import mirror


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).parent / "fixtures"


QUESTION = """---
id: py-gil-9202
title: "Question fixture"
track: python
section: concurrency-and-gil
sources:
  - source_id: fixture-source
    title: "Fixture source"
    url: https://example.com/reference
---

## Short answer

This answer is written.[^fixture-source] It has two sentences.

## Detailed explanation

This explanation is written.[^fixture-source]
"""


def _question(qid: str = "py-gil-9202", *, title: str = "Question fixture", explanation: str | None = None) -> str:
    text = QUESTION.replace("py-gil-9202", qid).replace('"Question fixture"', f'"{title}"')
    if explanation is not None:
        text = text.replace("This explanation is written.[^fixture-source]", explanation)
    return text


def _make_content_tree(tmp_path: Path, files: dict[str, str], language: str = "en") -> Path:
    """A single-language content tree. The mirror does not require both
    languages to exist; only the validator's lang-files-exist gate does."""
    content = tmp_path / "content"
    section_dir = content / language / "python" / "concurrency-and-gil"
    section_dir.mkdir(parents=True)
    for name, text in files.items():
        (section_dir / f"{name}.md").write_text(text, encoding="utf-8")
    return content


def _question_stems(out: Path) -> set[str]:
    """Stems of the question pages only.

    The mirror also writes index pages (home, track, section) that carry the
    navigation, and those are all named `index.md`. Question pages are the ones
    under `{lang}/q/`, so select on that rather than on "not directly in the
    locale directory", which stopped meaning the same thing.
    """
    return {path.stem for path in out.rglob("*.md") if "q" in path.relative_to(out).parts}


def _frontmatter(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8").split("---", 2)[1])


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

    The headings stay in `content/` so both languages share one structure, but
    a "not written yet" notice on the page tells the reader nothing.
    """
    content = _make_content_tree(tmp_path, {"partial-fixture": _question(explanation="TODO")})
    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", root=ROOT)

    body = next(out.rglob("partial-fixture.md")).read_text(encoding="utf-8").split("---", 2)[2]
    headings = [line[3:].strip() for line in body.splitlines() if line.startswith("## ")]

    assert "TODO" not in body
    assert headings == ["Short answer", "Sources"]


def test_every_question_gets_a_page(tmp_path: Path) -> None:
    content = _make_content_tree(
        tmp_path, {"one-fixture": _question(), "two-fixture": _question("py-gil-9203")}
    )
    out = tmp_path / "out"
    count = mirror.generate(content, out, "/interview-qa", root=ROOT)

    assert _question_stems(out) == {"one-fixture", "two-fixture"}
    assert count == 2


def test_a_question_without_sources_has_no_sources_heading(tmp_path: Path) -> None:
    text = re.sub(r"sources:\n(?:  .*\n)+", "", _question()).replace("[^fixture-source]", "")
    content = _make_content_tree(tmp_path, {"plain-fixture": text})
    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", root=ROOT)

    body = next(out.rglob("plain-fixture.md")).read_text(encoding="utf-8").split("---", 2)[2]
    headings = [line[3:].strip() for line in body.splitlines() if line.startswith("## ")]
    assert headings == ["Short answer", "Detailed explanation"]


def test_pagination_follows_home_taxonomy_section_and_questions(tmp_path: Path) -> None:
    content = _make_content_tree(
        tmp_path, {"one-fixture": _question(), "two-fixture": _question("py-gil-9203")}
    )
    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", root=ROOT)

    home = _frontmatter(out / "en" / "index.md")
    track = _frontmatter(out / "en" / "python" / "index.md")
    section = _frontmatter(out / "en" / "python" / "concurrency-and-gil" / "index.md")
    questions = sorted(
        ((_frontmatter(path), path) for path in (out / "en" / "q").rglob("*.md")),
        key=lambda item: item[0]["question_id"],
    )

    assert "prev" not in home
    assert home["next"]["link"] == "/interview-qa/en/python/"
    assert track["prev"]["link"] == "/interview-qa/en/"
    assert track["next"]["link"] == "/interview-qa/en/python/concurrency-and-gil/"
    assert section["prev"]["link"] == "/interview-qa/en/python/"
    assert section["next"]["link"].startswith("/interview-qa/en/q/")

    first, last = questions[0][0], questions[-1][0]
    assert first["prev"]["link"] == "/interview-qa/en/python/concurrency-and-gil/"
    assert last["prev"]["link"].startswith("/interview-qa/en/q/")
    assert "next" not in last


def test_section_index_and_pagination_sorted_by_question_id_not_alphabetical_title(
    tmp_path: Path,
) -> None:
    # The lower QID has the alphabetically last title, and the other way round.
    content = _make_content_tree(
        tmp_path,
        {
            "zebra-slug": _question("py-gil-0001", title="Zebra title"),
            "alpha-slug": _question("py-gil-0002", title="Alpha title"),
        },
    )
    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", root=ROOT)

    # Section index must list questions by QID (Zebra 0001 first, Alpha 0002 second)
    section_index = (
        out / "en" / "python" / "concurrency-and-gil" / "index.md"
    ).read_text(encoding="utf-8")
    zebra_pos = section_index.find("Zebra title")
    alpha_pos = section_index.find("Alpha title")
    assert zebra_pos != -1 and alpha_pos != -1
    assert zebra_pos < alpha_pos, "Section index must be sorted by QID, not alphabetical title"

    # Pagination must also follow QID order: section -> Zebra (0001) -> Alpha (0002)
    zebra_page = next((out / "en" / "q" / "py-gil-0001").glob("*.md"))
    alpha_page = next((out / "en" / "q" / "py-gil-0002").glob("*.md"))
    zebra_fm = _frontmatter(zebra_page)
    alpha_fm = _frontmatter(alpha_page)

    assert zebra_fm["prev"]["link"] == "/interview-qa/en/python/concurrency-and-gil/"
    assert zebra_fm["next"]["link"] == f"/interview-qa/en/q/py-gil-0002/{alpha_page.stem}/"
    assert alpha_fm["prev"]["link"] == f"/interview-qa/en/q/py-gil-0001/{zebra_page.stem}/"
    assert "next" not in alpha_fm


def test_sidebar_lists_the_taxonomy_without_a_status_page(tmp_path: Path) -> None:
    content = _make_content_tree(tmp_path, {"one-fixture": _question()})
    out = tmp_path / "out"
    sidebar_path = tmp_path / "sidebar.json"
    mirror.generate(content, out, "/interview-qa", root=ROOT, sidebar_out=sidebar_path)

    sidebar = json.loads(sidebar_path.read_text(encoding="utf-8"))
    assert len(sidebar) == 1
    assert sidebar[0]["items"] == [{"slug": "python/concurrency-and-gil"}]
    assert not (out / "en" / "status.md").exists()


def test_citations_become_links_into_the_sources_list(tmp_path: Path) -> None:
    """A citation is a superscript link to its entry in `Sources`, and no raw

    token survives. Markdown footnotes are deliberately not used: the renderer
    appends its own footnote block below `Sources`, which put every cited source
    on the page twice."""
    content = _make_content_tree(tmp_path, {"published-fixture": _question()})
    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", root=ROOT)

    mirrored = next(out.rglob("published-fixture.md")).read_text(encoding="utf-8")
    assert '<sup class="iqa-cite"><a href="#source-fixture-source">1</a></sup>' in mirrored
    assert '<li id="source-fixture-source">' in mirrored
    # no raw token and no footnote definition is left for the renderer to expand
    assert re.search(r"\[\^[a-z0-9-]+\]", mirrored) is None
    assert re.search(r"(?m)^\[\^[a-z0-9-]+\]:", mirrored) is None


def test_sources_section_is_rendered_from_frontmatter(tmp_path: Path) -> None:
    content = _make_content_tree(tmp_path, {"published-fixture": _question()})
    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", root=ROOT)

    mirrored = next(out.rglob("published-fixture.md")).read_text(encoding="utf-8")
    assert "## Sources" in mirrored
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
    mirror.generate(content, out, "/interview-qa", root=ROOT)

    mirrored = next(out.rglob("base-fixture.md")).read_text(encoding="utf-8")
    assert "## Short answer" in mirrored
    assert "## Detailed explanation" in mirrored
    assert "## Sources" in mirrored


def test_ukrainian_content_shows_ukrainian_headings(tmp_path: Path) -> None:
    # The source headings are English identifiers in every language
    # (meta/questions.md); the page shows them in its own language.
    content = _make_content_tree(tmp_path, {"published-fixture": _question()}, language="uk")
    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", root=ROOT)

    mirrored = next(out.rglob("published-fixture.md")).read_text(encoding="utf-8")
    assert "## Short answer" not in mirrored
    assert "## Коротка відповідь" in mirrored
    assert "## Detailed explanation" not in mirrored
    assert "## Розгорнуте пояснення" in mirrored


def test_qid_token_resolves_to_a_resolver_url(tmp_path: Path) -> None:
    content = _make_content_tree(
        tmp_path,
        {
            "source-fixture": _question(
                explanation="This explanation is written.[^fixture-source] See also qid:py-gil-9299."
            ),
            "target-fixture": _question("py-gil-9299"),
        },
    )
    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", root=ROOT)
    mirrored = next(out.rglob("source-fixture.md")).read_text(encoding="utf-8")
    # A bare token becomes a link titled with the target question, not a bare path.
    assert "See also [Question fixture](/interview-qa/en/q/py-gil-9299/)." in mirrored
    assert "qid:" not in mirrored


def test_qid_link_target_keeps_its_own_text(tmp_path: Path) -> None:
    content = _make_content_tree(
        tmp_path,
        {
            "source-fixture": _question(
                explanation="This explanation is written.[^fixture-source] See [the other one](qid:py-gil-9299)."
            ),
            "target-fixture": _question("py-gil-9299"),
        },
    )
    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", root=ROOT)
    mirrored = next(out.rglob("source-fixture.md")).read_text(encoding="utf-8")
    assert "See [the other one](/interview-qa/en/q/py-gil-9299/)." in mirrored


def test_unknown_qid_target_raises(tmp_path: Path) -> None:
    text = _question(
        explanation="This explanation is written.[^fixture-source] See also qid:py-gil-0000."
    )
    content = _make_content_tree(tmp_path, {"broken-fixture": text})

    out = tmp_path / "out"
    with pytest.raises(ValueError, match="unknown qid target"):
        mirror.generate(content, out, "/interview-qa", root=ROOT)
