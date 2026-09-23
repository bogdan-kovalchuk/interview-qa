---
id: py-oop-0005
title: "Чим `__getattribute__` відрізняється від `__getattr__` і коли викликається кожен із них?"
description: "__getattribute__ викликається безумовно для кожного доступу до атрибута; __getattr__ – лише як fallback, коли звичайний lookup завершився AttributeError."
track: python
section: oop-and-data-model
level: middle
type: comparison
tags: [getattribute, getattr]
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

**`__getattribute__` викликається безумовно для кожного доступу до атрибута; `__getattr__` – лише як fallback, коли звичайний lookup завершився `AttributeError`.**[^py314-reference-datamodel] <span class="warn">Якщо перевизначити `__getattribute__`, потрібно обережно делегувати до `super().__getattribute__()`, інакше можна зламати доступ до всіх атрибутів, включно з методами.</span> `__getattr__` безпечніший: він не зачіпає нормальний шлях пошуку.

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
