from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

from verify_cards import EXPECTED_HEADER, load_topic_specs, validate_file  # noqa: E402


class VerifyCardsRegressionTests(unittest.TestCase):
    def test_project_manifest_loads(self) -> None:
        self.assertEqual(len(load_topic_specs(ROOT)), 23)

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.temp_dir.name)
        self.path = self.root / "cards" / "01_python_fundamentals.txt"
        self.path.parent.mkdir(parents=True)
        self.specs = {
            self.path.name: {
                "id": "01",
                "topic_tag": "topic::01_python_fundamentals",
                "scope_tag": "scope::Core",
            }
        }

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def write_card(self, front: str, tags: str) -> list[str]:
        text = "\n".join(EXPECTED_HEADER + [f"{front}\t\t{tags}"]) + "\n"
        self.path.write_text(text, encoding="utf-8")
        _, errors, _ = validate_file(self.path, self.specs, {}, front_only=True)
        return errors

    def valid_tags(self) -> str:
        return (
            "topic::01_python_fundamentals type::Mechanism level::Middle "
            "scope::Core stage::FrontOnly card::PYI_01_001 "
            "ref::OFFICIAL source::PythonDocs"
        )

    def test_valid_front_passes(self) -> None:
        self.assertEqual(self.write_card("How does <code>len(x)</code> work?", self.valid_tags()), [])

    def test_filename_topic_mismatch_fails(self) -> None:
        tags = self.valid_tags().replace(
            "topic::01_python_fundamentals", "topic::02_syntax_control_flow"
        )
        self.assertTrue(any("topic tag must be" in error for error in self.write_card("Question?", tags)))

    def test_scope_mismatch_fails(self) -> None:
        tags = self.valid_tags().replace("scope::Core", "scope::Overview")
        self.assertTrue(any("scope tag must be" in error for error in self.write_card("Question?", tags)))

    def test_card_id_topic_mismatch_fails(self) -> None:
        tags = self.valid_tags().replace("PYI_01_001", "PYI_02_001")
        self.assertTrue(any("card ID topic number" in error for error in self.write_card("Question?", tags)))

    def test_unknown_version_fails(self) -> None:
        tags = f"{self.valid_tags()} version::Py9_99"
        self.assertTrue(any("unsupported version::" in error for error in self.write_card("Question?", tags)))

    def test_unknown_namespace_fails(self) -> None:
        tags = f"{self.valid_tags()} surprise::value"
        self.assertTrue(any("unsupported tag namespaces" in error for error in self.write_card("Question?", tags)))

    def test_unsafe_html_tag_fails(self) -> None:
        errors = self.write_card("Why <script>alert(1)</script>?", self.valid_tags())
        self.assertTrue(any("unsupported HTML tag" in error for error in errors))

    def test_mismatched_html_fails(self) -> None:
        errors = self.write_card("Why <code>x</span>?", self.valid_tags())
        self.assertTrue(any("mismatched" in error for error in errors))

    def test_raw_operator_inside_code_fails(self) -> None:
        errors = self.write_card("What is <code>x < y</code>?", self.valid_tags())
        self.assertTrue(any("raw < or >" in error for error in errors))

    def test_sensitive_card_requires_source_tag(self) -> None:
        tags = self.valid_tags().replace(" source::PythonDocs", "") + " version::Py3_14"
        errors = self.write_card("What changed?", tags)
        self.assertTrue(any("requires source::*" in error for error in errors))

    def write_completed(self, front: str, back: str, tags: str) -> list[str]:
        text = "\n".join(EXPECTED_HEADER + [f"{front}\t{back}\t{tags}"]) + "\n"
        self.path.write_text(text, encoding="utf-8")
        _, errors, _ = validate_file(self.path, self.specs, {}, front_only=False)
        return errors

    def completed_tags(self) -> str:
        return self.valid_tags().replace(" stage::FrontOnly", "")

    def test_completed_card_passes(self) -> None:
        errors = self.write_completed(
            "How does <code>len(x)</code> work?",
            "<span class=\"key\">It calls the object protocol.</span>",
            self.completed_tags(),
        )
        self.assertEqual(errors, [])

    def test_front_only_tag_with_back_fails(self) -> None:
        errors = self.write_completed(
            "How does <code>len(x)</code> work?",
            "<span class=\"key\">It calls the object protocol.</span>",
            self.valid_tags(),
        )
        self.assertTrue(
            any("stage::FrontOnly is not allowed" in error for error in errors)
        )


if __name__ == "__main__":
    unittest.main()
