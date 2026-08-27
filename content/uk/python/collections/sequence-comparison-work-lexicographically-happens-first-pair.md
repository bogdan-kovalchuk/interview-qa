---
id: py-coll-0019
title: "Як sequence comparison працює lexicographically і що станеться при першій парі елементів, які не підтримують ordering?"
description: "Послідовності порівнюються лексикографічно: елемент за елементом, поки не знайдеться перша нерівна пара – вона й визначає результат."
track: python
section: collections
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/sequences.md#L503-L516
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Послідовності порівнюються лексикографічно: елемент за елементом, поки не знайдеться перша нерівна пара – вона й визначає результат.**[^py314-library-stdtypes] Якщо всі спільні елементи рівні, коротша послідовність вважається меншою: `[1, 2] < [1, 2, 3]` -> `True`. Якщо пара елементів не підтримує ordering (наприклад, `int` і `str`), виникає `TypeError`. Порівняння різних типів послідовностей (`list` vs `tuple`) також викликає `TypeError`.

## Detailed explanation

Механізм лексикографічного порівняння працює як послідовний обхід елементів обох послідовностей
парами: спочатку перевіряється рівність поточної пари через `__eq__`; якщо пара рівна, порівняння
переходить до наступної пари без виклику `__lt__`. Лише коли знайдено першу нерівну пару, результат
порівняння всієї послідовності визначається результатом порівняння саме цієї пари через `__lt__`
(або відповідний rich comparison метод).[^py314-library-stdtypes] Це дає складність
O(min(len(a), len(b))) у гіршому випадку – обхід зупиняється щойно знайдено розбіжність, і не
обов'язково доходить до кінця коротшої послідовності.

Важливо розрізняти `==` і порядкові оператори (`<`, `<=`, `>`, `>=`). Рівність (`==`) між
послідовностями різних типів, наприклад `list` і `tuple`, не викликає виняток – вона просто
повертає `False`, бо `==` не вимагає сумісності типів, лише порівнюваності елементів попарно. А от
`<` між `list` і `tuple` завжди підіймає `TypeError`, незалежно від вмісту, бо сам тип
послідовності є частиною контракту порядкових операторів, а не лише елементи всередині.[^py314-howto-sorting]

Ця сама механіка лежить в основі того, як `sorted()` і `list.sort()` порівнюють кортежі-ключі при
multi-key сортуванні: `(1, 'b') < (1, 'a')` порівнює перші елементи, бачить рівність, переходить до
других і порівнює вже їх. Якщо на якомусь кроці елементи не підтримують `__lt__` один з одним
(наприклад `int` і `str`), виняток `TypeError` виникає саме в момент порівняння цієї конкретної
пари, а не на початку виклику – тобто префікс послідовностей, який складається з порівнюваних
елементів, встигає безпечно оброблятися.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
