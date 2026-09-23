---
id: py-objtypes-0012
title: "Why shouldn't a mutable class with a value-based `__eq__` usually inherit the identity-based hash from `object`?"
description: "Why shouldn't a mutable class with a value-based `__eq__` usually inherit the identity-based hash from `object`?"
track: python
section: objects-and-types
level: senior
type: mechanism
tags: [eq, object]
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

**Python requires that if two objects compare equal via `__eq__`, they must produce the same hash; an identity-based hash from `object` uses unique `id()`, causing equal objects to land in different hash buckets and become unfindable.**[^py314-reference-datamodel] For a mutable class with value-based `__eq__`, the proper solution is either making it unhashable (`__hash__ = None`) or deriving `__hash__` from the same fields and keeping them immutable. <span class="warn">In CPython, `object.__hash__` derives from `id()`, which is the object's memory address.</span>

## Detailed explanation

Python's hash table contract strictly requires that if `a == b`, then `hash(a) == hash(b)` must hold across the entire lifetime of both objects.[^py314-reference-datamodel] By default, user-defined classes inherit `__eq__` and `__hash__` from `object`. In this base implementation, equality signifies identity (`self is other`), and the hash derives from `id()` (in CPython, the memory address). If a class overrides `__eq__` to compare values (value-based equality) but retains identity-based hashing, this contract immediately breaks: two separate instances holding identical data evaluate to `True` under `==`, yet yield distinct hashes.

Violating this invariant undermines `set` and `dict` operations. During a lookup, the hash table calculates `hash(key)` to locate the appropriate bucket, checking `__eq__` only against collisions in that bucket. If two equal objects produce different hashes, checking `b in {a}` directs the search to a different bucket and returns `False`, even though `a == b`. Consequently, a set can accumulate duplicate entries that compare equal, destroying the container's fundamental uniqueness guarantees.

Python is intentionally designed to prevent this flaw: in Python 3, defining `__eq__` without declaring `__hash__` causes the interpreter to implicitly set `__hash__ = None`, disabling inherited hashing from `object`.[^py314-reference-datamodel] Attempting to hash such an instance or insert it into a set raises `TypeError: unhashable type`. If a developer explicitly restores `__hash__ = object.__hash__`, they reintroduce this pitfall, creating objects that behave unpredictably inside hash tables.

An example demonstrating contract violation when forcing `object.__hash__`:

```python
class BrokenPoint:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, BrokenPoint):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

    # Forcing identity hash breaks hash table lookups
    __hash__ = object.__hash__


p1 = BrokenPoint(1, 2)
p2 = BrokenPoint(1, 2)

print(p1 == p2)               # True (equal values)
print(hash(p1) == hash(p2))   # False (different id-based hashes)

points = {p1}
print(p2 in points)           # False (lookup checks different bucket!)

points.add(p2)
print(len(points))            # 2 (duplicate entries in a set)
```

**Practical consequences and architectural rules:**
- automatic safeguarding: overriding `__eq__` automatically sets `__hash__ = None` unless `__hash__` is explicitly declared;
- immutability of hashed fields: if an object hashes its attribute values, those attributes must remain immutable (for instance, via `frozen=True` in dataclasses or read-only properties);
- in-place mutation hazards: mutating a field used in `__hash__` after insertion into a `set` or `dict` strands the element in the wrong bucket, making it impossible to retrieve or remove;
- deliberate design choice: mutable entities should either remain unhashable (`__hash__ = None`) or rely strictly on object identity for both equality and hashing (`object.__eq__` and `object.__hash__`).

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
