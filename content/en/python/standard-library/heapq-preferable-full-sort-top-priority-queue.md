---
id: py-stdlib-0013
title: "When is `heapq` preferable to a full sort for top-k or a priority queue?"
description: "When is `heapq` preferable to a full sort for top-k or a priority queue?"
track: python
section: standard-library
level: middle
type: comparison
tags: [heapq]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-heapq
    title: "Python 3.14: Library/heapq"
    url: https://docs.python.org/3.14/library/heapq.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: heap[0] is the smallest item; nlargest and nsmallest are equivalent to sorted()[:n] and perform best for small n; for n==1, min() and max() are more efficient; a counter is recommended for a priority queue with equal priorities."
  - source_id: cpython-heapq-source
    title: "CPython Lib/heapq.py: heap queue implementation"
    url: https://github.com/python/cpython/blob/3.14/Lib/heapq.py
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "CPython 3.14 implementation of heapq: heappush sifts an element up towards the root, heappop sifts an element down to a leaf and back up, nlargest keeps a heap of size n. This describes CPython, not a language guarantee."
  - source_id: cpython-listsort-notes
    title: "CPython Objects/listsort.txt: implementation notes for list.sort"
    url: https://github.com/python/cpython/blob/3.14/Objects/listsort.txt
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "CPython notes on list.sort: lg(n!) is the information-theoretic limit for comparison sorting on average. This describes the implementation, not a language guarantee."
---

## Short answer

**In the worst case, `heappush` and `heappop` cost O(log n).**[^cpython-heapq-source] Any comparison sort needs at least on the order of `n log n` comparisons on average.[^cpython-listsort-notes] For top-k with a small k, `nlargest`/`nsmallest` beat `sorted()[:k]`; for a large k a full sort is better, and for `n==1`, `min()`/`max()` are more efficient.[^py314-library-heapq] A heap fits data that arrives as a stream and must support repeated insertions and minimum extraction without re-sorting the whole list.

## Detailed explanation

`heapq` implements a min-heap on a plain list: for every `k`, `heap[k] <= heap[2*k+1]` and `heap[k] <= heap[2*k+2]` hold, so the smallest element is always at `heap[0]`.[^py314-library-heapq] `heappush` appends the element and sifts it up towards the root while its parent is larger. `heappop` removes the root, moves the last element into its place, sifts it down to a leaf, and then sifts it back up to its correct position. Both operations follow a path of length on the order of log2(n), so each costs O(log n) in the worst case.[^cpython-heapq-source]

A full sort is wasteful when you need only the minimum or the k largest items. `nlargest(k, data)` without a `key` takes the first k elements into a heap, and then each element larger than the smallest one in the heap replaces it through `heapreplace`. Each replacement costs O(log k), so the whole pass takes O(n log k), not the O(n log n) of a full sort.[^cpython-heapq-source]
An example, run on CPython 3.13 and 3.14:

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

The first block returns the three largest values, and `heap[0]` is the smallest element. In a priority queue, the tuples `(priority, count, task)` break ties with the counter: for equal priorities the smaller counter comes out first, and the task objects are never compared. Without the counter, comparing two `Task` objects raises `TypeError`.[^py314-library-heapq]

**Common mistakes:**
- assuming that `for x in heap` gives a sorted order: only `heap[0]` is guaranteed to be the smallest;
- using `nlargest` for a large k, where `sorted()` is more efficient according to the documentation;
- putting tuples with equal priorities and non-comparable objects into a heap without a counter.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
