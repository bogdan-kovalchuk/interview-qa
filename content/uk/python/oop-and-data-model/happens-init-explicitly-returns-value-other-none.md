---
id: py-oop-0003
title: "Що станеться, якщо `__init__` явно поверне значення, відмінне від `None`, і чому?"
description: "Python підніме TypeError: __init__() should return None, not '...'."
track: python
section: oop-and-data-model
level: middle
type: pitfall
tags: [init]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-descriptor
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-mro
    title: "Python 3.14: Howto/mro"
    url: https://docs.python.org/3.14/howto/mro.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Python підніме `TypeError: __init__() should return None, not '...'`.**[^py314-reference-datamodel] Інтерпретатор перевіряє return value `__init__` після кожного виклику; повернення будь-якого об'єкта, відмінного від `None`, вважається помилкою, оскільки `__init__` призначений лише для ініціалізації вже створеного instance, а не для його створення.

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
