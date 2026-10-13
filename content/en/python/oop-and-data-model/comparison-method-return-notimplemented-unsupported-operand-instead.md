---
id: py-oop-0023
title: "Why should a comparison method return `NotImplemented` for an unsupported operand instead of an immediate `False` or an exception?"
description: "If a comparison method returns NotImplemented, Python tries the other operand's reflected method; if that also refuses, == and != compare identity and ordering operators raise TypeError."
track: python
section: oop-and-data-model
level: senior
type: mechanism
tags: [notimplemented]
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
  - source_id: py314-reference-datamodel-object-eq
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__eq__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: rich comparison methods, the reflected method of the other operand, the fallback of == and != to is and is not, and the default behaviour of object."
  - source_id: py314-reference-datamodel-notimplemented
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#notimplemented
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: NotImplemented and its behaviour in a Boolean context (deprecated since 3.9, TypeError since 3.14)."
  - source_id: py314-reference-expressions-value-comparisons
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#value-comparisons
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: value comparisons, including the absence of a default order comparison, whose attempt raises TypeError."
---

## Short answer

**A comparison method returns `NotImplemented` when it does not support the other operand, and then the interpreter tries the reflected method of the other operand.**[^py314-reference-datamodel-object-eq] If that method also returns `NotImplemented`, `==` and `!=` compare identity with `is` and `is not`.[^py314-reference-datamodel-object-eq] Ordering operators raise `TypeError` in that case (in CPython). Returning `False` instead of `NotImplemented` closes this path for the other operand.[^py314-reference-datamodel-object-eq]

## Detailed explanation

For `a == b`, the interpreter normally calls `type(a).__eq__(a, b)` first. If the types differ and the type of the right operand is a direct or indirect subclass of the type of the left operand, the reflected method of the right operand is called first. `__eq__` is its own reflection, so the second call is `type(b).__eq__(b, a)`.[^py314-reference-datamodel-object-eq] If no method returns a value other than `NotImplemented`, `==` and `!=` fall back to `is` and `is not`.[^py314-reference-datamodel-object-eq]

The important difference is the value `False`. It is a final answer, and the other method is never called. `NotImplemented` means "this type does not know about this operand", and the decision passes to the other side. The example shows both behaviours:

```python
class Strict:
    def __eq__(self, other):
        return False                  # final answer: the reflected method is never tried

class Lenient:
    def __eq__(self, other):
        return NotImplemented         # "not mine": the other operand decides

class Accepting:
    def __eq__(self, other):
        return True

print(Strict() == Accepting())        # False: Strict answered first
print(Lenient() == Accepting())       # True: Accepting.__eq__ is tried next
print(Lenient() == 1)                 # False: both sides gave NotImplemented, so == uses is
```

`Strict` answers at once, so `Accepting` is never asked. `Lenient` returns `NotImplemented`, and the decision passes to `Accepting.__eq__`. The third line shows the fallback: when both operands refuse, `==` compares identity.

An exception in `__eq__` is worse: `a == b` with any "foreign" object (also `in`, `list.index`) fails, and the reflected method of the other operand never gets a chance.

Ordering operators have no fallback to identity. The documentation says that there is no default order comparison and that an attempt to use one raises `TypeError`.[^py314-reference-expressions-value-comparisons] In CPython, when both operands return `NotImplemented` for `<`, the message names both types, for example `'<' not supported between instances of 'A' and 'int'`.

`NotImplemented` must not be used in a Boolean context. Until Python 3.14 this was deprecated (a DeprecationWarning since 3.9), and in 3.14 `bool(NotImplemented)` raises `TypeError`.[^py314-reference-datamodel-notimplemented] So `if self.__eq__(other):` raises `TypeError` in 3.14 when the method returned `NotImplemented`.

**Common mistakes:**
- returning `None` or `False` instead of `NotImplemented` for an unsupported type: an `__eq__` that returns `None` makes `None` the result of `==`, and `False` blocks the other operand;
- expecting `TypeError` from `==` with an unsupported type: `==` gives `False`, and `TypeError` appears for ordering operators;
- writing `if self.__eq__(other):` or `bool(NotImplemented)`: in 3.9–3.13 this is a DeprecationWarning, and in 3.14 it is a `TypeError`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
