---
id: py-oop-0011
title: "Why can `property` be seen as a descriptor, and when is it better than explicit `get_*`/`set_*` methods?"
description: "Why can `property` be seen as a descriptor, and when is it better than explicit `get_*`/`set_*` methods?"
track: python
section: oop-and-data-model
level: middle
type: comparison
tags: [property, get, set]
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
    applicability: "Official Python 3.14 documentation: Invoking Descriptors section of the data model; data descriptors and their precedence over the instance dictionary."
  - source_id: py314-howto-descriptor-properties
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#properties
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: Properties section; property as a data descriptor that calls a function on attribute access."
  - source_id: py314-howto-descriptor-invocation-summary
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#summary-of-invocation-logic
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: Summary of invocation logic section; descriptors are invoked by __getattribute__, so overriding it prevents automatic descriptor calls."
---

## Short answer

**`property` is a built-in data descriptor that implements `__get__`, `__set__` and `__delete__`.**[^py314-reference-datamodel-invoking-descriptors] It is better than explicit `get_*`/`set_*` methods when validation or computation must be added to an existing attribute access without changing the public API: callers keep writing `obj.attr`, not `obj.get_attr()`. As a data descriptor, `property` takes precedence over `instance.__dict__`: a read goes through the getter unless the class's `__getattribute__` implementation bypasses the `object` mechanism.[^py314-reference-datamodel-invoking-descriptors][^py314-howto-descriptor-invocation-summary] An assignment goes through the setter under the default `__setattr__`; a class-defined `__setattr__` can behave differently.

## Detailed explanation

When `@property` sits above a method, Python puts an object of type `property` into the class namespace in place of the function. That object is a descriptor: it defines `__get__`, `__set__` and `__delete__`, so it is a data descriptor.[^py314-reference-datamodel-invoking-descriptors] You can check this directly: `hasattr(property, "__set__")` is `True`.

The mechanism is simple. For `t.celsius`, Python finds the `property` in the class, sees a data descriptor and calls its `__get__`, which runs the getter function. Assignment `t.celsius = v` calls the setter, and `del t.celsius` calls the deleter if one is defined.[^py314-howto-descriptor-properties] A data descriptor takes precedence over the instance dictionary, so the entry `t.__dict__["celsius"] = 999` changes nothing: `t.celsius` still returns the getter's result.[^py314-reference-datamodel-invoking-descriptors]

The example shows a getter, a setter, and an attempt to bypass the descriptor through `__dict__`. The comments show the output (CPython 3.14):

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("below absolute zero")
        self._celsius = value

t = Temperature(20)
print(t.celsius)                                                       # 20: the getter runs
print(hasattr(property, "__set__"), hasattr(property, "__delete__"))   # True True
t.__dict__["celsius"] = 999                                            # a plain entry in the instance dict
print(t.celsius)                                                       # 20: the data descriptor wins
try:
    t.celsius = -300                                                   # the setter runs and rejects the value
except ValueError as error:
    print("ValueError:", error)                                        # ValueError: below absolute zero
```

When `property` is better than explicit methods. The `get_*`/`set_*` methods change the contract: once validation appears, every caller must be rewritten. With `property`, the caller still writes `t.celsius` and the logic moves into the class. This fits when the attribute really is the object's state and the check or computation is cheap. The limits: every access runs the function, so an expensive getter, or one that raises an exception, surprises a caller who expects a plain field. Also, a `property` describes one attribute in one class; to reuse the same check for many attributes, write a descriptor class (see qid:py-oop-0012).

**Common mistakes:**
- treating `property` as a method and writing `t.celsius()`: the value is not callable, so this raises `TypeError`;
- expecting a property without a setter to accept assignment: it raises `AttributeError`;
- hiding expensive work or side effects in a getter when the caller expects a plain field read.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
