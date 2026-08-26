---
id: cs-dstruct-0001
title: "Коли для потоку jobs обрати hash table для lookup by ID, а коли min-heap для постійного вилучення найменшого priority?"
description: "dict дає O(1) середню складність пошуку за ключем; min-heap на основі heapq дає O(log n) для push/pop і O(1) для перегляду найменшого елемента."
track: cs
section: data-structures
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/data_structures.md#L85-L154
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`dict` дає O(1) середню складність пошуку за ключем; min-heap на основі `heapq` дає O(log n) для push/pop і O(1) для перегляду найменшого елемента.**[^py314-library-collections] Обирайте hash table, коли основна операція – пошук або оновлення job за унікальним ID. Обирайте min-heap, коли потрібно постійно вилучати job з найменшим priority – heap не підтримує O(1) довільний пошук за ID.

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
