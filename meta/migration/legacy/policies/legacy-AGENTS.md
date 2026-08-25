# Python Interview Questions - operating guide

This file is the sole project guide. The repository intentionally contains no
README files.

## Purpose and scope

Build and maintain one high-quality Anki package for general Python interviews.
Python is the primary subject. Algorithms/data structures, databases/SQL, and
Git/CI/CD/SDLC are brief overview topics only. Web frameworks, APIs, frontend,
cloud platforms, and detailed system design are out of scope.

Explanations are Ukrainian. Python code, identifiers, APIs, and standard terms
remain English. The baseline is stable Python 3.14. Qualify other versions and
separate language guarantees from CPython-specific implementation details,
including the GIL-enabled and free-threaded builds.

## Repository layout

```text
cards/
  01_...txt through 23_...txt    The 23 reviewed TSV source decks.
  Python Interview Questions.apkg  Current user-importable production package.
authoring/
  collection/                   Persistent Anki build state and media. Preserve it.
  manifest.json                 Machine-readable deck and topic configuration.
  CARD_SPEC.md                  TSV, HTML, tags, and card-quality rules.
  TAXONOMY.md                   The 23-topic curriculum.
  SOURCE_POLICY.md              Evidence and citation rules.
  QUALITY_GATES.md              Promotion and release gates.
  FRONT_PROVENANCE.md           Stable Front provenance rules.
  NOTE_TYPE_TEMPLATE.md         Anki Front/Back/CSS template.
  templates/                    Topic-brief template.
  prompts/                      Generation, review, and coverage-audit prompts.
  research/                     Design and package-update decisions.
  examples/                     Non-production example TSV files.
sources/
  official/                     Local indexes or extracts of official sources.
  community/                    Candidate-question sources only.
  notes/                        One source and objective brief per topic.
scripts/                        Builders, validators, smoke tests, and unit tests.
tracking/                       Coverage, reviews, provenance, and smoke records.
  reviews/                      Review reports and PROJECT_REVIEW_PROMPT.md.
requirements/                   Pinned build dependencies.
```

The 23 TSV files in `cards/` and `authoring/NOTE_TYPE_TEMPLATE.md` are the
canonical package content. `authoring/collection/Python Interview Questions.anki2` preserves
Anki-assigned note GUIDs. Do not recreate it for an ordinary content correction.
The complete package is rebuilt after a correction; importing it into a learner
profile updates matching notes while retaining the learner's scheduling.

## Current release contract

- Package: `cards/Python Interview Questions.apkg`.
- Root deck: `Python Interview Questions`.
- Child decks: 23, declared by `authoring/manifest.json`.
- Note type: `Python Interview Basic` with `Front` and `Back` fields.
- Build dependency: `requirements/anki-build.txt` (`anki==26.8.1`).
- Package export excludes scheduling data.
- Internal tags identify and update notes; the template does not display them.

## Card lifecycle

1. Read `authoring/CARD_SPEC.md`, `authoring/TAXONOMY.md`, and
   `authoring/SOURCE_POLICY.md` before editing cards.
2. Read the topic brief in `sources/notes/` and every source it names. Create or
   update that brief from `authoring/templates/TOPIC_BRIEF_TEMPLATE.md` if needed.
3. Map sources to learning objectives before writing. Community material is only
   a candidate-question locator; ground technical claims in authoritative sources.
4. Edit one topic TSV directly in `cards/`. Keep one physical line per card and
   exactly two TAB characters. One card tests one primary idea.
5. Run `python scripts/verify_cards.py cards/<topic>.txt`, perform an
   independent review using `authoring/prompts/REVIEW_CARDS.md`, then verify again.
6. Update `tracking/coverage.csv`, record the review in `tracking/reviews/`,
   and rebuild the package only after every gate in `authoring/QUALITY_GATES.md`
   passes.

Use `tracking/reviews/PROJECT_REVIEW_PROMPT.md` for a full independent project
review. Store its resulting review reports in the same directory.

Every TSV in `cards/` is package source and therefore must have a completed
Back and no `review::NeedsFactCheck`. Do not keep duplicate draft copies in the
repository. Record rejected proposals in `tracking/reviews/` with a reason such
as `duplicate`, `trivia`, `ambiguous`, `outdated`, `incorrect`, or
`out_of_scope`.

For each official source index or extract, record its URL, version, access date,
and licence or terms. Community material may help locate a useful question but
must not supply an accepted technical claim without an official check. Keep one
`<NN_topic_slug>.md` topic brief in `sources/notes/` using the template above.

## Build and verify

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements\anki-build.txt
.\.venv\Scripts\python.exe scripts\verify_cards.py cards
.\.venv\Scripts\python.exe scripts\verify_front_sources.py
.\.venv\Scripts\python.exe scripts\verify_project.py
.\.venv\Scripts\python.exe scripts\build_apkg.py
.\.venv\Scripts\python.exe scripts\verify_apkg.py
.\.venv\Scripts\python.exe scripts\anki_update_smoke.py
.\.venv\Scripts\python.exe -m unittest discover -s scripts\tests -v
```

Never directly edit the `.apkg` or `.anki2` with SQLite. The builder uses the
Anki API. A missing accepted card is a migration event, not an implicit deletion
from the persistent collection. Refer to
`authoring/research/apkg-generation-and-update-strategy.md` for migration and
learner-update semantics.
Card-design rationale is retained in `authoring/research/anki_card_design.md`.

## Non-negotiable quality rules

- Do not pad a topic to reach a card count.
- Do not copy source wording at length; preserve facts and rewrite concisely.
- Every accepted card must be factual, atomic, unambiguous, interview-relevant,
  tagged, UTF-8 encoded, source-grounded, and semantically deduplicated.
- Use `topic::`, `type::`, `level::`, and `scope::` tags. They are internal
  metadata and must not be shown to learners.
- Include a source link in each card's HTML source block. It is retained in the
  note for provenance but hidden in the learner-facing template until a detailed
  explanation website is available.
- Keep user-facing placeholder links as `Розгорнуте пояснення` until the project
  website exists.
- Preserve unrelated user work. Send explicitly requested deletions to the
  Windows Recycle Bin rather than permanently removing them.
