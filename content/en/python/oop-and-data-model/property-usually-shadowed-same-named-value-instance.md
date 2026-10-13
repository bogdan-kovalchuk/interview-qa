---
id: py-oop-0007
title: "Why can a property usually not be shadowed by a same-named value in `instance.__dict__`?"
description: "Why can a property usually not be shadowed by a same-named value in `instance.__dict__`?"
track: python
section: oop-and-data-model
level: senior
type: mechanism
tags: [instance-dict]
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
    title: "Python 3.14: Reference/datamodel, Invoking Descriptors"
    url: https://docs.python.org/3.14/reference/datamodel.html#invoking-descriptors
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: a data descriptor defines __set__ or __delete__ and takes precedence over the instance dictionary; a non-data descriptor (including ordinary methods) can be overridden by the instance dictionary; @property is implemented as a data descriptor. Does not describe user-written descriptor examples."
  - source_id: py314-howto-descriptor-properties
    title: "Python 3.14: Howto/descriptor, Properties"
    url: https://docs.python.org/3.14/howto/descriptor.html#properties
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: property() builds a data descriptor that calls a function when the attribute is accessed. Does not describe assignment to a property without a setter."
---

## Short answer

**`property` is implemented as a data descriptor (it defines `__get__`, `__set__`, `__delete__`), so under the attribute lookup rules it takes precedence over the instance `__dict__`.**[^py314-reference-datamodel-invoking-descriptors] Even if you write `obj.__dict__['x'] = value` by hand, `obj.x` calls the property getter and does not return the value from the dictionary. <span class="warn">The dictionary is still reachable directly through `obj.__dict__['x']`, but `obj.x` does not return it; the behaviour of `obj.x` can only be changed at class level, for example by replacing the property itself.</span>

## Detailed explanation

Attribute lookup for `obj.x` first finds `x` in the class. If the object found defines `__get__` and `__set__` (and/or `__delete__`), it is a data descriptor that overrides the instance dictionary: Python calls its `__get__` and does not read the dictionary.[^py314-reference-datamodel-invoking-descriptors] `property()` builds exactly such a descriptor, which calls a function when the attribute is accessed.[^py314-howto-descriptor-properties] So even a `property` without a setter is a data descriptor: assigning `obj.x = ...` to it raises `AttributeError` and does not store a value in the dictionary.

An example: a class with a property, and a value with the same name written into the dictionary directly:

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

t = Temperature(20)
t.__dict__['celsius'] = 99     # the dict now holds a value under the same name
print(t.celsius)               # 20: the property wins, the dict entry is ignored
print(t.__dict__['celsius'])   # 99: the value is there, but attribute access never returns it
try:
    t.celsius = 5
except AttributeError as e:
    print(e)                   # property 'celsius' of 'Temperature' object has no setter
```

The word "usually" in the question matters. Only a data descriptor takes precedence over the dictionary; a non-data descriptor, such as an ordinary method, can be overridden by the instance dictionary.[^py314-reference-datamodel-invoking-descriptors] This is what makes a property reliable as a control point: the getter and setter logic runs on every access through `obj.x`, so an instance cannot bypass it by writing to its own dictionary.[^py314-reference-datamodel-invoking-descriptors] For that reason, the value a property stores usually lives in a different attribute (here `_celsius`), not under the property's own name.

**Common mistakes:**
- assuming that writing `obj.__dict__['x']` changes the result of `obj.x` when a property named `x` exists;
- expecting an assignment to a property without a setter to create a value in the dictionary: it raises `AttributeError`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
