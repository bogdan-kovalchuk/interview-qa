---
id: py-oop-0001
title: "How does `__new__` differ from `__init__` in its role in creating an instance and in its return value?"
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
  - source_id: py314-reference-datamodel-object-new
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__new__
  - source_id: py314-reference-datamodel-object-init
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__init__
---

## Short answer

**`__new__` creates and returns a new instance, while `__init__` only initializes an instance that already exists.**[^py314-reference-datamodel-object-new] `__new__` is an implicit staticmethod that receives `cls` and returns an object, usually an instance of `cls`. `__init__` receives the ready `self`, sets up its attributes, and returns nothing but `None`.[^py314-reference-datamodel-object-init]

## Detailed explanation

`__new__` and `__init__` handle different stages of creating an object. `__new__` is a static method (you do not need to decorate it with `@staticmethod`) that receives the class as its first argument and returns a new object, usually an instance of that class.[^py314-reference-datamodel-object-new] `__init__` does not create the object: Python calls it after `__new__`, on the finished instance, to set up its attributes.[^py314-reference-datamodel-object-init]

When you write `Cls(...)`, Python first calls `__new__(cls, ...)` with the same arguments. It then calls `__init__` only if `__new__` returned an instance of `cls`. If the result has another type, `__init__` is not run, and the value of `Cls(...)` is whatever `__new__` returned.[^py314-reference-datamodel-object-new] This is what it looks like in practice:

```python
class Redirect:
    def __new__(cls, x):
        return x                  # an int, not an instance of Redirect

    def __init__(self, x):
        print("never printed")    # skipped: __new__ did not return a Redirect

r = Redirect(5)
print(r, type(r))                 # 5 <class 'int'>
```

The rule for `__init__` is different: it must not return anything except `None`. That rule is covered in qid:py-oop-0003. So `__init__` is used to configure an object, and `__new__` decides which object gets created at all.

**When `__new__` is needed.** Ordinary classes only need `__init__`. Override `__new__` when you must influence the object being created. The documentation states its purpose plainly: it lets subclasses of immutable types (`int`, `str`, `tuple`) customize instance creation.[^py314-reference-datamodel-object-new]

**Common mistakes:**
- assuming `__init__` creates the object, so a `return self` at its end looks like a way to return the result;
- forgetting `return` in `__new__`: `super().__new__(cls)` without a `return` gives `None`, and `__init__` is not called;
- expecting `__init__` to run every time, even when `__new__` returned an object of another type.
