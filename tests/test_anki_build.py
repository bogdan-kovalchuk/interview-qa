from __future__ import annotations

from pathlib import Path

import pytest

from corpus import EN_CARDS, UK_CARDS
from iqa import anki as anki_build
from iqa.export import build_export


ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def vocabulary() -> dict:
    import yaml

    return yaml.safe_load((ROOT / "meta" / "vocabulary.yml").read_text(encoding="utf-8")) or {}


@pytest.fixture(scope="module")
def payload() -> dict:
    return build_export(ROOT / "content")


def test_guid_formula_matches_frozen_vectors() -> None:
    vectors = {
        "py-asyncio-0007": ("n]E+uj-m)+", "D6lFSx(GBF"),
        "cpp-mem-0001": ("wpQwRgBDb/", "QG.5@&4Wg."),
        "bhv-team-0001": ("iZkvA-a5~j", "qzNLi3Nt`Y"),
        "emb-dtypes-0113": ("NF6SM#hdrt", "Jy@~xst2Q4"),
    }
    for qid, (uk_guid, en_guid) in vectors.items():
        assert anki_build.guid_for(qid) == uk_guid
        assert anki_build.guid_for(qid, "uk") == uk_guid
        assert anki_build.guid_for(qid, "en") == en_guid


def test_a_track_package_is_a_subset_with_the_same_guids(payload: dict, vocabulary: dict) -> None:
    # meta/anki.md: "перетин пакетів нешкідливий - та сама нотатка, той самий GUID,
    # та сама колода". A narrowed package must therefore change nothing except
    # which notes are present, so importing it alongside the full library cannot
    # duplicate a note or move one to another deck.
    model = anki_build.make_model()
    everything = anki_build.build_notes(payload["questions"], vocabulary, model)
    python_only = anki_build.build_notes(payload["questions"], vocabulary, model, "uk", "python")

    assert 0 < len(python_only) < len(everything)

    by_guid = {note.guid: (deck, note.fields) for deck, note in everything}
    for deck, note in python_only:
        assert note.guid in by_guid
        assert (deck, note.fields) == by_guid[note.guid]

    qid_index = anki_build.FIELD_ORDER.index("QID")
    assert all(note.fields[qid_index].startswith("py-") for _deck, note in python_only)


def test_english_notes_get_their_own_guid_namespace(payload: dict, vocabulary: dict) -> None:
    # meta/anki.md "GUID": a separate English deck uses `iqa:v1:en:{id}`. If the two
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


def test_english_notes_ship_exactly_the_written_english_short_answers(
    payload: dict, vocabulary: dict
) -> None:
    # A card ships on the Short answer written in *that* language, nothing else
    # (meta/anki.md "Коли картка з'являється в пакеті"). Most English bodies are
    # still TODO, so this number is far below the Ukrainian one - and that is the
    # honest state, not a bug.
    model = anki_build.make_model()
    notes = anki_build.build_notes(payload["questions"], vocabulary, model, "en")

    expected = {
        question["id"]
        for question in payload["questions"]
        if question["languages"]["en"]["card"]["short_answer"] is not None
    }
    assert len(notes) == len(expected) == EN_CARDS
    shipped = {note.fields[anki_build.FIELD_ORDER.index("QID")] for _deck, note in notes}
    assert shipped == expected

    reference_index = anki_build.FIELD_ORDER.index("Reference")
    assert all("/en/q/" in note.fields[reference_index] for _deck, note in notes)


def test_ukrainian_notes_ship_exactly_the_written_short_answers(
    payload: dict, vocabulary: dict
) -> None:
    model = anki_build.make_model()
    notes = anki_build.build_notes(payload["questions"], vocabulary, model)

    expected_shipped = {
        question["id"]
        for question in payload["questions"]
        if question["languages"]["uk"]["card"]["short_answer"] is not None
    }
    assert len(notes) == len(expected_shipped) == UK_CARDS

    shipped_ids = {note.fields[anki_build.FIELD_ORDER.index("QID")] for _deck, note in notes}
    assert shipped_ids == expected_shipped


def test_front_label_comes_from_vocabulary_not_from_the_qid_prefix(payload: dict, vocabulary: dict) -> None:
    # The trap meta/plan.md calls out: the track label must not be decoded from the
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
    # meta/plan.md's named trap: the visible track label used to come from splitting
    # the QID prefix in a <script> block. Fixed by baking the label into the
    # generated Front field instead; the templates must carry neither the
    # QID field reference nor any prefix-splitting logic.
    for name in ("front.html", "back.html"):
        text = (ROOT / "anki" / "notetype" / name).read_text(encoding="utf-8")
        assert "{{text:QID}}" not in text
        assert ".split(" not in text
        assert "<script>" not in text


def test_question_code_goes_to_the_front_not_the_back(payload: dict, vocabulary: dict) -> None:
    question = next(
        question
        for question in payload["questions"]
        if question["languages"]["uk"]["card"]["question_code"] is not None
    )
    card = question["languages"]["uk"]["card"]
    front_html = anki_build.render_front(vocabulary, question, card, question["languages"]["uk"]["title"])
    assert '<div class="prompt-body"><pre class="code-block">' in front_html
    assert '<pre class="code-block">' not in anki_build.render_back(card)


def test_tags_carry_only_the_topic_and_the_qid(payload: dict) -> None:
    question = payload["questions"][0]
    assert anki_build.build_tags(question) == [
        f"topic::{question['track']}::{question['section']}",
        f"qid::{question['id']}",
    ]


def test_back_strips_citation_tokens_and_keeps_warn_span(payload: dict, vocabulary: dict) -> None:
    by_id = {question["id"]: question for question in payload["questions"]}
    question = by_id["emb-align-0004"]
    card = question["languages"]["uk"]["card"]
    back_html = anki_build.render_back(card)
    assert "[^" not in back_html
    assert '<span class="warn">' in back_html


def test_sources_field_is_one_link_per_source(payload: dict) -> None:
    by_id = {question["id"]: question for question in payload["questions"]}
    sources = by_id["py-async-0012"]["languages"]["uk"]["sources"]
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
    assert count == UK_CARDS
    assert out_path.is_file()
    assert out_path.stat().st_size > 0
