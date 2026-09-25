---
id: py-coll-0001
title: "Коли tuple є кращим вибором за list не через syntax, а через семантику незмінної структури даних?"
description: "Tuple варто обирати, коли дані логічно є незмінним записом (record) – його immutability сигналізує про намір і дозволяє використовувати tuple як dict key або елемент set."
track: python
section: collections
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-27
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
---

## Short answer

**Tuple варто обирати, коли дані логічно є незмінним записом (record) – його immutability сигналізує про намір і дозволяє використовувати tuple як dict key або елемент set.**[^py314-library-stdtypes] Наприклад, координати `(x, y)`, row tuple з БД, або складений ключ словника. <span class="warn">Якщо всередині tuple є mutable об'єкт (наприклад `list`), його вміст можна змінити – сам tuple залишається тим самим об'єктом з тим самим `id`.</span>

## Detailed explanation

Семантична різниця між `tuple` та `list` полягає в призначенні: `list` моделює змінну однорідну послідовність елементів (де порядок чи розмір можуть динамічно змінюватися), тоді як `tuple` призначений для фіксованих неоднорідних записів (records), де кожна позиція має специфічне змістове навантаження.[^py314-library-stdtypes]

Незмінність (`immutability`) кортежу несе чіткий інженерний намір: передача `tuple` у сторонні функції або між модулями гарантує захист від побічних ефектів, оскільки викликаний код не може випадково додати, видалити чи перевпорядкувати елементи. Важливим наслідком незмінності є гешованість (`hashability`): якщо всі складові елементи кортежу є незмінними та гешованими, сам `tuple` стає гешованим.[^py314-library-stdtypes] Це дозволяє використовувати кортежі як складені ключі в словниках (`dict`) або додавати їх до множин (`set`), що принципово неможливо для `list` (який завжди викидає `TypeError: unhashable type: 'list'`).

З точки зору організації пам'яті CPython оптимізує кортежі: оскільки їхній розмір зафіксований на момент створення, вони не виділяють надлишкового буфера пам'яті (over-allocation), який обов'язково резервується для динамічного зростання списків. Крім того, CPython кешує виділені структури для невеликих кортежів для повторного використання. Проте незмінність кортежу є поверхневою (shallow immutability): кортеж блокує переприв'язку лише своїх власних посилань на комірки. Якщо комірка вказує на змінюваний об'єкт (наприклад, список або словник), стан цього вкладеного об'єкта можна вільно модифікувати in-place, і такий кортеж втрачає властивість гешованості.

Різниця між семантикою запису, ключами словника та shallow immutability:

```python
# 1. Semantic distinction: tuple represents a fixed heterogeneous record
user_record = ("usr_101", "alice@example.com", 30)

# 2. Hashability enables using tuples as composite dictionary keys:
cache: dict[tuple[str, int], str] = {}
cache[("GET", 200)] = "OK"

# A list cannot be hashed because it is mutable:
try:
    cache[["GET", 200]] = "FAIL"  # type: ignore[index]
except TypeError as exc:
    print(exc)  # unhashable type: 'list'

# 3. Shallow immutability: fixed slot bindings, but mutable contents:
nested: tuple[int, list[str]] = (1, ["read"])
nested[1].append("write")
print(nested)  # (1, ['read', 'write'])
```

**Практичні висновки та підводні камені:**
- використання списків замість кортежів для фіксованих структур (наприклад, координат точки чи конфігураційних параметрів) відкриває шлях до випадкової мутації коду іншими частинами системи;
- очікування повної незмінності від `tuple`, який містить змінювані елементи (`list`, `dict`, `set`), що також унеможливлює його використання в ролі ключа словника;
- недооцінка захисного проектування: використання `tuple` як типу повернення функцій гарантує клієнтському коду, що колекція не зміниться;
- заміна `tuple` на `list` заради незначних зручностей синтаксису, коли семантично структура є фіксованим кортежем значень.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
