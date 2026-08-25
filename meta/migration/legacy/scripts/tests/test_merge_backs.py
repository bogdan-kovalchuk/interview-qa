from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from merge_backs import merge  # noqa: E402
from verify_cards import EXPECTED_HEADER  # noqa: E402


HEADER = "\n".join(EXPECTED_HEADER) + "\n"
FRONT = "Чим <code>is</code> відрізняється від <code>==</code>?"
DRAFT_TAGS = (
    "topic::03_objects_types_mutability type::Contrast level::Middle "
    "scope::Core stage::FrontOnly card::PYI_03_001 ref::OFFICIAL "
    "source::PythonDocs"
)
BACK = "<span class=\"key\"><code>is</code> перевіряє ідентичність.</span>"
COMPLETED_TAGS = (
    "topic::03_objects_types_mutability type::Contrast level::Middle "
    "scope::Core card::PYI_03_001 ref::OFFICIAL source::PythonDocs"
)


class MergeBacksTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.draft = self.root / "03_objects_types_mutability.txt"
        self.draft.write_text(
            HEADER + f"{FRONT}\t\t{DRAFT_TAGS}\n", encoding="utf-8"
        )

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write_batch(self, name: str, rows: list[str]) -> Path:
        path = self.root / name
        path.write_text(HEADER + "".join(f"{row}\n" for row in rows), encoding="utf-8")
        return path

    def merged_lines(self) -> list[str]:
        return self.draft.read_text(encoding="utf-8").splitlines()

    def test_happy_path_replaces_row_and_keeps_front(self) -> None:
        batch = self.write_batch(
            "batch.txt", [f"{FRONT}\t{BACK}\t{COMPLETED_TAGS}"]
        )
        merged, errors = merge(self.draft, [batch])
        self.assertEqual(errors, [])
        self.assertEqual(merged, ["card::PYI_03_001"])
        lines = self.merged_lines()
        self.assertEqual(lines[:5], EXPECTED_HEADER)
        self.assertEqual(lines[5], f"{FRONT}\t{BACK}\t{COMPLETED_TAGS}")

    def test_allows_adding_optional_tags(self) -> None:
        tags = COMPLETED_TAGS + " runtime::CPython version::Py3_14"
        batch = self.write_batch("batch.txt", [f"{FRONT}\t{BACK}\t{tags}"])
        _merged, errors = merge(self.draft, [batch])
        self.assertEqual(errors, [])
        self.assertIn("runtime::CPython", self.merged_lines()[5])

    def test_front_drift_fails(self) -> None:
        batch = self.write_batch(
            "batch.txt", [f"{FRONT} extra\t{BACK}\t{COMPLETED_TAGS}"]
        )
        merged, errors = merge(self.draft, [batch])
        self.assertEqual(merged, [])
        self.assertTrue(any("Front differs" in error for error in errors))

    def test_removing_existing_tag_fails(self) -> None:
        tags = COMPLETED_TAGS.replace(" ref::OFFICIAL", "")
        batch = self.write_batch("batch.txt", [f"{FRONT}\t{BACK}\t{tags}"])
        merged, errors = merge(self.draft, [batch])
        self.assertEqual(merged, [])
        self.assertTrue(any("tags removed" in error for error in errors))

    def test_adding_core_tag_fails(self) -> None:
        tags = COMPLETED_TAGS + " level::Senior"
        batch = self.write_batch("batch.txt", [f"{FRONT}\t{BACK}\t{tags}"])
        merged, errors = merge(self.draft, [batch])
        self.assertEqual(merged, [])
        self.assertTrue(any("unsupported added tags" in error for error in errors))

    def test_unknown_card_id_fails(self) -> None:
        tags = COMPLETED_TAGS.replace("PYI_03_001", "PYI_03_099")
        batch = self.write_batch("batch.txt", [f"{FRONT}\t{BACK}\t{tags}"])
        merged, errors = merge(self.draft, [batch])
        self.assertEqual(merged, [])
        self.assertTrue(any("not in the draft" in error for error in errors))

    def test_empty_back_fails(self) -> None:
        batch = self.write_batch("batch.txt", [f"{FRONT}\t\t{COMPLETED_TAGS}"])
        merged, errors = merge(self.draft, [batch])
        self.assertEqual(merged, [])
        self.assertTrue(any("Back must be non-empty" in error for error in errors))

    def test_stage_front_only_kept_fails(self) -> None:
        tags = COMPLETED_TAGS + " stage::FrontOnly"
        batch = self.write_batch("batch.txt", [f"{FRONT}\t{BACK}\t{tags}"])
        merged, errors = merge(self.draft, [batch])
        self.assertEqual(merged, [])
        self.assertTrue(any("stage::FrontOnly must be removed" in error for error in errors))

    def test_failed_merge_does_not_touch_draft(self) -> None:
        before = self.draft.read_text(encoding="utf-8")
        batch = self.write_batch("batch.txt", [f"{FRONT} extra\t{BACK}\t{COMPLETED_TAGS}"])
        merge(self.draft, [batch])
        self.assertEqual(self.draft.read_text(encoding="utf-8"), before)

    def test_row_order_is_preserved(self) -> None:
        second_front = "Друге запитання?"
        second_draft_tags = DRAFT_TAGS.replace("PYI_03_001", "PYI_03_002")
        second_completed_tags = COMPLETED_TAGS.replace("PYI_03_001", "PYI_03_002")
        self.draft.write_text(
            HEADER
            + f"{FRONT}\t\t{DRAFT_TAGS}\n"
            + f"{second_front}\t\t{second_draft_tags}\n",
            encoding="utf-8",
        )
        batch = self.write_batch(
            "batch.txt", [f"{second_front}\t{BACK}\t{second_completed_tags}"]
        )
        merged, errors = merge(self.draft, [batch])
        self.assertEqual(errors, [])
        self.assertEqual(merged, ["card::PYI_03_002"])
        lines = self.merged_lines()
        self.assertIn("PYI_03_001", lines[5])
        self.assertIn("PYI_03_002", lines[6])
        self.assertIn(BACK, lines[6])


if __name__ == "__main__":
    unittest.main()
