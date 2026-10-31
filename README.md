# Interview Questions and Answers

A bilingual (English / Ukrainian) set of technical interview questions in three tracks:
**Python**, **Embedded** and **Electronics**.

Every question is exactly three things in both languages: **the question, a short answer and a
detailed answer**. One question = one file = one page = one flashcard: the same file becomes a page
on the site and a card in an Anki deck that links back to that page.

- Site: `https://bogdan-kovalchuk.github.io/interview-qa/`
- Question permalink: `…/interview-qa/{lang}/q/{id}/` – stable forever, taxonomy-independent

**Current state:** 2047 questions in both languages. Every question has a Ukrainian short answer,
1239 have an English one, and those are the cards that ship (2047 Ukrainian, 1239 English).
Detailed answers are written for 1991 Ukrainian and 423 English files, including all 363 Python
questions in both languages. An unwritten section is marked `TODO` in the source and is not shown on
the page.

## A question

```markdown
---
id: py-async-0012
title: "How does `asyncio.gather()` preserve the order of results?"
track: python
section: asyncio
sources:                          # optional
  - source_id: py314-asyncio-task
    title: "Python 3.14: asyncio Tasks"
    url: https://docs.python.org/3.14/library/asyncio-task.html
---

## Short answer

Two to five sentences – this is the back of the card.

## Detailed explanation

As long as it needs to be – this is the page.
```

An optional `## Question code` section before the short answer holds a code snippet the question is
about; it goes on the front of the card. The full contract is `meta/questions.md`.

## How it works

```
content/{en,uk}/{track}/**/*.md     plain Markdown + YAML frontmatter
  tools/iqa  ->  site/              generated mirror -> Astro Starlight -> GitHub Pages
  tools/iqa  ->  dist/export/       questions.json -> Anki .apkg decks
```

Links inside content are written as `qid:<id>` tokens, never as URLs – the site and the Anki card
each materialise their own form.

Cards are updated, not replaced: note GUIDs are derived deterministically from the question id, so
re-importing a rebuilt deck edits the existing note and **keeps your review schedule**. This was
measured on real collections, not assumed – see `meta/measurements.md`.

## Layout

| Path | What |
|---|---|
| `content/` | the questions, in both languages |
| `meta/` | the specification, decisions and measurements (Ukrainian) |
| `anki/` | note type and fonts (the deck builder is `tools/iqa/anki.py`) |
| `site/` | Astro Starlight – the only Node part |
| `tools/` | the Python pipeline |
| `tests/` | quality gates and regression tests |
| `requirements/` | reproducible Python dependency lock |

## Commands

```
python -m iqa validate                  content and language-parity gates
python -m iqa export                    dist/export/questions.json
python -m iqa deck --language {uk,en}   the .apkg, from the export
python -m iqa build                     validate -> export -> mirror -> astro build -> verify
python -m pytest --basetemp=<dir>
```

## Licence

[MIT](LICENSE) – code and content alike.

The Python material uses community sources only to find questions worth asking; its wording is
written for this project. The `embedded/` questions were imported from the owner's own two decks,
and the `electronics/` questions are the owner's flashcards for the Udemy course *Crash Course
Electronics and PCB Design*; their answers started from the owner's card wording and have since been
checked against technical sources and corrected where wrong.
