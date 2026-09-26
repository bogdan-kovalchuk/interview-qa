---
id: py-cpyint-0018
title: "How does `sys.getsizeof()` differ from a recursive measurement of the whole object graph?"
description: "How does `sys.getsizeof()` differ from a recursive measurement of the whole object graph?"
track: python
section: cpython-internals
level: middle
type: comparison
tags: [sys-getsizeof]
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

**`sys.getsizeof()` returns only the shallow size of the object itself (via `__sizeof__`), without accounting for the memory of referenced objects.**[^py314-library-dis] For example, `sys.getsizeof([1]*1000)` reports only the size of the list container (its array of pointers), not the size of the 1,000 int objects. A full object graph measurement requires a recursive traversal that visits all nested objects and tracks `id()` to avoid double-counting duplicates and cycles. `getsizeof()` also adds garbage collector overhead for objects tracked by the GC.

## Detailed explanation

The `sys.getsizeof()` function performs an exclusively shallow memory measurement by invoking the object's `__sizeof__()` method and adding garbage collector header overhead (`PyGC_Head`) if the object is tracked by the GC.[^py314-library-sys] For compound containers such as lists, dictionaries, tuples, or user class instances, the returned value reflects only the size of the container's own C structure and its internal pointer array (`PyObject*`), completely ignoring the memory of the objects those pointers reference.

Because of this shallow nature, calling `sys.getsizeof()` on large nested data structures gives a misleading picture of actual memory consumption. For instance, a list containing a million strings or dictionaries reports only the size of its pointer buffer (several megabytes), while the actual heap memory occupied by the contained objects may reach hundreds of megabytes. Similarly, for regular class instances, `sys.getsizeof(instance)` measures only the instance struct itself, omitting the instance's attribute dictionary `__dict__` and any referenced resources.

A complete measurement of an object graph requires recursively traversing all referenced objects, which can be accomplished using `gc.get_referents()` or custom container inspection.[^py314-library-gc] During recursive traversal, maintaining a registry of visited object addresses (`id(obj)`) is critical to avoid infinite recursion on cyclic references and to prevent double-counting shared objects, such as interned strings, cached small integers, or singletons like `None`.

The difference between a shallow measurement and a recursive object-graph traversal:

```python
import gc
import sys

def total_size(obj, seen=None):
    """Recursively calculate the full memory footprint of an object graph."""
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    size = sys.getsizeof(obj)
    for referent in gc.get_referents(obj):
        size += total_size(referent, seen)
    return size

nested_data = [[1, 2, 3] for _ in range(100)]

shallow = sys.getsizeof(nested_data)
deep = total_size(nested_data)

print(f"Shallow: {shallow} bytes")  # ~920 bytes (outer list container only)
print(f"Deep: {deep} bytes")        # ~9800+ bytes (includes nested lists and ints)
```

**Common mistakes and pitfalls:**
- Estimating the memory footprint of caches, trees, or parsed JSON structures with `sys.getsizeof()`, yielding values that underreport actual usage by orders of magnitude.
- Implementing recursive traversal without a `seen` set, which triggers `RecursionError` on cyclic data structures or multiplies the cost of shared objects.
- Double-counting shared substructures: if two distinct containers point to the same underlying sub-objects, naively summing their individual deep sizes overstates memory consumption.
- Overlooking C-extension allocations and raw buffers: `__sizeof__` does not necessarily reflect memory managed by C libraries outside CPython's allocator (for tracking real process allocations, `tracemalloc` is more appropriate).

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
