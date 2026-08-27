---
id: py-coll-0014
title: "Чим `set` відрізняється від `frozenset` щодо mutability та можливості бути елементом іншого set?"
description: "set – mutable і не hashable, тому не може бути елементом іншого set; frozenset – immutable й hashable, тому може."
track: python
section: collections
level: middle
type: comparison
tags: [set, frozenset]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L36-L70
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`set` – mutable і не hashable, тому не може бути елементом іншого set; `frozenset` – immutable й hashable, тому може.**[^py314-library-stdtypes] Спроба додати `set` у інший set викличе `TypeError: unhashable type: 'set'`. `frozenset` підтримує ті самі set-операції (union, intersection, subset), але не має методів `add()`, `remove()`.

## Detailed explanation

Причина заборони – не довільне обмеження, а необхідна умова коректності хеш-таблиці: хеш об'єкта
визначає, у яку комірку (bucket) його розміщено, і ця комірка не змінюється, поки об'єкт лежить у
хеш-таблиці. Якби `set` був хешованим і його можна було мутувати після додавання в іншу структуру,
зміна вмісту змінила б і хеш – об'єкт залишився б у старій комірці, але пошук за новим хешем більше
не знаходив би його; хеш-таблиця стала б неузгодженою.[^py314-library-stdtypes] Тому Python свідомо
не визначає `__hash__` для mutable `set`, і спроба `{1, 2}` як елемента іншого set одразу підіймає
`TypeError: unhashable type: 'set'`, а не мовчки ламає структуру.

`frozenset` розв'язує це, фіксуючи вміст на момент створення: після конструювання додати чи видалити
елемент неможливо, тому його хеш можна обчислити один раз і покладатися на нього назавжди. Це робить
`frozenset` придатним і як елемент іншого set, і як ключ dict – там, де потрібна множина-значення,
яка сама бере участь у хешованій структурі.

Операційно `frozenset` підтримує всі ті самі бінарні операції, що й `set` – `union`, `intersection`,
`difference`, `symmetric_difference`, а також оператори `|`, `&`, `-`, `^` і порівняння
subset/superset – але кожна з них повертає новий `frozenset`, а не змінює наявний.[^py314-library-collections]
Методів, що мутують на місці (`add`, `remove`, `discard`, `update`, `pop`, `clear`), у `frozenset`
просто немає – це узгоджено з тим, що immutability є не рекомендацією, а гарантією типу.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
