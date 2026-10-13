---
id: py-oop-0015
title: "How does the function descriptor turn a function into a bound method when accessed through an instance, but not when accessed through the class?"
description: "How does the function descriptor turn a function into a bound method when accessed through an instance, but not when accessed through the class?"
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
    applicability: "Official Python 3.14 documentation: Invoking Descriptors section of the data model; the __get__ arguments for access through an instance and through the class."
  - source_id: py314-howto-descriptor-functions-and-methods
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#functions-and-methods
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: Functions and Methods section; a function as a non-data descriptor that returns itself for obj None and a MethodType otherwise."
  - source_id: py314-howto-descriptor-class-methods
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#class-methods
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: Class methods section; a classmethod receives the class whether it is called through the class or an instance."
  - source_id: py314-howto-descriptor-static-methods
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#static-methods
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: Static methods section; a staticmethod returns the underlying function unchanged."
  - source_id: cpython-funcobject-func-descr-get
    title: "CPython Objects/funcobject.c: func_descr_get"
    url: https://github.com/python/cpython/blob/v3.14.7/Objects/funcobject.c
    accessed: 2026-10-13
    kind: official
    version: "3.14.7"
    applicability: "CPython 3.14.7 source: the func_descr_get function; an implementation detail of CPython, not a language guarantee."
---

## Short answer

**`function.__get__(obj, objtype)` checks `obj`: if `obj is None` (access through the class), it returns the function itself; otherwise it returns `MethodType(func, obj)`.**[^py314-howto-descriptor-functions-and-methods] So `MyClass.method` gives a plain function with no binding to an instance, while `instance.method` gives a bound method with `__self__` already fixed. This logic lives in `func_descr_get()` in CPython and applies to all user-defined functions.[^cpython-funcobject-func-descr-get]

## Detailed explanation

When Python finds a descriptor in a class (or its bases) and the name is not shadowed by a value in the instance dictionary, it calls `__get__(obj, objtype)`. For access through an instance, `obj` is the instance itself. For access through the class, `obj` is `None`, and `objtype` is the class.[^py314-reference-datamodel-invoking-descriptors] The function implements this as follows: for `None` it returns itself, otherwise it creates a bound method.[^py314-howto-descriptor-functions-and-methods][^cpython-funcobject-func-descr-get]

The consequence is visible in the code. `Calc.add` is a plain function, so `self` must be passed explicitly. Accessed through the class, the function is returned unchanged, so nothing checks the first argument: `Calc.add(42, 1)` works and gives `2`. `c.add` is a bound method that passes `c` itself.

The example shows that access through the class does not bind a function, while a classmethod binds even when accessed through the class. The comments show the output (CPython 3.14):

```python
class Calc:
    def add(self, x):
        return x + 1

    @classmethod
    def make(cls):
        return cls

c = Calc()
print(type(Calc.add).__name__)       # function: no binding on class access
print(Calc.add(c, 1))                # 2: self must be passed explicitly
print(Calc.add(42, 1))               # 2: no type check on the first argument
print(type(c.add).__name__)          # method: bound on instance access
print(c.add.__self__ is c)           # True
print(Calc.make)                     # <bound method Calc.make of <class '__main__.Calc'>>
```

Binding on class access depends on the type of the descriptor. A `classmethod` binds the class both when accessed through the class and through an instance. A `staticmethod` returns the function unchanged in both cases.[^py314-howto-descriptor-class-methods][^py314-howto-descriptor-static-methods] So the rule "class access does not bind" applies to plain functions, not to every method.

**Common mistakes:**
- treating `Calc.add` as a bound method and calling `Calc.add(1)`: this raises `TypeError`, because `1` becomes `self` and the argument `x` is not passed;
- assuming that a `classmethod` accessed through the class behaves like a plain function: it binds to the class;
- confusing `c.add` without parentheses with a call: it returns a bound method, not a result.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
