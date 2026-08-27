---
id: py-coll-0006
title: "Що саме гарантує insertion order словника в сучасному Python і чого ця гарантія не говорить про внутрішню hash table?"
description: "Починаючи з Python 3.7, dict зберігає елементи в порядку вставки – це гарантія мови, а не деталь реалізації."
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
applies_to:
  - product: "CPython"
    version: "3.14"
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L293-L387
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Починаючи з Python 3.7, `dict` зберігає елементи в порядку вставки – це гарантія мови, а не деталь реалізації.**[^py314-library-stdtypes] Гарантія стосується порядку ітерації (`keys()`, `values()`, `items()`), але не розкриває структуру hash table. У CPython це реалізовано через компактну таблицю з масивом індексів і масивом записів; інші реалізації Python можуть досягти того ж порядку іншим шляхом.

## Detailed explanation

Гарантія стосується виключно порядку ітерації: якщо вставити ключі `a`, `b`, `c`, то `keys()`,
`values()`, `items()` і сам `for k in d` завжди пройдуть саме в цьому порядку. Вона нічого не каже
про те, куди фізично потрапляє запис усередині hash table, який саме `hash()` мають ключі чи в
якому бакеті лежить кожен з них – це деталь реалізації, і вона може відрізнятися між процесами
через `PYTHONHASHSEED`.

У CPython (з 3.6 як деталь реалізації, з 3.7 як гарантія мови) `dict` фізично складається з двох
масивів: щільного масиву записів (ключ, значення, hash), куди нові пари додаються в кінець, і
розрідженого індекс-масиву, що мапить `hash(key)` на позицію в щільному масиві.[^py314-library-stdtypes]
Ітерація йде по щільному масиву послідовно, тому порядок вставки зберігається автоматично, а
пошук за ключем усе одно йде через індекс-масив і `hash()`, тобто швидкість lookup не залежить від
порядку вставки.

Звідси дві нетривіальні деталі поведінки. По-перше, оновлення значення для вже наявного ключа
(`d[k] = new_value`) не змінює його позицію в порядку ітерації. По-друге, видалення ключа й
повторна вставка того самого ключа переносить його в кінець – це вже нова позиція, а не
відновлення старої, бо запис у щільному масиві створюється заново.

Порядок ітерації – частина поведінки, але не частина семантики рівності: `dict.__eq__` порівнює
лише набори пар ключ-значення, тому `{'a': 1, 'b': 2} == {'b': 2, 'a': 1}` дає `True`, хоча
порядок ітерації в них різний. Саме тому інші реалізації Python (наприклад PyPy) можуть
дотримуватися тієї самої мовної гарантії порядку вставки, використовуючи зовсім іншу внутрішню
структуру hash table – гарантується поведінка, а не конкретний layout у пам'яті.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
