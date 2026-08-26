---
id: py-syntax-0012
title: "У якому порядку Python обчислює function expression, positional arguments і keyword arguments у виклику, якщо вони мають side effects?"
description: "Python обчислює callable-вираз першим, потім усі argument expressions до початку виклику, причому *expr обчислюється перед keyword arguments, навіть якщо стоїть після них у коді."
track: python
section: syntax-and-control-flow
level: senior
type: mechanism
tags: []
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
---

## Short answer

**Python обчислює callable-вираз першим, потім усі argument expressions до початку виклику, причому `*expr` обчислюється перед keyword arguments, навіть якщо стоїть після них у коді.**[^py314-reference-expressions] Загальний порядок: primary expression -> позиційні аргументи (зліва направо) -> `*unpack` -> keyword arguments -> `**unpack`. Це гарантія мови (left-to-right evaluation), а не деталь реалізації.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
