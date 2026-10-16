---
id: py-stdlib-0006
title: "Чому `itertools.groupby()` групує лише consecutive equal keys і коли input потрібно попередньо відсортувати?"
track: python
section: standard-library
sources:
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
  - source_id: py314-library-datetime
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html
  - source_id: py314-library-re
    title: "Python 3.14: Library/re"
    url: https://docs.python.org/3.14/library/re.html
  - source_id: py314-library-itertools-groupby
    title: "Python 3.14: Library/itertools, groupby"
    url: https://docs.python.org/3.14/library/itertools.html#itertools.groupby
---

## Short answer

**`groupby()` створює нову групу щоразу, коли змінюється значення ключа – як Unix `uniq`, а не SQL `GROUP BY`.**[^py314-library-itertools-groupby] Однакові ключі мають іти поспіль: якщо вони розкидані по input, спершу відсортуйте дані за тим самим key function. Група є ітератором, що ділить underlying iterable з `groupby`; якщо дані потрібні пізніше, одразу зберігайте їх у `list`.[^py314-library-itertools-groupby]

## Detailed explanation

`groupby(iterable, key=None)` проходить вхідний iterable один раз і порівнює ключ кожного елемента з ключем попереднього. Коли ключ змінюється, починається нова група. Тому `groupby` бачить лише сусідні елементи, так само як Unix `uniq` бачить лише сусідні рядки.[^py314-library-itertools-groupby] У CPython ключі порівнюються оператором `==`; упорядкування (`<`) для цього не потрібне.

Документація зазвичай вимагає, щоб iterable уже був відсортований за тим самим key function.[^py314-library-itertools-groupby] Сортування – один зі способів зібрати однакові ключі поспіль, але не єдиний: достатньо, щоб вони вже йшли поспіль. Без сортування однаковий ключ розбивається на кілька груп, а словник втрачає дані:

```python
from itertools import groupby
from operator import itemgetter

data = ['b', 'a', 'a', 'b', 'b', 'c']
print([(k, list(g)) for k, g in groupby(data)])
# [('b', ['b']), ('a', ['a', 'a']), ('b', ['b', 'b']), ('c', ['c'])]

rows = [('b', 1), ('a', 2), ('b', 3)]
by_key = {k: [v for _, v in g] for k, g in groupby(rows, key=itemgetter(0))}
print(by_key)   # {'b': [3], 'a': [2]}: the first 'b' group was overwritten
rows.sort(key=itemgetter(0))
by_key = {k: [v for _, v in g] for k, g in groupby(rows, key=itemgetter(0))}
print(by_key)   # {'a': [2], 'b': [1, 3]}
```

Друга пастка – час життя групи. Група ділить стан із `groupby`, тож щойно `groupby` переходить до наступної групи, попередня стає порожньою. Список груп, зібраний без `list()`, містить порожні групи:

```python
from itertools import groupby

pairs = [(k, g) for k, g in groupby([1, 1, 2])]
print([(k, list(g)) for k, g in pairs])  # [(1, []), (2, [])]: a group is empty once groupby moves on
```

Правильна схема: дані сортуються за тим самим key або вже розташовані поспіль, а кожна група, яку треба зберегти, одразу перетворюється на `list`. Для агрегування без урахування порядку введення `groupby` не підходить: там потрібен словник, що накопичує значення, наприклад `defaultdict(list)` (див. qid:py-stdlib-0003).

**Типові помилки:**
- очікувати, що `groupby` об’єднає всі однакові ключі з усього input, як SQL `GROUP BY`;
- будувати словник із `groupby` без сортування: повторний ключ перезаписує попередню групу;
- зберігати групу як ітератор і читати її після переходу до наступної групи.
