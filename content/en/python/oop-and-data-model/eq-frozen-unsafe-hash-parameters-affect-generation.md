---
id: py-oop-0027
title: "How do the `eq`, `frozen`, and `unsafe_hash` parameters affect the generation of `__eq__` and `__hash__` for a `@dataclass`?"
description: "eq=True generates __eq__; with frozen=False, eq=True makes the class unhashable, while frozen=True with eq=True generates __hash__; unsafe_hash=True forces __hash__ to be generated."
track: python
section: oop-and-data-model
level: middle
type: mechanism
tags: [eq, frozen, unsafe-hash, hash, dataclass]
status: published
updated: 2026-10-13
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
  - source_id: py314-howto-descriptor
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-mro
    title: "Python 3.14: Howto/mro"
    url: https://docs.python.org/3.14/howto/mro.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-datamodel-object-hash
    title: "Python 3.14: Reference/datamodel (object.__hash__)"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__hash__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the __hash__ and __eq__ contract, including that mutable objects with their own __eq__ should not implement __hash__."
  - source_id: py314-library-dataclasses-dataclass
    title: "Python 3.14: Library/dataclasses (dataclasses.dataclass)"
    url: https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: rules for generating __eq__ and __hash__ from the eq, frozen and unsafe_hash parameters; the TypeError for unsafe_hash with an explicit __hash__, and for frozen=True with a user-defined __setattr__."
  - source_id: py314-library-dataclasses-frozeninstanceerror
    title: "Python 3.14: Library/dataclasses (FrozenInstanceError)"
    url: https://docs.python.org/3.14/library/dataclasses.html#dataclasses.FrozenInstanceError
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: FrozenInstanceError is raised by the generated __setattr__ and __delattr__ of a frozen dataclass; it is a subclass of AttributeError."
---

## Short answer

**`eq=True` (default) generates `__eq__`; if the class does not define `__hash__` explicitly, with `frozen=True` it generates `__hash__`, and with `frozen=False` it sets `__hash__ = None`, making the class unhashable; `eq=False` leaves `__hash__` alone, so it is inherited from the superclass.**[^py314-library-dataclasses-dataclass] `frozen=True` makes assigning to a field raise `FrozenInstanceError`.[^py314-library-dataclasses-frozeninstanceerror] `unsafe_hash=True` forces `__hash__` to be generated, although the documentation calls this not recommended and a specialized use case.[^py314-library-dataclasses-dataclass]

## Detailed explanation

All of these rules come down to the `__hash__` contract. Objects that compare equal must have the same hash, and for a mutable object the hash must not change while the object is a dictionary key or a set member. For that reason the Python documentation advises against implementing `__hash__` in a class that has mutable objects and its own `__eq__`.[^py314-reference-datamodel-object-hash] The dataclass applies this itself: if the class does not define `__hash__` explicitly, then with `eq=True` and `frozen=False` it sets `__hash__ = None`, so the class cannot be a set member or a dictionary key.[^py314-library-dataclasses-dataclass]

A generated `__hash__` must follow the same contract, so equal instances of a frozen class have the same hash:

```python
from dataclasses import dataclass


@dataclass
class Mutable:  # eq=True, frozen=False
    x: int


@dataclass(frozen=True)
class Frozen:  # eq=True, frozen=True
    x: int


print(Mutable.__hash__)                    # None: the class is unhashable
print(hash(Frozen(1)) == hash(Frozen(1)))  # True: equal fields give equal hashes
```

`eq=False` works differently: the dataclass does not create `__eq__`, so comparison is inherited from the superclass (for `object` that is identity), and `__hash__` is not changed. If the class defines `__eq__` itself, the `eq` parameter is ignored.[^py314-library-dataclasses-dataclass]

`frozen=True` adds `__setattr__` and `__delattr__` that raise `FrozenInstanceError`, so fields cannot be assigned after creation. If the class defines `__setattr__` or `__delattr__` itself, combining it with `frozen=True` raises `TypeError` already during decoration.[^py314-library-dataclasses-frozeninstanceerror][^py314-library-dataclasses-dataclass]

`unsafe_hash=True` makes the dataclass generate `__hash__` even for a mutable class, but then changing a field after the object has been added to a set breaks lookups:

```python
from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Point:
    x: int


p = Point(1)
seen = {p}        # the hash is computed from x == 1
p.x = 2           # the hash changes while p is stored in the set
print(p in seen)  # False: the lookup computes the new hash and misses
```

Combining `unsafe_hash=True` with an explicitly defined `__hash__` in the same class raises `TypeError`.[^py314-library-dataclasses-dataclass]

**Common mistakes:**
- assuming that `eq=True` alone gives `__hash__`: for a mutable class it gives `None`;
- expecting `eq=False` to make the class unhashable: `__hash__` stays inherited from the superclass, and for `object` that is identity-based hashing;
- putting `unsafe_hash=True` on a mutable class that is stored in sets or used as dictionary keys.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
