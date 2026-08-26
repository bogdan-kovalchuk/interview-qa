---
id: py-syntax-0014
title: "Як chained comparison `a < b < c` відрізняється від `a < b and b < c` щодо кількості обчислень середнього operand?"
description: "У chained comparison a < b < c середній операнд b обчислюється лише один раз, тоді як у a < b and b < c – двічі (якщо a < b істинне)."
track: python
section: syntax-and-control-flow
level: middle
type: comparison
tags: [a-lt-b-lt-c, a-lt-b-and-b-lt-c]
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

**У chained comparison `a < b < c` середній операнд `b` обчислюється лише один раз, тоді як у `a < b and b < c` – двічі (якщо `a < b` істинне).**[^py314-reference-expressions] Обидва варіанти семантично еквівалентні за результатом і short-circuit поведінкою (якщо `a < b` хибне, `c` не обчислюється в жодному випадку), але chained comparison уникає повторного обчислення `b`, що важливо, коли `b` – вираз із side effects або дорогим обчисленням.

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
