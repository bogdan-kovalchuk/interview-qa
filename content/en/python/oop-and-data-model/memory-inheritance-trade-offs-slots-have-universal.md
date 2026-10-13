---
id: py-oop-0028
title: "What memory and inheritance trade-offs does `__slots__` have, and why is it not a universal performance optimisation?"
description: "__slots__ removes the per-instance `__dict__` and can reduce memory, but it restricts attributes, weak references and inheritance."
track: python
section: oop-and-data-model
level: senior
type: practical
tags: [slots]
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
  - source_id: py314-reference-datamodel-slots
    title: "Python 3.14: Reference/datamodel (__slots__)"
    url: https://docs.python.org/3.14/reference/datamodel.html#slots
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the __slots__ section on missing __dict__ and __weakref__, inheritance, the multiple-inheritance restriction and the clash with class attributes."
---

## Short answer

**`__slots__` replaces the instance `__dict__` with a fixed set of slots, so memory can shrink, but the class loses flexibility.**[^py314-reference-datamodel-slots] New attributes outside `__slots__` cannot be created unless `__dict__` is added to `__slots__`, and weak references require `__weakref__` in `__slots__`.[^py314-reference-datamodel-slots] A subclass without its own `__slots__` gets a `__dict__`, so the savings for its instances disappear, and among several parent classes only one may have non-empty slots, otherwise `TypeError` is raised.[^py314-reference-datamodel-slots]

## Detailed explanation

Without `__slots__`, each instance keeps its attributes in its own dictionary, `__dict__`. When a class defines `__slots__`, space is reserved only for the listed names, and access to them is implemented by descriptors at class level.[^py314-reference-datamodel-slots] Not having a dictionary for each instance saves memory, and the saving can be significant; attribute lookup can also become noticeably faster.[^py314-reference-datamodel-slots] The gain grows with the number of instances, so it should be measured on a real workload. Below is a class with slots that does not accept new attributes:

```python
class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(1, 2)
print(hasattr(p, "__dict__"))  # False: there is no per-instance dict
try:
    p.z = 3
except AttributeError as error:
    print(error)  # 3.13+: 'Point' object has no attribute 'z' and no __dict__ for setting new attributes
```

Inheritance changes the picture. A parent class with `__slots__` has no `__dict__` of its own, but a subclass without its own `__slots__` gets a `__dict__` and a `__weakref__` for each instance, so the memory savings for its instances disappear:[^py314-reference-datamodel-slots]

```python
class Base:
    __slots__ = ("x",)


class Child(Base):  # Child defines no __slots__
    pass


c = Child()
print(hasattr(c, "__dict__"))  # True: Child instances get a __dict__
c.extra = 1                    # allowed, so the savings from __slots__ are gone for Child
```

Multiple inheritance is restricted too. If two parent classes have non-empty slots, defining a class from them fails with `TypeError`, because only one base class may have attributes created by slots.[^py314-reference-datamodel-slots] Another trap: a default value cannot be set with a class attribute that has the same name as a slot, because the class attribute would overwrite the slot descriptor.[^py314-reference-datamodel-slots] In CPython this error appears already when the class is created, as a `ValueError`.

In summary, `__slots__` suits large numbers of similar objects with a fixed structure, not general optimisation. Flexibility can be restored by adding `__dict__` or `__weakref__` to `__slots__`, but then part of the saving is lost.[^py314-reference-datamodel-slots]

**Common mistakes:**
- expecting memory savings from `__slots__` in a subclass that has no `__slots__` of its own;
- assuming that `__slots__` speeds up code automatically, without measuring on a real workload;
- setting a default value with a class attribute that has the name of a slot.

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
