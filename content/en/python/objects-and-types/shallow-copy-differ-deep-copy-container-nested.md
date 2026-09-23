---
id: py-objtypes-0009
title: "How does a shallow copy differ from a deep copy for a container with nested mutable objects?"
description: "How does a shallow copy differ from a deep copy for a container with nested mutable objects?"
track: python
section: objects-and-types
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**A shallow copy creates a new outer container while its nested objects remain shared references; a deep copy recursively duplicates everything down the entire object graph.**[^py314-reference-datamodel] For `a = [[1, 2]]`: after `s = copy.copy(a)`, the expression `s[0] is a[0]` evaluates to `True`, so mutating `s[0]` also modifies `a[0]`. After `d = copy.deepcopy(a)`, the expression `d[0] is a[0]` evaluates to `False`, and mutating `d[0]` has no effect on `a[0]`.

## Detailed explanation

The fundamental difference between a shallow copy and a deep copy lies in the depth to which the underlying object graph is traversed and duplicated.[^py314-library-copy]

A shallow copy (created via `copy.copy()`, slice notation `lst[:]`, constructors like `list(lst)`, or `.copy()` methods) allocates a new top-level container, but populates it strictly with references to the existing elements. If the contained elements are immutable scalar types (integers, strings), the copy operates independently because elements cannot mutate in place. However, if the container holds mutable objects (such as nested lists or dictionaries), both containers store identical memory addresses, meaning modifications to nested objects through one reference immediately affect the other.[^py314-reference-datamodel]

In contrast, a deep copy (created via `copy.deepcopy()`) recursively traverses the entire object graph, constructing new instances for every compound object it encounters. For immutable primitive objects (integers, strings, or tuples containing exclusively immutable items), Python optimizes execution by returning the original object reference directly, as immutability guarantees safety. For all mutable containers, brand new isolated objects are instantiated, eliminating shared-state side effects entirely.

Choosing between the two involves balancing execution speed against safety. Shallow copying runs in $O(n)$ time proportional to the outer container's length with minimal memory overhead, whereas deep copying incurs significant performance penalties due to full graph traversal, internal memo table management, and extensive object allocation.

An example contrasting shallow copy and deep copy behavior on nested lists:

```python
import copy

original = [[1, 2], [3, 4]]

# Shallow copy: new outer list, shared inner lists
shallow = copy.copy(original)
print(shallow is original)        # False (new outer container)
print(shallow[0] is original[0])  # True (shared inner reference)

shallow[0].append(99)
print(original[0])                # [1, 2, 99] - mutation is visible in original!

# Deep copy: recursive duplicate of all nested mutable objects
deep = copy.deepcopy(original)
print(deep is original)           # False
print(deep[0] is original[0])     # False (new independent inner list)

deep[0].append(100)
print(original[0])                # [1, 2, 99] - untouched by mutation in deep
```

**Common mistakes and practical rules:**
- using `copy.copy()`, `lst[:]`, or `d.copy()` on nested data structures and erroneously expecting full mutation isolation;
- invoking `copy.deepcopy()` unconditionally across large collections, resulting in substantial CPU overhead and excessive memory allocation;
- attempting to deep-copy objects that encapsulate external system resources (such as file descriptors, open sockets, or threading locks), triggering copy failures or invalid states;
- leveraging list or dictionary comprehensions for targeted, shallow-depth copies when only specific levels of a data structure need to be duplicated.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
