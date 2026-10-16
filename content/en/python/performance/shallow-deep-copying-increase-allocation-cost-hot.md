---
id: py-perf-0009
title: "How can shallow and deep copying increase allocation cost on a hot path?"
track: python
section: performance
sources:
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
  - source_id: cpython-copy-py
    title: "CPython 3.14: Lib/copy.py"
    url: https://github.com/python/cpython/blob/v3.14.6/Lib/copy.py
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
---

## Short answer

**A shallow copy creates a new top-level container while nested objects stay shared; a deep copy recursively creates copies of nested containers, so the number of allocations grows with the size of the structure.**[^py314-library-copy] `copy.copy(x)` gives one new container, while `copy.deepcopy(x)` copies each nested container and keeps a memo dictionary of objects already copied to handle cycles. On a hot path, copying large or deeply nested structures adds noticeable allocation of memory and time.

## Detailed explanation

Assignment in Python does not copy an object; it only creates another reference. A copy is needed when two containers must change independently. The `copy` module distinguishes two cases: a shallow copy creates a new top-level container but the nested objects remain the same; a deep copy recursively creates copies of the nested containers.[^py314-library-copy] Example:

```python
import copy

orders = [[1, 2], [3]]             # nested lists
shallow = copy.copy(orders)
shallow[0].append(99)              # the nested list is shared by both copies
print(orders)                      # [[1, 2, 99], [3]]
print(shallow[0] is orders[0])     # True

deep = copy.deepcopy(orders)
deep[1].append(7)
print(orders)                      # [[1, 2, 99], [3]]: the original is unchanged
print(deep[1] is orders[1])        # False

cyclic = []
cyclic.append(cyclic)              # a list that contains itself
copied = copy.deepcopy(cyclic)     # the memo dict stops the recursion
print(copied[0] is copied)         # True

text = 'abc'
print(copy.deepcopy(text) is text) # True: atomic values such as str are returned as is
```

`deepcopy` keeps a memo dictionary of objects already copied; without it, a cycle of references could lead to an endless recursion.[^py314-library-copy] That is why the copy of the self-containing list is correct, and its element refers to the copy itself. In CPython, `deepcopy` returns atomic values such as `str` and `int` without copying them; the list of such types is defined in `copy.py`.[^cpython-copy-py] So the cost of a deep copy falls on the containers and their contents.

This is where the cost on a hot path comes from. A shallow copy of a list with `N` elements allocates one new list holding `N` references. A deep copy creates a new object for every nested container; in CPython each step runs through the Python code of `deepcopy`.[^cpython-copy-py] If such a copy happens on every request or in every iteration, the allocations of memory and time grow with the size of the structure.

On a hot path it is usually enough to copy only the level that changes: `list.copy()` or the slice `x[:]` give a shallow copy, and the nested objects stay shared.[^py314-library-copy] Immutable values, for example a `tuple` of immutable items, can be passed without a copy. To see how much is allocated, compare `tracemalloc` snapshots.[^py314-library-tracemalloc]

A shallow copy is enough when the nested objects are not changed, or when changing them in both copies is acceptable. A deep copy is needed when nested mutable state must be independent. A deep copy can also copy more than necessary: the documentation warns that it copies data meant to be shared between copies as well.[^py314-library-copy]

**Common mistakes:**
- assuming that a shallow copy isolates nested lists or dictionaries, and changing them in one copy;
- calling `deepcopy` on every request for a large structure instead of copying only the changing level;
- using a deep copy for data that must remain shared between copies.
