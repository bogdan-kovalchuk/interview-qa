---
id: py-coll-0016
title: "Чому некоректний `__eq__` у custom objects може призвести до несподіваних результатів membership у set?"
description: "Set шукає елемент спочатку за hash() (bucket), потім порівнює __eq__; якщо __eq__ і __hash__ неузгоджені, membership дає хибні результати."
track: python
section: collections
level: senior
type: pitfall
tags: [eq]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L388-L440
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Set шукає елемент спочатку за `hash()` (bucket), потім порівнює `__eq__`; якщо `__eq__` і `__hash__` неузгоджені, membership дає хибні результати.**[^py314-library-stdtypes] Контракт: `a == b` -> `hash(a) == hash(b)`. Якщо `__eq__` повертає `True`, але `hash()` різний, set не знайде об'єкт у правильному bucket – `b in {a}` поверне `False`, хоча `a == b`. <span class="warn">Завжди визначайте `__hash__` і `__eq__` разом, використовуючи одні й ті самі поля.</span>

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
