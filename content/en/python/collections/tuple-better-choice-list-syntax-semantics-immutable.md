---
id: py-coll-0001
title: "When is a tuple the better choice over a list, not because of syntax but because of the semantics of an immutable data structure?"
description: "When is a tuple the better choice over a list, not because of syntax but because of the semantics of an immutable data structure?"
track: python
section: collections
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
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-sorting
    title: "Python 3.14: Howto/sorting"
    url: https://docs.python.org/3.14/howto/sorting.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**A tuple is the better choice when data logically represents an immutable record – its immutability signals intent and allows using the tuple as a dict key or a set element.**[^py314-library-stdtypes] Examples include coordinates `(x, y)`, database record rows, or composite dictionary keys. <span class="warn">If a tuple contains a mutable object (such as a `list`), that object's contents can be mutated in-place – while the tuple itself remains the identical object with the same `id`.</span>

## Detailed explanation

The semantic distinction between a `tuple` and a `list` lies in their conceptual intent: a `list` models a mutable, homogeneous sequence of varying length, whereas a `tuple` represents a fixed, heterogeneous record where position dictates meaning.[^py314-library-stdtypes]

The immutability of a tuple explicitly communicates architectural intent: passing a `tuple` to external functions or modules guarantees protection against accidental side effects, as the receiving code cannot append, delete, or reorder elements. A crucial capability stemming from immutability is hashability: if all elements contained in a tuple are immutable and hashable, the tuple itself is hashable.[^py314-library-stdtypes] This enables tuples to serve as composite keys in dictionaries (`dict`) or members of sets (`set`), which is impossible with a `list` (raising `TypeError: unhashable type: 'list'`).

From an internal memory perspective, CPython optimizes tuples: because their size is immutable upon creation, they do not allocate extra capacity buffers (over-allocation) that lists require for dynamic growth. Furthermore, CPython maintains internal freelists for deallocated small tuples to reduce allocation overhead. However, tuple immutability is strictly shallow: a tuple locks only its own slot references. If a slot references a mutable object (such as a list or dictionary), the contents of that nested object can still be modified in-place, and the resulting tuple cannot be hashed.

Demonstrating record semantics, dictionary keys, and shallow immutability:

```python
# 1. Semantic distinction: tuple represents a fixed heterogeneous record
user_record = ("usr_101", "alice@example.com", 30)

# 2. Hashability enables using tuples as composite dictionary keys:
cache: dict[tuple[str, int], str] = {}
cache[("GET", 200)] = "OK"

# A list cannot be hashed because it is mutable:
try:
    cache[["GET", 200]] = "FAIL"  # type: ignore[index]
except TypeError as exc:
    print(exc)  # unhashable type: 'list'

# 3. Shallow immutability: fixed slot bindings, but mutable contents:
nested: tuple[int, list[str]] = (1, ["read"])
nested[1].append("write")
print(nested)  # (1, ['read', 'write'])
```

**Practical takeaways and subtle pitfalls:**
- using lists instead of tuples for fixed records (like coordinates or configuration pairs), inviting accidental mutation bugs across callers;
- assuming deep immutability when storing mutable objects (`list`, `dict`) inside a tuple, which also causes hashing to fail with `TypeError`;
- underestimating defensive API design: returning a `tuple` from functions guarantees to consumers that the returned sequence cannot be altered in-place;
- converting tuples to lists merely for minor convenience when the underlying data is structurally a fixed record.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
