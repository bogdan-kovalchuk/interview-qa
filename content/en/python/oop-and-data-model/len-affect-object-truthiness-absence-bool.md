---
id: py-oop-0022
title: "How can `__len__` affect an object's truthiness in the absence of `__bool__`?"
description: "If __bool__ is not defined, Python calls __len__: a zero result makes the object false and any nonzero result makes it true."
track: python
section: oop-and-data-model
level: middle
type: mechanism
tags: [len, bool]
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
  - source_id: py314-reference-datamodel-object-bool
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__bool__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: object.__bool__, truth value testing, the fallback to __len__, and the rule for classes that define neither method."
  - source_id: py314-reference-datamodel-object-len
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__len__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: object.__len__, a zero length as false in a Boolean context when __bool__ is not defined, and the requirement that the value be at least 0."
  - source_id: py314-reference-datamodel-special-method-lookup
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#special-method-lookup
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the Special method lookup section of the data model."
---

## Short answer

**If `__bool__` is not defined, Python calls `__len__`: a zero result makes the object false, and a nonzero result makes it true.**[^py314-reference-datamodel-object-bool] If neither `__bool__` nor `__len__` is defined, all instances of such a class are true.[^py314-reference-datamodel-object-bool] For example, `bool(obj)` for an object whose `__len__` returns 0 gives `False`.[^py314-reference-datamodel-object-len]

## Detailed explanation

Truth value testing happens in a Boolean context: `if obj:`, `while obj:`, `not obj` and `bool(obj)`. Python first looks for the `__bool__` method, which must return `True` or `False`.[^py314-reference-datamodel-object-bool] If it is missing but `__len__` is defined, the interpreter uses the result of `__len__`: the object is false when `__len__` returns 0, and true for any nonzero value.[^py314-reference-datamodel-object-len]

The example shows these rules and that `__bool__` takes precedence over `__len__`.

```python
class Basket:
    def __init__(self, items):
        self.items = list(items)

    def __len__(self):
        return len(self.items)

class Flag(Basket):
    def __bool__(self):
        return True

class Ticket:
    pass

print(bool(Basket([])))          # False: __len__() returns 0
print(bool(Basket(["apple"])))   # True: __len__() returns 1
print(bool(Flag([])))            # True: __bool__() takes precedence over __len__()
print(bool(Ticket()))            # True: neither __bool__ nor __len__ is defined

ticket = Ticket()
ticket.__bool__ = lambda: False  # instance attribute, not on the type
print(bool(ticket))              # True: special methods are looked up on the type
```

Implicit invocations of special methods are guaranteed to work correctly only when the method is defined on the object's type, not in the instance dictionary. So assigning `ticket.__bool__` does not change `bool(ticket)`. The documentation shows the same effect for `len()`: after `c.__len__ = lambda: 5`, calling `len(c)` raises `TypeError`.[^py314-reference-datamodel-special-method-lookup]

The documentation requires `__len__` to return an integer that is at least 0.[^py314-reference-datamodel-object-len] In CPython, a negative value raises `ValueError` already during truth value testing.

**Common mistakes:**
- thinking that `__len__` affects only `len()`, not `if obj:` and `bool()`;
- returning 0 from `__len__` for an "empty" state without realising that the object is then false in every Boolean context;
- defining `__bool__` and `__len__` with contradictory logic, so that `bool()` and `len()` give conflicting answers.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
