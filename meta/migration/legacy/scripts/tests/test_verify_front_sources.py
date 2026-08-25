from __future__ import annotations

import csv
import hashlib
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from verify_cards import EXPECTED_HEADER  # noqa: E402
from verify_front_sources import REQUIRED_COLUMNS, verify  # noqa: E402


FRONT = "Що поверне другий виклик?"
FRONT_ONLY_TAGS = (
    "topic::05_functions_scope_closures type::Code level::Middle "
    "scope::Core stage::FrontOnly card::PYI_05_001 ref::OFFICIAL"
)
COMPLETED_TAGS = (
    "topic::05_functions_scope_closures type::Code level::Middle "
    "scope::Core card::PYI_05_001 ref::OFFICIAL source::PythonDocs"
)
BACK = "Другий виклик поверне <code>[1, 2]</code>."
PERMALINK = (
    "https://github.com/tavor118/pj_python_interview_questions_and_answers/"
    "blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/general.md#L38-L67"
)
OFFICIAL = "https://docs.python.org/3.14/tutorial/controlflow.html"


class VerifyFrontSourcesTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.cards = self.root / "cards"
        self.cards.mkdir(parents=True)
        self.register = self.root / "front_sources.csv"

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write_cards(self, rows: list[str]) -> None:
        text = "\n".join(EXPECTED_HEADER) + "\n" + "".join(f"{row}\n" for row in rows)
        (self.cards / "05_functions_scope_closures.txt").write_text(
            text, encoding="utf-8"
        )

    def write_register(self, back_status: str, card_id: str = "PYI_05_001") -> None:
        with self.register.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=REQUIRED_COLUMNS, lineterminator="\n")
            writer.writeheader()
            writer.writerow(
                {
                    "card_id": card_id,
                    "topic_tag": "topic::05_functions_scope_closures",
                    "card_file": "cards/05_functions_scope_closures.txt",
                    "front_sha256": hashlib.sha256(FRONT.encode("utf-8")).hexdigest(),
                    "community_answer_ref": "",
                    "official_refs": OFFICIAL,
                    "source_role": "official_only",
                    "back_status": back_status,
                    "notes": "",
                }
            )

    def test_front_only_with_pending_passes(self) -> None:
        self.write_cards([f"{FRONT}\t\t{FRONT_ONLY_TAGS}"])
        self.write_register("pending")
        _cards, _records, errors = verify(self.cards, self.register)
        self.assertEqual(errors, [])

    def test_completed_with_reviewed_passes(self) -> None:
        self.write_cards([f"{FRONT}\t{BACK}\t{COMPLETED_TAGS}"])
        self.write_register("reviewed")
        _cards, _records, errors = verify(self.cards, self.register)
        self.assertEqual(errors, [])

    def test_completed_with_pending_fails(self) -> None:
        self.write_cards([f"{FRONT}\t{BACK}\t{COMPLETED_TAGS}"])
        self.write_register("pending")
        _cards, _records, errors = verify(self.cards, self.register)
        self.assertTrue(any("requires back_status" in error for error in errors))

    def test_front_only_with_drafted_fails(self) -> None:
        self.write_cards([f"{FRONT}\t\t{FRONT_ONLY_TAGS}"])
        self.write_register("drafted")
        _cards, _records, errors = verify(self.cards, self.register)
        self.assertTrue(any("requires back_status pending" in error for error in errors))

    def test_orphaned_register_row_fails(self) -> None:
        self.write_cards([f"{FRONT}\t\t{FRONT_ONLY_TAGS}"])
        self.write_register("pending")
        with self.register.open("a", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=REQUIRED_COLUMNS, lineterminator="\n")
            writer.writerow(
                {
                    "card_id": "PYI_05_099",
                    "topic_tag": "topic::05_functions_scope_closures",
                    "card_file": "cards/05_functions_scope_closures.txt",
                    "front_sha256": "0" * 64,
                    "community_answer_ref": "",
                    "official_refs": OFFICIAL,
                    "source_role": "official_only",
                    "back_status": "pending",
                    "notes": "",
                }
            )
        _cards, _records, errors = verify(self.cards, self.register)
        self.assertTrue(any("orphaned provenance row" in error for error in errors))

    def test_hash_mismatch_fails(self) -> None:
        self.write_cards([f"{FRONT}\t\t{FRONT_ONLY_TAGS}"])
        self.write_register("pending")
        text = self.register.read_text(encoding="utf-8").replace(
            hashlib.sha256(FRONT.encode("utf-8")).hexdigest(), "1" * 64
        )
        self.register.write_text(text, encoding="utf-8")
        _cards, _records, errors = verify(self.cards, self.register)
        self.assertTrue(any("front_sha256 does not match" in error for error in errors))

    def test_missing_register_row_fails(self) -> None:
        self.write_cards([f"{FRONT}\t\t{FRONT_ONLY_TAGS}"])
        self.write_register("pending", card_id="PYI_05_099")
        _cards, _records, errors = verify(self.cards, self.register)
        self.assertTrue(any("no provenance row" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
