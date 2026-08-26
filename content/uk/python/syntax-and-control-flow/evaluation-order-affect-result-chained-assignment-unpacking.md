---
id: py-syntax-0006
title: "Як evaluation order впливає на результат chained assignment або unpacking, якщо правий вираз має side effects?"
description: "Права частина обчислюється першою, потім цілі зліва присвоюються зліва направо; тому side effects у правому виразі впливають на всі target."
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

**Права частина обчислюється першою, потім цілі зліва присвоюються зліва направо; тому side effects у правому виразі впливають на всі target.**[^py314-reference-expressions] Наприклад, при `i, x[i] = 1, 2` (де `i=0, x=[0,1]`) спочатку обчислюється кортеж `(1, 2)`, потім `i` стає `1`, і після цього `x[1]` (вже з новим `i`) стає `2` – результат `x == [0, 2]`.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
