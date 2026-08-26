---
id: py-syntax-0013
title: "Чому вираз `-3 ** 2` дає інший результат, ніж `(-3) ** 2`?"
description: "-3"
track: python
section: syntax-and-control-flow
level: middle
type: mechanism
tags: [3-2]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14"
  flags: []
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

**`-3 ** 2` дає `-9`, а `(-3) ** 2` дає `9`, тому що оператор `**` має вищий пріоритет, ніж унарний мінус зліва від нього.**[^py314-reference-expressions] Тобто `-3 ** 2` інтерпретується як `-(3 ** 2)`. Дужки змінюють порядок: спочатку обчислюється `-3`, потім піднесення до степеня.

```text
>>> print(-3 ** 2)
-9
>>> print((-3) ** 2)
9
```

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
