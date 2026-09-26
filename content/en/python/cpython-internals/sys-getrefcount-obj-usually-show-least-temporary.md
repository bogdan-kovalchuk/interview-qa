---
id: py-cpyint-0007
title: "Why does `sys.getrefcount(obj)` usually show at least one temporary reference more than expected?"
description: "Why does `sys.getrefcount(obj)` usually show at least one temporary reference more than expected?"
track: python
section: cpython-internals
level: senior
type: pitfall
tags: [sys-getrefcount-obj]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-library-dis
    title: "Python 3.14: Library/dis"
    url: https://docs.python.org/3.14/library/dis.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-gc
    title: "Python 3.14: Library/gc"
    url: https://docs.python.org/3.14/library/gc.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-c-api-memory
    title: "Python 3.14: C Api/memory"
    url: https://docs.python.org/3.14/c-api/memory.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-sys
    title: "Python 3.14: Library/sys"
    url: https://docs.python.org/3.14/library/sys.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-free-threading-python
    title: "Python 3.14: Howto/free Threading Python"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-datamodel-traceback-objects
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#traceback-objects
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**Because calling `sys.getrefcount(obj)` itself creates a temporary reference to `obj` passed as an argument to the function, which is counted in the refcount at measurement time.**[^py314-library-dis] This temporary reference exists only during the function call and is dropped immediately upon returning. The `sys` documentation explicitly notes that the returned value is generally one higher than expected. For immortal objects (such as small integers or interned strings), the refcount is extremely large and does not reflect actual active references.

## Detailed explanation

The `sys.getrefcount(obj)` function inspects the `ob_refcnt` field of the underlying C-level `PyObject`, which is always inflated by at least one at measurement time because passing the object as a function argument creates a live reference on the call stack.[^py314-library-sys] When the expression `sys.getrefcount(obj)` executes, the bytecode pushes `obj` onto the VM evaluation stack before entering the call frame. Inside the C implementation `sys_getrefcount_impl`, `Py_REFCNT(op)` is read while that frame is still active and holding the argument, so its local reference is unavoidably included in the reported total.

As soon as the function returns and the evaluation stack frame unwinds, this borrowed argument reference is released, but the returned integer already recorded that temporary inflation. Evaluating dynamic expressions, list comprehensions, or helper calls within the argument expression can introduce additional compiler-generated temporaries, inflating the count even further. Furthermore, interactive REPL environments, debugging tools, and active traceback objects (`sys.exc_info()`) frequently retain hidden references in stack frames that confound manual leak diagnostics.

In modern CPython runtimes (from Python 3.12 onwards with PEP 683), immortal objects introduce another vital caveat: statically allocated singletons such as small integers, interned strings, `True`, `False`, and `None` have their refcount pinned to a sentinel constant in the billions.[^py314-c-api-memory] This optimization prevents cache-line thrashing across CPU cores in concurrent workloads. For these objects, `sys.getrefcount()` always returns a massive constant value that bears no relationship to the number of active variables in user code.

Demonstration of the baseline +1 argument offset and the behavior of immortal objects:

```python
import sys

class Item:
    pass

item = Item()
# Baseline: 1 variable reference in local scope + 1 inside getrefcount argument
print(f"Direct: {sys.getrefcount(item)}")

container = [item, item]
# Now: 1 in item + 2 in container + 1 in getrefcount argument
print(f"In list: {sys.getrefcount(item)}")

# Immortal objects (PEP 683) do not reflect real references
print(f"Immortal: {sys.getrefcount(None)}")

# Output:
# Direct: 2
# In list: 4
# Immortal: 4294967295
```

**Common mistakes and debugging pitfalls:**
- forgetting the +1 offset during memory leak analysis: an object held by a single variable produces a refcount of 2, which indicates normal single ownership;
- attempting to diagnose immortal objects: reference counts for `0`, `""`, or `None` are fixed sentinel values and never reflect allocation counts;
- overlooking hidden frame references: exception tracebacks, global scopes, and closures quietly retain references that keep objects alive unexpectedly.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
