from __future__ import annotations

from pathlib import Path
import sys

import pytest

from iqa import report
from iqa.lifecycle import Completeness
from iqa.model import parse_question_text


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
FIXTURES = Path(__file__).parent / "fixtures"


def _write_question(directory: Path, text: str, filename: str) -> None:
    directory.mkdir(parents=True, exist_ok=True)
    (directory / filename).write_text(text, encoding="utf-8")


def test_guid_formula_matches_the_anki_builder() -> None:
    sys.path.insert(0, str(ROOT / "anki"))
    import build as anki_build  # noqa: E402

    for qid in ("py-asyncio-0007", "cpp-mem-0001", "bhv-team-0001"):
        assert report.guid_for(qid) == anki_build.guid_for(qid)


def test_report_covers_all_808_questions_both_languages() -> None:
    built = report.build_report(CONTENT)
    assert len(built["questions"]) == 808
    for row in built["questions"]:
        assert set(row["languages"]) == {"en", "uk"}
        assert row["guid"] == report.guid_for(row["id"])
    assert built["aggregates"]["totals"]["total"] == 808


def test_missing_required_sections_reported_for_a_stub_question(tmp_path: Path) -> None:
    content = tmp_path / "content"
    directory = content / "en" / "python" / "concurrency-and-gil"
    _write_question(directory, (FIXTURES / "states" / "stub.md").read_text(encoding="utf-8"), "stub.md")

    built = report.build_report(content)
    row = built["questions"][0]
    en = row["languages"]["en"]
    assert en["completeness"] == Completeness.STUB.value
    assert en["missing_required_sections"] == ["Detailed explanation", "Evaluation guide"]
    assert row["languages"]["uk"]["exists"] is False


def test_needs_reconciliation_is_directional(tmp_path: Path) -> None:
    content = tmp_path / "content"
    en_dir = content / "en" / "python" / "concurrency-and-gil"
    uk_dir = content / "uk" / "python" / "concurrency-and-gil"

    en_text = (FIXTURES / "valid" / "base-en.md").read_text(encoding="utf-8")
    uk_text = (FIXTURES / "valid" / "base-uk.md").read_text(encoding="utf-8")
    # English moves to revision 2 but the Ukrainian file still declares en: 1 -
    # Ukrainian now needs reconciliation, English does not.
    en_text = en_text.replace("content_revision: 1", "content_revision: 2", 1)

    _write_question(en_dir, en_text, "q.md")
    _write_question(uk_dir, uk_text, "q.md")

    built = report.build_report(content)
    row = built["questions"][0]
    assert row["languages"]["en"]["needs_reconciliation"] is False
    assert row["languages"]["uk"]["needs_reconciliation"] is True


def test_qid_resolvable_detects_unknown_targets(tmp_path: Path) -> None:
    content = tmp_path / "content"
    en_dir = content / "en" / "python" / "concurrency-and-gil"
    en_text = (FIXTURES / "valid" / "base-en.md").read_text(encoding="utf-8")
    en_text = en_text.replace(
        "The event loop runs callbacks on one thread.",
        "The event loop runs callbacks on one thread. See qid:py-gil-9999.",
    )
    _write_question(en_dir, en_text, "q.md")

    built = report.build_report(content)
    row = built["questions"][0]
    assert row["languages"]["en"]["qid_resolvable"] is False


def test_csv_and_json_round_trip(tmp_path: Path) -> None:
    built = report.build_report(CONTENT)
    text = report.report_csv(built)
    header = text.splitlines()[0].split(",")
    assert header == report.CSV_FIELDS
    assert len(text.splitlines()) == 1 + len(built["questions"])

    json_text = report.report_json(built)
    assert '"by_section_field"' in json_text


def test_aggregate_by_section_field_shows_the_detailed_explanation_gap() -> None:
    built = report.build_report(CONTENT)
    detailed = built["aggregates"]["by_section_field"]["Detailed explanation"]
    # The documented skeleton state (AGENTS.md): migrated questions carry a written
    # Ukrainian short answer and TODO everywhere else, including Detailed explanation.
    assert detailed["uk"]["written"] < detailed["uk"]["applicable"]
    assert detailed["en"]["written"] < detailed["en"]["applicable"]


def test_write_report_creates_both_files(tmp_path: Path) -> None:
    json_path = tmp_path / "progress.json"
    csv_path = tmp_path / "progress.csv"
    count = report.write_report(CONTENT, json_path, csv_path)
    assert count == 808
    assert json_path.exists()
    assert csv_path.exists()


def test_todo_cli_lists_incomplete_pairs(tmp_path: Path, capsys: pytest.CaptureFixture[str]) -> None:
    content = tmp_path / "content"
    directory = content / "en" / "python" / "concurrency-and-gil"
    _write_question(directory, (FIXTURES / "states" / "stub.md").read_text(encoding="utf-8"), "stub.md")

    exit_code = report.main(["--root", str(tmp_path), "--todo"])
    assert exit_code == 0
    out = capsys.readouterr().out
    assert "py-gil-9101" in out
    assert "en" in out
