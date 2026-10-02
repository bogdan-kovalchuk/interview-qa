# Electronics course import

Source material of the owner's flashcards for the Udemy course
[Crash Course Electronics and PCB Design](https://www.udemy.com/course/crash-course-electronics-and-pcb-design/)
(Andre LaMothe). The cards were written while taking the course and moved here from the
`course-electronics-and-pcb-design` learning repository on 2026-09-27, which now keeps only the
short lecture notes.

This folder is evidence, not a build input. Nothing in `tools/iqa/` reads it.

## Where the cards live now

Course sections 2–8 are 828 questions in `content/{uk,en}/electronics/`:

| Course section | Section in this repository | ID prefix | Questions |
|---|---|---|---|
| 2 Introduction to Electronics | `electronics/introduction` | `emb-elintro` | 310 |
| 3 Advanced Circuit Analysis | `electronics/circuit-analysis` | `emb-elcirc` | 46 |
| 4 Electrical Engineering 101 | `electronics/ee101` | `emb-elee` | 263 |
| 5 Digital Logic Systems | `electronics/digital-logic` | `emb-eldig` | 38 |
| 6 Digital Integration | `electronics/digital-integration` | `emb-elinteg` | 73 |
| 7 PCB Design with CircuitMaker | `electronics/pcb-design` | `emb-elpcb` | 25 |
| 8 CircuitMaker Projects | `electronics/circuitmaker-projects` | `emb-elcmproj` | 73 |

`question-mapping.csv` maps every course card id (`electronics-sNN-NNNN`) to its question id and
path. Each question names the course and the lecture in its `udemy-electronics-course` source.

At initial import, the Ukrainian `Short answer` retained the card's Back. Only the form changed:

- `<code>` and `<strong>` became Markdown, `<strong class="warn">` became `<span class="warn">`;
  `<span class="formula">` with MathJax is kept, so formulas render on the Anki card;
- em dash became en dash and the arrows became `->` or an en dash (forbidden characters);
- 33 answers outside the 2-5 sentence limit were split or joined, adding only connectives
  such as «також» or «якщо»; no claim was added or removed;
- a citation token for the course source was appended.

On 2026-10-04, `emb-elintro-0001` through `emb-elintro-0020` were revised against specific
technical references and received complete short answers and detailed explanations in EN/UK.
Six inherited factual/procedural inaccuracies were corrected. Original TSV cards remain unchanged
as provenance. These 20 questions now ship English cards; the other 808 English files retain a
translated title and `TODO` bodies. The course source identifies provenance, not proof of the
revised technical claims.

## Not moved into `content/`

Course section 1 (6 cards, `cards/Section_1_anki_cards.txt`) is about the course itself - folder
layout, the Master Outline, the parts list - not about electronics, so it has no question.

## What the folders hold

| Path | Contents |
|---|---|
| `cards/` | The canonical TSV cards, card spec, note template, stable note identities and the old `.apkg` packages |
| `pipeline/` | The LLM subtitle/PDF -> Anki pipeline and its sample output |
| `tools/` | The course package builder, its verifiers and tests |
| `reports/` | Card provenance and package verification evidence |

The scripts are kept as they were. Their paths assume the course repository layout, so they do
not run from here without adjusting `BASE_DIR`.

## Anki collections

The questions have new GUIDs derived from their ids (`meta/anki.md`); the course GUIDs in
`cards/note-identities.json` are not reused. A collection that imported the old
`Electronics and PCB Design::*` decks keeps them as separate notes: delete those decks after
importing `Interview QA - Full Library.apkg`, or the cards are studied twice.
