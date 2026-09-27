# Course card specification

Audience: learners following the existing first four electronics sections.
Keep the existing Ukrainian learning language and the Electronics Basic
two-field template in `electronics_basic_template.md`.

Canonical source: `Section_N_anki_cards.txt`, UTF-8, five import directives,
then Front, Back, Tags separated by exactly two real tabs. Escape HTML, keep
each card on one line, and use `<br>` for intentional line breaks.

Route course sections 1-4 to `Electronics and PCB Design::SNN: <section title>`.
Every card needs a `Лекція_NN` tag. Stable identity tags `id::electronics-...`
are assigned by the course package builder and must be preserved during edits.
Do not change existing questions or answers merely to normalize wording.

New cards must be self-contained, focus on one concept, and have substantive
answers grounded in the existing lecture documents/transcripts. No placeholders,
invented measurements, or standalone questions referring to an unspecified
"example", "this circuit", or "the video". Include the circuit/numbers when needed.
Use Concept, Definition, Formula, or Trap tags for new cards.

Coverage follows source learning objectives, not a fixed card count. Section 1
focuses on setup and learning workflow. Section 4 must cover every lecture 32-80,
using the three-to-five existing self-assessment concepts per short note as the
minimum, splitting coupled questions or adding a key concept where necessary.
Review for conceptual duplicates; preserve intentional review context explicitly.

Record provenance for new cards in `reports/new-card-provenance.json` with
lecture number, question, and the relative source document path.

The supported final package builder is `tools/build_course_anki.py`. It creates
four section packages and one combined package using the same persistent GUIDs
and the Electronics Basic field schema. The earlier five-field LLM experiment
and `S02_Test_Sample.apkg` are separate artifacts, not sources for this package.
