---
id: py-excpt-0012
title: "Яку проблему вирішують `ExceptionGroup` та `except*` у concurrent code?"
description: "ExceptionGroup дозволяє підняти кілька незалежних exception одночасно, а except* – вибірково обробити потрібні типи, не втрачаючи решти."
track: python
section: exceptions
level: middle
type: mechanism
tags: [exceptiongroup]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/exceptions.md#L222-L249
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`ExceptionGroup` дозволяє підняти кілька незалежних exception одночасно, а `except*` – вибірково обробити потрібні типи, не втрачаючи решти.**[^py314-tutorial-errors] У concurrent code (наприклад, `asyncio.TaskGroup`) кілька задач можуть згенерувати різні exception. Замість того щоб зберегти лише першу, `ExceptionGroup` агрегує їх в один об’єкт. `except*` розщеплює групу за типом, обробляючи кожну підгрупу окремо.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
