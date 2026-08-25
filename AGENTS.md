# Interview Questions and Answers – operating guide

This file is the entry point for anyone (human or agent) working in this repository.

## What this project is, and how big it is

**One person's interview preparation, published.** The owner writes the questions, reviews them,
and studies the resulting deck. The site is public so the material is useful to others and easy to
link, but there is no team, no editorial board, and no audience whose workflow a change could
disrupt.

Read every risk assessment in `meta/` with that in mind. Where an inherited document says
"learners", it means the owner's own Anki collection. Where a review finding assumes a second
person – a separate reviewer, a translator, a sign-off record – the finding does not apply here,
and importing it wholesale is how this repository has already acquired two rules the owner had to
overrule twice (ADR-0012).

Keep what catches real breakage cheaply: machine parity, GUID stability, the note-type
fingerprint, executed examples. These cost nothing per question and fail loudly. Reject process
whose only justification is a second person.

## Current phase

**End of M0.** The repository holds architecture documentation in `meta/`, nine bilingual pilot
questions in `content/`, and the measured Anki spikes in `packaging/anki/`. There is no `tools/`
pipeline and no site content yet.

An independent plan review (`meta/PROJECT_PLAN_REVIEW.md`) blocked the move to M1; its findings are
answered in `meta/adr/0010-plan-review-corrections.md`. Phase A wrote the pilots to break the
specification and phase B closed what they found (`meta/SPEC_DEFECTS.md`, wave 2). The order of
work and the stopping points are `meta/WORK_PROGRAMME.md`; the milestones are `meta/ROADMAP.md`.

## Document precedence

When two documents disagree, the higher one wins and the lower one is wrong and must be fixed:

1. `meta/LIFECYCLE.md` – when a question is published, shipped as a card, and linked.
2. `AGENTS.md` – this file: invariants.
3. Accepted ADRs in `meta/adr/`, later numbers refining earlier ones.
4. Normative specs: `CONTENT_SPEC.md`, `NAMING.md`, `I18N.md`, `ANKI_INTEGRATION.md`,
   `QUALITY_GATES.md`, `PROGRESS_TRACKING.md`, `REPOSITORY_TOPOLOGY.md`.
5. Narrative: `PIPELINE.md`, `ANALYSIS.md`, `TAXONOMY.md`.

Never leave two live descriptions of the same behaviour. Delete the losing one.

## Read before doing anything

0. `meta/HANDOFF.md` – if you are picking this project up cold, start here.
   Then `meta/WORK_PROGRAMME.md` for the order of work and where to stop.
1. `meta/PIPELINE.md` – the end-to-end story: how a question becomes a page, a card and a deck.
2. `meta/LIFECYCLE.md` – the normative table. Read it before writing any publication logic.
3. `meta/adr/` – the decisions. A change that contradicts an ADR needs a superseding ADR.
4. `meta/CONTENT_SPEC.md` and `meta/NAMING.md` – before touching any question file.
5. `meta/QUALITY_GATES.md` – before touching the build or CI.

## Decisions already fixed (2026-09-03)

Do not revisit these without an explicit instruction from the owner:

- Repository name is **`interview-qa`**, on the default GitHub Pages address, **no custom domain**:
  a lapsed domain would kill every link embedded in learners' flashcards at once (ADR-0005).
- **`defaultLocale: en`**, bilingual EN+UK from day one, and therefore **Astro Starlight** as the
  site generator (ADR-0001). `site/` is the only Node part; everything else stays Python.
- **Monorepo**; the predecessor deck is migrated **after milestone M3**, and cutover is phased with
  a rollback window rather than a single step (ADR-0010 §8).
- **One `LICENSE` (MIT)** covers code and content. Third-party dependency licensing is a separate
  question, open until the M3 review (ADR-0010 §7).
- **A distribution package is not a deck.** Packages select questions per direction; decks are
  always topic-shaped; tags carry the facets (ADR-0008).
- **Both language versions are written by an agent**, in whichever language is convenient, and an
  AI translation **is** the translation – there is no separate translation-quality gate. Machine
  parity checks stay because they catch mechanical breakage cheaply; they do not prove translation
  quality, and nothing else does either. That is an accepted cost, not a hole to plug (ADR-0012).

## Non-negotiable invariants

Breaking any of these is a migration event, not an edit.

- **A question ID is immutable and never reused**, even after the question is deleted.
- **Anki note GUIDs never change.** A changed GUID gives learners duplicate cards and destroys their
  review scheduling. Every GUID is derived deterministically from the question id with the salt
  `iqa:v1:`; nothing is inherited from the predecessor collection and there is no GUID map
  (ADR-0006, ADR-0011).
- **The note type is frozen from the first published package, not before it.** The target is a new,
  clean `Interview QA Basic`, `model_id 1600000000001`, carrying all five fields – `Front` 0,
  `Back` 1, `Reference` 2, `Sources` 3, `QID` 4 – and one template from the start, with field and
  template ids fixed in `packaging/anki/note_type.md`. The predecessor's `Python Interview Basic`,
  `model_id 1788409800655`, is **not** inherited: the M0.4 spike measured that no collection
  anywhere holds its notes, so there is no installed base to preserve (ADR-0010 §1). Once a package
  has shipped, changing `model_id` is forbidden and the `anki-notetype-stable` gate blocks it –
  measured on the same spike: a package with the same GUID but a different `model_id` raises no
  error and creates no duplicate note, it silently merges the note types, shifts fields to other
  ords and adds extra cards.
- **Content links are written as `qid:<id>` tokens, never as URLs.** Each consumer materialises its
  own form; the site must account for `base: '/interview-qa'` (ADR-0010 §2).
- **`content/` stays generator-agnostic**: plain Markdown, no MDX, no component imports.
- **Only `tools/` reads `content/`.** The site consumes a generated mirror at
  `site/src/content/docs/`; every other consumer reads `dist/export/` (ADR-0010 §3).
- **A question exists in exactly one place.** Cross-track membership is expressed with facets and
  programs, never with a copy (ADR-0007).
- **Every required section exists in every language from creation**, holding `TODO` until written.
  An absent section is a structural error; an empty one is not (`CONTENT_SPEC.md` §3a).
- **Publication, card shipping and `Reference` follow `meta/LIFECYCLE.md`** and nothing else.
- **Progress is a projection, never a hand-kept file** (`PROGRESS_TRACKING.md`).
- **Editing any note field is safe; changing identity or structure is not.** Every build diffs
  against the last release manifest and fails on an identity or structure change (ADR-0009).

## Typography

Use en dash U+2013, never em dash U+2014. A CI gate enforces this.

## Language policy

- `README.md`, code, identifiers and public-facing site chrome: English.
- `meta/` design documents: Ukrainian (maintainer's working language).
- Question content: both languages, per `meta/I18N.md`.
- Technical terms stay in English inside Ukrainian text (`event loop`, `GIL`, `move semantics`).

## The predecessor

`python_interview_questions` no longer exists as a working repository. Everything of value was
moved here on 2026-09-03 and its full history archived as
`Desktop/python_interview_questions-archive.bundle` (749 KB, 22 commits, verified).

| What | Where it lives now |
|---|---|
| 392 finished cards, 23 TSV | `meta/migration/legacy/cards/` |
| per-card provenance, executed examples | `meta/migration/legacy/*.csv` |
| 23 research topic briefs | `meta/topic-briefs/` |
| authoring and review prompts | `meta/prompts/` |
| community source record and index | `meta/sources/` |
| old specs, scripts, research, reviews | `meta/migration/legacy/` |

`meta/migration/legacy/` is **input for M4, not current specification**. It disappears when the
migration completes. Nothing in it may be cited as a live rule.
