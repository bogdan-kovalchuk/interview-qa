---
id: py-itergen-0014
title: "Яку проблему створює передавання одного iterator двом consumers, які читають його по черзі?"
description: "Iterator – односпрямований і stateful: два consumers ділять один cursor, тому елементи, прочитані одним, стають недоступними для іншого."
track: python
section: iterators-and-generators
level: middle
type: practical
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

**Iterator – односпрямований і stateful: два consumers ділять один cursor, тому елементи, прочитані одним, стають недоступними для іншого.**[^py314-library-stdtypes-iterator-types] Наприклад, якщо перший consumer витягнув три елементи, другий почне з четвертого, а не з першого. Щоб обидва отримали повну копію даних, потрібно або зберегти iterator у `list`, або використати `itertools.tee()`, яка створить незалежні iterators ціною додаткової пам'яті.

## Detailed explanation

TODO

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
