---
id: py-oop-0016
title: "Як C3 MRO визначає порядок пошуку methods для множинного успадкування і яку властивість порядку він зберігає?"
description: "C3 будує лінеаризацію L[C] = C + merge(L[B₁], …, L[Bₙ], B₁, …, Bₙ), зберігаючи local precedence order (порядок bases у class C(A, B)) і monotonicity (клас завжди перед своїми батьками)."
track: python
section: oop-and-data-model
level: senior
type: mechanism
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/class_and_object.md#L355-L412
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**C3 будує лінеаризацію `L[C] = C + merge(L[B₁], …, L[Bₙ], B₁, …, Bₙ)`, зберігаючи local precedence order (порядок bases у `class C(A, B)`) і monotonicity (клас завжди перед своїми батьками).**[^py314-reference-datamodel] Merge на кожному кроці обирає «good head» – голову першого списку, яка не зустрічається в хвостах інших списків. Якщо такого не знайдено – `TypeError`. Результат – лінійний порядок, у якому кожен клас зустрічається рівно один раз і пошук атрибутів іде зліва направо.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
