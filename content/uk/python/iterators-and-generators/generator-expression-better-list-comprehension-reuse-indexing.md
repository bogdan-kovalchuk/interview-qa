---
id: py-itergen-0016
title: "Коли generator expression кращий за list comprehension, а коли повторне використання або indexing робить list доречнішим?"
description: "Generator expression кращий для одного проходу по великій або нескінченній послідовності: він обчислює значення на запит і не зберігає всі результати."
track: python
section: iterators-and-generators
level: middle
type: comparison
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-generator-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-expressions
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, розділ generator expressions: результат є generator iterator, а вирази обчислюються ліниво, коли iterator просять віддати значення."
  - source_id: py314-library-stdtypes-generator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#generator-types
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, розділ Generator Types: generator object надає методи __iter__() і __next__()."
  - source_id: py314-reference-expressions-generator-iterator-methods
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-iterator-methods
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, розділ generator-iterator methods: методи send(), throw() і close() generator iterator."
---

## Short answer

**Generator expression кращий, коли потрібен один прохід по великій або нескінченній послідовності: він обчислює значення на запит і не зберігає всі результати.**[^py314-reference-expressions-generator-expressions] Після вичерпання generator більше нічого не віддає, тому повторне читання неможливе.[^py314-library-stdtypes-iterator-types] List comprehension доречніший, коли потрібні повторне читання, indexing (`lst[i]`), `len()`, slicing або збереження результатів: список тримає всі значення разом.

## Detailed explanation

Вибір стоїть між двома моделями. List comprehension одразу виконує весь цикл і повертає list з усіма значеннями. Generator expression повертає generator iterator, який обчислює наступне значення тільки тоді, коли його попросять через `next()` або під час `for`.[^py314-reference-expressions-generator-expressions] Тому generator не потребує пам’яті під усі результати, але не може відповісти на запити, які потребують усіх значень одразу.

Приклад показує це на короткій послідовності: у списку доступні індекс і `len()`, а generator після одного проходу порожній.

```python
values = [1, 2, 3]
as_list = [x * x for x in values]      # the list holds all three results
as_gen = (x * x for x in values)       # the generator computes values on demand

print(as_list[1], len(as_list))        # 4 3
print(sum(as_gen), sum(as_gen))        # 14 0: the second pass finds nothing left
# len(as_gen)                          # TypeError: object of type 'generator' has no len()
```

Економія пам’яті у generator реальна, але стосується лише результатів. Він тримає свій стан і посилання на вхідний iterable, тож якщо `values` сам є великим списком, його пам’ять нікуди не зникає. У CPython список із мільйона результатів займає суттєво більше пам’яті, ніж generator над тим самим входом; це можна перевірити через `tracemalloc`, але абсолютні числа залежать від платформи.

Тому list доречніший, коли результат читають кілька разів, звертаються за індексом або беруть `len()`. Ці можливості відсутні у generator не через брак пам’яті: generator object реалізує протокол iterator (`__iter__()` і `__next__()`)[^py314-library-stdtypes-generator-types] і не має `__len__()` чи `__getitem__()`; крім того, він має `send()`, `throw()` і `close()`.[^py314-reference-expressions-generator-iterator-methods] Після вичерпання він лишається порожнім.[^py314-library-stdtypes-iterator-types]

**Типові помилки:**
- брати generator expression для коду, який читає результати двічі: другий прохід порожній;
- вважати, що generator завжди швидший за list comprehension: він економить пам’ять, а не обов’язково час;
- передавати generator туди, де очікують `len()` або доступ за індексом, і отримувати `TypeError`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
