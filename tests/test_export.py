from __future__ import annotations

from pathlib import Path

from corpus import QUESTIONS
from iqa.export import build_export, canonical_path, resolver_path
from iqa.lifecycle import lifecycle_for
from iqa.model import Language, parse_question_file


ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"


def test_export_covers_every_question_in_both_languages() -> None:
    payload = build_export(CONTENT)
    assert payload["base"] == "/interview-qa"
    assert len(payload["questions"]) == QUESTIONS
    for question in payload["questions"]:
        assert set(question["languages"]) == {"en", "uk"}


def test_cross_references_are_qid_objects_never_urls() -> None:
    payload = build_export(CONTENT)
    by_id = {question["id"]: question for question in payload["questions"]}
    cpp_tooling = by_id["cpp-tooling-0001"]
    assert cpp_tooling["see_also"] == [{"qid": "cpp-ptrref-0001"}]
    for question in payload["questions"]:
        for ref in (*question["see_also"], *question["prerequisites"]):
            assert set(ref) == {"qid"}
            assert not ref["qid"].startswith(("http://", "https://", "/"))


def test_paths_match_the_site_url_contract() -> None:
    payload = build_export(CONTENT)
    by_id = {question["id"]: question for question in payload["questions"]}
    py_gil = by_id["py-gil-0001"]["languages"]["uk"]
    assert py_gil["path"] == (
        "/interview-qa/uk/q/py-gil-0001/free-threaded-build-removes-the-gil-not-contention/"
    )
    assert py_gil["resolver_path"] == "/interview-qa/uk/q/py-gil-0001/"


def test_lifecycle_in_export_matches_lifecycle_module() -> None:
    payload = build_export(CONTENT)
    by_id = {question["id"]: question for question in payload["questions"]}

    question = parse_question_file(
        CONTENT / "en" / "python" / "concurrency-and-gil" / "free-threaded-build-removes-the-gil-not-contention.md",
        content_root=CONTENT,
    )
    decision = lifecycle_for(question, Language.EN)
    exported = by_id["py-gil-0001"]["languages"]["en"]["lifecycle"]
    assert exported["production_page"] == decision.production_page.value
    assert exported["card_in_apkg"] == decision.card_in_apkg
    assert exported["reference_filled"] == decision.reference_filled
    assert exported["card_blocked_reason"] == decision.card_blocked_reason


def test_card_body_only_carries_type_relevant_sections() -> None:
    payload = build_export(CONTENT)
    by_id = {question["id"]: question for question in payload["questions"]}

    coding = by_id["py-prac-0001"]
    assert coding["type"] == "coding"
    coding_card = coding["languages"]["en"]["card"]
    assert coding_card["short_answer"]
    assert coding_card["task"]
    assert coding_card["constraints"]
    assert coding_card["scale_prompt"] is None

    system_design = by_id["sd-msgq-0001"]
    assert system_design["type"] == "system-design"
    sd_card = system_design["languages"]["en"]["card"]
    assert sd_card["scale_prompt"]
    assert sd_card["task"] is None
    assert sd_card["constraints"] is None

    concept = by_id["cs-cmplx-0001"]
    concept_card = concept["languages"]["en"]["card"]
    assert concept_card["task"] is None
    assert concept_card["constraints"] is None
    assert concept_card["scale_prompt"] is None
    assert concept_card["short_answer"]


def test_helpers_agree_on_url_shape() -> None:
    assert canonical_path("/interview-qa", Language.UK, "py-gil-0001", "slug") == (
        "/interview-qa/uk/q/py-gil-0001/slug/"
    )
    assert resolver_path("/interview-qa", Language.UK, "py-gil-0001") == "/interview-qa/uk/q/py-gil-0001/"
