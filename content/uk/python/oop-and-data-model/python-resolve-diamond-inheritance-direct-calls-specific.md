---
id: py-oop-0018
title: "Як Python розв’язує успадкування типу diamond і чому прямі виклики конкретних parent methods можуть виконати одну ланку двічі?"
description: "C3 MRO гарантує, що кожен клас у diamond зустрічається один раз, а super() проходить лінеаризацію послідовно; прямі виклики Parent.method(self) обходять MRO і можуть викликати спільного предка двічі."
track: python
section: oop-and-data-model
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/class_and_object.md#L413-L435
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**C3 MRO гарантує, що кожен клас у diamond зустрічається один раз, а `super()` проходить лінеаризацію послідовно; прямі виклики `Parent.method(self)` обходять MRO і можуть викликати спільного предка двічі.**[^py314-reference-datamodel] <span class="warn">Якщо `B(A)` і `C(A)`, а `D(B, C)`, то `B.method(self); C.method(self)` у `D` викличе `A.method` двічі.</span> Розв'язок – cooperative pattern: кожен клас викликає `super().method()`, і MRO забезпечує single-pass по всім унікальним класам.

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
