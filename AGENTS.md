# AGENTS.md

Source of truth for anyone working in this repository, human or agent. Read this file first and in
full; everything else is detail you fetch when you need it.

## What this is, and how big it is

A bilingual (EN/UK) knowledge base of technical interview questions. One question = one file =
one page = one Anki card. It feeds a public site on GitHub Pages and generated Anki decks.

**It is the owner's own interview preparation, published.** One person writes the questions,
reviews them, and studies the deck. The site is public so the material is useful to others and easy
to link, but there is no team, no editorial board, and no audience whose workflow a change could
disrupt.

Read every risk assessment here with that in mind. Where an inherited document says "learners", it
means the owner's own Anki collection. Where a finding assumes a second person – a separate
reviewer, a translator, a sign-off record – it does not apply, and importing it wholesale is how
this repository twice acquired rules the owner had to overrule.

Keep what catches real breakage cheaply: machine parity, GUID stability, the note-type fingerprint,
executed examples. These cost nothing per question and fail loudly. Reject process whose only
justification is a second person.

## Where things are

| Path | What it holds |
|---|---|
| `content/{en,uk}/{track}/**/*.md` | the questions – the only source of truth for content |
| `meta/QUESTIONS.md` | the question contract: naming, frontmatter, body, types, lifecycle |
| `meta/TAXONOMY.md` | the track and section tree |
| `meta/ANKI.md` | note type, GUID, packaging, when a card ships |
| `meta/SITE.md` | site build, URLs, localisation, progress report |
| `meta/QUALITY_GATES.md` | what CI checks |
| `meta/DECISIONS.md` | every decision that is settled, and why |
| `meta/MEASUREMENTS.md` | what was measured on real Anki collections |
| `meta/vocabulary.yml` | section labels, glossary, frameworks, section prefixes |
| `meta/id-registry.csv` | issued question IDs – the arbiter |
| `meta/topic-briefs/` | 23 research briefs, raw material for objectives and questions |
| `meta/migration/` | frozen inputs for the predecessor deck migration |
| `packaging/anki/notetype/` | the note type: ids, markup, styling – defined once |
| `packaging/anki/{fonts,spike,test-deck}/` | embedded fonts, measurement harness, manual-test decks |
| `site/` | Astro Starlight; the only Node part |
| `tools/` | the Python pipeline; the only component that reads `content/` |
| `PLAN.md` | what happens next |

Nothing else outranks this file. If another document disagrees with it, that document is wrong and
must be fixed – not worked around.

## Current state

End of design. Twelve decisions settled, the schema frozen, nine bilingual pilot questions written
and published, the Anki behaviour measured on real collections. There is no pipeline code yet:
`tools/` has only the site mirror, and `site/` is the M0.3 spike grown into a working build.

The next step and everything after it is `PLAN.md`.

## Non-negotiable invariants

Breaking any of these is a migration event, not an edit.

- **A question ID is immutable and never reused**, even after the question is deleted.
- **Anki note GUIDs never change.** Every GUID is derived deterministically from the question id
  with the salt `iqa:v1:`; nothing is inherited and there is no GUID map.
- **The note type is frozen from the first published package.** It is defined once, in
  `packaging/anki/notetype/`. After a package ships, changing `model_id`, the fields or the template
  count silently merges note types, shifts fields to other ords and creates extra cards – measured,
  not assumed.
- **Content links are written as `qid:<id>` tokens, never as URLs.** Each consumer materialises its
  own form; the site must account for `base: '/interview-qa'`.
- **`content/` stays generator-agnostic**: plain Markdown, no MDX, no component imports.
- **Only `tools/` reads `content/`.** The site consumes a generated mirror; everything else reads
  `dist/export/`.
- **A question exists in exactly one place.** Cross-track membership is expressed with facets and
  programs, never with a copy.
- **Every required section exists in every language from creation**, holding `TODO` until written.
  An absent section is a structural error; an empty one is not.
- **An AI translation is the translation.** There is no translation-quality gate and there will not
  be one. Machine parity stays because it catches mechanical breakage cheaply.
- **Publication, card shipping and `Reference` follow the lifecycle table** in `meta/QUESTIONS.md`
  §8 and nothing else.

## How work is done here

- **Commits:** one short line, empty body. Do not push without explicit permission – the remote is
  configured, the upstream deliberately is not.
- **Typography:** en dash U+2013, never em dash U+2014. Arrows `←` U+2190 and `→` U+2192 are **not
  covered** by the embedded font subsets – they fall back to a system font on cards.
- **Language:** `meta/` in Ukrainian, `README.md`, `AGENTS.md` and code in English. Technical terms
  stay English inside Ukrainian text (`event loop`, `GIL`, `move semantics`).
- **Never leave two live descriptions of one behaviour.** Changed a rule? Find and fix every other
  place it is stated. This class of defect has cost this project a whole phase.
- **Measure, do not paraphrase.** Claims about Anki behaviour come from `packaging/anki/spike/`,
  which is re-runnable, and land in `meta/MEASUREMENTS.md`. Documentation and measurement have
  already disagreed twice here, and measurement won both times.
- **Report a phase, then stop.** Each phase in `PLAN.md` ends with a report and waits for the owner.

## Traps already stepped in

- **Do not write root-relative URLs in content.** On GitHub Pages `/q/...` points at the domain
  root, not at the project. Check links on a **production** build with `base=/interview-qa`, never
  on the dev server, where the root happens to match.
- **Do not revive `legacy_card_id` or a GUID map.** The predecessor's 392 notes exist in no
  collection; on the new `model_id` an inherited GUID is the one combination that can corrupt a
  collection.
- **Do not treat `meta/migration/legacy/` as a live specification.** It is a frozen input; it
  disappears after the migration.
- **`type::Definition` and `level::Junior` have zero cards in the old deck**, so their mapping and
  the junior criteria are not validated against any real question.
- **Do not publish anything outward without direct permission.**
- **Do not call something done that has not been checked.**
