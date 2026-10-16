---
id: py-oop-0002
title: "Why does customizing an immutable subclass such as a custom `tuple` require `__new__`, while changes made only in `__init__` come too late?"
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
  - source_id: py314-library-stdtypes-tuple
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#tuple
---

## Short answer

**Immutable types (`tuple`, `str`, `int`) fix their value during creation in `__new__`, and `__init__` is called only after that.**[^py314-reference-datamodel-object-new] So customizing the contents of an immutable subclass must happen in `__new__`: `__init__` receives an object that already exists, and `tuple` does not allow its elements to be changed.[^py314-library-stdtypes-tuple]

```python
class Doubled(tuple):
    def __new__(cls, *args):
        return super().__new__(cls, (x * 2 for x in args))
```

## Detailed explanation

To see why `__init__` does not help here, separate the two stages. First `__new__` is called, and it is the step that creates the object with its contents. Only after that is `__init__` called, on the object that already exists.[^py314-reference-datamodel-object-init] For an ordinary class this hardly matters, because attributes can be added later. For a `tuple`, the contents are part of the value itself, and they cannot be changed after creation.[^py314-library-stdtypes-tuple]

The documentation states the purpose of `__new__` directly: it lets subclasses of immutable types (`int`, `str`, `tuple`) customize instance creation.[^py314-reference-datamodel-object-new] Here is a `tuple` subclass in which `__new__` builds the contents and `__init__` only sees them:

```python
class Doubled(tuple):
    def __new__(cls, *args):
        return super().__new__(cls, (x * 2 for x in args))

    def __init__(self, *args):
        # args are the original values; self already holds the doubled ones
        print("in __init__:", tuple(self), args)

d = Doubled(1, 2, 3)  # in __init__: (2, 4, 6) (1, 2, 3)
print(d)              # (2, 4, 6)
# d[0] = 10           # TypeError: 'Doubled' object does not support item assignment
```

So `__init__` sees both sets of data: the input arguments and the already built `self`. It can read the contents but cannot replace them. Item assignment on a `tuple` is not supported[^py314-library-stdtypes-tuple], and the attempt raises `TypeError`. Therefore, if the contents must differ from the arguments, build them in `__new__`. `__init__` suits work that does not change the contents, such as setting extra attributes on the subclass.

**Common mistakes:**
- moving the construction of the contents into `__init__`: the code runs there, but the contents are already fixed;
- writing `super().__new__(cls, *args)`: `tuple.__new__` takes one iterable argument, so three values raise `TypeError: tuple expected at most 1 argument, got 3`;
- assuming that `str` or `int` can be configured through `__init__` the same way as an ordinary class.
