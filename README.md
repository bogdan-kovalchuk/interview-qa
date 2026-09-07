# Interview Questions and Answers

A bilingual (English / Ukrainian) knowledge base of technical interview questions with in-depth
answers, covering **Python**, **C/C++**, and specialization tracks such as **Embedded**,
**Data Science**, **Machine Learning**, **Backend**, **DevOps** and **QA Automation**.

**One question = one file = one page = one flashcard.** The same file becomes a page on the site, a
card in an Anki deck that links back to that page, and an entry in one or more role-based study
programs. A fix made once is a fix everywhere.

- Site: `https://bogdan-kovalchuk.github.io/interview-qa/`
- Question permalink: `…/interview-qa/{lang}/q/{id}/` – stable forever, taxonomy-independent

> **Work in progress, by design.** Every question exists in both languages from the day it is
> created, with unwritten sections marked `TODO`, and is filled in over time. An unwritten section
> is not rendered on the page at all: on 224 of the pages that existed at the time it produced four
> or more identical "not written yet" notices, so the gaps are reported as data instead.
>
> **Current state:** 1254 questions in both languages, 1222 shipping as Ukrainian flashcards and
> 145 as English ones, and the site is live at the link above. 1235 have a Ukrainian short answer;
> 145 also carry a written detailed explanation and a full English body, 9 of them complete. For the
> rest, the detailed explanation and the English text are still `TODO`. A `/status/` page that
> reports the gaps as a table is next – the data behind it is already generated as
> `dist/export/progress.{json,csv}`.

## How it works

```
content/{en,uk}/{track}/**/*.md      plain Markdown + YAML frontmatter, no generator lock-in
        │
        ├─ tools/   →  site/         generated mirror → Astro Starlight → GitHub Pages
        ├─ tools/   →  dist/export/  questions.json, progress table
        └─ anki/                    .apkg decks, one per study direction
```

Links inside content are written as `qid:<id>` tokens, never as URLs – the site, the JSON export and
the Anki card each materialise their own form. That is why a card printed in 2026 still resolves
after the taxonomy is reorganised.

Cards are updated, not replaced: note GUIDs are derived deterministically from the question id, so
re-importing a rebuilt deck edits the existing note and **keeps your review schedule**. This was
measured on real collections, not assumed – see `meta/measurements.md`.

## Layout

| Path | What |
|---|---|
| `content/` | the questions, in both languages |
| `meta/` | the specification, decisions and measurements (Ukrainian) |
| `anki/` | note type, fonts, deck builder, measurement harness |
| `site/` | Astro Starlight – the only Node part |
| `tools/` | the Python pipeline |
| `tests/` | automated quality gates and regression tests |
| `requirements/` | reproducible Python dependency lock |
| `meta/plan.md` | what happens next |

## Stack

Plain Markdown + YAML for content, Astro Starlight for the site (built-in i18n, Pagefind search),
Python for validation, export and reports, `genanki` for the decks, GitHub Pages via Actions for
hosting.

## Licence

[MIT](LICENSE) – code and content alike.

Community sources are treated as all-rights-reserved, since they carry no licence of their own, and
they are used in two different ways. The Python material uses them only to find questions worth
asking; its wording is written for this project. The `embedded/` track is different: 853 of its
questions were imported from the owner's own two decks, and their Ukrainian short answers keep the
source's wording, normalised rather than rewritten. Every such question names its origin in
`sources`, and `meta/questions.md` records which is which.
