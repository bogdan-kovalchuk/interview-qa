---
id: py-oop-0008
title: "How does the absence of `__dict__` in a class with `__slots__` affect dynamically adding attributes?"
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
  - source_id: py314-reference-datamodel-slots
    title: "Python 3.14: Reference/datamodel, __slots__"
    url: https://docs.python.org/3.14/reference/datamodel.html#slots
---

## Short answer

**An instance of a class in which every class of the inheritance chain defines `__slots__` has no `__dict__`, so trying to add an attribute that is not listed in `__slots__` raises `AttributeError`.**[^py314-reference-datamodel-slots] Attributes are stored in slots (class-level descriptors) instead of a dictionary; this saves memory on large sets of instances but limits flexibility.[^py314-reference-datamodel-slots] <span class="warn">If you add `'__dict__'` to `__slots__`, the instance gets a dictionary again and can accept arbitrary attributes.</span>[^py314-reference-datamodel-slots]

## Detailed explanation

By default, instance attributes are stored in the instance's `__dict__`, that is, in a separate dictionary for each instance. `__slots__` changes this: the class declares a fixed set of names, a descriptor is created on the class for each name, and `__dict__` and `__weakref__` are not created automatically unless they are listed.[^py314-reference-datamodel-slots] The memory saving can be significant, and attribute access can be faster.[^py314-reference-datamodel-slots]

The effect on dynamic attribute addition is easy to see in a small example:

```python
class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(hasattr(p, '__dict__'))  # False: no per-instance dictionary
try:
    p.z = 3                    # 'z' is not in __slots__
except AttributeError as e:
    print(e)                   # 3.13+: 'Point' object has no attribute 'z' and no __dict__ for setting new attributes (3.12 and earlier: only "...has no attribute 'z'")
```

The condition "every class in the chain" matters. If one of the base classes does not define `__slots__`, its `__dict__` is inherited, and the child class accepts arbitrary attributes even when it defines `__slots__` itself.[^py314-reference-datamodel-slots] Example:

```python
class Base:              # no __slots__: instances get __dict__
    pass

class Child(Base):
    __slots__ = ('x',)

c = Child()
c.extra = 1              # works: the inherited __dict__ accepts it
print(hasattr(c, '__dict__'))  # True
print(c.extra)                 # 1
```

Two more rules matter. A class attribute cannot provide a default value for a slot, because it would overwrite the slot's descriptor.[^py314-reference-datamodel-slots] In CPython such a class is not created (`ValueError`: `'x' in __slots__ conflicts with class variable`). If you need both slots and arbitrary attributes, add `'__dict__'` to `__slots__`, but then the instance has a dictionary again and part of the benefit of slots is lost.[^py314-reference-datamodel-slots]

**Common mistakes:**
- assuming that any class with `__slots__` forbids new attributes: with a base class that has no `__slots__`, a dictionary is present;
- writing a default value as a class attribute with the same name as a slot;
- adding `'__dict__'` to `__slots__` and expecting all the benefits of slots to remain.
