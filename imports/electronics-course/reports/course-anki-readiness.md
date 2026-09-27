# Course Anki set: final state before the move

Excerpt of `reports/sections-1-4-readiness.md` from the course repository as of 2026-09-27,
before the cards moved into `content/`. Paths refer to the course repository layout.

## Anki set

- Canonical sources: `anki cards/Section_1..4_anki_cards.txt`, 621 notes, Electronics
  Basic two-field note type (model 2026092701). Every note carries a stable
  `id::electronics-sNN-NNNN` tag; GUIDs derive from it (`note-identities.json`).
- Packages: `Section_1.apkg`-`Section_4.apkg` and `Electronics_Sections_1-4.apkg`
  (alternative import routes for the same notes and GUIDs).
- Section 4: 259 cards covering all 49 lectures (3-8 per lecture; Concept 92,
  Trap 73, Formula 69, Definition 25), written from the lecture documents. Where a
  document contains an error, the card uses the correct form (see Remaining notes).
- Provenance: 269 new-card entries in `new-card-provenance.json` (lecture 01: 6,
  lecture 02: 4, lectures 32-80: 259) with the exact question and source document.
- Rendering fix: four legacy cards contained a raw `<` (two inside MathJax
  formulas in lectures 22 and 23, where the browser would have parsed it as a tag
  and dropped the formula). They are now `&lt;`; wording and identities unchanged.
- Update test: the combined package was imported into a temporary collection, a
  card was given review history, one Back field was changed in copied sources and
  the rebuilt package re-imported. Note IDs, GUIDs and the review schedule were
  preserved, the Back field updated, no duplicates (621 notes).

## Tool fixes in this pass

- `tools/verify_course_anki.py`: closes each SQLite connection explicitly (the
  `with` block only committed, so Windows could not delete the temporary
  database); now also fails on any unescaped `<` in a card field.
- `tools/verify_anki_update.py`: initialises Anki's i18n layer (`set_lang`), which
  the standalone package importer needs.

## Anki checks executed then

| Check | Result |
|---|---|
| `python -B -X utf8 tools/build_course_anki.py` | exit 0; 621 notes (6/310/46/259), no genanki HTML warnings |
| `python -B -X utf8 tools/verify_course_anki.py` | `passed: true`; 5 packages; 80 lectures covered; 621 GUIDs |
| `python -B -X utf8 tools/verify_anki_update.py` | `passed: true`; IDs, GUIDs and schedule preserved |
| Card format (`verify_cards.py`, anki-card-generation skill) | 621 cards, 0 malformed lines |
| Pipeline CLIs `--help` from outside the course root | 5 of 5 exit 0 |

## Note on legacy collections

1. Learners who earlier imported the legacy section 2/3 TSV files through a
   hand-cloned note type have notes with unknown GUIDs. Importing the new packages
   into such a collection adds new notes instead of updating the old ones; move or
   delete the old notes first. This build does not modify live collections.
