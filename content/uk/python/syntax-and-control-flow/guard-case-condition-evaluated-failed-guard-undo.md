---
id: py-syntax-0010
title: "Коли guard у `case ... if condition` обчислюється і чи скасовує невдалий guard bindings, створені самим pattern?"
description: "Guard обчислюється лише після успішного pattern; якщо guard хибний, case не обирається, але bindings з pattern НЕ гарантовано скасовуються."
track: python
section: syntax-and-control-flow
level: senior
type: mechanism
tags: [case-if-condition]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
applies_to:
  - product: "CPython"
    version: "3.14"
anki:
  export: true
sources:
  - source_id: py314-reference-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-simple-stmts
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/syntax.md#L164-L228
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Guard обчислюється лише після успішного pattern; якщо guard хибний, case не обирається, але bindings з pattern НЕ гарантовано скасовуються.**[^py314-reference-expressions] Language Reference явно застерігає: «Do not rely on bindings being made for a failed match. Conversely, do not rely on variables remaining unchanged after a failed match.» У CPython 3.14 bindings зберігаються (наприклад, після `case (y,) if y > 100:` змінна `y` залишається прив'язаною навіть при невдалому guard), але це implementation detail.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
