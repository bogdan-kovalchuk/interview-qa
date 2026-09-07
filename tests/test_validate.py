from __future__ import annotations

import csv
from pathlib import Path
import shutil

import pytest
import yaml

from corpus import FILES, QUESTIONS
from iqa.__main__ import main
from iqa.validate import _sentence_count, validate_repository


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = Path(__file__).parent / "fixtures"
BASE_SLUG = "negative-fixture-question.md"
BASE_PATH = f"python/concurrency-and-gil/{BASE_SLUG}"
EXPECTED_FIXTURE_GATES = {
    "schema",
    "id-unique",
    "id-immutable",
    "sections",
    "sections-by-level",
    "short-answer-limits",
    "sources",
    "facets-vocabulary",
    "xref",
    "taxonomy",
    "lang-files-exist",
    "lang-structure-parity",
    "lang-code-identical",
    "lang-links-parity",
    "lang-glossary",
    "lang-reconciliation",
    "source-present",
    "claim-linked",
    "source-applicability",
    "example-executed",
    "no-duplicates",
}


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def _replace(text: str, old: str, new: str) -> str:
    assert text.count(old) >= 1, f"fixture mutation did not find {old!r}"
    return text.replace(old, new)


def test_sentence_count_preserves_boundaries_across_html_breaks() -> None:
    assert _sentence_count("First sentence.<br>Second sentence.") == 2
    assert _sentence_count("First sentence.<br />Second sentence.") == 2
    assert _sentence_count("First sentence. <code>mutex</code> starts the second.") == 2


def test_sentence_count_does_not_depend_on_the_markup_form() -> None:
    """The 2-5 sentence limit bounds what fits on a card, so the same answer
    must count the same however it is written.

    A sentence may legitimately start with a lowercase identifier in inline code
    or in a highlighted fragment. Marking that position only for the HTML form
    made `<code>mutex</code>` count as a new sentence and `` `mutex` `` not, so
    normalising an imported answer from HTML to Markdown silently changed how
    many sentences the gate saw in it."""
    html_form = "First sentence. <code>mutex</code> starts the second."
    markdown_form = "First sentence. `mutex` starts the second."
    bold_html = "First sentence. <span class=\"key\">mutex</span> starts the second."
    bold_markdown = "First sentence. **mutex** starts the second."

    assert _sentence_count(html_form) == _sentence_count(markdown_form) == 2
    assert _sentence_count(bold_html) == _sentence_count(bold_markdown) == 2


def _registry(path: Path, rows: list[tuple[str, str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(("id", "created", "status", "current_path"))
        for qid, status, current_path in rows:
            writer.writerow((qid, "2026-09-04", status, current_path))


def _make_repository(tmp_path: Path, scenario_path: Path) -> tuple[Path, dict]:
    scenario = yaml.safe_load(scenario_path.read_text(encoding="utf-8"))
    for name in ("vocabulary.yml", "taxonomy.md"):
        destination = tmp_path / "meta" / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / "meta" / name, destination)
    schema_destination = tmp_path / "meta" / "question.schema.json"
    shutil.copy2(ROOT / "meta" / "question.schema.json", schema_destination)

    texts = {
        "en": (FIXTURES / "valid" / "base-en.md").read_text(encoding="utf-8"),
        "uk": (FIXTURES / "valid" / "base-uk.md").read_text(encoding="utf-8"),
    }
    mode = scenario.get("mode", "replace")
    if mode == "replace":
        language = scenario["language"]
        for replacement in scenario["replacements"]:
            texts[language] = _replace(
                texts[language], replacement["old"], replacement["new"]
            )
    elif mode == "remove-language":
        del texts[scenario["language"]]

    for language, text in texts.items():
        _write(tmp_path / "content" / language / BASE_PATH, text)

    rows = [("py-gil-9000", "published", BASE_PATH)]
    if mode == "duplicate-file":
        language = scenario["language"]
        duplicate_path = (
            tmp_path
            / "content"
            / language
            / "python"
            / "concurrency-and-gil"
            / "another-negative-fixture-question.md"
        )
        _write(duplicate_path, texts[language])
    elif mode == "registry-replace":
        rows[0] = ("py-gil-9000", "published", scenario["new"])
    elif mode == "add-duplicate-question":
        duplicate_path = "python/concurrency-and-gil/duplicate-negative-fixture-question.md"
        for language, text in texts.items():
            duplicate = text.replace("py-gil-9000", "py-gil-9001")
            _write(tmp_path / "content" / language / duplicate_path, duplicate)
        rows.append(("py-gil-9001", "published", duplicate_path))

    _registry(tmp_path / "meta" / "id-registry.csv", rows)
    return tmp_path, scenario


def negative_fixture_paths() -> list[Path]:
    return sorted((FIXTURES / "negative").glob("*.yml"))


def test_every_in_scope_gate_has_a_negative_fixture() -> None:
    assert {path.stem for path in negative_fixture_paths()} == EXPECTED_FIXTURE_GATES


@pytest.mark.parametrize("scenario_path", negative_fixture_paths(), ids=lambda path: path.stem)
def test_negative_fixture_is_caught(tmp_path: Path, scenario_path: Path) -> None:
    repository, scenario = _make_repository(tmp_path, scenario_path)
    report = validate_repository(repository)
    matches = [item for item in report.diagnostics if item.gate == scenario["gate"]]

    assert matches, f"{scenario_path.name} did not trigger {scenario['gate']}: {report.diagnostics}"
    assert {item.severity for item in matches} == {scenario.get("severity", "error")}


def _base_repository(tmp_path: Path, *, en_text: str, uk_text: str) -> Path:
    """A minimal repository around one hand-built question, without going
    through the yaml-driven negative-fixture machinery above (that path is
    reserved for the one-fixture-per-gate set `EXPECTED_FIXTURE_GATES`
    enumerates)."""
    for name in ("vocabulary.yml", "taxonomy.md"):
        destination = tmp_path / "meta" / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / "meta" / name, destination)
    schema_destination = tmp_path / "meta" / "question.schema.json"
    shutil.copy2(ROOT / "meta" / "question.schema.json", schema_destination)
    _write(tmp_path / "content" / "en" / BASE_PATH, en_text)
    _write(tmp_path / "content" / "uk" / BASE_PATH, uk_text)
    _registry(tmp_path / "meta" / "id-registry.csv", [("py-gil-9000", "published", BASE_PATH)])
    return tmp_path


def test_lang_parity_gates_ignore_a_todo_section(tmp_path: Path) -> None:
    """meta/quality-gates.md: a `TODO` placeholder is exempt from having text -

    including the code block and citation token that section would otherwise
    need to match between languages. A Ukrainian `Detailed explanation` with a
    written code block and its own citation must not be compared against an
    English `Detailed explanation` that is still `TODO`."""
    en_base = (FIXTURES / "valid" / "base-en.md").read_text(encoding="utf-8")
    uk_base = (FIXTURES / "valid" / "base-uk.md").read_text(encoding="utf-8")

    en_text = _replace(
        en_base,
        "The event loop depends on tasks returning control while they wait.[^python-asyncio-docs]",
        "TODO",
    )
    uk_text = _replace(
        uk_base,
        "Event loop залежить від того, що tasks повертають керування під час очікування.[^python-asyncio-docs]",
        "Event loop залежить від того, що tasks повертають керування під час очікування.[^python-asyncio-docs]\n\n"
        "```python\nasync def slow() -> None:\n    time.sleep(1)\n```",
    )

    repository = _base_repository(tmp_path, en_text=en_text, uk_text=uk_text)
    report = validate_repository(repository)

    blocked_gates = {item.gate for item in report.errors}
    assert "lang-code-identical" not in blocked_gates
    assert "lang-links-parity" not in blocked_gates


def test_lang_code_identical_still_catches_a_real_mismatch(tmp_path: Path) -> None:
    """Two sections that are written in *both* languages must still match -

    the TODO exemption only ever widens what is skipped, never what a written
    section is allowed to disagree on."""
    en_base = (FIXTURES / "valid" / "base-en.md").read_text(encoding="utf-8")
    uk_base = (FIXTURES / "valid" / "base-uk.md").read_text(encoding="utf-8")

    en_text = _replace(
        en_base,
        "The event loop depends on tasks returning control while they wait.[^python-asyncio-docs]",
        "The event loop depends on tasks returning control while they wait.[^python-asyncio-docs]\n\n"
        "```python\nasync def slow() -> None:\n    time.sleep(1)\n```",
    )
    uk_text = _replace(
        uk_base,
        "Event loop залежить від того, що tasks повертають керування під час очікування.[^python-asyncio-docs]",
        "Event loop залежить від того, що tasks повертають керування під час очікування.[^python-asyncio-docs]\n\n"
        "```python\nasync def slow() -> None:\n    time.sleep(2)\n```",
    )

    repository = _base_repository(tmp_path, en_text=en_text, uk_text=uk_text)
    report = validate_repository(repository)

    assert "lang-code-identical" in {item.gate for item in report.errors}


def test_inline_code_indexing_a_function_pointer_table_is_not_a_link(tmp_path: Path) -> None:
    """`table[opcode](ctx, frame)` in backticks is C, not a Markdown link.

    `MARKDOWN_LINK_RE` matches `[...](...)` and the link and URL checks used to
    run over text that still contained inline code spans, so a perfectly legal
    array of function pointers tripped both `xref` and `short-answer-limits`.
    There is no other way to write that expression in prose."""
    en_base = (FIXTURES / "valid" / "base-en.md").read_text(encoding="utf-8")
    uk_base = (FIXTURES / "valid" / "base-uk.md").read_text(encoding="utf-8")

    en_text = _replace(
        en_base,
        "The event loop depends on tasks returning control while they wait.[^python-asyncio-docs]",
        "A dispatch table calls `table[opcode](ctx, frame)` for the selected "
        "handler.[^python-asyncio-docs]",
    )
    uk_text = _replace(
        uk_base,
        "Event loop залежить від того, що tasks повертають керування під час очікування.[^python-asyncio-docs]",
        "Dispatch table викликає `table[opcode](ctx, frame)` для обраного "
        "handler-а.[^python-asyncio-docs]",
    )

    repository = _base_repository(tmp_path, en_text=en_text, uk_text=uk_text)
    report = validate_repository(repository)

    assert "xref" not in {item.gate for item in report.errors}
    assert not [
        item
        for item in report.errors
        if item.gate == "short-answer-limits" and "ready URL" in item.message
    ]


def test_question_code_is_an_optional_section_before_the_answer(tmp_path: Path) -> None:
    """`Question code` holds the snippet the question is about.

    It is optional, it sits immediately before `Short answer`, it does not take
    part in `completeness`, and - because both languages carry it written - its
    block is compared byte-for-byte by `lang-code-identical` like any other."""
    en_base = (FIXTURES / "valid" / "base-en.md").read_text(encoding="utf-8")
    uk_base = (FIXTURES / "valid" / "base-uk.md").read_text(encoding="utf-8")
    block = "## Question code\n\n```python\nasync def slow() -> None:\n    time.sleep(1)\n```\n\n## Short answer"

    repository = _base_repository(
        tmp_path,
        en_text=_replace(en_base, "## Short answer", block),
        uk_text=_replace(uk_base, "## Short answer", block),
    )
    report = validate_repository(repository)

    assert report.errors == []


def test_question_code_holds_one_block_and_nothing_else(tmp_path: Path) -> None:
    """Prose belongs to the title or to the answer, not to `Question code`.

    The section exists to carry one snippet onto the card Front next to the
    title; a second block or a run of text around it would be rendered as part
    of the question without being one."""
    en_base = (FIXTURES / "valid" / "base-en.md").read_text(encoding="utf-8")
    uk_base = (FIXTURES / "valid" / "base-uk.md").read_text(encoding="utf-8")
    block = (
        "## Question code\n\nSome prose that is not code.\n\n"
        "```python\nasync def slow() -> None:\n    time.sleep(1)\n```\n\n## Short answer"
    )

    repository = _base_repository(
        tmp_path,
        en_text=_replace(en_base, "## Short answer", block),
        uk_text=_replace(uk_base, "## Short answer", block),
    )
    report = validate_repository(repository)

    messages = [item.message for item in report.errors if item.gate == "sections"]
    assert any("exactly one code block" in message for message in messages), messages


def test_real_content_passes_all_blocking_content_gates() -> None:
    """The whole real `content/` tree has zero blocking failures.

    The nine original pilots, the 392 questions migrated from the predecessor
    deck (meta/plan.md step 4) and the embedded import of step 7a. Word-count
    is a documented soft warning (meta/questions.md SS7), not asserted away
    here. The sizes live in `tests/corpus.py`."""
    report = validate_repository(ROOT)
    assert report.files_checked == FILES
    assert report.questions_checked == QUESTIONS
    assert report.errors == []


def test_module_cli_validate_command_exists() -> None:
    assert main(["validate", "--root", str(ROOT)]) == 0
