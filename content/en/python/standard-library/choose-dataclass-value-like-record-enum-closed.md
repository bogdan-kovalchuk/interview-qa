---
id: py-stdlib-0016
title: "When should you choose `dataclass` for a value-like record, and when `Enum` for a closed set of symbolic values?"
description: "When should you choose `dataclass` for a value-like record, and when `Enum` for a closed set of symbolic values?"
track: python
section: standard-library
level: middle
type: comparison
tags: [dataclass, enum]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: @dataclass generates __init__, __repr__ and __eq__; the generated __eq__ compares fields in order for objects of the identical type; since 3.13 the fields are compared individually."
  - source_id: py314-library-dataclasses-dataclass
    title: "Python 3.14: Library/dataclasses, dataclass"
    url: https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the rules for generating __hash__ in a dataclass depend on the eq and frozen parameters."
  - source_id: py314-library-enum
    title: "Python 3.14: Library/enum"
    url: https://docs.python.org/3.14/library/enum.html#module-enum
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: an enum is a set of symbolic names bound to unique values; members with the same value become aliases; @unique forbids aliases; iteration yields the canonical members in definition order."
---

## Short answer

**`dataclass` automatically generates `__init__`, `__repr__` and `__eq__` for a class with fields.**[^py314-library-dataclasses] `Enum` binds symbolic names to constants: members with the same value become aliases, and `@unique` forbids that.[^py314-library-enum] `dataclass` fits when several fields must be grouped into one record, such as `Point(x, y)`; with `frozen=True` (under the default `eq=True` and without its own `__hash__`) such a record is also hashable.[^py314-library-dataclasses-dataclass] `Enum` fits when the set of values is known in advance and exhaustive, such as states or statuses; its members are iterable in definition order.[^py314-library-enum]

## Detailed explanation

`@dataclass` reads the class annotations and generates `__init__`, `__repr__` and `__eq__`. The generated `__eq__` compares the fields in order and requires both objects to be of the identical type. Since Python 3.13 the fields are compared one by one rather than as tuples.[^py314-library-dataclasses] This is what makes the record value-like: two separate `Point(1, 2)` objects are equal, because their fields are equal.

Hashability depends on the parameters. By default `eq=True` and `frozen=False`, so `__hash__` is set to `None`, and such a record cannot be used as a dictionary key or a set member. With `frozen=True` the fields cannot be changed, and `__hash__` is generated only when `eq=True` (the default) and the class does not define `__hash__` itself. An explicitly defined `__hash__` is left unchanged, and with `eq=False` the superclass's `__hash__` remains.[^py314-library-dataclasses-dataclass]

An example, run on CPython 3.13 and 3.14:

```python
from dataclasses import dataclass
from enum import Enum, unique

@dataclass(frozen=True)
class Point:
    x: int
    y: int

@unique
class Status(Enum):
    OPEN = "open"
    CLOSED = "closed"

p = Point(1, 2)
print(p)                                  # Point(x=1, y=2)
print(p == Point(1, 2))                   # True
print({p: "ok"})                          # {Point(x=1, y=2): 'ok'}  frozen=True makes it hashable
print(list(Status))                       # [<Status.OPEN: 'open'>, <Status.CLOSED: 'closed'>]
print(Status("open") is Status.OPEN)      # True
print(Status.OPEN == "open")              # False: a plain Enum member is not equal to its value

@dataclass
class MutablePoint:
    x: int
    y: int

try:
    {MutablePoint(1, 2): "ok"}
except TypeError as error:
    print(type(error).__name__)           # TypeError (the message text differs between 3.13 and 3.14)
```

In the example, `Point` with `frozen=True` works as a dictionary key, while `MutablePoint` without `frozen` raises `TypeError` when it is hashed. `Status("open")` returns the same member as `Status.OPEN`, but the member itself is not equal to its value: `Status.OPEN == "open"` is `False` (observed on CPython 3.13 and 3.14). The `@unique` decorator checks that no two names share a value; without it, the second name becomes an alias of the first.[^py314-library-enum]

**Common mistakes:**
- using a `@dataclass` without `frozen=True` as a dictionary key or a set member: `__hash__` is `None`, which raises `TypeError`.[^py314-library-dataclasses-dataclass]
- writing an `Enum` with two names on one value without `@unique`: the second member becomes an alias and does not appear in iteration.[^py314-library-enum]
- comparing an `Enum` member with its value (`Status.OPEN == "open"`) and expecting `True`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
