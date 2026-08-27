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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/sequences.md#L292-L321
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`list.sort()` сортує список на місці та повертає `None`; `sorted()` повертає новий відсортований список і приймає будь-який iterable.**[^py314-library-stdtypes] `sorted()` працює з рядками, generators, set тощо, тоді як `list.sort()` доступний лише для `list`. Обидва методи гарантовано стабільні. <span class="warn">`list.sort()` трохи швидший, бо не створює нового списку – використовуйте його, коли початковий список більше не потрібен у старому порядку.</span>

## Detailed explanation

Обидва алгоритми використовують Timsort – гібридний sort, що поєднує insertion sort для коротких
прогонів і merge sort для об'єднання вже впорядкованих ділянок, тому асимптотика однакова:
O(n log n) у гіршому випадку і O(n) на вже майже відсортованих даних.[^py314-howto-sorting]
Різниця – не в алгоритмі, а в тому, що саме сортується і куди йде результат.

`sorted()` приймає будь-який iterable – генератор, рядок, set, ключі словника – і завжди спершу
матеріалізує його в новий список, а вже потім сортує цю копію на місці; вихідний iterable
залишається незмінним (і, якщо це генератор, вичерпаним після одного проходу). `list.sort()`
існує лише як метод конкретного `list`, бо сортування на місці має сенс лише для мутабельної
структури з довільним доступом за індексом – для `tuple` чи рядка такого методу немає взагалі,
оскільки вони immutable.

Те, що `list.sort()` повертає `None`, а не сам список, – свідоме рішення: воно унеможливлює
ланцюжок на кшталт `x = x.sort()`, який виглядає як створення нової відсортованої змінної, а
насправді просто перезаписує `x` на `None`, знищуючи дані. Повертаючи `None`, API явно сигналізує,
що операція – мутація, а не побудова нового значення, і той самий стиль витримано в інших
in-place методах, наприклад `list.reverse()` чи `list.extend()`.

Продуктивність відрізняється передбачувано: `list.sort()` не виділяє пам'ять під новий список і не
копіює елементи, тому для великого списку, який більше не потрібен у старому порядку, він трохи
швидший і економніший за пам'яттю, ніж `sorted(x)`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
