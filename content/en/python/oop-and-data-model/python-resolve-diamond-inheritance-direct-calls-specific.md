---
id: py-oop-0018
title: "How does Python resolve diamond inheritance, and why can direct calls to specific parent methods run one link twice?"
track: python
section: oop-and-data-model
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
  - source_id: py314-howto-descriptor
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html
  - source_id: py314-howto-mro
    title: "Python 3.14: Howto/mro"
    url: https://docs.python.org/3.14/howto/mro.html
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
  - source_id: py314-builtins-functions-super
    title: "Python 3.14: Built-in Functions/super"
    url: https://docs.python.org/3.14/builtins/functions.html#super
---

## Short answer

**The C3 MRO places each class of a diamond exactly once, and `super()` follows that order; direct calls such as `Parent.method(self)` look up the method in `Parent` itself and its ancestors, so they bypass the MRO of the object's actual type.**[^py314-howto-mro][^py314-reference-datamodel] <span class="warn">If `Left.method` and `Right.method` call `Base.method(self)` directly, then `Bottom.method`, which calls both, runs `Base.method` twice.</span> The fix is the cooperative pattern: each class calls `super().method()`, and the chain visits each class of the MRO once.[^py314-builtins-functions-super]

## Detailed explanation

The diamond is `Bottom(Left, Right)`, where `Left(Base)` and `Right(Base)`. For this hierarchy, C3 builds `Bottom.__mro__ = Bottom, Left, Right, Base, object`. The merge step adds a class to the result and removes it from all lists, so the shared base `Base` appears in the MRO only once.[^py314-howto-mro] Attribute lookup through the base classes uses the same C3 MRO and works correctly with diamonds.[^py314-reference-datamodel]

First the direct calls, then the cooperative version with `super()` in the same example:

```python
class Base:
    def method(self):
        print('Base.method')

class Left(Base):
    def method(self):
        print('Left.method')
        Base.method(self)      # direct call: bypasses the MRO

class Right(Base):
    def method(self):
        print('Right.method')
        Base.method(self)

class Bottom(Left, Right):
    def method(self):
        print('Bottom.method')
        Left.method(self)
        Right.method(self)

Bottom().method()
# Bottom.method
# Left.method
# Base.method
# Right.method
# Base.method   <- the shared base runs twice

class CoBase:
    def method(self):
        print('CoBase.method')

class CoLeft(CoBase):
    def method(self):
        print('CoLeft.method')
        super().method()

class CoRight(CoBase):
    def method(self):
        print('CoRight.method')
        super().method()

class CoBottom(CoLeft, CoRight):
    def method(self):
        print('CoBottom.method')
        super().method()

CoBottom().method()
# CoBottom.method
# CoLeft.method
# CoRight.method
# CoBase.method   <- each class runs once, in MRO order
```

In the direct version, `Base.method(self)` names the class explicitly. The lookup starts in `Base` and its ancestors, not in the MRO of `Bottom`, so both `Left` and `Right` reach `Base.method`, and it runs twice.[^py314-reference-datamodel]

In the cooperative version, each class calls `super().method()`. `CoBottom` passes control through `super()` to `CoLeft`, `CoLeft` passes it to `CoRight` because the class after `CoLeft` in the MRO of `CoBottom` is `CoRight`, and `CoRight` passes it to `CoBase`. Each class runs once, in MRO order.[^py314-builtins-functions-super]

A class that does not call `super()` ends the chain: the classes after it in the MRO do not run. That is why the pattern works only when every class in the chain calls `super()`.

**Common mistakes:**
- writing `Parent.method(self)` in a class with several bases instead of `super().method()`;
- assuming that a shared base in a diamond runs once automatically when two parents call it directly;
- leaving out `super()` in one class of the chain, so the classes after it in the MRO silently do not run.
