---
id: py-coll-0011
title: "Як dict union operators `|` і `|=` вирішують конфлікти однакових keys та чим відрізняються за mutation?"
description: "Обидва оператори при дублікаті keys залишають значення з правого операнда; | повертає новий dict, а |= оновлює лівий in-place."
track: python
section: collections
level: middle
type: comparison
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L118-L138
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Обидва оператори при дублікаті keys залишають значення з правого операнда; `|` повертає новий dict, а `|=` оновлює лівий in-place.**[^py314-library-stdtypes] `d1 | d2` створює новий словник, `d1` не змінюється. `d1 |= d2` еквівалентний `d1.update(d2)` – модифікує `d1` на місці. Порядок keys у результаті: спочатку keys з лівого операнда в їхньому порядку, потім нові keys з правого.

## Detailed explanation

Оператори `|` і `|=` для `dict` зʼявилися в Python 3.9 (PEP 584) як синтаксичний аналог операцій
над множинами – до цього злиття словників робили через `{**d1, **d2}` або `dict(d1, **d2)`, обидва
варіанти менш очевидні для читання.[^py314-library-stdtypes]

Є асиметрія в тому, що приймає кожен оператор: `d1 | d2` вимагає, щоб правий операнд був `dict`
(або підтримував `keys()` як mapping) – інакше `TypeError`. А `d1 |= d2` реалізований через
`__ior__`, що для `dict` фактично викликає `update()`, тому приймає значно ширший діапазон типів:
будь-який iterable пар `(key, value)`, не лише mapping. Ця асиметрія повторює відому пару
`list.__add__` проти `list.__iadd__`, де `+=` теж приймає довільний iterable, а `+` – лише той
самий тип.

Позиція ключа в результаті визначається лише порядком першої появи: `d1 | d2` еквівалентний
побудові копії `d1` з подальшим `update(d2)`, тому наявні ключі з `d1` зберігають свою позицію в
порядку ітерації, навіть якщо їхнє значення перезаписане значенням з `d2`; нові ключі з `d2`
додаються в кінець у порядку їхньої появи в `d2`.

На відміну від `dict.update()`, який завжди мутує `self` і повертає `None`, `d1 | d2` – вираз, що
можна одразу передати далі як аргумент, не створюючи проміжну named-змінну.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
