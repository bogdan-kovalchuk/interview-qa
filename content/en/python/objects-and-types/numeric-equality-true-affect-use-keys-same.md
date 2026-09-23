---
id: py-objtypes-0016
title: "How does numeric equality between `1`, `1.0`, and `True` affect their use as keys of the same dictionary?"
description: "How does numeric equality between `1`, `1.0`, and `True` affect their use as keys of the same dictionary?"
track: python
section: objects-and-types
level: senior
type: pitfall
tags: [1-0]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14.7"
  flags: []
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

**`1`, `1.0`, and `True` have the same hash and compare equal (`1 == 1.0 == True`), so in a dict they resolve to the same slot – the last assignment wins.**[^py314-reference-datamodel]

```text
d = {1: 'a', 1.0: 'b', True: 'c'}
print(d)        # {1: 'c'}
print(len(d))   # 1
```

This is a consequence of Python's numeric hierarchy: `bool` is a subclass of `int`, so `True == 1`, while `float` and `int` compare by numeric value. <span class="warn">An identical collapse occurs in `set`: `{1, 1.0, True}` contains only one element.</span>

## Detailed explanation

Lookup and insertion in Python hash tables (`dict` and `set`) rely on two mandatory conditions: matching hash values (`hash(k1) == hash(k2)`) and object equality (`k1 is k2 or k1 == k2`).[^py314-reference-datamodel]

Because `bool` is a direct subclass of `int` (`isinstance(True, int)` is `True`), the boolean `True` evaluates to the numeric value `1`. A fundamental invariant of Python's object model requires that if two objects compare equal via `==`, their hash values must be identical (`a == b` implies `hash(a) == hash(b)`). Consequently, `hash(1) == hash(1.0) == hash(True) == 1`, meaning that all three objects resolve to the exact same hash table bucket.[^py314-library-stdtypes]

When a `dict` receives a key whose hash and value already match an existing entry, it overwrites the mapped value but preserves the original key object (the first one inserted). This CPython implementation detail avoids redundant reference count adjustments for immutable keys, but it introduces subtle failure modes: the retained key's type depends strictly on insertion order, whereas the associated value always reflects the most recent write.

Demonstration of numeric key collision and initial key object retention:

```python
# Keys with equal numeric values share the same hash
print(hash(1) == hash(1.0) == hash(True))  # True
print(1 == 1.0 == True)  # True

# Dict overwrites value but preserves the FIRST inserted key object
data = {1: "integer", 1.0: "float", True: "boolean"}
print(data)  # {1: 'boolean'}
first_key = list(data.keys())[0]
print(type(first_key), first_key)  # <class 'int'> 1

# Lookup succeeds with any numerically equal key
print(data[True])  # boolean
print(data[1.0])  # boolean

# Set deduplication retains only the first inserted object
unique_items = {True, 1, 1.0}
print(unique_items)  # {True}
```

**Practical consequences for architecture and code:**
- implicit key collisions: storing configuration entries or parsed payloads with mixed types (such as boolean flag `True` and numeric ID `1`) in the same `dict` silently overwrites values;
- unexpected retained key type: `dict` updates values but retains the first inserted key object, so iteration over `keys()` may yield `int` instead of an expected `bool`;
- collection collapse in `set`: using `set` to deduplicate collections with mixed types silently drops items that the developer intended to treat as distinct entities;
- defensive pattern: when key types must remain segregated, composite keys such as `(type(k), k)` or separate dictionaries per type should be used.

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
