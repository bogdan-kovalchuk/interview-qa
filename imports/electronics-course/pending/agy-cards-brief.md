# Work order: complete the flashcards for one course section

You are finishing the Anki flashcards (questions) for ONE section of the Udemy course
"Crash Course Electronics and PCB Design". The section number is given in the prompt that
launched you. Work only on that section. Do not ask questions; follow this order exactly.

Working directory: `C:\Users\bogdan\Documents\Projects\learning\interview-qa` (IQA).
Course repository: `C:\Users\bogdan\Documents\Projects\learning\course-electronics-and-pcb-design` (COURSE).
Run Python as `python -B -X utf8`. Never write the em dash U+2014 or the arrows U+2190/U+2192.
Do not run any git command that writes. Do not edit files outside the paths named below.

## Sections

| Section | Transcripts (COURSE/subtitles/...) | Lectures | IQA section | ID prefix | Existing cards |
|---|---|---|---|---|---|
| 4 | `Section 4 - Electrical Engineering 101 - And Here Comes the Crash Course Part...Buckle Up!` | 32-80 | `electronics-course-ee101` | `emb-elee` | 263 (`emb-elee-0001`..`0263`) |
| 5 | `Section 5 - Introduction to Digital Logic Systems, Boolean Algebra, Timing Diagrams and TTL` | 81-88 | `electronics-course-digital-logic` | `emb-eldig` | none |
| 6 | `Section 6 - Taking Digital to the Next Level with Small, Medium, and Large Scale Integration` | 89-106 | `electronics-course-digital-integration` | `emb-elinteg` | none |
| 7 | `Section 7 - Printed Circuit Board Design and Technology with CircuitMaker` | 107-109 | `electronics-course-pcb-design` | `emb-elpcb` | 11 (not yet registered) |
| 8 | `Section 8 - Graduating to Design Engineer CircuitMaker Fundamentals and Real-World Projects` | 110-134 | `electronics-course-circuitmaker-projects` | `emb-elcmproj` | made by another agent (may be unregistered) |

Lecture notes, where they exist, are in the section's `helpers/sectionN_notes.md`,
`helpers/section4_full_notes.md` (lecture 66, the reference quality) and `section7/8_notes.md`.
The TRANSCRIPT of each lecture is the primary source; notes and the book
(`COURSE/books/Design_Game_Console_013.pdf`, read with `pymupdf`) only supplement.
Section 5 and 6 notes are short drafts: do not trust them over the transcript.

## Step 1 – read the contract

Read `IQA/meta/questions.md` sections 1-4, 6 (owner decks, including the electronics course
paragraph) and 7-9, then study 3 existing files in both languages under
`IQA/content/{uk,en}/embedded/electronics-course-ee101/`, including one `type: pitfall`
file and `ferrite-bead-passes-dc-blocks-noise.md`. New cards must match that structure exactly.

## Step 2 – decide the card set, lecture by lecture

For every lecture of the section: read the whole transcript, list its main ideas (what is
explained, demonstrated, measured, and the practical rules and typical mistakes), then:

- **Existing cards** (section 4, 7, 8): find the cards of the lecture (section 4:
  `IQA/imports/electronics-course/question-mapping.csv` maps `electronics-s04-NNNN` card ids
  to question ids, and each question's `udemy-electronics-course` source names its lecture).
  Check each against the transcript. Fix a factual error or a claim the lecture does not
  support by editing the Ukrainian `Short answer` (and the title if needed); keep the `id`
  and the file name. For every edited question: Ukrainian `content_revision` + 1 and
  `updated: 2026-09-27`; in the English file set `reconciled_with.uk` to the new Ukrainian
  revision. Do not rewrite correct cards for style.
- **Missing topics**: add a card for every main idea of the lecture that no card covers.
  Target: every main idea covered, usually 4-8 cards per hour-long lecture, 2-4 for a
  short one; a purely procedural lecture needs only its reusable engineering ideas.
- Cards must be self-contained single-concept questions with the circuit and numbers in
  the question when needed; never "in this video", "this circuit" without the circuit.
  Where the lecturer is wrong, the card states the correct fact.

## Step 3 – write new cards

Each new card is two files with the same ASCII kebab-case slug (from the English title,
3-7 significant words, unique in the section):
`IQA/content/uk/embedded/<iqa section>/<slug>.md` and `IQA/content/en/embedded/<iqa section>/<slug>.md`.

- `id`: next unused number of the section prefix (check `IQA/meta/id-registry.csv` and the
  existing files; never reuse a number).
- frontmatter exactly as the ee101 files: `title` = question, `description` = the same
  text, `track: embedded`, `section`, `level: junior`, `type: concept` (or `pitfall` with
  `Symptom`, `Why it happens`, `How to avoid` set to `TODO`), `tags: []`,
  `status: published`, `updated: 2026-09-27`, `content_revision: 1`, `reconciled_with`
  naming the other language with 1, `anki: export: true`.
- `sources` (identical set in both files; all seven keys; text in the file's language):
  1. `udemy-electronics-course` – copy title, url, kind and version from an ee101 file;
     `applicability` names the lecture number and says the card was written from the
     lecture transcript.
  2. The section-level authority, copied from an existing card of the same section; for
     sections 5-6 use `aac-digital` ("All About Circuits textbook, Volume IV: Digital",
     https://www.allaboutcircuits.com/textbook/digital/, kind book, version null); for
     sections 7-8 use `circuitmaker-docs` ("CircuitMaker documentation",
     https://www.altium.com/documentation/altium-circuitmaker, kind official, version null).
- Ukrainian `## Short answer`: 2-5 sentences (a boundary counts only before an upper-case
  letter, digit, `<`, `**`, `` ` `` or `[`), at most 90 words, no headings, links or URLs,
  at most one fenced code block, formulas as `<span class="formula">\(...\)</span>`, and
  ending with `[^udemy-electronics-course]`. `## Detailed explanation`: `TODO`. Last
  section `## Sources` with the single line `<!-- generated from frontmatter -->`.
- English file: translated title and description, every body section `TODO`.

## Step 4 – register and verify

1. Append one row per NEW id to `IQA/meta/id-registry.csv`:
   `id,2026-09-27,published,embedded/<iqa section>/<slug>.md,`. Also append the rows from
   `IQA/imports/electronics-course/pending/section-N-registry.csv` for your section if that
   file exists and its ids are not yet in the registry, then delete that pending file.
2. Update `IQA/tests/corpus.py`: `FILES` and `QUESTIONS` from the output of
   `python -m iqa validate` (run with `$env:PYTHONPATH='tools'`), `UK_CARDS` from
   `python -m iqa deck --language uk` (notes count), `EN_CARDS` unchanged.
3. `python -m iqa validate` must report 0 blocking failures and 0 warnings for your files.
   If another section's unregistered files cause failures, list them in the report and
   continue; do not touch them.
4. Run `python -m pytest -q -p no:cacheprovider` once and record the result.
One pass. No retry loops beyond fixing your own validation errors.

## Step 5 – report

Write `IQA/imports/electronics-course/pending/agy-report-section-N.md` (English):
per lecture – existing cards checked, cards fixed (id + what was wrong), cards added
(id + title); totals; validation and pytest results; anything you doubt or could not do.
