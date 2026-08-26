---
id: py-syntax-0004
title: "Як extended iterable unpacking працює у присвоєнні `head, *middle, tail = items` і що станеться, якщо елементів недостатньо?"
description: "*middle збирає всі проміжні елементи у list; для успіху потрібно щонайменше 2 елементи (для head і tail)."
track: python
section: syntax-and-control-flow
level: middle
type: mechanism
tags: [head-middle-tail-items]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/syntax.md#L252-L352
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`*middle` збирає всі проміжні елементи у `list`; для успіху потрібно щонайменше 2 елементи (для `head` і `tail`).**[^py314-reference-expressions] Наприклад, `head, *middle, tail = [1, 2, 3, 4, 5]` дає `head=1, middle=[2, 3, 4], tail=5`. Якщо елементів лише один – `head, *middle, tail = [1]` – виникає `ValueError: not enough values to unpack (expected at least 2, got 1)`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
