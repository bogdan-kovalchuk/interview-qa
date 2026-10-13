---
id: py-oop-0005
title: "How does `__getattribute__` differ from `__getattr__`, and when is each one called?"
description: "How does `__getattribute__` differ from `__getattr__`, and when is each one called?"
track: python
section: oop-and-data-model
level: middle
type: comparison
tags: [getattribute, getattr]
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
  - source_id: py314-reference-datamodel-object-getattribute
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the object.__getattribute__ section of the data model."
  - source_id: py314-reference-datamodel-object-getattr
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__getattr__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the object.__getattr__ section of the data model."
  - source_id: py314-reference-datamodel-special-method-lookup
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#special-method-lookup
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the Special method lookup section of the data model."
---

## Short answer

**`__getattribute__` runs for every explicit attribute access on an instance (`obj.name` or `getattr(obj, 'name')`), while `__getattr__` runs only as a fallback when the normal lookup raises `AttributeError`.**[^py314-reference-datamodel-object-getattribute] <span class="warn">If you override `__getattribute__`, delegate carefully to `super().__getattribute__()`, or you can break access to all attributes, including methods.</span>[^py314-reference-datamodel-object-getattribute] `__getattr__` is safer: it does not affect the normal lookup path.[^py314-reference-datamodel-object-getattr]

## Detailed explanation

`__getattribute__` implements the access to an instance attribute itself. Python calls it for every explicit access `obj.name` and `getattr(obj, 'name')`, even when the attribute exists and the normal lookup would find it.[^py314-reference-datamodel-object-getattribute] `__getattr__` works differently: it is called only when the normal access ended with `AttributeError`, or when `__getattribute__` itself raised `AttributeError`.[^py314-reference-datamodel-object-getattr] So `__getattr__` is a fallback for missing attributes, while `__getattribute__` sees every explicit access.

The example shows the order of calls:

```python
class Tracer:
    def __init__(self):
        self.real = 1

    def __getattribute__(self, name):
        print(f"__getattribute__({name!r})")
        return object.__getattribute__(self, name)

    def __getattr__(self, name):
        print(f"__getattr__({name!r})")
        return "fallback"

    def __len__(self):
        return 3

t = Tracer()
print(t.real)      # __getattribute__('real'), then 1
print(t.nothing)   # __getattribute__('nothing'), __getattr__('nothing'), then 'fallback'
print(len(t))      # no __getattribute__ line: len() looks up __len__ on the type, prints 3
```

The `len(t)` line prints nothing from `__getattribute__`, because an implicit call of a special method looks up `__len__` on the type, not through ordinary attribute access. So this interceptor does not see implicit special-method calls.[^py314-reference-datamodel-special-method-lookup]

The main trap lies in how the override is written. `__getattribute__` must reach attributes through the base `object.__getattribute__` or `super().__getattribute__()`.[^py314-reference-datamodel-object-getattribute] If you write `return self.__dict__[name]`, the access to `self.__dict__` goes through `__getattribute__` again, the calls loop, and the program fails with `RecursionError`. If you instead return values only for some names and raise `AttributeError` otherwise, the class's methods stop being found.

That is why `__getattr__` is safer: it does not change the normal lookup path and is called only for missing attributes. For proxies, lazy computation, or default values it is usually sufficient. `__getattribute__` fits when every explicit access must be intercepted, for example for auditing, and then delegating to the base method is mandatory.

**Common mistakes:**
- assuming that `__getattr__` is called for every access and logging existing-attribute access in it; it never sees those;
- writing `self.__dict__` or `self.name` inside `__getattribute__`, which causes recursion;
- expecting `len(obj)` or `obj + 1` to pass through `__getattribute__`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
