---
id: py-itergen-0018
title: "How does `itertools.tee()` let you create independent iterators, and what memory trade-off arises if the consumers advance at different speeds?"
track: python
section: iterators-and-generators
sources:
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
  - source_id: py314-library-itertools-tee
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html#itertools.tee
---

## Short answer

**`itertools.tee(iterable, n)` returns `n` independent iterators over one input iterable.**[^py314-library-itertools-tee] This itertool may require significant auxiliary storage, and if one iterator consumes most of the data before another starts, `list()` is faster.[^py314-library-itertools-tee] In CPython, the values that the fastest copy has already read but the slowest copy has not yet read are kept in a buffer, so memory grows with the gap between the copies.

## Detailed explanation

`tee()` is useful when one input iterable must be read by several consumers independently of one another.[^py314-library-itertools-tee] In CPython, the input iterable is read only when one of the copies asks for the next value, and a value that has already been read is kept in a buffer for the remaining copies. So the buffer is the memory that `tee()` spends.

The example below measures the memory held by that buffer in CPython. It is an observation, not a language guarantee:

```python
import itertools
import tracemalloc

def kept_bytes(lockstep):
    a, b = itertools.tee(range(1_000_000))
    tracemalloc.start()
    if lockstep:
        for _x, _y in zip(a, b):     # both copies move together
            pass
    else:
        for _x in a:                 # a reads everything; b has not started
            pass
    current, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return current

print(kept_bytes(lockstep=False) > 10_000_000)  # True: tee keeps the items b has not read
print(kept_bytes(lockstep=True) < 1_000_000)    # True: little is kept when both move together
```

Memory depends on the gap between the copies. If copy `a` has consumed the whole input while `b` has not started, the buffer holds every value, so in memory terms this is roughly like `list(iterable)` (observed in CPython). If the copies move together, the gap is small and the buffer is almost empty. The documentation advises `list()` when one iterator uses most or all of the data before another starts.[^py314-library-itertools-tee]

Separately, tee iterators are not thread-safe. Using the copies from one `tee()` call simultaneously from different threads can raise `RuntimeError`, even if the original iterable is thread-safe.[^py314-library-itertools-tee]

**Common mistakes:**
- assuming that `tee()` is cheaper than `list()` when one copy consumes the whole input first;
- leaving a copy unread while another copy advances: the buffer grows with the gap;
- sharing tee iterators between threads without synchronization.
