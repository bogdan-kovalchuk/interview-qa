---
id: py-stdlib-0013
title: "Коли `heapq` доречніший за повне сортування для top-k або priority queue?"
description: "heapq дає O(log n) у найгіршому випадку для heappush/heappop, тоді як повне сортування – O(n log n); для top-k при малому k функції nlargest/nsmallest ефективніші за sorted()[:k]."
track: python
section: standard-library
level: middle
type: comparison
tags: [heapq]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-heapq
    title: "Python 3.14: Library/heapq"
    url: https://docs.python.org/3.14/library/heapq.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: heap[0] є найменшим елементом; nlargest і nsmallest еквівалентні sorted()[:n] та найкращі при малих n; при n==1 ефективніші min() і max(); для пріоритетної черги з рівними пріоритетами рекомендовано лічильник."
  - source_id: cpython-heapq-source
    title: "CPython Lib/heapq.py: heap queue implementation"
    url: https://github.com/python/cpython/blob/3.14/Lib/heapq.py
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Реалізація heapq у CPython 3.14: heappush піднімає елемент до кореня, heappop опускає елемент до листка й піднімає назад, nlargest тримає heap розміром n. Це опис CPython, а не гарантія мови."
  - source_id: cpython-listsort-notes
    title: "CPython Objects/listsort.txt: implementation notes for list.sort"
    url: https://github.com/python/cpython/blob/3.14/Objects/listsort.txt
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Нотатки CPython про list.sort: lg(n!) є інформаційною межею для сортування порівняннями в середньому. Це опис реалізації, а не гарантія мови."
---

## Short answer

**`heappush` і `heappop` у найгіршому випадку коштують O(log n).**[^cpython-heapq-source] Будь-яке сортування порівняннями в середньому потребує щонайменше порядку `n log n` порівнянь.[^cpython-listsort-notes] Для top-k при малому k `nlargest`/`nsmallest` ефективніші за `sorted()[:k]`; при великому k краще повне сортування, а при `n==1` ефективніші `min()`/`max()`.[^py314-library-heapq] Heap доречний, коли дані надходять потоком і потрібно постійно вставляти елементи та витягувати мінімум без пересортування всього масиву.

## Detailed explanation

`heapq` реалізує min-heap поверх звичайного списку: для кожного `k` виконується `heap[k] <= heap[2*k+1]` і `heap[k] <= heap[2*k+2]`, тож найменший елемент завжди в `heap[0]`.[^py314-library-heapq] `heappush` піднімає новий елемент до кореня, а `heappop` переносить останній елемент на місце кореня, опускає його до листка і піднімає назад. Обидві операції проходять шлях довжиною порядку log2(n), тому в найгіршому випадку кожна коштує O(log n).[^cpython-heapq-source]

Повне сортування зайве, якщо потрібен лише мінімум або k найбільших. `nlargest(k, data)` без `key` бере перші k елементів у heap, далі замінює найменший через `heapreplace` кожен більший елемент. Кожна заміна коштує O(log k), тож прохід займає O(n log k), а не O(n log n).[^cpython-heapq-source]

Приклад (виконано на CPython 3.13 і 3.14):

```python
import heapq

values = [42, 7, 99, 15, 63, 28]

# Top 3 in one pass: the same result as sorted(values, reverse=True)[:3].
print(heapq.nlargest(3, values))           # [99, 63, 42]

# A min-heap: heap[0] is the smallest item; each push or pop is O(log n) in the worst case.
heap = []
for v in values:
    heapq.heappush(heap, v)
print(heap[0])                             # 7
print(heapq.heappop(heap), heapq.heappop(heap))  # 7 15

# Equal priorities: a counter keeps tuples from comparing the task objects.
class Task:
    def __init__(self, name):
        self.name = name

tasks = []
for count, (priority, name) in enumerate([(2, "write"), (1, "fix"), (2, "reply")]):
    heapq.heappush(tasks, (priority, count, Task(name)))
print(heapq.heappop(tasks)[2].name)        # fix
print(heapq.heappop(tasks)[2].name)        # write

# Without the counter, equal priorities compare Task objects and fail.
bad = []
heapq.heappush(bad, (2, Task("a")))
try:
    heapq.heappush(bad, (2, Task("b")))
except TypeError as error:
    print(error)                           # '<' not supported between instances of 'Task' and 'Task'
```

Перший блок дає три найбільші значення; `heap[0]` – найменший елемент. У пріоритетній черзі кортеж `(priority, count, task)` розриває нічию лічильником, тож об’єкти задач не порівнюються. Без лічильника порівняння двох `Task` дає `TypeError`.[^py314-library-heapq]

**Типові помилки:**
- вважати, що `for x in heap` дає відсортований порядок: гарантовано найменший лише `heap[0]`;
- брати `nlargest` для великого k, коли `sorted()` за документацією ефективніший;
- класти в heap кортежі з однаковим пріоритетом і не порівнюваними об’єктами без лічильника.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
