from __future__ import annotations

from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "packaging" / "anki"))

import build as anki_build  # noqa: E402  (path insertion must happen first)
from iqa.export import build_export


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def vocabulary() -> dict:
    import yaml

    return yaml.safe_load((ROOT / "meta" / "vocabulary.yml").read_text(encoding="utf-8")) or {}


@pytest.fixture(scope="module")
def payload() -> dict:
    return build_export(ROOT / "content")


def test_guid_formula_matches_test_deck_reference_implementation() -> None:
    # packaging/anki/test-deck/build_test_deck.py is the worked example whose
    # guid_for() the real builder must reproduce exactly (meta/ANKI.md "GUID").
    test_deck_dir = ROOT / "packaging" / "anki" / "test-deck"
    sys.path.insert(0, str(test_deck_dir))
    import build_test_deck  # noqa: E402

    for qid in ("py-asyncio-0007", "cpp-mem-0001", "bhv-team-0001"):
        assert anki_build.guid_for(qid) == build_test_deck.guid_for(qid)


def test_all_nine_pilots_ship_a_card(payload: dict, vocabulary: dict) -> None:
    model = anki_build.make_model()
    notes = anki_build.build_notes(payload["questions"], vocabulary, model)
    assert len(notes) == 9

    shipped_ids = {note.fields[anki_build.FIELD_ORDER.index("QID")] for _deck, note in notes}
    assert shipped_ids == {question["id"] for question in payload["questions"]}


def test_front_label_comes_from_vocabulary_not_from_the_qid_prefix(payload: dict, vocabulary: dict) -> None:
    # The trap PLAN.md calls out: the track label must not be decoded from the
    # QID prefix. Build the same question under a spoofed id whose prefix maps
    # to a different track in the old front.html/back.html JS map, and confirm
    # the rendered label still reflects the real `track` field.
    by_id = {question["id"]: question for question in payload["questions"]}
    question = dict(by_id["py-gil-0001"])
    card = question["languages"]["uk"]["card"]
    front_html = anki_build.render_front(vocabulary, question, card, question["languages"]["uk"]["title"])
    assert "<div class=\"deck-label\">Python</div>" in front_html

    spoofed = dict(question, id="cpp-gil-0001")  # cpp-* prefix, but track is still python
    front_spoofed = anki_build.render_front(vocabulary, spoofed, card, question["languages"]["uk"]["title"])
    assert front_spoofed == front_html  # unaffected by the id string


def test_front_and_back_templates_no_longer_parse_the_qid() -> None:
    # PLAN.md's named trap: the visible track label used to come from splitting
    # the QID prefix in a <script> block. Fixed by baking the label into the
    # generated Front field instead; the templates must carry neither the
    # QID field reference nor any prefix-splitting logic.
    for name in ("front.html", "back.html"):
        text = (ROOT / "packaging" / "anki" / "notetype" / name).read_text(encoding="utf-8")
        assert "{{text:QID}}" not in text
        assert ".split(" not in text
        assert "<script>" not in text


def test_coding_front_includes_task_and_constraints_list(payload: dict, vocabulary: dict) -> None:
    by_id = {question["id"]: question for question in payload["questions"]}
    question = by_id["py-prac-0001"]
    card = question["languages"]["uk"]["card"]
    front_html = anki_build.render_front(vocabulary, question, card, question["languages"]["uk"]["title"])
    assert '<div class="prompt-body">' in front_html
    assert "<ul class=\"constraints\">" in front_html
    assert front_html.count("<li>") == card["constraints"].count("\n- ") + 1


def test_answer_label_present_only_for_the_three_documented_types(vocabulary: dict) -> None:
    assert anki_build.card_label(vocabulary, "coding") == "Кістяк розв'язання"
    assert anki_build.card_label(vocabulary, "system-design") == "Кістяк архітектури"
    assert anki_build.card_label(vocabulary, "behavioral") == "Каркас відповіді"
    assert anki_build.card_label(vocabulary, "concept") is None
    assert anki_build.card_label(vocabulary, "mechanism") is None


def test_back_strips_citation_tokens_and_keeps_warn_span(payload: dict, vocabulary: dict) -> None:
    by_id = {question["id"]: question for question in payload["questions"]}
    question = by_id["db-orm-0001"]
    card = question["languages"]["uk"]["card"]
    back_html = anki_build.render_back(vocabulary, question, card)
    assert "[^" not in back_html
    assert '<span class="warn">' in back_html


def test_sources_field_is_one_link_per_source(payload: dict) -> None:
    by_id = {question["id"]: question for question in payload["questions"]}
    sources = by_id["cpp-ptrref-0001"]["languages"]["uk"]["sources"]
    rendered = anki_build.render_sources_field(sources)
    assert rendered.count("<a href=") == len(sources)
    for source in sources:
        assert f'<a href="{source["url"]}">{source["title"]}</a>' in rendered


def test_build_package_end_to_end(tmp_path: Path) -> None:
    questions_path = tmp_path / "questions.json"
    import json

    payload_data = build_export(ROOT / "content")
    questions_path.write_text(json.dumps(payload_data), encoding="utf-8")
    out_path = tmp_path / "Interview QA - Full Library.apkg"

    count = anki_build.build_package(questions_path, ROOT / "meta" / "vocabulary.yml", out_path)
    assert count == 9
    assert out_path.is_file()
    assert out_path.stat().st_size > 0
