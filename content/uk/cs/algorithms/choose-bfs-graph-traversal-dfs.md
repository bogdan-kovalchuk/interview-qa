---
id: cs-algo-0002
title: "Коли для graph traversal обрати BFS, а коли DFS?"
description: "BFS обходить граф рівень за рівнем через queue і знаходить найкоротший шлях у неважених графах; DFS йде вглиб через stack і використовує менше пам'яті на широких графах."
track: cs
section: algorithms
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/algorithmes.md#L416-L436
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**BFS обходить граф рівень за рівнем через queue і знаходить найкоротший шлях у неважених графах; DFS йде вглиб через stack і використовує менше пам'яті на широких графах.**[^py314-library-collections] Обирайте BFS, коли потрібен найкоротший шлях або обхід за рівнями. Обирайте DFS для topological sorting, виявлення циклів або коли ціль глибоко, а граф широкий – пам'ять DFS становить O(depth) проти O(width) у BFS.

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
