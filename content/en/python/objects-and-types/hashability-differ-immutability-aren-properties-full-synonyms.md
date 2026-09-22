---
id: py-objtypes-0013
title: "How does hashability differ from immutability, and why aren't these properties full synonyms?"
description: "How does hashability differ from immutability, and why aren't these properties full synonyms?"
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L3-L16
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Hashability means that an object has a hash value that never changes during its lifetime and supports `__eq__`; immutability means that the object's value cannot change after creation.**[^py314-reference-datamodel] These are not synonyms: a `tuple` is immutable, yet `(1, [2, 3])` is unhashable because it contains a mutable element. Conversely, a custom class can be immutable, but if it defines `__eq__` without `__hash__`, Python automatically sets `__hash__ = None`, making it unhashable.

## Detailed explanation

In Python's data model, hashability and immutability serve distinct purposes and are not synonyms.[^py314-reference-datamodel] An object is hashable if it provides a `__hash__` method returning an integer that never changes across its lifetime, implements `__eq__`, and satisfies the invariant that if `a == b`, then `hash(a) == hash(b)`. Immutability, by contrast, describes object state: an object is immutable if its value and internal references cannot be modified after construction (`int`, `str`, `tuple`, `frozenset`).

These two properties diverge for three fundamental reasons. First, an immutable container can hold mutable objects. A `tuple` is structurally immutable, yet `(1, [2, 3])` is unhashable: calling `hash()` recursively inspects its elements, failing with `TypeError: unhashable type: 'list'` when encountering the nested list. A tuple is hashable only if every element it contains is also hashable.

Second, a mutable object can be hashable. Instances of standard user-defined classes that do not override `__eq__` inherit identity-based hashing and equality (`id()`) from `object`. The attributes of such an instance can be modified freely, yet the object remains hashable because its identity never changes. Third, a conceptually immutable class becomes unhashable (`__hash__ = None`) by default as soon as it defines `__eq__` without an explicit `__hash__`.

Examples demonstrating the separation between hashability and immutability:

```python
# 1. An immutable container holding a mutable object is unhashable
t = (1, 2, [3, 4])
try:
    hash(t)
except TypeError as error:
    print(error)  # unhashable type: 'list'

# 2. A mutable object can be hashable via object identity
class MutableNode:
    def __init__(self, value: int):
        self.value = value

node = MutableNode(10)
print(isinstance(hash(node), int))  # True
node.value = 99                     # Mutated state, but identity hash is unchanged
print(isinstance(hash(node), int))  # True

# 3. Defining __eq__ without __hash__ disables hashing
class Point:
    def __init__(self, x: int):
        self.x = x

    def __eq__(self, other):
        return isinstance(other, Point) and self.x == other.x

print(Point.__hash__ is None)  # True (Python sets __hash__ = None)
```

**Key differences and practical takeaways:**
- container immutability does not guarantee hashability: a `tuple` or `frozenset` is hashable only when every element inside it is hashable;
- mutability does not preclude hashing by default: classes without `__eq__` remain hashable via object identity regardless of state mutations;
- explicit contract for value-based equality: using custom objects as dictionary keys requires immutable fields and a matching `__hash__`, or `dataclass(frozen=True)`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
