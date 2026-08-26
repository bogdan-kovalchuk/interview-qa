---
id: py-coll-0010
title: "Чому зміна розміру словника під час ітерації його keys може завершитися помилкою, тоді як зміна value наявного key часто допустима?"
description: "Ітерація по словнику фіксує його розмір (кількість key-слотів); додавання або видалення ключа змінює цей розмір і викликає RuntimeError: dictionary changed size during iteration."
track: python
section: collections
level: senior
type: pitfall
tags: []
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L154-L172
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Ітерація по словнику фіксує його розмір (кількість key-слотів); додавання або видалення ключа змінює цей розмір і викликає `RuntimeError: dictionary changed size during iteration`.**[^py314-library-stdtypes] Зміна значення наявного ключа не змінює розмір таблиці, тому не порушує ітерацію. Безпечний патерн – ітерувати копію ключів: `for k in list(d):`.

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
