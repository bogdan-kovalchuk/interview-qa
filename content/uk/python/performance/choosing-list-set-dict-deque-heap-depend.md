---
id: py-perf-0006
title: "Як вибір між `list`, `set`, `dict`, `deque` та heap впливає на dominant operations workload?"
description: "Вибір контейнера залежить від домінантної операції: deque дає O(1) на обох кінцях, heapq тримає мінімум у heap[0], а list перевіряє належність перебором."
track: python
section: performance
level: middle
type: comparison
tags: [list, set, dict, deque]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-collections-deque
    title: "Python 3.14: Library/collections, deque"
    url: https://docs.python.org/3.14/library/collections.html#collections.deque
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Документація collections.deque (Python 3.14): додавання й видалення з обох кінців мають приблизно однакову O(1) вартість; list має O(n) вартість переміщення для pop(0) і insert(0, v)."
  - source_id: py314-library-heapq
    title: "Python 3.14: Library/heapq"
    url: https://docs.python.org/3.14/library/heapq.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Документація heapq (Python 3.14): найменший елемент доступний як heap[0] без вилучення (опис heappop)."
  - source_id: cpython-heapq-source
    title: "CPython Lib/heapq.py: heap queue implementation"
    url: https://github.com/python/cpython/blob/3.14/Lib/heapq.py
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Реалізація heapq у CPython 3.14: heappush піднімає елемент до кореня, heappop опускає елемент до листа і піднімає його назад, nlargest тримає купу розміру n. Опис CPython, не гарантія мови."
  - source_id: py314-reference-expressions-membership-test-operations
    title: "Python 3.14: Reference/expressions, membership test operations"
    url: https://docs.python.org/3.14/reference/expressions.html#membership-test-operations
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Довідник мови Python 3.14, операції належності: для list, tuple, set, frozenset, dict і collections.deque вираз x in y еквівалентний any(x is e or x == e for e in y). Не описує складність."
---

## Short answer

**Вибір залежить від домінантної операції: `deque` дає приблизно однакову O(1) вартість додавання й видалення з обох кінців, тоді як `list` має O(n) вартість для `pop(0)` і `insert(0, v)`.**[^py314-library-collections-deque] `x in list` перевіряє елементи по одному.[^py314-reference-expressions-membership-test-operations] `set` і `dict` шукають за хешем, у середньому за O(1); це середній випадок хеш-таблиці, який документація Python для set і dict не задає. `heapq` тримає найменший елемент у `heap[0]`.[^py314-library-heapq] Вилучення найменшого та додавання елемента в CPython виконуються за O(log n).[^cpython-heapq-source]

## Detailed explanation

Контейнер вибирають не за загальною швидкістю, а за тим, які операції в workload повторюються найчастіше. Для `list` вираз `x in y` за визначенням мови еквівалентний `any(x is e or x == e for e in y)`, тобто є перебором елементів.[^py314-reference-expressions-membership-test-operations] Перевірка належності в гарячому циклі на великому `list` тому має лінійну вартість на кожен виклик.

`deque` створено для черг: додавання й видалення з обох кінців мають приблизно однакову O(1) вартість, тоді як `list.pop(0)` і `insert(0, v)` змушують зсувати всі елементи.[^py314-library-collections-deque] Нижче приклад вибору контейнера для черги, для перевірки належності та для мінімуму; `#` коментарі показують результат і пастку:

```python
from collections import deque
import heapq

jobs = [3, 1, 2]
queue = deque(jobs)
print(queue.popleft(), queue)      # 3 deque([1, 2]): O(1) at the left end
jobs.pop(0)                        # list: removing the head shifts every item, O(n)

allowed_list = ['alice', 'bob', 'carol']
allowed_set = set(allowed_list)
print('carol' in allowed_list)    # True, found by scanning items one by one
print('carol' in allowed_set)     # True, found by hashing

heap = [5, 1, 4]
heapq.heapify(heap)
print(heap[0])                     # 1: the smallest item, without removing it
print(heapq.heappop(heap), heap)   # 1 [4, 5]: removal is logarithmic
```

`set` і `dict` шукають елемент за хешем, і в середньому це стала кількість кроків, а не перебір. Це властивість середнього випадку хеш-таблиці, а не гарантія для будь-яких даних; документація Python для set і dict такої складності не задає. `heapq` дає найменший елемент через `heap[0]`.[^py314-library-heapq] Вилучення й додавання виконуються за O(log n), бо цикли в CPython ідуть по шляху від кореня до листа або назад, тобто по висоті дерева.[^cpython-heapq-source] Але купа впорядкована лише вздовж шляхів від кореня, тому конкретне значення в ній знаходиться тільки перебором.

Вибір міняється разом із домінантною операцією. Якщо найчастіше перевіряють належність, потрібні `set` або `dict`; якщо важливі краї черги, `deque`; якщо важливий мінімум, `heapq`. Для малих колекцій різниця може бути несуттєвою, тож рішення варто перевірити на реальних розмірах.

**Типові помилки:**
- `x in list` у гарячому циклі замість `set`, коли потрібна перевірка належності;
- `list.pop(0)` як черга замість `deque.popleft()`;
- очікувати від `heapq` швидкого пошуку довільного елемента: через `heap[0]` доступний лише мінімум.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
