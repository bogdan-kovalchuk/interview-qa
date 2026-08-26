---
id: cs-dstruct-0002
title: "Коли `deque` кращий за `list` для queue або sliding-window algorithm?"
description: "deque дає O(1) для append і pop з обох кінців, тоді як list коштує O(n) для pop(0) або insert(0, v), бо елементи доводиться зсувати в пам'яті."
track: cs
section: data-structures
level: middle
type: comparison
tags: [deque, list]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-heapq
    title: "Python 3.14: Library/heapq"
    url: https://docs.python.org/3.14/library/heapq.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-bisect
    title: "Python 3.14: Library/bisect"
    url: https://docs.python.org/3.14/library/bisect.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/data_structures.md#L367-L398
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`deque` дає O(1) для append і pop з обох кінців, тоді як `list` коштує O(n) для `pop(0)` або `insert(0, v)`, бо елементи доводиться зсувати в пам'яті.**[^py314-library-collections] Для FIFO-черги або sliding-window алгоритму, що додає/видаляє елементи на початку, `collections.deque` уникає цієї лінійної вартості. Використовуйте `list`, коли append/pop потрібні лише в кінці (стек) або потрібен O(1) доступ за індексом.

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
