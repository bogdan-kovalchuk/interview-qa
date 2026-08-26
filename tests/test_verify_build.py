from __future__ import annotations

import importlib.util
from pathlib import Path
import shutil
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).parent / "fixtures"

_SPEC = importlib.util.spec_from_file_location("verify_build", ROOT / "tools" / "verify_build.py")
verify_build = importlib.util.module_from_spec(_SPEC)
assert _SPEC.loader is not None
sys.modules["verify_build"] = verify_build
_SPEC.loader.exec_module(verify_build)


SITE_HOST = "bogdan-kovalchuk.github.io"
BASE_PREFIX = "/interview-qa/"


def _write_bilingual_question(content_root: Path) -> None:
    en_dir = content_root / "en" / "python" / "concurrency-and-gil"
    uk_dir = content_root / "uk" / "python" / "concurrency-and-gil"
    en_dir.mkdir(parents=True)
    uk_dir.mkdir(parents=True)
    shutil.copy(FIXTURES / "valid" / "base-en.md", en_dir / "sample-question.md")
    shutil.copy(FIXTURES / "valid" / "base-uk.md", uk_dir / "sample-question.md")

    # A second minimal question, so a canonical page can carry a real
    # resolved qid:-style cross-link to a *different* question (the existing
    # "no resolved qid cross-link" check needs at least one, and it must point
    # at a page that actually exists, or the link-integrity check fails it).
    second_en = (FIXTURES / "valid" / "base-en.md").read_text(encoding="utf-8").replace(
        "id: py-gil-9000", "id: py-gil-9001"
    )
    second_uk = (FIXTURES / "valid" / "base-uk.md").read_text(encoding="utf-8").replace(
        "id: py-gil-9000", "id: py-gil-9001"
    )
    (en_dir / "second-question.md").write_text(second_en, encoding="utf-8")
    (uk_dir / "second-question.md").write_text(second_uk, encoding="utf-8")


def _page(
    *,
    lang: str,
    title: str,
    canonical_path: str,
    alternates: dict[str, str] = {},
    body: str = "",
    anchors: list[str] = [],
    with_navigation_script: bool = False,
) -> str:
    alt_links = "".join(
        f'<link rel="alternate" hreflang="{code}" href="https://{SITE_HOST}{href}"/>'
        for code, href in alternates.items()
    )
    anchor_html = "".join(f'<a href="{href}">link</a>' for href in anchors)
    script = "<script>window.location.replace('x')</script>" if with_navigation_script else ""
    return (
        f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"/>'
        f"<title>{title}</title>"
        f'<link rel="canonical" href="https://{SITE_HOST}{canonical_path}"/>'
        f"{alt_links}</head><body><starlight-lang-select></starlight-lang-select>"
        f"{body}{anchor_html}{script}</body></html>"
    )


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def _build_minimal_dist(dist: Path) -> None:
    """A hand-built dist tree for two bilingual published questions

    (py-gil-9000/"sample-question" and py-gil-9001/"second-question"), shaped
    like Starlight's real output closely enough for verify_build's parsers:
    canonical + resolver pages per language, locale indexes, a language
    switcher, a root redirect, robots.txt and a sitemap. The two questions
    cross-link each other so the pre-existing "resolved qid cross-link" check
    (unrelated to this task's new gates) has something real to find.
    """
    paths = {}
    for qid, slug in (("py-gil-9000", "sample-question"), ("py-gil-9001", "second-question")):
        for lang in ("en", "uk"):
            paths[(lang, qid, "canonical")] = f"{BASE_PREFIX}{lang}/q/{qid}/{slug}/"
            paths[(lang, qid, "resolver")] = f"{BASE_PREFIX}{lang}/q/{qid}/"

    body_text = {
        "en": (
            '<h1>Sample</h1><h2 id="short-answer">Short answer</h2><p>Answer text.</p>'
            '<h2 id="detailed-explanation">Detailed explanation</h2><p>More text.</p>'
        ),
        "uk": (
            '<h1>Приклад</h1><h2 id="korotka-vidpovid">Коротка відповідь</h2><p>Текст.</p>'
            '<h2 id="rozgornute">Розгорнуте пояснення</h2><p>Більше тексту.</p>'
        ),
    }

    for qid, other_qid in (("py-gil-9000", "py-gil-9001"), ("py-gil-9001", "py-gil-9000")):
        slug = "sample-question" if qid == "py-gil-9000" else "second-question"
        for lang in ("en", "uk"):
            canonical = paths[(lang, qid, "canonical")]
            other_canonical = paths[(lang, other_qid, "canonical")]
            alt = {code: paths[(code, qid, "canonical")] for code in ("en", "uk")}
            title = "Sample" if lang == "en" else "Приклад"
            _write(
                dist / lang / "q" / qid / slug / "index.html",
                _page(
                    lang=lang,
                    title=title,
                    canonical_path=canonical,
                    alternates=alt,
                    body=body_text[lang],
                    anchors=[paths[(lang, qid, "resolver")], f"{BASE_PREFIX}{lang}/q/{other_qid}/"],
                ),
            )
            _write(
                dist / lang / "q" / qid / "index.html",
                _page(
                    lang=lang,
                    title="Redirecting",
                    canonical_path=canonical,
                    anchors=[canonical],
                    with_navigation_script=True,
                ),
            )

    _write(dist / "en" / "index.html", _page(lang="en", title="Index", canonical_path=f"{BASE_PREFIX}en/"))
    _write(dist / "uk" / "index.html", _page(lang="uk", title="Індекс", canonical_path=f"{BASE_PREFIX}uk/"))
    _write(
        dist / "index.html",
        _page(
            lang="en",
            title="Root",
            canonical_path=f"{BASE_PREFIX}en/",
            anchors=[f"{BASE_PREFIX}en/"],
            with_navigation_script=True,
        ),
    )
    _write(dist / "robots.txt", "User-agent: *\nAllow: /\n")
    _write(dist / "sitemap-index.xml", "<?xml version=\"1.0\"?><sitemapindex/>")


@pytest.fixture()
def repo(tmp_path: Path) -> Path:
    _write_bilingual_question(tmp_path / "content")
    shutil.copy(ROOT / "meta" / "vocabulary.yml", _mkparent(tmp_path / "meta" / "vocabulary.yml"))
    _build_minimal_dist(tmp_path / "site" / "dist")
    _write(
        tmp_path / "site" / ".build-metrics.json",
        '{"build_seconds": 1.0, "exit_code": 0}',
    )
    return tmp_path


def _mkparent(path: Path) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def test_expected_pages_from_the_model(repo: Path) -> None:
    canonical, resolver = verify_build.expected_pages(repo / "content", "/interview-qa")
    expected_keys = {
        ("en", "py-gil-9000"),
        ("uk", "py-gil-9000"),
        ("en", "py-gil-9001"),
        ("uk", "py-gil-9001"),
    }
    assert set(canonical) == expected_keys
    assert canonical[("en", "py-gil-9000")] == "/interview-qa/en/q/py-gil-9000/sample-question/"
    assert set(resolver) == expected_keys


def test_section_heading_leaks_excludes_identical_pairs() -> None:
    leaks = verify_build.section_heading_leaks(ROOT / "meta" / "vocabulary.yml")
    assert leaks["Short answer"] == "Коротка відповідь"
    assert leaks["Sources"] == "Джерела"
    for en_label, uk_label in leaks.items():
        assert en_label != uk_label


def _run_capture(repo: Path, capsys: pytest.CaptureFixture[str]) -> tuple[int, str]:
    argv_backup = sys.argv
    try:
        sys.argv = ["verify_build.py", "--root", str(repo), "--site-host", SITE_HOST]
        exit_code = verify_build.main()
    finally:
        sys.argv = argv_backup
    return exit_code, capsys.readouterr().out


def test_clean_minimal_build_passes(repo: Path, capsys: pytest.CaptureFixture[str]) -> None:
    exit_code, out = _run_capture(repo, capsys)
    assert exit_code == 0, out
    assert "PASS" in out


def test_raw_citation_token_fails(repo: Path, capsys: pytest.CaptureFixture[str]) -> None:
    target = repo / "site" / "dist" / "en" / "q" / "py-gil-9000" / "sample-question" / "index.html"
    target.write_text(target.read_text(encoding="utf-8").replace("Answer text.", "Answer[^stray]."), encoding="utf-8")
    exit_code, out = _run_capture(repo, capsys)
    assert exit_code == 1
    assert "raw citation token" in out


def test_generated_from_frontmatter_placeholder_fails(repo: Path, capsys: pytest.CaptureFixture[str]) -> None:
    target = repo / "site" / "dist" / "en" / "q" / "py-gil-9000" / "sample-question" / "index.html"
    target.write_text(
        target.read_text(encoding="utf-8").replace("More text.", "<!-- generated from frontmatter -->"),
        encoding="utf-8",
    )
    exit_code, out = _run_capture(repo, capsys)
    assert exit_code == 1
    assert "Sources placeholder" in out


def test_english_heading_on_uk_page_fails(repo: Path, capsys: pytest.CaptureFixture[str]) -> None:
    target = repo / "site" / "dist" / "uk" / "q" / "py-gil-9000" / "sample-question" / "index.html"
    target.write_text(
        target.read_text(encoding="utf-8").replace(
            '<h2 id="korotka-vidpovid">Коротка відповідь</h2>',
            '<h2 id="short-answer">Short answer</h2>',
        ),
        encoding="utf-8",
    )
    exit_code, out = _run_capture(repo, capsys)
    assert exit_code == 1
    assert "English heading" in out


def test_missing_root_index_fails(repo: Path, capsys: pytest.CaptureFixture[str]) -> None:
    (repo / "site" / "dist" / "index.html").unlink()
    exit_code, out = _run_capture(repo, capsys)
    assert exit_code == 1
    assert "site root" in out


def test_missing_robots_fails(repo: Path, capsys: pytest.CaptureFixture[str]) -> None:
    (repo / "site" / "dist" / "robots.txt").unlink()
    exit_code, out = _run_capture(repo, capsys)
    assert exit_code == 1
    assert "robots.txt" in out


def test_missing_sitemap_fails(repo: Path, capsys: pytest.CaptureFixture[str]) -> None:
    (repo / "site" / "dist" / "sitemap-index.xml").unlink()
    exit_code, out = _run_capture(repo, capsys)
    assert exit_code == 1
    assert "sitemap" in out


def test_missing_hreflang_alternate_fails(repo: Path, capsys: pytest.CaptureFixture[str]) -> None:
    target = repo / "site" / "dist" / "en" / "q" / "py-gil-9000" / "sample-question" / "index.html"
    text = target.read_text(encoding="utf-8")
    text = text.replace(
        f'<link rel="alternate" hreflang="uk" href="https://{SITE_HOST}{BASE_PREFIX}uk/q/py-gil-9000/sample-question/"/>',
        "",
    )
    target.write_text(text, encoding="utf-8")
    exit_code, out = _run_capture(repo, capsys)
    assert exit_code == 1
    assert 'hreflang="uk"' in out


def test_stale_extra_page_not_in_model_fails(repo: Path, capsys: pytest.CaptureFixture[str]) -> None:
    stale = repo / "site" / "dist" / "en" / "q" / "py-gil-0000" / "old-question" / "index.html"
    _write(
        stale,
        _page(lang="en", title="Stale", canonical_path=f"{BASE_PREFIX}en/q/py-gil-0000/old-question/"),
    )
    exit_code, out = _run_capture(repo, capsys)
    assert exit_code == 1
    assert "not in the model's production set" in out


def test_missing_expected_page_fails(repo: Path, capsys: pytest.CaptureFixture[str]) -> None:
    shutil.rmtree(repo / "site" / "dist" / "en" / "q" / "py-gil-9000" / "sample-question")
    exit_code, out = _run_capture(repo, capsys)
    assert exit_code == 1
    assert "was not emitted" in out
