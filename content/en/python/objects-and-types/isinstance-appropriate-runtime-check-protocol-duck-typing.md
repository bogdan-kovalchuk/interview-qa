---
id: py-objtypes-0021
title: "When is `isinstance()` an appropriate runtime check, and when does a protocol or duck typing make code less coupled to concrete classes?"
description: "When is `isinstance()` an appropriate runtime check, and when does a protocol or duck typing make code less coupled to concrete classes?"
track: python
section: objects-and-types
level: middle
type: comparison
tags: [isinstance]
status: published
updated: 2026-09-27
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
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**`isinstance()` is appropriate at API boundaries for defensive guards, in dispatch logic (such as serialization), and with ABCs for virtual subclasses.**[^py314-reference-datamodel] However, checking against a concrete class tightly couples code to a specific inheritance hierarchy. `typing.Protocol` with `@runtime_checkable` and duck typing inspect behaviour (the presence of methods or attributes) without requiring nominal subclasses. Duck typing relies on handling `AttributeError` at runtime, whereas a `@runtime_checkable` Protocol only verifies attribute presence without inspecting method signatures.

## Detailed explanation

The `isinstance()` function is designed for nominal type checking and inheritance hierarchies, whereas duck typing and `typing.Protocol` focus on structural compatibility – the presence of required methods and attributes regardless of an object's origin.[^py314-reference-datamodel]

A direct `isinstance(obj, ConcreteClass)` check is justified at system boundaries for defensive guards (such as distinguishing `str` from generic iterables), as well as in dispatch logic (like `functools.singledispatch` or serializers). Moreover, Abstract Base Classes (ABCs) provide `__instancecheck__` and virtual subclass registration via `.register()`, allowing types to satisfy `isinstance()` without concrete inheritance.[^py314-reference-datamodel] However, binding runtime checks to concrete implementation classes violates the Liskov substitution principle and hinders mocking during testing.

Duck typing adheres to the EAFP (*Easier to Ask for Forgiveness than Permission*) idiom: instead of inspecting an object beforehand, the code directly performs the operation and catches `AttributeError` or `TypeError`. The `@runtime_checkable` decorator on `typing.Protocol` bridges static type checking with runtime inspection by enabling `isinstance(obj, MyProtocol)`.[^py314-library-typing] However, at runtime `@runtime_checkable` only verifies attribute presence (`hasattr`), completely ignoring method signatures, argument counts, and return types.

Differences between nominal checks, `@runtime_checkable`, and duck typing:

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Closable(Protocol):
    def close(self) -> None:
        ...

class Resource:
    def close(self) -> None:
        pass

class FaultyResource:
    close: int = 1  # attribute exists, but it is not callable

res = Resource()
faulty = FaultyResource()

# Protocol with @runtime_checkable inspects structural attributes via isinstance:
print(isinstance(res, Closable))     # True
print(isinstance(faulty, Closable))  # True: only checks hasattr(obj, 'close')!

# Duck typing (EAFP) verifies actual invocation at runtime:
def safe_close(obj: object) -> None:
    try:
        obj.close()  # type: ignore[attr-defined]
    except (AttributeError, TypeError):
        pass  # Object does not provide a callable close() method
```

**Common mistakes and practical limitations:**
- checking against concrete classes like `isinstance(obj, list)` instead of structural ABCs (`collections.abc.Sequence`), breaking generator and custom collection compatibility;
- assuming `@runtime_checkable` validates method signatures or parameter types at runtime;
- littering business logic with cascades of `if/elif isinstance(...)` branches instead of using polymorphism;
- catching overly broad exceptions like `Exception` instead of specific `(AttributeError, TypeError)` when applying duck typing.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
