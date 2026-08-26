---
id: py-coll-0008
title: "Чим `d[key]`, `d.get(key)` і `setdefault()` відрізняються за поведінкою при відсутньому key та можливими side effects?"
description: "d[key] викликає KeyError; d.get(key) повертає None (або переданий default) без побічних ефектів; d.setdefault(key, default) вставляє default у словник, якщо ключ відсутній, і повертає його."
track: python
section: collections
level: middle
type: comparison
tags: [d-key, d-get-key, setdefault]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L118-L138
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`d[key]` викликає `KeyError`; `d.get(key)` повертає `None` (або переданий default) без побічних ефектів; `d.setdefault(key, default)` вставляє `default` у словник, якщо ключ відсутній, і повертає його.**[^py314-library-stdtypes] Метод <span class="warn">`setdefault()` завжди обчислює аргумент `default`, навіть коли ключ існує – це може бути небажаним side effect, якщо створення default дороге.</span>

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
