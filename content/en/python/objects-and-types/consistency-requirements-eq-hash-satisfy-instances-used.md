---
id: py-objtypes-0004
title: "What consistency requirements must `__eq__` and `__hash__` satisfy if instances are used as dictionary keys?"
description: "What consistency requirements must `__eq__` and `__hash__` satisfy if instances are used as dictionary keys?"
track: python
section: objects-and-types
level: middle
type: mechanism
tags: [eq, hash]
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

**Objects that compare equal via `__eq__` must produce the exact same `__hash__` value.**[^py314-reference-datamodel] If a class defines `__eq__` without `__hash__`, its `__hash__` is implicitly set to `None`, making instances unhashable in hash-based collections. Mutable objects should not implement `__hash__`, because mutating their state would alter equality and break collection lookups.

## Detailed explanation

For objects to function correctly as dictionary keys or set elements, Python's data model enforces a fundamental invariant: if two objects compare equal via `__eq__`, they must produce the exact same `__hash__` value.[^py314-reference-datamodel]

Python dictionaries (`dict`) and sets (`set`) are built on hash tables. When looking up or inserting a key, the interpreter first evaluates `hash(key)` to determine the target bucket index. If that bucket contains an entry, Python verifies equality using `k is target or k == target`. If two equal objects produce different hash codes, Python searches entirely different buckets and fails to find the existing key, causing duplicate entries in a `set` or retrieval failures in a `dict`.[^py314-library-stdtypes]

By default, user-defined classes inherit `__eq__` and `__hash__` from `object`: equality relies on object identity (`is`), and the hash is derived from memory identity. However, when a class overrides `__eq__`, Python automatically sets `__hash__ = None`. This safety mechanism prevents objects with custom equality from being hashed incorrectly, raising `TypeError: unhashable type` if placed into a hash-based collection.

To make instances with custom equality hashable, a class must explicitly implement `__hash__` using immutable attributes that participate in `__eq__`. If any attribute used to compute the hash changes after an object is added to a dictionary, its hash value shifts while the object remains stuck in its original bucket, corrupting the collection and making the key unretrievable.

An example of a correct and consistent implementation of `__eq__` and `__hash__`:

```python
class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self._x, self._y) == (other._x, other._y)

    def __hash__(self):
        # Consistent hash based on the exact same fields as __eq__
        return hash((self._x, self._y))

p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)              # True: equal coordinates
print(hash(p1) == hash(p2))  # True: satisfies the hash consistency invariant

point_map = {p1: "origin_offset"}
print(point_map[p2])         # "origin_offset": successfully resolved via hash and equality
```

**Implementation requirements and common mistakes:**
- violating the consistency invariant: objects with equal fields produce distinct hashes, preventing dictionaries from locating an existing key;
- calculating `__hash__` over mutable attributes: after modifying an attribute, the key becomes unfindable in the collection, corrupting the hash table state;
- including attributes in `__hash__` that are omitted from `__eq__`: this causes equal objects to produce different hash codes;
- omitting `__hash__` when overriding `__eq__`: the class automatically receives `__hash__ = None`, rendering its instances unhashable.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
