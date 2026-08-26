---
id: py-oop-0014
title: "Коли обирати instance method, `@classmethod` або `@staticmethod` з огляду на потрібний binding і polymorphism?"
description: "Instance method – коли потрібен доступ до стану конкретного об'єкта; @classmethod – коли потрібен доступ до класу з підтримкою polymorphism; @staticmethod – коли метод не залежить ні від instance, ні від класу."
track: python
section: oop-and-data-model
level: middle
type: comparison
tags: [classmethod, staticmethod]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/class_and_object.md#L840-L940
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Instance method – коли потрібен доступ до стану конкретного об'єкта; `@classmethod` – коли потрібен доступ до класу з підтримкою polymorphism; `@staticmethod` – коли метод не залежить ні від instance, ні від класу.**[^py314-reference-datamodel] Тут `@classmethod` отримує підклас як `cls`, тому factory-методи коректно працюють при успадкуванні (повертають екземпляр підкласу). А `@staticmethod` не отримує жодного implicit аргументу і фактично є звичайною функцією, розміщеною в namespace класу; polymorphism для нього неможливий.

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
