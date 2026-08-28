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
        # The default is Ukrainian and its namespace is empty, so asking for it
        # explicitly must not move a single GUID that has already been issued.
        assert anki_build.guid_for(qid, "uk") == build_test_deck.guid_for(qid)


def test_english_notes_get_their_own_guid_namespace(payload: dict, vocabulary: dict) -> None:
    # meta/ANKI.md "GUID": a separate English deck uses `iqa:v1:en:{id}`. If the two
    # languages shared a GUID, importing both packages into one collection would make
    # each note overwrite the other - the one failure this project cannot recover from.
    model = anki_build.make_model()
    uk_notes = anki_build.build_notes(payload["questions"], vocabulary, model, "uk")
    en_notes = anki_build.build_notes(payload["questions"], vocabulary, model, "en")

    uk_guids = {note.guid for _deck, note in uk_notes}
    en_guids = {note.guid for _deck, note in en_notes}
    assert uk_guids and en_guids
    assert uk_guids.isdisjoint(en_guids)

    # And the two languages never share a deck either, so no deck holds both.
    uk_decks = {deck for deck, _note in uk_notes}
    en_decks = {deck for deck, _note in en_notes}
    assert uk_decks.isdisjoint(en_decks)
    assert all(deck.startswith("Interview QA::") for deck in uk_decks)
    assert all(deck.startswith("Interview QA (EN)::") for deck in en_decks)


def test_english_notes_ship_exactly_what_lifecycle_says_for_english(
    payload: dict, vocabulary: dict
) -> None:
    # A card ships on the Short answer written in *that* language, nothing else
    # (meta/ANKI.md "Коли картка з'являється в пакеті"). Most English bodies are
    # still TODO, so this number is far below the Ukrainian one - and that is the
    # honest state, not a bug.
    model = anki_build.make_model()
    notes = anki_build.build_notes(payload["questions"], vocabulary, model, "en")

    expected = {
        question["id"]
        for question in payload["questions"]
        if question["languages"]["en"]["lifecycle"]["card_in_apkg"]
    }
    assert len(notes) == len(expected)
    shipped = {note.fields[anki_build.FIELD_ORDER.index("QID")] for _deck, note in notes}
    assert shipped == expected

    reference_index = anki_build.FIELD_ORDER.index("Reference")
    assert all("/en/q/" in note.fields[reference_index] for _deck, note in notes)


def test_notes_ship_exactly_the_questions_lifecycle_says_should(payload: dict, vocabulary: dict) -> None:
    # 401 real questions: the 9 original pilots plus the 392 migrated in
    # PLAN.md step 4, of which 13 keep type `coding` with `anki.export: false`
    # (their Task/Solution/Tests were never authored - see the M4 report) and
    # so must not ship a card even though their Ukrainian Short answer reads
    # fine on its own.
    model = anki_build.make_model()
    notes = anki_build.build_notes(payload["questions"], vocabulary, model)

    expected_shipped = {
        question["id"]
        for question in payload["questions"]
        if question["languages"]["uk"]["lifecycle"]["card_in_apkg"]
    }
    assert len(notes) == len(expected_shipped) == 388

    shipped_ids = {note.fields[anki_build.FIELD_ORDER.index("QID")] for _deck, note in notes}
    assert shipped_ids == expected_shipped


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
    assert count == 388
    assert out_path.is_file()
    assert out_path.stat().st_size > 0
