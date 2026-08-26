---
id: cs-algo-0003
title: "Як мемоїзація або bottom-up dynamic programming змінює complexity recursive solution з overlapping subproblems?"
description: "Мемоїзація або bottom-up DP зводить рекурсію з експоненційним часом і overlapping subproblems до поліноміального часу, розв'язуючи кожен унікальний subproblem лише один раз."
track: cs
section: algorithms
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/computer_science/algorithmes.md#L516-L530
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Мемоїзація або bottom-up DP зводить рекурсію з експоненційним часом і overlapping subproblems до поліноміального часу, розв'язуючи кожен унікальний subproblem лише один раз.**[^py314-library-collections] Наприклад, наївний рекурсивний Fibonacci має складність O(2^n), але з таблицею memo кожен з n subproblems обчислюється один раз – це дає O(n) часу і O(n) пам'яті. Компроміс – додаткова пам'ять під кеш замість повторних обчислень.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
