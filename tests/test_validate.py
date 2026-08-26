from __future__ import annotations

import csv
from pathlib import Path
import shutil

import pytest
import yaml

from iqa.__main__ import main
from iqa.validate import validate_repository


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


def _registry(path: Path, rows: list[tuple[str, str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(("id", "created", "status", "current_path"))
        for qid, status, current_path in rows:
            writer.writerow((qid, "2026-09-04", status, current_path))


def _make_repository(tmp_path: Path, scenario_path: Path) -> tuple[Path, dict]:
    scenario = yaml.safe_load(scenario_path.read_text(encoding="utf-8"))
    for name in ("vocabulary.yml", "TAXONOMY.md"):
        destination = tmp_path / "meta" / name
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / "meta" / name, destination)
    schema_destination = tmp_path / "meta" / "schema" / "question.schema.json"
    schema_destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "meta" / "schema" / "question.schema.json", schema_destination)

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


def test_real_pilots_pass_all_blocking_content_gates() -> None:
    report = validate_repository(ROOT)
    assert report.files_checked == 18
    assert report.questions_checked == 9
    assert report.errors == []


def test_module_cli_validate_command_exists() -> None:
    assert main(["validate", "--root", str(ROOT)]) == 0
