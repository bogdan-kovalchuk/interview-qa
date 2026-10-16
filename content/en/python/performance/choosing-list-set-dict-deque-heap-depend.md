---
id: py-perf-0006
title: "How does choosing between `list`, `set`, `dict`, `deque`, and a heap depend on the workload's dominant operations?"
track: python
section: performance
sources:
  - source_id: py314-library-collections-deque
    title: "Python 3.14: Library/collections, deque"
    url: https://docs.python.org/3.14/library/collections.html#collections.deque
  - source_id: py314-library-heapq
    title: "Python 3.14: Library/heapq"
    url: https://docs.python.org/3.14/library/heapq.html
  - source_id: cpython-heapq-source
    title: "CPython Lib/heapq.py: heap queue implementation"
    url: https://github.com/python/cpython/blob/3.14/Lib/heapq.py
  - source_id: py314-reference-expressions-membership-test-operations
    title: "Python 3.14: Reference/expressions, membership test operations"
    url: https://docs.python.org/3.14/reference/expressions.html#membership-test-operations
---

## Short answer

**The choice depends on the dominant operation: `deque` gives approximately the same O(1) cost at either end, while `list` costs O(n) for `pop(0)` and `insert(0, v)`.**[^py314-library-collections-deque] `x in list` checks the items one by one.[^py314-reference-expressions-membership-test-operations] `set` and `dict` look items up by hash, on average in O(1), an average-case property that the Python documentation does not state for them. `heapq` keeps the smallest item at `heap[0]`.[^py314-library-heapq] Removal and insertion take O(log n) in CPython.[^cpython-heapq-source]

## Detailed explanation

Containers are chosen not by overall speed, but by which operations the workload repeats most often. For a `list`, the language defines `x in y` as equivalent to `any(x is e or x == e for e in y)`, which means scanning the items.[^py314-reference-expressions-membership-test-operations] A membership test on a large `list` inside a hot loop therefore costs linear time on every call.

`deque` is built for queues: adding and removing at either end cost approximately the same O(1), while `list.pop(0)` and `insert(0, v)` have to shift all the items.[^py314-library-collections-deque] Below is an example of choosing a container for a queue, for membership tests and for the minimum; the `#` comments show the result and the trap:

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

`set` and `dict` find an element by its hash, and on average this takes a constant number of steps rather than a scan. This is the average-case behaviour of a hash table, not a guarantee for every input, and the Python documentation does not state this complexity for set and dict. `heapq` gives the smallest item through `heap[0]`.[^py314-library-heapq] Removal and insertion take O(log n) because the CPython loops follow a path from the root to a leaf or back, that is, the height of the tree.[^cpython-heapq-source] But a heap is ordered only along paths from the root, so a specific value can be found only by scanning.

The choice changes with the dominant operation. If membership tests dominate, use a `set` or `dict`; if the ends of a queue matter, use a `deque`; if the minimum matters, use `heapq`. For small collections the difference may be negligible, so check the decision with realistic sizes.

**Common mistakes:**
- `x in list` in a hot loop instead of a `set` when membership tests are needed;
- `list.pop(0)` as a queue instead of `deque.popleft()`;
- expecting fast lookup of an arbitrary element from `heapq`: only the minimum is available through `heap[0]`.
