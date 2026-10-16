---
id: py-coll-0015
title: "Як set operations дозволяють виразити перевірку subset/superset без ручних nested loops?"
track: python
section: collections
sources:
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
  - source_id: py314-howto-sorting
    title: "Python 3.14: Howto/sorting"
    url: https://docs.python.org/3.14/howto/sorting.html
---

## Short answer

**Оператори `<=` (`issubset`) і `>=` (`issuperset`) виконують перевірку включення всіх елементів за один виклик, без явних циклів.**[^py314-library-stdtypes] `a <= b` повертає `True`, якщо кожен елемент `a` міститься в `b`. Оператор `<` – strict (proper) subset: `a < a` дає `False`, тоді як `a <= a` – `True`. Це працює за O(len(a)) у середньому, бо кожен `in` для set – O(1).

## Detailed explanation

Ключова відмінність між методами (`issubset`, `issuperset`) і операторами (`<=`, `>=`) – у типі
допустимого аргумента. `a.issubset(b)` приймає будь-який iterable для `b` (список, кортеж,
генератор) і сам перетворює його на set перед перевіркою, тоді як оператор `a <= b` вимагає, щоб
`b` теж був set (або frozenset) – для довільного iterable він підійме `TypeError`, бо `<=`
визначений через `__le__`/`__ge__` саме для типу set, а не для протоколу iterable.[^py314-library-stdtypes]

Реалізаційно перевірка `a <= b` (subset) ітерує саме по `a` і для кожного елемента виконує `in b` –
членство в set-і O(1) у середньому, тому загальна складність O(len(a)), незалежно від розміру `b`.
Це асиметрично: `a <= b` і `b >= a` еквівалентні за результатом, але обидва виконують ітерацію по
меншому за семантикою операнду (`a`), а не по більшому.

Практична перевага перед ручними вкладеними циклами не лише в стислості запису, а й у складності:
наївна перевірка "кожен елемент a є в b" через вкладений цикл по списках дає O(len(a) * len(b)),
тоді як set-based перевірка – O(len(a)) завдяки хеш-таблиці всередині `b`.

Строгі варіанти `<` і `>` (proper subset/superset) додають умову нерівності множин: `a < b` істинне,
якщо `a <= b` і `a != b`. На відміну від `issubset`/`issuperset`, для строгих операторів немає
окремого методу – `a < b` доступне лише як оператор, а еквівалент через методи потрібно писати
вручну: `a.issubset(b) and a != b`.[^py314-library-collections]
