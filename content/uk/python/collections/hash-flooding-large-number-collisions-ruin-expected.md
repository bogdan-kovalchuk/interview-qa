---
id: py-coll-0024
title: "Чому hash-flooding або велика кількість collisions може зруйнувати expected O(1) lookup і чому це не змінює логічний contract словника?"
description: "Hash-flooding – це ситуація, коли багато ключів потрапляють в один бакет hash-таблиці, і lookup деградує з average O(1) до O(n) через довгі probe-послідовності."
track: python
section: collections
level: senior
type: mechanism
tags: []
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L441-L511
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Hash-flooding – це ситуація, коли багато ключів потрапляють в один бакет hash-таблиці, і lookup деградує з average O(1) до O(n) через довгі probe-послідовності.**[^py314-library-stdtypes] У CPython dict і set використовують open addressing, тому collision-и змушують інтерпретатор шукати вільний слот зондуванням. Логічний contract словника при цьому не порушується: `__eq__` перевіряється для кожного кандидата в бакеті, тому правильний ключ знаходиться – змінюється лише швидкодія, а не коректність.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
