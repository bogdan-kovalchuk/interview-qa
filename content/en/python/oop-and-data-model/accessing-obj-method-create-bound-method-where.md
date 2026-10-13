---
id: py-oop-0013
title: "Why does accessing `obj.method` create a bound method, and where does the implicit `self` come from at call time?"
description: "Why does accessing `obj.method` create a bound method, and where does the implicit `self` come from at call time?"
track: python
section: oop-and-data-model
level: middle
type: mechanism
tags: [obj-method]
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
  - source_id: py314-howto-descriptor-functions-and-methods
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#functions-and-methods
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: Functions and Methods section; functions as non-data descriptors, MethodType, and bound methods with __func__ and __self__."
  - source_id: py314-reference-datamodel-invoking-descriptors
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#invoking-descriptors
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: Invoking Descriptors section of the data model; a non-data descriptor yields to a write in the instance dictionary."
  - source_id: py314-library-dis-load-attr
    title: "Python 3.14: Library/dis"
    url: https://docs.python.org/3.14/library/dis.html#opcode-LOAD_ATTR
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the LOAD_ATTR opcode with the method flag; CPython bytecode detail, not a language guarantee."
  - source_id: cpython-funcobject-func-descr-get
    title: "CPython Objects/funcobject.c: func_descr_get"
    url: https://github.com/python/cpython/blob/v3.14.7/Objects/funcobject.c
    accessed: 2026-10-13
    kind: official
    version: "3.14.7"
    applicability: "CPython 3.14.7 source: the func_descr_get function; an implementation detail of CPython, not a language guarantee."
---

## Short answer

**Functions are non-data descriptors: their `__get__`, when accessed through an instance, returns `MethodType(func, obj)`, which is the bound method.**[^py314-howto-descriptor-functions-and-methods] A bound method stores the pair `(__func__, __self__)`; when you call `obj.method(x)`, it automatically inserts `__self__` as the first argument before `x`.[^py314-reference-datamodel] So the implicit `self` is not syntax magic but the result of the function descriptor protocol.

## Detailed explanation

A function in a class is an object of type `function` that defines only `__get__`, with no `__set__` or `__delete__`. So it is a non-data descriptor. On `obj.method`, Python calls that function's `__get__` with `obj` and the class, and the function returns a bound method. The logic is short: if `obj` is `None`, return the function itself; otherwise create `MethodType(func, obj)`.[^py314-howto-descriptor-functions-and-methods][^cpython-funcobject-func-descr-get]

A bound method is a pair: `__func__` (the function from the class) and `__self__` (the instance). When it is called, `__self__` goes first, so `m(5)` means the same as `Counter.incr(c, 5)`.[^py314-reference-datamodel] The function `incr` itself does not contain `c`: the binding happens at access time, through the instance.

The example: access without a call creates a bound method, and `Counter.incr(c, 2)` is an ordinary function call with an explicit `self`. The comments show the output (CPython 3.14):

```python
class Counter:
    def __init__(self):
        self.n = 0

    def incr(self, step):
        self.n += step
        return self.n

c = Counter()
m = c.incr                           # no call yet: a bound method object is created
print(type(m).__name__)              # method
print(m.__self__ is c)               # True
print(m.__func__ is Counter.incr)    # True: the same function, found on the class
print(m(5))                          # 5: __self__ is passed as the first argument
print(Counter.incr(c, 2))            # 7: explicit self, the same function
print(c.incr is c.incr)              # False: a new bound method object on each access
print(c.incr == c.incr)              # True: equal, because __self__ and __func__ match
```

Each access to `c.incr` creates a new bound method. So `c.incr is c.incr` is `False`, and `c.incr == c.incr` is `True`: equality compares `__self__` and `__func__`. Because a function is a non-data descriptor, a write `c.incr = ...` into the instance dictionary takes precedence over the class, and `c.incr` then returns the written value.[^py314-reference-datamodel-invoking-descriptors]

In the expression `c.incr(5)`, CPython does not create an intermediate bound method: in CPython 3.12+ the `LOAD_ATTR` bytecode with the method flag (formerly `LOAD_METHOD`) pushes the function and `self` onto the stack, and `CALL` passes `self` as the first argument.[^py314-library-dis-load-attr] The semantics are the same, so both forms are correct; the difference is only an implementation detail.

A bound method kept in a variable holds `__self__`, which is the instance itself.[^py314-reference-datamodel] So the variable keeps a reference to the instance, and while the variable is alive, the instance is not freed.

**Common mistakes:**
- expecting `c.incr` to run the method: without parentheses it returns a bound method, not a result;
- treating `c.incr is c.incr` as proof that the method is the same object: each access creates a new one;
- storing a bound method as a callback without realizing that it keeps the instance alive.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
