---
id: py-itergen-0003
title: "Як правильно сигналізувати завершення custom iterator і чому повернення sentinel value з `__next__` не є еквівалентом?"
description: "Коректний спосіб – підняти StopIteration з __next__(); повернення sentinel value не завершує ітерацію."
track: python
section: iterators-and-generators
level: middle
type: pitfall
tags: [next]
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

**Коректний спосіб – підняти `StopIteration` з `__next__()`; повернення sentinel value не завершує ітерацію.**[^py314-library-stdtypes-iterator-types] Протокол ітерації покладається саме на виняток `StopIteration` як сигнал завершення: `for`, `list()`, `tuple()` та інші споживачі ловлять цей виняток. Якщо `__next__` повертає sentinel, споживач сприйме його як черговий елемент і додасть до результату.

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
