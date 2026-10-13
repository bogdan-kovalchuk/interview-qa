---
id: py-stdlib-0008
title: "What boilerplate does `functools.total_ordering` remove, and what performance and traceback trade-offs should you take into account?"
description: "What boilerplate does `functools.total_ordering` remove, and what performance and traceback trade-offs should you take into account?"
track: python
section: standard-library
level: senior
type: practical
tags: [functools-total-ordering]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-functools-total-ordering
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.total_ordering
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, total_ordering section: which methods the class must define, the recommended __eq__, slower execution and more complex stack traces, advice to implement all methods explicitly, no override of inherited methods."
---

## Short answer

**`@total_ordering` fills in the missing comparison methods (`__lt__`, `__le__`, `__gt__`, `__ge__`) from one ordering method that the class defines; the class must define at least one of them and should also define `__eq__`.**[^py314-library-functools-total-ordering] The trade-off: derived methods run more slowly and produce more complex tracebacks. If benchmarks show that comparison is a bottleneck, implement all the methods explicitly.[^py314-library-functools-total-ordering]

## Detailed explanation

`@total_ordering` is a class decorator that fills in the remaining comparison methods from one ordering method the class defines. The documentation requires the class to define at least one of `__lt__`, `__le__`, `__gt__`, and `__ge__`, and recommends defining `__eq__`.[^py314-library-functools-total-ordering] The decorator does not override methods that the class or its superclasses already declare, even if the superclass method is abstract.[^py314-library-functools-total-ordering] In CPython, a class with no ordering method raises `ValueError`.

The class below defines only `__eq__` and `__lt__`; the decorator supplies the rest:

```python
import functools

@functools.total_ordering
class Version:
    def __init__(self, major, minor):
        self.major = major
        self.minor = minor

    def __eq__(self, other):
        return (self.major, self.minor) == (other.major, other.minor)

    def __lt__(self, other):
        return (self.major, self.minor) < (other.major, other.minor)

print(Version(1, 2) <= Version(1, 3))  # True, __le__ is derived from __lt__ and __eq__
print(Version(2, 0) > Version(1, 9))   # True, __gt__ is derived too
```

The derived methods are ordinary functions defined in `functools.py`. In CPython, the body of the derived `__gt__` that `total_ordering` generates (the `_gt_from_lt` function) computes `not (a < b) and a != b`: `__lt__` runs first, and `__eq__` (through `!=`) runs only when `__lt__` returns `False`. So `Version(2, 0) > Version(1, 9)` calls `__lt__` and `__eq__`, whereas an explicit `__gt__` would be a single call.

The cost is an extra Python-level call for every derived comparison. If `__lt__` raises an exception during a `>` comparison, the traceback shows a `_gt_from_lt` frame from `functools.py` between the operator and your code. The documentation describes this as slower execution and more complex stack traces for the derived methods, and advises implementing all six rich comparison methods explicitly if benchmarks show a bottleneck.[^py314-library-functools-total-ordering] The frame name is the same on CPython 3.13 and 3.14.

**Common mistakes:**
- treating the decorator as free: derived methods are slower and harder to debug;
- not defining `__eq__`: then `==` compares identity, and for a class that defines only `__lt__`, `NoEq(2) <= NoEq(2)` returns `False`;
- expecting the decorator to replace an operator that the base class already defines: it leaves that operator alone.

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
