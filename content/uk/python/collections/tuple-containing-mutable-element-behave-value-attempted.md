---
id: py-coll-0005
title: "Як tuple, що містить mutable element, поводиться під час спроби `t[0] += value`, і чому mutation може статися до `TypeError`?"
description: "+= для mutable елемента всередині tuple спочатку виконує in-place mutation, а потім намагається присвоїти результат назад у tuple – присвоєння викликає TypeError, але мутація вже відбулася."
track: python
section: collections
level: senior
type: pitfall
tags: [t-0-value, typeerror]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14.7"
  flags: []
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-sorting
    title: "Python 3.14: Howto/sorting"
    url: https://docs.python.org/3.14/howto/sorting.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/sequences.md#L202-L291
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`+=` для mutable елемента всередині tuple спочатку виконує in-place mutation, а потім намагається присвоїти результат назад у tuple – присвоєння викликає `TypeError`, але мутація вже відбулася.**[^py314-library-stdtypes]

```text
t = ([1, 2], [3])
t[0] += [3]    # TypeError, але t[0] вже [1, 2, 3]
```

Вираз `t[0] += [3]` фактично виконує `t[0] = t[0].__iadd__([3])`: `__iadd__` модифікує список, а потім `tuple.__setitem__` відхиляє присвоєння.

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
