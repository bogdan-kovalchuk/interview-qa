---
id: py-funcs-0001
title: "Які різні обмеження на спосіб передавання аргументів задають символи `/` і `*` у сигнатурі `def f(a, /, b, *, c): ...`?"
description: "/ розділяє positional-only та решту параметрів, а * розділяє звичайні та keyword-only параметри."
track: python
section: functions-and-scope
level: middle
type: comparison
tags: [def-f-a-b-c]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-calls
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#calls
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functions.md#L57-L93
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`/` розділяє positional-only та решту параметрів, а `*` розділяє звичайні та keyword-only параметри.**[^py314-reference-compound-stmts-function-definitions] Параметр `a` (ліворуч від `/`) приймається лише позиційно – виклик `f(a=1)` дасть `TypeError`. Параметр `b` (між `/` і `*`) приймається обома способами. Параметр `c` (праворуч від `*`) приймається лише як keyword – виклик `f(1, 2, 3)` дасть `TypeError`.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
