---
id: py-coll-0012
title: "Які наслідки має custom `dict.__missing__()` і чому він не викликається однаково всіма способами доступу до key?"
description: "__missing__(key) викликається лише методом __getitem__(), коли key відсутній; get(), pop() та setdefault() його не викликають."
track: python
section: collections
level: senior
type: mechanism
tags: [dict-missing]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L173-L190
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`__missing__(key)` викликається лише методом `__getitem__()`, коли key відсутній; `get()`, `pop()` та `setdefault()` його не викликають.**[^py314-library-stdtypes] Це означає, що `d[missing_key]` запустить `__missing__`, а `d.get(missing_key)` поверне `None` (або вказаний default) без виклику `__missing__`. Саме на цьому механізмі побудований `collections.defaultdict`: його `__missing__` викликає `default_factory` і записує результат у словник.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
