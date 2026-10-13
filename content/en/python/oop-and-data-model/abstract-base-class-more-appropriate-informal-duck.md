---
id: py-oop-0025
title: "When is an abstract base class more appropriate than an informal duck-typing check?"
description: "An ABC fits when an interface must be enforced at instance creation, or when a virtual subclass is registered explicitly with register(); for simple cases duck typing is enough."
track: python
section: oop-and-data-model
level: middle
type: comparison
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
  - source_id: py314-library-abc-abstractmethod
    title: "Python 3.14: Library/abc"
    url: https://docs.python.org/3.14/library/abc.html#abc.abstractmethod
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: abc.abstractmethod, the requirement that the metaclass is ABCMeta, and the fact that a class with unimplemented abstract methods cannot be instantiated."
  - source_id: py314-library-abc-abcmeta-register
    title: "Python 3.14: Library/abc"
    url: https://docs.python.org/3.14/library/abc.html#abc.ABCMeta.register
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: ABCMeta.register and virtual subclasses, for which issubclass() and isinstance() return True."
  - source_id: py314-library-abc-abcmeta-subclasshook
    title: "Python 3.14: Library/abc"
    url: https://docs.python.org/3.14/library/abc.html#abc.ABCMeta.__subclasshook__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: ABCMeta.__subclasshook__ and its return values True, False or NotImplemented, with an example that checks for __iter__."
  - source_id: py314-library-typing-runtime-checkable
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html#typing.runtime_checkable
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: runtime_checkable, which checks only the presence of methods or attributes, not their signatures or types."
---

## Short answer

**An ABC is the better choice when the contract must be checked earlier: a class that inherits from `ABC` (metaclass `ABCMeta`) and does not implement every `abstractmethod` cannot be instantiated.**[^py314-library-abc-abstractmethod] `register()` declares a class a virtual subclass without inheritance, but it does not check the existing methods (in CPython).[^py314-library-abc-abcmeta-register] For simple cases, where only the object's behaviour matters, duck typing is enough and more flexible.

## Detailed explanation

Duck typing checks behaviour at the point of use: if an object has the required method, the code works; if not, the error appears deep in the code, often as an `AttributeError`. An ABC moves the check to the moment an instance is created: a class with unimplemented abstract methods cannot be instantiated.[^py314-library-abc-abstractmethod] Example:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): ...

    @abstractmethod
    def perimeter(self): ...

class Half(Shape):
    def area(self):
        return 2

try:
    Half()
except TypeError as error:
    print(error)   # 3.12+: Can't instantiate abstract class Half without an implementation for abstract method 'perimeter'

class Registered:              # no base class, no methods
    pass

Shape.register(Registered)
print(isinstance(Registered(), Shape))  # True: register() does not check methods
```

The condition matters: the `abstractmethod` decorator requires that the class's metaclass is `ABCMeta` or derived from it.[^py314-library-abc-abstractmethod] Without `ABC` or `metaclass=ABCMeta`, it enforces nothing: in CPython, a class with `@abstractmethod` but without `ABCMeta` is created without error.

`isinstance()` and `issubclass()` can be extended in two ways. `register()` makes a class a virtual subclass, so the check returns `True` even without inheritance.[^py314-library-abc-abcmeta-register] The existence of methods is not checked (in CPython). This is an explicit claim by the author, not a structural check. The `__subclasshook__` method provides custom logic: it returns `True`, `False` or `NotImplemented`, and it can be written to check for the required methods; the documentation shows an example that checks for `__iter__`.[^py314-library-abc-abcmeta-subclasshook]

For structural checks without inheritance, there is `typing.Protocol`. The `@runtime_checkable` decorator allows `isinstance()` with a protocol, but such a check sees only the presence of methods or attributes, not their signatures or types.[^py314-library-typing-runtime-checkable]

**Common mistakes:**
- thinking that `@abstractmethod` without `ABC` or `ABCMeta` forbids anything;
- thinking that `register()` checks the class's methods (in CPython it does not);
- thinking that `isinstance()` with a `@runtime_checkable` Protocol checks method signatures.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
