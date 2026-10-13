---
id: py-stdlib-0007
title: "How does `cached_property` differ from `property` in caching, attribute writes, and invalidation?"
description: "How does `cached_property` differ from `property` in caching, attribute writes, and invalidation?"
track: python
section: standard-library
level: middle
type: comparison
tags: [cached-property, property]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-functools-cached-property
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.cached_property
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, cached_property section: caching, attribute writes, deleting the attribute to clear the cache, race condition, requirement for a mutable __dict__."
---

## Short answer

**`cached_property` computes its value on first access and stores it in the instance's `__dict__`, whereas `property` calls its getter on every access.**[^py314-library-functools-cached-property] Assigning to a `cached_property` replaces the stored value; assigning to a `property` calls its setter, and without a setter it raises `AttributeError`. Invalidation works through `del instance.attr`, after which the next access recomputes the value. It requires a mutable `__dict__`, so it does not work with `__slots__` classes that lack `__dict__`.[^py314-library-functools-cached-property]

## Detailed explanation

`cached_property` differs from `property` in that it stores the result of its getter. The first access calls the function and writes the result into `instance.__dict__` under the attribute name. Later accesses find the value there and never reach the descriptor. The documentation says that after this, an instance attribute with the same name takes precedence over the `cached_property`: reads and writes go to it.[^py314-library-functools-cached-property] In CPython, `cached_property` defines `__get__` and `__set_name__` but not `__set__`, so it is a non-data descriptor.

A `property` is the opposite: its getter runs on every access. Without a setter, assigning to it raises `AttributeError`. A `cached_property` allows writes: an assignment replaces the stored value, and the next read returns it without running the getter. That is convenient for filling the cache by hand, but the stored value can then differ from what the getter would return.[^py314-library-functools-cached-property]

The example compares the two descriptors. The output is the same on CPython 3.13 and 3.14:

```python
from functools import cached_property

class Report:
    def __init__(self, rows):
        self.rows = rows

    @cached_property
    def total(self):
        print("computing total")
        return sum(self.rows)

    @property
    def count(self):
        print("computing count")
        return len(self.rows)

r = Report([1, 2, 3])
print(r.total)   # computing total, then 6
print(r.total)   # 6, no recomputation
print(r.count)   # computing count, then 3
print(r.count)   # computing count again, then 3
r.total = 100    # cached_property allows the write
print(r.total)   # 100
del r.total      # clears the cache
print(r.total)   # computing total, then 6
r.count = 5      # AttributeError: property 'count' of 'Report' object has no setter
```

Invalidation is `del instance.attr`: the next access runs the getter again. The documentation says the cached value can be cleared by deleting the attribute.[^py314-library-functools-cached-property] The cache is not refreshed when the data the getter uses changes, though: after `self.rows` changes, `r.total` keeps returning the old value until the attribute is deleted.

Two limits matter. First, before Python 3.12 `cached_property` had an undocumented lock that guaranteed the getter ran only once per instance; since 3.12 the lock is gone. In multi-threaded code the getter may now run more than once on the same instance, and the last run sets the cached value. If that is harmful, add locking inside the getter.[^py314-library-functools-cached-property] Second, it needs a mutable `__dict__`, so metaclasses and `__slots__` classes without `__dict__` are not supported.[^py314-library-functools-cached-property] In CPython, reading such an attribute raises `TypeError`.

**Common mistakes:**
- assuming the getter of a `cached_property` runs only once under all conditions;
- assigning a value to a cached attribute and forgetting that it may not match what the getter returns;
- expecting an update after `rows` changes, without deleting the attribute;
- using `cached_property` in a class that has `__slots__` but no `__dict__`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
