---
id: py-objtypes-0007
title: "Why can a tuple be unhashable even though the tuple itself is immutable?"
description: "Why can a tuple be unhashable even though the tuple itself is immutable?"
track: python
section: objects-and-types
level: middle
type: pitfall
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

**A tuple is hashable only if all of its elements are hashable.**[^py314-reference-datamodel] The hash of a tuple is calculated recursively from the hashes of its contained elements. If a tuple contains a mutable object without a `__hash__` method (such as a `list` or a `dict`), calling `hash()` raises a `TypeError`. Consequently, such a tuple cannot be used as a key in a `dict` or as an element in a `set`.

## Detailed explanation

An object in Python is hashable only when its hash value remains constant throughout its entire lifetime, which for a tuple requires every single one of its elements to be hashable as well.[^py314-reference-datamodel]

Container immutability is not synonymous with hashability. A `tuple` guarantees only the immutability of its own reference structure: the number of slots and the object references they hold cannot change once allocated. However, the referenced objects themselves may be mutable (such as `list`, `dict`, or `set`). In CPython, computing a tuple's hash involves iterating through all of its elements and combining their individual hashes; encountering an element where `__hash__ = None` immediately triggers a `TypeError`.[^py314-library-stdtypes]

This behavior enforces the foundational invariant of hash tables: if two objects compare equal (`a == b`), their hash values must also be equal (`hash(a) == hash(b)`). If a tuple holding a mutable list possessed a static hash, modifying the list would change object equality while the hash remained constant; conversely, if the hash dynamically tracked the list's mutations, the tuple would drift into the wrong hash bucket in a `dict` or `set`, becoming unretrievable.

To resolve this issue, nested mutable structures must be recursively converted to immutable counterparts. Nested lists should become nested tuples, mutable sets should be converted to `frozenset`, and complex record-like structures should be represented with frozen dataclasses or `NamedTuple`.

An example demonstrating tuple hashability depending on element types:

```python
# A tuple of immutable objects is hashable
t1 = (1, "hello", (2, 3))
print(hash(t1))  # integer hash value
lookup = {t1: "valid_key"}
print(lookup[t1])  # 'valid_key'

# A tuple containing a mutable object (list) is unhashable
t2 = (1, [2, 3])
try:
    hash(t2)
except TypeError as exc:
    print(exc)  # unhashable type: 'list'

# It cannot be placed into a dict or set
try:
    bad_set = {t2}
except TypeError as exc:
    print(exc)  # unhashable type: 'list'
```

**Common mistakes and recommendations:**
- assuming that any tuple is inherently valid as a `dict` key or a `set` element without inspecting its contents;
- constructing composite cache keys directly from arbitrary function arguments `(*args)` without validating or normalizing mutable arguments;
- performing only a shallow conversion `tuple(data)`, which leaves nested lists mutable and keeps the resulting tuple unhashable;
- recursively transforming nested collections into frozen equivalents: `tuple` for sequences and `frozenset` for unordered sets.

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
