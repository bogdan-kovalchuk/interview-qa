---
id: py-itergen-0013
title: "Чому повторна ітерація вже exhausted generator не починає обчислення спочатку?"
description: "Після першого StopIteration generator остаточно завершений: протокол вимагає, що всі наступні __next__() також піднімають StopIteration."
track: python
section: iterators-and-generators
level: middle
type: pitfall
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

**Після першого `StopIteration` generator остаточно завершений: протокол вимагає, що всі наступні `__next__()` також піднімають `StopIteration`.**[^py314-library-stdtypes-iterator-types] Generator зберігає свій frame і стан виконання; коли тіло функції завершилось (return або кінець блоку), повторно запустити його неможливо. На відміну від iterable-контейнера, який щоразу створює новий iterator, generator – це одноразовий iterator без механізму «перемотування».

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
