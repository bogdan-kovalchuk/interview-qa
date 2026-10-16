---
id: py-funcs-0019
title: "Why can an object captured by a closure stay alive after the enclosing function has finished, and how does that affect memory retention?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#user-defined-functions
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
  - source_id: py314-reference-executionmodel-dynamic-features
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#dynamic-features
  - source_id: py314-reference-datamodel-object-del
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__del__
---

## Short answer

**A closure keeps its captured variables alive through the `__closure__` attribute (a tuple of cell objects), so those objects stay reachable while the closure exists.**[^py314-reference-datamodel] This can unexpectedly retain large objects: if a closure captures a large list and lives long (for example, as a callback), the list stays alive too. Capture only the value you need (for example `n = len(big)`), not the large object; `del` in the enclosing function does not help if the closure still reads the variable.

## Detailed explanation

When a nested function refers to a variable of the enclosing function, that variable lives in a cell object, not only in the enclosing function's frame. The function keeps its cell objects in `__closure__`, and that is what keeps the captured objects alive after the enclosing function has finished.[^py314-reference-datamodel] When the enclosing function returns, its frame goes away, but the cell remains as long as the closure exists.

Example: the function has already returned, but a large list is still in memory because `handler` reads it.

```python
def make_handler():
    big = list(range(1_000_000))   # a large list
    def handler():
        return len(big)            # the closure references big, so its cell keeps the list alive
    return handler

h = make_handler()                 # make_handler() has returned
print(len(h.__closure__[0].cell_contents))  # 1000000: the list is still reachable
```

A closure captures the variable itself, not its value at creation time: if the enclosing function later rebinds `big`, the closure sees the new value.[^py314-reference-executionmodel-dynamic-features] In CPython an object is freed as soon as its reference count reaches zero, unless a reference cycle prevents that.[^py314-reference-datamodel-object-del] So `del h` frees the list immediately in CPython, without waiting for the garbage collector.

The trap is trying to free memory with `del big` in the enclosing function. If the closure still reads `big`, the cell becomes empty, and `h()` raises `NameError: cannot access free variable 'big' ...`. The more reliable approach is to keep only what the closure needs: `n = len(big)`, then `del big` before the closure is created. The list is then freed at once, and the closure reads `n`.

**Common mistakes:**
- assuming that a closure freezes the value of a variable at creation time, rather than the variable itself;
- using `del` in the enclosing function while the closure still reads the variable: instead of freeing memory, it raises `NameError`;
- expecting the GC to free a captured object while the closure is alive: as long as a reference to it exists through the cell, it is not freed.
