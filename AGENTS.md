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
| `meta/predecessor-baseline.json` | hashes of the migrated predecessor deck, kept as evidence |
| `packaging/anki/notetype/` | the note type: ids, markup, styling – defined once |
| `packaging/anki/{fonts,spike,test-deck}/` | embedded fonts, measurement harness, manual-test decks |
| `site/` | Astro Starlight; the only Node part |
| `tools/iqa/` | the Python pipeline; the only component that reads `content/` |
| `tests/` | negative fixtures - one per gate - plus model, lifecycle and CLI tests |
| `PLAN.md` | what happens next |

One-time setup: `pip install -e .` and `pip install pytest`. After that
`python -m iqa validate` checks the content gates and `python -m pytest` runs the suite. Nothing
else in the repository is runnable yet.

Nothing else outranks this file. If another document disagrees with it, that document is wrong and
must be fixed – not worked around.

## Current state

**401 questions, both languages, 388 Ukrainian cards and 145 English ones.** The 392 predecessor
cards are migrated; nine hand-written pilots cover every question type. Decisions are settled (`meta/DECISIONS.md`),
the Anki behaviour is measured on real collections (`meta/MEASUREMENTS.md`), and the question
contract is frozen.

A migrated question starts with a real Ukrainian `Short answer` and `TODO` everywhere else,
including the whole English body. That is the documented skeleton state, not an unfinished job: the
card ships from the Ukrainian answer, and the page shows honestly what is not written yet.

Writing over that skeleton has started (`PLAN.md` step 7). **136 of the 392** now carry a written
Ukrainian `Detailed explanation` together with the full English body – the translated `Short answer`
and `Detailed explanation`. Two sections, `python/fundamentals` and `python/syntax-and-control-flow`,
are finished end to end. The Ukrainian card count is unchanged at 388 – a card ships on the `Short
answer` in its own language, and every Ukrainian one was already written – while the English package
grows with each English `Short answer` that gets translated.

What works today, and how to run it:

```
python -m iqa validate    the content and parity gates, one negative fixture each
python -m iqa export      dist/export/questions.json
python -m iqa report      dist/export/progress.{json,csv}; --todo prints the next gaps
python -m iqa build       validate -> export+report -> mirror -> astro build -> verify
python packaging/anki/build.py --language {uk,en}    the .apkg, from the export
python -m pytest --basetemp=<writable dir>
```

CI runs that same sequence on every pull request. Deploying to GitHub Pages is deliberately
**manual only** (`workflow_dispatch`) until the owner authorises automatic publication, and the
deck is released by tagging `deck-v*`.

The site navigates by taxonomy: a generated sidebar (track, then section, in `meta/TAXONOMY.md`
order) plus track and section index pages, with the questions listed on their section's page rather
than in the menu. It is styled as a port of the reference site's Material for MkDocs theme
(`site/src/styles/`, values read off that site's CSS). **An unwritten section is not rendered on the
page at all** - the heading stays in `content/` because the contract requires it, but the gaps are
reported as data (`dist/export/progress.{json,csv}`, and `/status/` once it exists) rather than as a
notice repeated down every page.

What does not exist yet: the `/status/` page, Pagefind checked in both locales, the scale spike, and
programs. `PLAN.md` steps 6-7. The progress report exists as data (`python -m iqa report`) and the
page that renders it does not.

## Non-negotiable invariants

Breaking any of these is a migration event, not an edit.

- **A question ID is immutable and never reused**, even after the question is deleted.
- **Anki note GUIDs never change.** Every GUID is derived deterministically from the question id
  with the salt `iqa:v1:` (`iqa:v1:en:` for the English package, so the two never collide in one
  collection); nothing is inherited and there is no GUID map.
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
- **Typography:** en dash U+2013, never em dash U+2014. Arrows `←` U+2190 and `→` U+2192 are
  **forbidden in content** and the validator rejects them: they are not covered by the embedded
  font subsets, so on a card they fall back to a system font. Use words, or `->` in code.
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
- **`type::Definition` and `level::Junior` have zero cards in the old deck**, so their mapping and
  the junior criteria are not validated against any real question.
- **Do not publish anything outward without direct permission.**
- **Do not call something done that has not been checked.**
