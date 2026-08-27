---
id: py-coll-0013
title: "Коли `set` є кращим за list для membership checks і який порядок елементів не слід використовувати як контракт?"
description: "set дає average-case O(1) для in завдяки hash-таблиці, тоді як list – O(n); тому для частих перевірок membership set значно швидший."
track: python
section: collections
level: middle
type: comparison
tags: [set]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L17-L35
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`set` дає average-case O(1) для `in` завдяки hash-таблиці, тоді як list – O(n); тому для частих перевірок membership set значно швидший.**[^py314-library-stdtypes] <span class="warn">Порядок ітерації set є implementation-dependent і не гарантує ні сортування, ні порядку вставки – його не можна використовувати як контракт.</span> На практиці: якщо потрібен і швидкий lookup, і стабільний порядок, використовують dict (з Python 3.7+ зберігає порядок вставки) або list з попереднім індексуванням.

## Detailed explanation

Швидкість `in` для `set` пояснюється прямим доступом за хешем: `hash(x)` обчислює позицію в
хеш-таблиці, і перевірка присутності зводиться до порівняння за цією позицією (з обробкою
колізій), тоді як `list` не має структури для прямого доступу за значенням і змушений послідовно
порівнювати кожен елемент.[^py314-library-stdtypes] Середній випадок O(1) для set тримається, поки
хеш-функція рівномірно розподіляє значення; за навмисно підібраних (adversarial) даних або великої
кількості колізій складність може деградувати до O(n), хоча на практиці для вбудованих типів це
рідкість.

Плата за швидкість – вимога хешованості: елементи `set` мають реалізовувати `__hash__` і `__eq__`
узгоджено (рівні об'єкти мають однаковий хеш), тому `list` чи `dict` не можуть бути елементами set,
а `int`, `str`, `tuple` (з хешованим вмістом) – можуть. `list` цієї вимоги не має і допускає mutable
елементи та дублікати.

Порядок ітерації `set` не варто плутати з порядком ітерації `dict`: починаючи з Python 3.7 `dict`
гарантовано зберігає порядок вставки як частину мовної специфікації, а `set` такої гарантії ніколи
не мав і не має – видима послідовність елементів залежить від їхніх хеш-значень і історії
вставок/видалень, і для рядків вона додатково змінюється між запусками процесу через рандомізацію
хешів (`PYTHONHASHSEED`).[^py314-library-collections] Тому код, що покладається на конкретний
порядок обходу set, може працювати сьогодні і ламатися на іншій версії Python чи іншому запуску –
це не гарантія, а випадковий побічний ефект реалізації.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
