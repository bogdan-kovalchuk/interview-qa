---
id: py-oop-0026
title: "Чим structural subtyping через `typing.Protocol` відрізняється від nominal inheritance через ABC?"
description: "Protocol використовує structural subtyping – клас задовольняє його, якщо має потрібні методи, без явного успадкування; ABC вимагає nominal inheritance – клас має явно успадкувати від ABC."
track: python
section: oop-and-data-model
level: middle
type: comparison
tags: [typing-protocol]
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/class_and_object.md#L770-L790
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`Protocol` використовує structural subtyping – клас задовольняє його, якщо має потрібні методи, без явного успадкування; ABC вимагає nominal inheritance – клас має явно успадкувати від ABC.**[^py314-reference-datamodel] `Protocol` призначений переважно для static type checkers; runtime перевірки працюють лише з `@runtime_checkable` і перевіряють лише наявність атрибутів, не типи. ABC підтримує `isinstance`/`issubclass` нативно.

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
