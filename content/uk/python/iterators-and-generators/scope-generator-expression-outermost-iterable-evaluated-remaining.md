---
id: py-itergen-0017
title: "У якому scope обчислюється outermost iterable generator expression і коли обчислюються решта його clauses?"
description: "Outermost iterable обчислюється негайно в enclosing scope; усі інші вирази (output expression, наступні for/if) обчислюються ліниво в окремому implicit nested scope."
track: python
section: iterators-and-generators
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
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Outermost iterable обчислюється негайно в enclosing scope; усі інші вирази (output expression, наступні `for`/`if`) обчислюються ліниво в окремому implicit nested scope.**[^py314-library-stdtypes-iterator-types] Це означає, що `NameError` або `TypeError` для зовнішнього iterable виникне в момент створення generator expression, а помилки у внутрішніх виразах – лише під час ітерації. Nested scope запобігає витоку змінних target list у зовнішню область.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
