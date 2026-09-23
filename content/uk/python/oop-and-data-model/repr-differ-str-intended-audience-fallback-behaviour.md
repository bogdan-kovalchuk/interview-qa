---
id: py-oop-0021
title: "Чим `__repr__` відрізняється від `__str__` за аудиторією та fallback behavior?"
description: "__repr__ повертає \"official\" string representation для debugging (має бути однозначним, бажано валідним Python виразом), а __str__ – \"informal\" representation для кінцевих користувачів (більш зручний та стислий)."
track: python
section: oop-and-data-model
level: middle
type: comparison
tags: [repr, str]
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

**`__repr__` повертає "official" string representation для debugging (має бути однозначним, бажано валідним Python виразом), а `__str__` – "informal" representation для кінцевих користувачів (більш зручний та стислий).**[^py314-reference-datamodel] Якщо клас визначає `__repr__`, але не `__str__`, тоді `__repr__` використовується як fallback для `str()`. За замовчуванням `object.__str__` викликає `object.__repr__`.

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
