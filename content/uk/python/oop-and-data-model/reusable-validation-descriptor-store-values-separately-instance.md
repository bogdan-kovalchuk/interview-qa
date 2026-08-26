---
id: py-oop-0012
title: "Як reusable validation descriptor має зберігати значення окремо для кожного instance, не створюючи shared state між об’єктами?"
description: "Descriptor зберігає дані не в собі (бо він один на клас), а в instance.__dict__ під приватним ключем, ім'я якого визначається через __set_name__."
track: python
section: oop-and-data-model
level: senior
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/class_and_object.md#L1206-L1292
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Descriptor зберігає дані не в собі (бо він один на клас), а в `instance.__dict__` під приватним ключем, ім'я якого визначається через `__set_name__`.**[^py314-reference-datamodel] `__set_name__` викликається автоматично при створенні класу й передає descriptor його public name; descriptor обчислює private name (наприклад, `'_' + name`) і зберігає/читає значення через `setattr(obj, self.private_name, value)` / `getattr(obj, self.private_name)`. Завдяки цьому один descriptor-об'єкт на клас обслуговує багато instance без shared mutable state.

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
