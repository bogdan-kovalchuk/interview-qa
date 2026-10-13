---
id: py-oop-0004
title: "In what order does Python look up an instance attribute when a data descriptor, instance dictionary, non-data descriptor, and class attribute are all present?"
description: "In what order does Python look up an instance attribute when a data descriptor, instance dictionary, non-data descriptor, and class attribute are all present?"
track: python
section: oop-and-data-model
level: senior
type: mechanism
tags: []
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
  - source_id: py314-reference-datamodel-invoking-descriptors
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#invoking-descriptors
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the Invoking Descriptors section of the data model."
  - source_id: py314-reference-datamodel-object-getattr
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the object.__getattr__ section of the data model."
---

## Short answer

**The order is: data descriptor -> instance `__dict__` -> non-data descriptor or class attribute -> `__getattr__`.**[^py314-reference-datamodel-invoking-descriptors] A data descriptor that defines `__get__` together with `__set__` and/or `__delete__` takes precedence over the instance `__dict__`, while a non-data descriptor (only `__get__`) yields to an entry in the instance `__dict__`. If the default `object.__getattribute__` finds nothing and `__getattr__` is defined, it is called; otherwise `AttributeError` is raised.[^py314-reference-datamodel-object-getattr]

## Detailed explanation

When Python evaluates `a.x`, it first looks in the class: is there an attribute `x` in `type(a)` (and in its bases, following the MRO), and is it a data descriptor (`__get__` together with `__set__` and/or `__delete__`)? A data descriptor found in the class takes precedence even over an entry with the same name in `a.__dict__`: its `__get__` is called immediately.[^py314-reference-datamodel-invoking-descriptors] This is how `property` works, since it is a data descriptor, so an instance cannot override its behaviour.[^py314-reference-datamodel-invoking-descriptors] A `property` without a `setter` does not allow the attribute to be written, not even with `self.x = ...`.

If the class has no data descriptor for the name, `a.__dict__` is checked. An entry in the instance wins over a non-data descriptor and over a plain class attribute. This is why methods, which are non-data descriptors, can be overridden on a single instance.[^py314-reference-datamodel-invoking-descriptors] Only when there is no entry in `__dict__` does Python return the result of the non-data descriptor's `__get__`, or the value of the class attribute.

The following example covers all of these cases, and each `print` shows which one applied:

```python
class DataDesc:
    def __get__(self, obj, objtype=None):
        return "data descriptor"

    def __set__(self, obj, value):
        pass

class NonDataDesc:
    def __get__(self, obj, objtype=None):
        return "non-data descriptor"

class C:
    d = DataDesc()
    n = NonDataDesc()
    k = "class attribute"

    def __getattr__(self, name):
        return f"__getattr__({name!r})"

c = C()
c.__dict__["d"] = "instance dict"
c.__dict__["n"] = "instance dict"
c.__dict__["k"] = "instance dict"
print(c.d)        # data descriptor: wins over the instance dict
print(c.n)        # instance dict: wins over a non-data descriptor
print(c.k)        # instance dict: wins over a plain class attribute
del c.__dict__["n"]
print(c.n)        # non-data descriptor, now that the dict entry is gone
print(c.missing)  # __getattr__('missing'): the normal lookup found nothing
```

`__getattr__` sits at the very end of the chain: it is called only when the normal lookup has ended with `AttributeError`. It therefore never overrides an existing attribute, even when it is defined.[^py314-reference-datamodel-object-getattr]

**Common mistakes:**
- assuming that an entry in `obj.__dict__` always overrides a class attribute: this is not true for a `property`, and `self.x = 5` in a class with a `property` that has no setter raises `AttributeError: property 'x' of 'Q' object has no setter`;
- expecting `__getattr__` to be called on every access; it runs only when the normal lookup found nothing;
- forgetting that the order describes the default `object.__getattribute__`: an overridden `__getattribute__` changes this path (see qid:py-oop-0005).

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
