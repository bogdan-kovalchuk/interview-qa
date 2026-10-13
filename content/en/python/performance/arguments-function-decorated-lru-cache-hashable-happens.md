---
id: py-perf-0011
title: "Why must the arguments to a function decorated with `lru_cache` be hashable, and what happens if you pass a `list` or `dict`?"
description: "Why must the arguments to a function decorated with `lru_cache` be hashable, and what happens if you pass a `list` or `dict`?"
track: python
section: performance
level: middle
type: pitfall
tags: [lru-cache, list, dict]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-functools-functools-lru-cache
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.lru_cache
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: results are stored in a dict, so the arguments must be hashable; maxsize=None disables the LRU feature."
  - source_id: py314-library-functools-functools-cache
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.cache
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: functools.cache() returns the same as lru_cache(maxsize=None), that is, a cache without a size limit."
  - source_id: py314-glossary-term-hashable
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-hashable
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the definition of hashable; a tuple is hashable only if all its elements are hashable; instances of user-defined classes are hashable by default, with a hash derived from id()."
  - source_id: py314-reference-datamodel-object-hash
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__hash__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: when __hash__ is None, retrieving the hash raises TypeError; a class that defines __eq__ without __hash__ cannot be used as an item in hashable collections."
---

## Short answer

**`lru_cache` stores results in an internal dict, so all positional and keyword arguments must be hashable.**[^py314-library-functools-functools-lru-cache] Passing a `list` or `dict` raises `TypeError: unhashable type`, and in CPython the function body does not run. The workaround is to convert the argument to a `tuple` or `frozenset` with hashable elements, if the function accepts that type. Hashable does not mean immutable: instances of user-defined classes are hashable by default, with a hash derived from `id()`[^py314-glossary-term-hashable], so changing their attributes leaves a stale result in the cache.

## Detailed explanation

`lru_cache` stores results in a dict. Each call first builds a key from the positional and keyword arguments and then looks it up in the dict, so the documentation requires all of these arguments to be hashable.[^py314-library-functools-functools-lru-cache] Hashable means that the object has a hash value that never changes during its lifetime and that it can be compared with other objects: that requires `__hash__` and `__eq__`.[^py314-glossary-term-hashable] If `__hash__` is `None`, retrieving the hash raises `TypeError`.[^py314-reference-datamodel-object-hash] Mutable containers, such as `list` and `dict`, are not hashable.[^py314-glossary-term-hashable]

The first call computes the result, the second one is served from the cache, and the `list` is rejected before the function runs:

```python
from functools import lru_cache


@lru_cache(maxsize=None)
def total(values):
    print("computing")
    return sum(values)


print(total((1, 2, 3)))    # computing, then 6
print(total((1, 2, 3)))    # 6: cache hit, nothing printed
try:
    total([1, 2, 3])
except TypeError as error:
    print(error)           # unhashable type: 'list'
```

The error happens during the cache lookup, so the function body does not run and nothing is stored (tested on 3.13 and 3.14). A `dict` gives the same error, and a `tuple` containing a `list` is not hashable either: an immutable container is hashable only if all of its elements are hashable.[^py314-glossary-term-hashable] For keyword arguments the rule is the same: `lookup(config={"x": 1})` raises `TypeError: unhashable type: 'dict'`.

The more dangerous case is an argument that is hashable but mutable. Here the cache sees the same key even after the attributes change:

```python
from functools import lru_cache


class Box:
    def __init__(self, value):
        self.value = value


@lru_cache(maxsize=None)
def read(box):
    return box.value


b = Box(1)
print(read(b))    # 1
b.value = 2
print(read(b))    # 1: same object, same hash, stale cached result
```

Here `hashable` does not mean `immutable`: the cache does not check the state of the object, so for mutable arguments the cached result may not match the current data.

Workarounds depend on the function. Converting to a `tuple` or `frozenset` works only if the function accepts that type and the elements are hashable; for a `dict`, `frozenset(d.items())` needs hashable values. `functools.cache` does not remove the requirement: it is equivalent to `lru_cache(maxsize=None)` and only drops the size limit.[^py314-library-functools-functools-cache]

**Common mistakes:**
- assuming that `functools.cache` accepts arguments that `lru_cache` rejects: the requirement is the same;
- converting a `list` to a `tuple` without checking that the elements are hashable: `hash(tuple([[1]]))` still raises `TypeError`;
- assuming that hashable guarantees an up-to-date result for a mutable object.

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
