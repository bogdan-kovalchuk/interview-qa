---
id: py-prac-0005
title: "The class `Key` defines `__eq__` based on `value` but does not define `__hash__`: what happens with `{Key(1): \"x\"}`, and how do you fix the contract for an immutable key?"
description: "A TypeError (unhashable) is raised, because a class with `__eq__` and no `__hash__` gets `__hash__ = None`."
track: python
section: practical-coding
level: senior
type: pitfall
tags: [key, eq, value, hash, key-1-x]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel-object-hash
    title: "Python 3.14: Reference/datamodel, object.__hash__"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__hash__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, object.__hash__: the requirement that objects equal under __eq__ have the same hash; the implicit __hash__ = None when __eq__ is overridden without __hash__; the advice not to define __hash__ for a mutable class with __eq__. Does not describe the text of TypeError messages."
  - source_id: py314-library-dataclasses-dataclass
    title: "Python 3.14: Library/dataclasses, dataclass"
    url: https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, dataclass: with eq and frozen both enabled the decorator generates __hash__; an explicitly defined __hash__ is not changed. Does not describe classes that are not dataclasses."
---

## Short answer

**A `TypeError` (unhashable) is raised, because a class that defines `__eq__` without `__hash__` gets `__hash__ = None`.**[^py314-reference-datamodel-object-hash] For an immutable key, define `__hash__` so that objects that compare equal under `__eq__` return the same hash, for example `def __hash__(self): return hash(self.value)`.[^py314-reference-datamodel-object-hash] For a mutable class with its own `__eq__`, `__hash__` should not be defined, because changing the value after insertion into a dict breaks lookup.[^py314-reference-datamodel-object-hash]

## Detailed explanation

Hashing exists so that `dict` and `set` can find a key by its hash. Python requires one mandatory property: objects that compare equal under `__eq__` must have the same hash.[^py314-reference-datamodel-object-hash] When a class overrides `__eq__` and does not define `__hash__`, Python sets `__hash__ = None`. Taking the hash then raises a `TypeError`, and `isinstance(obj, collections.abc.Hashable)` returns `False` for such an object.[^py314-reference-datamodel-object-hash]

An example: a class with `__eq__` and no `__hash__`, used in a dict literal. The error happens while the dict is being built:

```python
class Key:
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return isinstance(other, Key) and self.value == other.value


try:
    d = {Key(1): "x"}
except TypeError as error:
    print(error)  # 3.13: unhashable type: 'Key'
                  # 3.14: cannot use 'Key' as a dict key (unhashable type: 'Key')
```

The message text depends on the version, so the comment lists both. To fix an immutable key, `__hash__` must hash the same fields that `__eq__` compares. The shortest option is `@dataclass(frozen=True)`: when `eq` and `frozen` are both enabled and the class does not define `__hash__` itself, the dataclass generates `__hash__`; an explicitly defined `__hash__` is kept. `eq` is enabled by default.[^py314-library-dataclasses-dataclass] Example:

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class Key:
    value: int


d = {Key(1): "x"}
print(d[Key(1)])  # x
```

Do not define `__hash__` for a mutable class. The object sits in the dict's bucket for the hash it had at insertion time. If a field that feeds the hash changes afterwards, the object is in the wrong bucket and lookup cannot find it.[^py314-reference-datamodel-object-hash] So a mutable class with `__eq__` should either stay unhashable or become immutable.

**Common mistakes:**
- defining `__eq__` and forgetting `__hash__`, then getting a `TypeError` on the first `dict` or `set`;
- defining `__hash__` for a mutable class, then changing a field that the hash uses;
- hashing fields that are not part of `__eq__`: equal objects then have different hashes.

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
