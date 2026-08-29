"""Build the real Interview QA `.apkg` package from `dist/export/questions.json`.

Reads only `dist/export/questions.json` (never `content/` - only `tools/` reads
that, per AGENTS.md) and the frozen note type in `packaging/anki/notetype/`.

Invariants this file must never violate (meta/ANKI.md, meta/DECISIONS.md #7-8):

- the note type is read from `packaging/anki/notetype/`, not copied here;
- `model_id`, field ids/ords and template ids come from `fingerprint.json` and
  are never invented here;
- the GUID formula (`guid_for`) is exactly the one in
  `packaging/anki/test-deck/build_test_deck.py` - a second definition of the
  same frozen formula, not a second formula;
- fields are written by name (`FIELD_ORDER` from the fingerprint), never by a
  hardcoded position;
- a card ships only when `tools/iqa/lifecycle.py` says `card_in_apkg` for the
  language being built - nothing else decides that, and no other language is
  ever substituted into Back (meta/ANKI.md: a mixed-language deck is worse than
  a smaller one). One package holds one language; the Ukrainian one is the
  default and keeps the GUID namespace it was released with.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
from pathlib import Path
import re
from typing import Any

import genanki
import yaml

ROOT = Path(__file__).resolve().parents[2]
NOTETYPE = ROOT / "packaging" / "anki" / "notetype"
FONTS = ROOT / "packaging" / "anki" / "fonts"
FINGERPRINT = json.loads((NOTETYPE / "fingerprint.json").read_text(encoding="utf-8"))
MODEL_ID = FINGERPRINT["model_id"]
FIELD_ORDER = [field["name"] for field in sorted(FINGERPRINT["fields"], key=lambda f: f["ord"])]

SITE_ORIGIN = "https://bogdan-kovalchuk.github.io"
DEFAULT_CARD_LANGUAGE = "uk"
GUID_SALT = "iqa:v1:"

# meta/ANKI.md "GUID": `iqa:v1:` is fixed forever for the Ukrainian deck, and a separate
# English deck gets its own namespace `iqa:v1:en:` so the two never collide in one
# collection. The Ukrainian namespace is empty here on purpose - adding a segment to it
# would rewrite every existing GUID, which is the one change that loses review progress.
GUID_NAMESPACE = {"uk": "", "en": "en:"}

# Separate deck trees per language. meta/ANKI.md: a deck holds one language, because
# "змішана мова в колоді гірша за меншу колоду"; the deck names stay English in both,
# so the trees sort next to each other in the profile.
DECK_ROOT = {"uk": "Interview QA", "en": "Interview QA (EN)"}
BASE91 = (
    "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    "!#$%&()*+,-./:;<=>?@[]^_`{|}~"
)

CITATION_RE = re.compile(r"\[\^[a-z0-9]+(?:-[a-z0-9]+)*\]")
CODE_FENCE_RE = re.compile(r"```[^\n]*\n(.*?)```", re.S)
INLINE_CODE_RE = re.compile(r"`([^`\n]+)`")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*", re.S)
LIST_ITEM_RE = re.compile(r"(?m)^-[ \t]+(.+)$")


def guid_for(qid: str, language: str = DEFAULT_CARD_LANGUAGE) -> str:
    """Deterministic note GUID. Never change this function.

    Identical formula to packaging/anki/test-deck/build_test_deck.py:guid_for -
    meta/ANKI.md fixes this once; this is a second reading of it, not a second
    definition. `language` selects the namespace and defaults to Ukrainian, whose
    namespace is empty, so every GUID already issued keeps its exact value.
    """
    namespaced = GUID_SALT + GUID_NAMESPACE[language] + qid
    digest = hashlib.sha256(namespaced.encode("utf-8")).digest()[:8]
    n = int.from_bytes(digest, "big")
    out = []
    while n:
        n, rem = divmod(n, len(BASE91))
        out.append(BASE91[rem])
    return "".join(reversed(out)) or BASE91[0]


def deterministic_id(name: str, *, low: int, high: int) -> int:
    """A stable integer id derived from a name, for genanki deck/model ids.

    genanki decks need an id genanki hasn't already used; deriving it from the
    deck name (rather than an enumeration counter) means the id for
    "Interview QA::Python::Asyncio" is the same across rebuilds regardless of
    what other decks exist in this run.
    """
    digest = hashlib.sha256(name.encode("utf-8")).hexdigest()
    return low + (int(digest[:16], 16) % (high - low))


def render_inline(text: str) -> str:
    """Bold -> <strong>, inline code -> <code>, citation tokens stripped.

    Shared by every Anki field that is not the Short answer (title, Task,
    Constraints, Scale prompt): none of those get the leading-bold `.key`
    treatment that meta/QUESTIONS.md section 7 reserves for Short answer.
    """
    text = CITATION_RE.sub("", text)
    text = BOLD_RE.sub(lambda m: f"<strong>{m.group(1)}</strong>", text)
    text = INLINE_CODE_RE.sub(lambda m: f"<code>{html.escape(m.group(1), quote=False)}</code>", text)
    return text


def render_paragraphs(text: str, *, key_lead: bool) -> str:
    """Render a Markdown answer body into the restricted HTML meta/QUESTIONS.md

    section 7 allows: paragraphs, at most one fenced code block, inline code,
    bold (the leading bold becomes `<span class="key">` only when `key_lead`
    is set - i.e. only for Short answer), and raw inline HTML such as
    `<span class="warn">` passed through untouched. Citation tokens are
    stripped entirely - the source stays in the hidden `Sources` field.
    """
    stripped = CITATION_RE.sub("", text)

    code_blocks: list[str] = []

    def stash_code(match: re.Match[str]) -> str:
        code_blocks.append(match.group(1).strip("\n"))
        return f"\x00CODEBLOCK{len(code_blocks) - 1}\x00"

    stripped = CODE_FENCE_RE.sub(stash_code, stripped)

    rendered_paragraphs: list[str] = []
    for raw_paragraph in re.split(r"\n\s*\n", stripped.strip()):
        paragraph = raw_paragraph.strip()
        if not paragraph:
            continue
        placeholder_match = re.fullmatch(r"\x00CODEBLOCK(\d+)\x00", paragraph)
        if placeholder_match:
            code = code_blocks[int(placeholder_match.group(1))]
            escaped_code = html.escape(code, quote=False)
            rendered_paragraphs.append(f'<pre class="code-block"><code>{escaped_code}</code></pre>')
            continue

        paragraph = re.sub(r"\s*\n\s*", " ", paragraph)
        if key_lead and paragraph.startswith("**"):
            paragraph = BOLD_RE.sub(
                lambda m: f'<span class="key">{m.group(1)}</span>', paragraph, count=1
            )
        paragraph = BOLD_RE.sub(lambda m: f"<strong>{m.group(1)}</strong>", paragraph)
        paragraph = INLINE_CODE_RE.sub(
            lambda m: f"<code>{html.escape(m.group(1), quote=False)}</code>", paragraph
        )
        rendered_paragraphs.append(f"<p>{paragraph}</p>")

    return "\n".join(rendered_paragraphs)


def render_constraints_list(text: str) -> str:
    """Compact-rendered Constraints: a single-level list, per meta/ANKI.md.

    "Compact rendering changes only the HTML: it removes extra margins and
    shows Constraints as a single-level list. The exporter does not shorten or
    paraphrase authored constraints." - so every `- ` line becomes one <li>,
    inline-rendered, in the original order, nothing dropped or reworded.
    """
    items = LIST_ITEM_RE.findall(text)
    rendered_items = "".join(f"<li>{render_inline(item.strip())}</li>" for item in items)
    return f'<ul class="constraints">{rendered_items}</ul>'


def render_sources_field(sources: list[dict[str, Any]]) -> str:
    """One line per source: title as link text, url as href (meta/ANKI.md)."""
    return "<br>".join(f'<a href="{source["url"]}">{source["title"]}</a>' for source in sources)


def track_label(vocabulary: dict[str, Any], track: str, language: str = DEFAULT_CARD_LANGUAGE) -> str:
    labels = (vocabulary.get("track_labels") or {}).get(track)
    if not isinstance(labels, dict) or language not in labels:
        raise ValueError(f"no {language} label for track `{track}` in meta/vocabulary.yml")
    return labels[language]


def track_label_en(vocabulary: dict[str, Any], track: str) -> str:
    labels = (vocabulary.get("track_labels") or {}).get(track)
    if not isinstance(labels, dict) or "en" not in labels:
        raise ValueError(f"no en label for track `{track}` in meta/vocabulary.yml")
    return labels["en"]


def section_nav_label_en(vocabulary: dict[str, Any], track: str, section: str) -> str:
    key = f"{track}/{section}"
    labels = (vocabulary.get("section_labels_nav") or {}).get(key)
    if not isinstance(labels, dict) or "en" not in labels:
        raise ValueError(f"no en navigation label for section `{key}` in meta/vocabulary.yml")
    return labels["en"]


def card_label(
    vocabulary: dict[str, Any], question_type: str, language: str = DEFAULT_CARD_LANGUAGE
) -> str | None:
    """The visible label above Back for types whose Short answer has special

    semantics (meta/ANKI.md "Що в яких полях"). Types with no entry here get
    no label, matching the ANKI.md table's "solid" (no label) row.
    """
    key = {
        "coding": "Solution outline",
        "system-design": "Architecture summary",
        "behavioral": "Answer framework",
    }.get(question_type)
    if key is None:
        return None
    labels = (vocabulary.get("card_labels") or {}).get(key)
    if not isinstance(labels, dict) or language not in labels:
        raise ValueError(f"no {language} card label for `{key}` in meta/vocabulary.yml")
    return labels[language]


def deck_name(
    vocabulary: dict[str, Any], track: str, section: str, language: str = DEFAULT_CARD_LANGUAGE
) -> str:
    """Deck names are English Title Case with `::`, even for Ukrainian cards

    (meta/ANKI.md: "predictably sorts next to others in the profile"). Only the root
    segment carries the language, so the two trees sort next to each other and a deck
    still holds exactly one language.
    """
    return (
        f"{DECK_ROOT[language]}"
        f"::{track_label_en(vocabulary, track)}"
        f"::{section_nav_label_en(vocabulary, track, section)}"
    )


def build_tags(question: dict[str, Any]) -> list[str]:
    tags = [
        f"topic::{question['track']}::{question['section']}",
        f"type::{question['type']}",
        f"level::{question['level']}",
        f"qid::{question['id']}",
    ]
    tags.extend(f"framework::{framework}" for framework in question["frameworks"])
    tags.extend(f"tag::{tag}" for tag in question["tags"])
    # role:: tags are omitted: they are derived from programs/*.yml membership,
    # which does not exist yet (PLAN.md step 7). Nothing to derive from means
    # no role:: tag - not a placeholder value.
    return tags


def render_front(
    vocabulary: dict[str, Any],
    question: dict[str, Any],
    card: dict[str, Any],
    title: str,
    language: str = DEFAULT_CARD_LANGUAGE,
) -> str:
    label = track_label(vocabulary, question["track"], language)
    parts = [f'<div class="deck-label">{label}</div>', render_inline(title)]
    if question["type"] == "coding":
        task_html = render_paragraphs(card["task"], key_lead=False)
        constraints_html = render_constraints_list(card["constraints"])
        parts.append(f'<div class="prompt-body">{task_html}{constraints_html}</div>')
    elif question["type"] == "system-design":
        scale_html = render_paragraphs(card["scale_prompt"], key_lead=False)
        parts.append(f'<div class="prompt-body">{scale_html}</div>')
    return "".join(parts)


def render_back(
    vocabulary: dict[str, Any],
    question: dict[str, Any],
    card: dict[str, Any],
    language: str = DEFAULT_CARD_LANGUAGE,
) -> str:
    label = card_label(vocabulary, question["type"], language)
    answer_html = render_paragraphs(card["short_answer"], key_lead=True)
    if label is None:
        return answer_html
    return f'<div class="answer-label">{label}</div>{answer_html}'


def font_face_css() -> str:
    faces = json.loads((FONTS / "fonts.json").read_text(encoding="utf-8"))
    blocks = []
    for face in faces:
        blocks.append(
            "@font-face {\n"
            f'  font-family: "{face["family"]}";\n'
            f'  src: url("{face["file"]}") format("woff2");\n'
            f'  font-weight: {face["weight"]};\n'
            "  font-style: normal;\n"
            "  font-display: swap;\n"
            f'  unicode-range: {face["unicode_range"]};\n'
            "}"
        )
    return "\n".join(blocks)


def make_model() -> genanki.Model:
    read = lambda name: (NOTETYPE / name).read_text(encoding="utf-8")
    return genanki.Model(
        MODEL_ID,
        FINGERPRINT["model_name"],
        fields=[dict(field) for field in FINGERPRINT["fields"]],
        templates=[
            dict(FINGERPRINT["templates"][0], qfmt=read("front.html"), afmt=read("back.html"))
        ],
        css=font_face_css() + "\n" + read("card.css"),
    )


def note_fields(values: dict[str, str]) -> list[str]:
    missing = set(FIELD_ORDER) - set(values)
    if missing:
        raise ValueError(f"missing field value(s): {sorted(missing)}")
    return [values[name] for name in FIELD_ORDER]


def build_notes(
    questions: list[dict[str, Any]],
    vocabulary: dict[str, Any],
    model: genanki.Model,
    language: str = DEFAULT_CARD_LANGUAGE,
    track: str | None = None,
) -> list[tuple[str, genanki.Note]]:
    """Return (deck_name, note) pairs for every question whose card ships in `language`.

    `track` narrows the package to one track. It selects a subset of the same
    notes - same ids, same GUIDs, same decks - so a narrowed package and the full
    library import into one collection without duplicating anything
    (meta/ANKI.md: "перетин пакетів нешкідливий").
    """
    notes: list[tuple[str, genanki.Note]] = []
    for question in questions:
        if track is not None and question["track"] != track:
            continue
        entry = question["languages"].get(language)
        if entry is None:
            continue
        if not entry["lifecycle"]["card_in_apkg"]:
            continue
        card = entry["card"]
        if card["short_answer"] is None:
            # lifecycle says it ships but the body says otherwise: a contract
            # invariant broke upstream. Fail loudly rather than ship an empty card.
            raise ValueError(f"{question['id']}: card_in_apkg is true but short_answer is empty")

        reference = f"{SITE_ORIGIN}{entry['resolver_path']}"
        fields = note_fields(
            {
                "Front": render_front(vocabulary, question, card, entry["title"], language),
                "Back": render_back(vocabulary, question, card, language),
                "Reference": reference,
                "Sources": render_sources_field(entry["sources"]),
                "QID": question["id"],
            }
        )
        note = genanki.Note(
            model=model,
            fields=fields,
            tags=build_tags(question),
            guid=guid_for(question["id"], language),
        )
        notes.append(
            (deck_name(vocabulary, question["track"], question["section"], language), note)
        )
    return notes


def build_package(
    questions_path: Path,
    vocabulary_path: Path,
    out_path: Path,
    language: str = DEFAULT_CARD_LANGUAGE,
    track: str | None = None,
) -> int:
    payload = json.loads(questions_path.read_text(encoding="utf-8"))
    vocabulary = yaml.safe_load(vocabulary_path.read_text(encoding="utf-8")) or {}

    # Exactly one shared Model instance for the whole package: one model_id, one
    # template, per the frozen fingerprint.
    model = make_model()

    notes = build_notes(payload["questions"], vocabulary, model, language, track)

    decks: dict[str, genanki.Deck] = {}
    for name, note in notes:
        if name not in decks:
            decks[name] = genanki.Deck(deterministic_id(name, low=1_600_000_100_000, high=1_700_000_000_000), name)
        decks[name].add_note(note)

    package = genanki.Package(list(decks.values()))
    package.media_files = [str(path) for path in sorted(FONTS.glob("_iqa-*.woff2"))]
    out_path.parent.mkdir(parents=True, exist_ok=True)
    package.write_to_file(str(out_path))
    return len(notes)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--questions", type=Path, default=ROOT / "dist" / "export" / "questions.json")
    parser.add_argument("--vocabulary", type=Path, default=ROOT / "meta" / "vocabulary.yml")
    parser.add_argument(
        "--language",
        choices=sorted(GUID_NAMESPACE),
        default=DEFAULT_CARD_LANGUAGE,
        help="which language's cards to package; one package holds exactly one language",
    )
    parser.add_argument(
        "--track",
        default=None,
        help="package only this track (e.g. `python`); default is every track",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help="output .apkg; defaults to the Full Library name for the chosen language",
    )
    args = parser.parse_args()

    scope = "Full Library" if args.track is None else args.track.replace("-", " ").title()
    out = args.out or (
        ROOT / "packaging" / "anki" / "dist" / f"{DECK_ROOT[args.language]} - {scope}.apkg"
    )
    count = build_package(args.questions, args.vocabulary, out, args.language, args.track)
    print(f"{out.name}: {count} notes")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
