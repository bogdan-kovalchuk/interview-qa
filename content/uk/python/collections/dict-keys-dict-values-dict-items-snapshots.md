---
id: py-coll-0017
title: "Чи є `dict.keys()`, `dict.values()` і `dict.items()` snapshots, і як їхня live-view природа впливає на подальші зміни словника?"
description: "Ні, це live views – вони миттєво відображають будь-які зміни словника, а не знімок на момент виклику."
track: python
section: collections
level: middle
type: mechanism
tags: [dict-keys, dict-values, dict-items]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L139-L153
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Ні, це live views – вони миттєво відображають будь-які зміни словника, а не знімок на момент виклику.**[^py314-library-stdtypes] Додавання або видалення key у словнику одразу видно через збережений об'єкт view. `dict.keys()` і `dict.items()` підтримують set-операції (union, intersection). <span class="warn">Зміна словника під час ітерації його view викликає `RuntimeError`.</span> Для snapshot потрібно явно створити копію: `list(d.keys())`.

## Detailed explanation

View-об'єкти реалізовані як тонкі C-структури, що тримають лише вказівник на сам словник, а не
копіюють ключі чи значення в момент створення.[^py314-library-stdtypes] Тому `len(d.keys())`
щоразу читає поточний розмір словника, а перевірка належності `key in d.keys()` працює через той
самий хеш-lookup, що й `key in d`, – O(1), а не лінійний прохід по збереженому списку.

Це принципова відмінність від Python 2, де `dict.keys()` повертав звичайний `list` – матеріалізовану
копію ключів на момент виклику; для великих словників це витрачало зайву пам'ять і час на побудову
списку, який часто був потрібен лише для одноразового проходу.

`dict.keys()` і `dict.items()` підтримують операції множин (`&`, `|`, `^`, `-`) саме тому, що
ключі словника за визначенням унікальні й hashable – той самий інваріант, що робить множину
множиною. `dict.values()` цих операцій не підтримує: значення можуть повторюватися і не зобов'язані
бути hashable, тож поводитися з ними як із множиною некоректно.

Практичне застосування set-семантики – знайти різницю між двома знімками стану:
`added = d2.keys() - d1.keys()` дає ключі, яких не було раніше, без побудови проміжних списків і
без циклів вручну.

Оскільки view прив'язаний до живого словника, ітерація по ньому одночасно зі зміною розміру
словника підпадає під те саме правило `RuntimeError: dictionary changed size during iteration`,
що й ітерація безпосередньо по словнику.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
