---
id: py-prac-0011
title: "In a descriptor with `__set__(self, obj, value): self._value = value`, two instances see the last value written: why does this happen, and where should per-instance state be stored?"
description: "self in __set__ is the descriptor object, which sits in the owner class as one class attribute, so self._value is shared by all instances."
track: python
section: practical-coding
level: middle
type: pitfall
tags: [set-self-obj-value-self-value-value]
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
  - source_id: py314-reference-datamodel-implementing-descriptors
    title: "Python 3.14: Reference/datamodel, Implementing Descriptors"
    url: https://docs.python.org/3.14/reference/datamodel.html#implementing-descriptors
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the descriptor must be in the class dictionary of the owner class or of a parent class; __set__ is called for an instance of the owner class. Does not describe a descriptor stored as an instance attribute."
  - source_id: py314-reference-datamodel-invoking-descriptors
    title: "Python 3.14: Reference/datamodel, Invoking Descriptors"
    url: https://docs.python.org/3.14/reference/datamodel.html#invoking-descriptors
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: a data descriptor with __get__ together with __set__ and/or __delete__ overrides a write to the instance dictionary; a descriptor without __get__ returns the descriptor object itself when the instance dictionary has no value. Does not describe user-written descriptor examples."
  - source_id: py314-reference-datamodel-object-set-name
    title: "Python 3.14: Reference/datamodel, object.__set_name__"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__set_name__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: __set_name__ is called when a class is created for a descriptor assigned to a class attribute, and receives the attribute name. Does not describe validation."
  - source_id: py314-reference-datamodel-slots
    title: "Python 3.14: Reference/datamodel, __slots__"
    url: https://docs.python.org/3.14/reference/datamodel.html#slots
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: __slots__ prevents the creation of __dict__ and __weakref__ unless they are declared in __slots__. Does not describe other ways of storing state."
  - source_id: py314-library-weakref-weakkeydictionary
    title: "Python 3.14: Library/weakref, WeakKeyDictionary"
    url: https://docs.python.org/3.14/library/weakref.html#weakref.WeakKeyDictionary
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: WeakKeyDictionary holds keys weakly, and entries are discarded when no strong reference to the key exists; not all objects support weak references. Does not describe hashability requirements for keys."
---

## Short answer

**`self` in `__set__` is a descriptor object, not an instance: it sits in the owner class once, so `self._value` is shared by all instances.**[^py314-reference-datamodel-implementing-descriptors] <span class="warn">Per-instance state must be stored on `obj`:</span> `obj.__dict__[self.name] = value` together with a `__get__` that reads the same key.[^py314-reference-datamodel-invoking-descriptors] The alternative is a `WeakKeyDictionary` keyed by `obj`, provided `obj` is hashable and supports weak references.[^py314-library-weakref-weakkeydictionary]

## Detailed explanation

A descriptor is an object that sits in the class dictionary of the owner class, and the protocol calls its methods with the instance as the `obj` argument.[^py314-reference-datamodel-implementing-descriptors] So `A.__dict__['x']` holds one `Shared` object, not one per `A()`. When `__set__` runs `self._value = value`, the value is written to that single object. `a.x = 1` and `b.x = 2` overwrite the same place, so both instances read the last value:

```python
class Shared:
    def __get__(self, obj, objtype=None):
        return self._value

    def __set__(self, obj, value):
        self._value = value  # stored on the descriptor, not on obj


class A:
    x = Shared()


a, b = A(), A()
a.x = 1
b.x = 2
print(a.x, b.x)  # 2 2
```

The right place for state is `obj` itself. A descriptor intercepts reads when it is a data descriptor defined with `__get__` together with `__set__` and/or `__delete__`: such a descriptor always overrides a write to the instance dictionary.[^py314-reference-datamodel-invoking-descriptors] A descriptor that has only `__set__` (or only `__delete__`) and no `__get__` does not intercept reads. The name for the key comes from `__set_name__`, which Python calls when the class is created with the descriptor in a class attribute.[^py314-reference-datamodel-object-set-name] In this example, reading before any write raises `KeyError` from `obj.__dict__[self.name]`; real code should handle that case.

```python
class Field:
    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        obj.__dict__[self.name] = value


class C:
    x = Field()


c1, c2 = C(), C()
c1.x = 1
c2.x = 2
print(c1.x, c2.x)  # 1 2
```

Without `__get__` the behaviour differs. A descriptor that has only `__set__` returns the value from `obj.__dict__` when there is one, and otherwise returns the descriptor object itself, without an error.[^py314-reference-datamodel-invoking-descriptors] So a class with a lone `__set__` that writes to `obj.__dict__` gives the descriptor, not a value, when it is read before the first write.

A `WeakKeyDictionary` keyed by `obj` does not change `obj`: its entries disappear when no strong reference to the key remains.[^py314-library-weakref-weakkeydictionary] The conditions are: `obj` must be hashable, because it is a dictionary key, and it must support weak references. A class with `__slots__` that has no `__dict__` has no `obj.__dict__`, and `__weakref__` is not created there either unless it is declared in `__slots__`.[^py314-reference-datamodel-slots]

**Common mistakes:**
- storing per-instance state in `self._value` of the descriptor: all instances then share one value;
- writing only `__set__` and expecting a read before any write to return a value: it returns the descriptor object itself;
- using `obj.__dict__` for a class with `__slots__` and no `__dict__`: this raises `AttributeError`.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
