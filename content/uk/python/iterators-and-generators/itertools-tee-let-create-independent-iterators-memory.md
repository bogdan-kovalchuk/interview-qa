---
id: py-itergen-0018
title: "Як `itertools.tee()` дозволяє створити незалежні iterators і який memory trade-off виникає, якщо consumers рухаються з різною швидкістю?"
description: "itertools.tee(iterable, n) повертає n незалежних iterators, які спільно використовують внутрішній буфер (зв'язаний список); кожен iterator зберігає власну позицію в цьому буфері."
track: python
section: iterators-and-generators
level: middle
type: practical
tags: [itertools-tee]
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

**`itertools.tee(iterable, n)` повертає `n` незалежних iterators, які спільно використовують внутрішній буфер (зв'язаний список); кожен iterator зберігає власну позицію в цьому буфері.**[^py314-library-stdtypes-iterator-types] Коли один consumer йде швидше за інший, різниця між їхніми позиціями накопичується в буфері. <span class="warn">Якщо один iterator проходить усі дані до того, як інший стартує, `tee()` споживає стільки ж пам'яті, скільки `list(iterable)`, – у такому разі краще одразу матеріалізувати список.</span>

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
