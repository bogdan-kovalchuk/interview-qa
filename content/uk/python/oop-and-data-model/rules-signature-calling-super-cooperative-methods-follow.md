---
id: py-oop-0019
title: "Яких правил сигнатури та виклику `super()` мають дотримуватися cooperative methods у multiple-inheritance hierarchy?"
description: "Кожен метод у hierarchy має викликати super().method(*args,"
track: python
section: oop-and-data-model
level: senior
type: practical
tags: [super]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/class_and_object.md#L348-L354
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Кожен метод у hierarchy має викликати `super().method(*args, **kwargs)` з тією самою сигнатурою, щоб ланцюжок MRO пройшовся без пропусків і без `TypeError`.**[^py314-reference-datamodel] На практиці це означає: (1) приймати `**kwargs` або сумісний набір позиційних аргументів, (2) завжди викликати `super()` навіть якщо «більше нікого немає» – останній у MRO зазвичай `object`, тому базовий `__init__` має приймати порожні args, (3) не пропускати `super()` «бо я останній». Порушення будь-якого правила ламає cooperative chain.

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
