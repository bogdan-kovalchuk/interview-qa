---
id: py-oop-0009
title: "Чим data descriptor відрізняється від non-data descriptor і як ця різниця змінює precedence під час attribute lookup?"
description: "Data descriptor визначає __set__ або __delete__ і перемагає instance __dict__; non-data descriptor визначає лише __get__ і поступається instance __dict__."
track: python
section: oop-and-data-model
level: senior
type: comparison
tags: []
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

**Data descriptor визначає `__set__` або `__delete__` і перемагає instance `__dict__`; non-data descriptor визначає лише `__get__` і поступається instance `__dict__`.**[^py314-reference-datamodel] Приклад data descriptor – `property`; приклад non-data descriptor – звичайний метод (функція, прив'язана до класу). Тому `obj.method = 42` перезаписує метод для конкретного instance, а `obj.prop = 42` викликає setter property.

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
