# Interview Questions and Answers

A bilingual (English / Ukrainian) knowledge base of technical interview questions with in-depth
answers, covering **Python**, **C/C++**, and specialization tracks such as **Embedded**,
**Data Science**, **Machine Learning**, **Backend**, **DevOps** and **QA Automation**.

The same content powers two products:

- a **public site** (GitHub Pages) with one page per question and stable permalinks;
- generated **Anki decks**, where every card links back to the full explanation.

> **Work in progress.** The project ships incrementally and will stay incomplete for a long time by
> design: every question exists in both languages from the day it is created, with unwritten
> sections marked `TODO`, and the content is filled in over time. Pages that are still thin say so.
> Exactly when a question is published, shipped as a flashcard and linked is defined in
> [`meta/LIFECYCLE.md`](meta/LIFECYCLE.md).
>
> **Current phase: design.** This repository contains architecture documentation only – no content,
> site or tooling has been implemented yet.
>
> Site: `https://bogdan-kovalchuk.github.io/interview-qa/` (default GitHub Pages address, no custom
> domain – see [ADR-0005](meta/adr/0005-stable-permalinks.md))
> Question permalink: `https://bogdan-kovalchuk.github.io/interview-qa/{lang}/q/{id}/`

---

## Why this exists

Interview preparation material is usually either a long unstructured list of questions or a set of
flashcards with no depth. This project keeps a single source of truth: **one question is one file**,
which becomes a page, a flashcard, and an entry in one or more role-based study programs – so a fix
made once is a fix everywhere.

---

## Design documents

All design documents live in [`meta/`](meta/) and are written in Ukrainian (the maintainer's working
language). Start with the analysis:

| Document | What it covers |
|---|---|
| [`meta/HANDOFF.md`](meta/HANDOFF.md) | **picking this up cold?** – state, decisions, measured facts, traps |
| [`meta/WORK_PROGRAMME.md`](meta/WORK_PROGRAMME.md) | the ordered phases, exit criteria and stop points |
| [`meta/PIPELINE.md`](meta/PIPELINE.md) | end-to-end – end-to-end: one question becomes a page, a card and a deck |
| [`meta/LIFECYCLE.md`](meta/LIFECYCLE.md) | **normative** – when a question is published, shipped and linked |
| [`meta/PROJECT_PLAN_REVIEW.md`](meta/PROJECT_PLAN_REVIEW.md) | independent review of this plan, and what it blocked |
| [`meta/RUBRIC.md`](meta/RUBRIC.md) | operational definitions of level and type |
| [`meta/ANALYSIS.md`](meta/ANALYSIS.md) | full architectural analysis, rationale and open decisions |
| [`meta/TAXONOMY.md`](meta/TAXONOMY.md) | the proposed tree of tracks and sections |
| [`meta/NAMING.md`](meta/NAMING.md) | naming conventions for paths, IDs, tags and decks |
| [`meta/CONTENT_SPEC.md`](meta/CONTENT_SPEC.md) | the question file format |
| [`meta/PROGRESS_TRACKING.md`](meta/PROGRESS_TRACKING.md) | the generated progress table, down to a single question |
| [`meta/I18N.md`](meta/I18N.md) | bilingual strategy and mechanics |
| [`meta/ANKI_INTEGRATION.md`](meta/ANKI_INTEGRATION.md) | question-to-flashcard pipeline |
| [`meta/REPOSITORY_TOPOLOGY.md`](meta/REPOSITORY_TOPOLOGY.md) | repository layout and migration plan |
| [`meta/QUALITY_GATES.md`](meta/QUALITY_GATES.md) | CI gates |
| [`meta/ROADMAP.md`](meta/ROADMAP.md) | milestones |
| [`meta/adr/`](meta/adr/) | architecture decision records |

---

## Planned stack

| Layer | Choice |
|---|---|
| Content | plain Markdown + YAML frontmatter, generator-agnostic |
| Site | Astro Starlight (built-in i18n, Pagefind search) |
| Tooling | Python (validation, export, reports) |
| Flashcards | Anki, built from the same content |
| Hosting | GitHub Pages via GitHub Actions |

Rationale for not following the reference project's Material for MkDocs stack is in
[`ADR-0001`](meta/adr/0001-site-generator.md).

---

## Licence

[MIT](LICENSE) – code and content alike.

Community sources used to locate topics (for example the reference project) carry no licence of
their own and are treated as all-rights-reserved: they are used to find questions worth asking,
never to copy wording. Everything published here is written for this project.
