---
id: py-coll-0003
title: "Яка різниця між `list.sort()` і `sorted()` щодо mutation, return value та допустимих input iterables?"
description: "list.sort() сортує список на місці та повертає None; sorted() повертає новий відсортований список і приймає будь-який iterable."
track: python
section: collections
level: middle
type: comparison
tags: [list-sort, sorted]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/sequences.md#L292-L321
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`list.sort()` сортує список на місці та повертає `None`; `sorted()` повертає новий відсортований список і приймає будь-який iterable.**[^py314-library-stdtypes] `sorted()` працює з рядками, generators, set тощо, тоді як `list.sort()` доступний лише для `list`. Обидва методи гарантовано стабільні. <span class="warn">`list.sort()` трохи швидший, бо не створює нового списку – використовуйте його, коли початковий список більше не потрібен у старому порядку.</span>

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
