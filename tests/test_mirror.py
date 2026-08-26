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


def test_production_excludes_draft_and_review(tmp_path: Path) -> None:
    content = _make_content_tree(tmp_path, ["draft", "review", "published", "withdrawn"])
    out = tmp_path / "out"
    count = mirror.generate(content, out, "/interview-qa", preview=False, root=ROOT)

    mirrored_ids = {path.stem for path in out.rglob("*.md") if path.parent.name != "en"}
    assert "draft-fixture" not in mirrored_ids
    assert "review-fixture" not in mirrored_ids
    assert "published-fixture" in mirrored_ids
    assert "withdrawn-fixture" in mirrored_ids
    assert count == 2


def test_preview_includes_draft_and_review(tmp_path: Path) -> None:
    content = _make_content_tree(tmp_path, ["draft", "review", "published", "withdrawn"])
    out = tmp_path / "out"
    count = mirror.generate(content, out, "/interview-qa", preview=True, root=ROOT)

    mirrored_ids = {path.stem for path in out.rglob("*.md") if path.parent.name != "en"}
    assert mirrored_ids == {"draft-fixture", "review-fixture", "published-fixture", "withdrawn-fixture"}
    assert count == 4


def test_withdrawn_renders_tombstone_not_full_body(tmp_path: Path) -> None:
    content = _make_content_tree(tmp_path, ["withdrawn"])
    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", preview=False, root=ROOT)

    mirrored = next(out.rglob("withdrawn-fixture.md")).read_text(encoding="utf-8")
    assert "withdrawn" in mirrored.lower() or "вилучено" in mirrored
    assert "This answer is written" not in mirrored  # the fixture's real body must not leak


def test_citations_become_footnote_definitions_and_no_raw_token_survives(tmp_path: Path) -> None:
    content = _make_content_tree(tmp_path, ["published"])
    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", preview=False, root=ROOT)

    mirrored = next(out.rglob("published-fixture.md")).read_text(encoding="utf-8")
    assert "[^fixture-source]: [Fixture source](https://example.com/reference)" in mirrored
    # every remaining `[^...]` must be an inline reference, never left un-defined
    import re

    tokens = set(re.findall(r"\[\^([a-z0-9-]+)\]", mirrored))
    definitions = set(re.findall(r"(?m)^\[\^([a-z0-9-]+)\]:", mirrored))
    assert tokens == definitions == {"fixture-source"}


def test_sources_section_is_rendered_not_the_placeholder_comment(tmp_path: Path) -> None:
    content = _make_content_tree(tmp_path, ["published"])
    out = tmp_path / "out"
    mirror.generate(content, out, "/interview-qa", preview=False, root=ROOT)

    mirrored = next(out.rglob("published-fixture.md")).read_text(encoding="utf-8")
    assert "generated from frontmatter" not in mirrored
    assert "- [Fixture source](https://example.com/reference)" in mirrored


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
    # source, per meta/QUESTIONS.md section 4 - "headings are identifiers,
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
