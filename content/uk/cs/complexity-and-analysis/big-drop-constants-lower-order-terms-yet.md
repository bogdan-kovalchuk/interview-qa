---
id: cs-cmplx-0003
title: "Чому в Big O відкидають constants і lower-order terms, але вони все ще важливі для real input sizes?"
description: "Big O описує швидкість зростання при n -> нескінченність, коли домінантний член переважає над константами й доданками нижчого порядку."
track: cs
section: complexity-and-analysis
level: middle
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/algorithmes.md#L156-L161
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Big O описує швидкість зростання при n -> нескінченність, коли домінантний член переважає над константами й доданками нижчого порядку.**[^py314-library-collections] Наприклад, 3n² + 5n + 100 спрощується до O(n²), бо для великих n домінує квадратичний член. Однак для реальних скінченних input constant factor і доданки нижчого порядку визначають фактичний час виконання – алгоритм O(n²) з малою константою може випереджати O(n log n) на практичних значеннях n.

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
