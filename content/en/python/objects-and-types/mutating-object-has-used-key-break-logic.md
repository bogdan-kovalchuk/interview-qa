---
id: py-objtypes-0008
title: "How can mutating an object after it has been used as a key break the logic of a hash-based collection?"
description: "How can mutating an object after it has been used as a key break the logic of a hash-based collection?"
track: python
section: objects-and-types
level: senior
type: practical
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

**If an object is mutated after being used as a key in a `dict` or an element in a `set`, its hash value changes and lookups based on the new hash return incorrect results – the key effectively becomes "lost".**[^py314-reference-datamodel] Hash-based collections compute and cache the key's hash at insertion time; once the object's attributes change, subsequent lookups compute a different hash and search the wrong bucket. To prevent this, only immutable objects with invariant `__hash__` implementations should be used as keys.

## Detailed explanation

Hash-based collections in Python (`dict` and `set`) strictly rely on the invariant that a key's `__hash__()` and `__eq__()` evaluation never change while the key resides in the collection.[^py314-reference-datamodel]

When an element is inserted, the interpreter calculates its hash value to determine its entry position and collision probe sequence in the hash table. In CPython, `dict` entries cache this computed hash value directly in the table. When retrieving an item, Python recomputes the hash of the lookup target and follows the corresponding probe sequence, testing for identity (`is`) or value equality (`==`) only against matching cached hashes.

If an object mutates after insertion such that its hash changes, any subsequent lookup evaluates the new hash and traverses a completely different probe sequence. The lookup encounters empty slots or unrelated keys and reports the key as missing, never inspecting the slot where the object was originally stored.[^py314-library-stdtypes] This introduces a corrupted state: the object is still enumerated by `keys()` and counted in `len()`, but direct membership and access operations (`k in d`, `d[k]`, `s.remove(k)`) fail with a `KeyError`.

The architectural consequences extend beyond lookup failures: attempting to insert the mutated key again will not find the original record and will insert a duplicate into what should be an invariant-enforcing set or dictionary. Furthermore, when the collection triggers an internal resize or table rebuild, the mutated key may be re-probed into a new bucket, making behavior entirely non-deterministic across executions.

An example showing broken dictionary lookups after mutating a key's state:

```python
class MutableKey:
    def __init__(self, val: str):
        self.val = val

    def __hash__(self) -> int:
        return hash(self.val)

    def __eq__(self, other: object) -> bool:
        return isinstance(other, MutableKey) and self.val == other.val

key = MutableKey("initial")
lookup = {key: "payload"}

# Successful initial lookup
print(lookup[key])  # 'payload'

# Mutate key state after insertion
key.val = "modified"

# Lookup fails because hash changed and targets the wrong bucket
print(key in lookup)  # False
try:
    _ = lookup[key]
except KeyError:
    print("KeyError: key cannot be found")

# The key is still physically inside the dictionary
print(len(lookup))  # 1
print([k.val for k in lookup.keys()])  # ['modified']
```

**Architectural requirements and prevention strategies:**
- maintain the fundamental hash contract: if two objects compare equal (`a == b`), their hashes must be equal (`hash(a) == hash(b)`), and neither value may change over the object's lifetime;
- rely on Python's default safety: defining `__eq__` automatically sets `__hash__ = None`, and developers should never manually implement `__hash__` based on mutable fields;
- represent composite dictionary keys and set members with immutable data structures such as `@dataclass(frozen=True)` or `NamedTuple`;
- if an entity must remain mutable, retain default identity-based hashing (`object.__hash__`) and avoid overriding `__eq__` based on mutable instance attributes.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
