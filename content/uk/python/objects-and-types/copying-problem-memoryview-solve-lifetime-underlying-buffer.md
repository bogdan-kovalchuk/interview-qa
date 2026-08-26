---
id: py-objtypes-0019
title: "Яку проблему копіювання вирішує `memoryview` і чому lifetime базового buffer object має значення?"
description: "memoryview надає zero-copy доступ до внутрішнього buffer об'єкта, що підтримує buffer protocol (наприклад, bytes, bytearray, array.array), дозволяючи читати та змінювати ділянки пам'яті без створення копій."
track: python
section: objects-and-types
level: senior
type: mechanism
tags: [memoryview]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
applies_to:
  - product: "CPython"
    version: null
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
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L498-L586
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`memoryview` надає zero-copy доступ до внутрішнього buffer об'єкта, що підтримує buffer protocol (наприклад, `bytes`, `bytearray`, `array.array`), дозволяючи читати та змінювати ділянки пам'яті без створення копій.**[^py314-reference-datamodel] Це критично для великих binary даних, де slicing або `copy` створили б повну копію. Lifetime базового об'єкта має значення: `memoryview` не володіє даними, а посилається на buffer; у CPython memoryview тримає reference на base-об'єкт, запобігаючи його звільненню, а поки буфер експортований, спроба змінити розмір base (наприклад, `bytearray.extend()`) піднімає `BufferError` – спочатку треба викликати `release()`. <span class="warn">Після виклику `mv.release()` доступ до memoryview викликає `ValueError`.</span>

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
