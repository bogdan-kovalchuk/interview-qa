# Electronics course decks: sections 1-4

Build: `python tools/build_course_anki.py` from the course root.
Verify: `python tools/verify_course_anki.py`.
Update test: `python tools/verify_anki_update.py` (requires the Python Anki library).

Import `Electronics_Sections_1-4.apkg` for the complete set, or import the four
`Section_N.apkg` files individually. Both options use the same notes and GUIDs;
they are alternative import routes, not different card sets.

The canonical editable content is in `Section_N_anki_cards.txt`. Keep each
`id::electronics-...` tag when correcting a card. The builder uses that ID to
preserve its GUID even when the question or answer changes. The generated
`note-identities.json` records those identities and content hashes.

Use the packaged update route for future question changes. Text imports use
Anki's text-matching rules and are not equivalent to a GUID-preserving package
update. Existing collections imported from earlier hand-cloned TSV note types
have unknown note-type IDs; this build does not modify or migrate those live
collections. The earlier five-field `S02_Test_Sample.apkg` is a separate demo
and is intentionally preserved unchanged.

The supported note type has Front and Back fields and uses
`electronics_basic_template.md`. Course section numbering is S01, S02, S03,
S04. Sources for newly added cards are recorded in `reports/` at course root.
