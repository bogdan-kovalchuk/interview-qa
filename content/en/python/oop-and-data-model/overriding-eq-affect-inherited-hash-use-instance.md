---
id: py-oop-0024
title: "How does overriding `__eq__` affect the inherited `__hash__` and the use of an instance in a set or dict?"
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
  - source_id: py314-reference-datamodel-object-hash
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__hash__
  - source_id: py314-library-dataclasses-dataclass
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass
---

## Short answer

**A class that overrides `__eq__` without defining `__hash__` gets `__hash__ = None`: its instances become unhashable, so using them in a `set` or as a `dict` key raises `TypeError`.**[^py314-reference-datamodel-object-hash] Equal objects must have equal hashes, and a new `__eq__` without a consistent `__hash__` does not ensure this.[^py314-reference-datamodel-object-hash] A parent's `__hash__` is not inherited automatically; you can restore it explicitly with `__hash__ = Base.__hash__`, but then the author is responsible for keeping it consistent.[^py314-reference-datamodel-object-hash]

## Detailed explanation

Hashed collections (`set`, `frozenset`, `dict`) use the hash to choose a bucket and `__eq__` to compare the elements inside it. So the main requirement for `__hash__` is that objects which compare equal have the same hash.[^py314-reference-datamodel-object-hash] For mutable classes with `__eq__`, the documentation advises not to implement `__hash__`: if the hash changes after the key has been added, the element ends up in the wrong bucket.[^py314-reference-datamodel-object-hash]

Python sets `__hash__ = None` in a class that overrides `__eq__` and does not define `__hash__`.[^py314-reference-datamodel-object-hash] So a subclass that overrides `__eq__` loses the hash even when its parent class has one. Example:

```python
class Base:
    def __hash__(self):
        return 1

class Child(Base):
    def __eq__(self, other):
        return True

print(Child.__hash__)                 # None: Base.__hash__ is not inherited
try:
    hash(Child())
except TypeError as error:
    print(error)                      # unhashable type: 'Child'

class Id:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Id) and self.name == other.name

    __hash__ = object.__hash__        # id-based hash kept by hand: wrong for this __eq__

a, b = Id("x"), Id("x")
print(a == b, hash(a) == hash(b))     # True False: equal objects, different hashes
print(len({a, b}))                    # 2: both stay in the set
```

To restore the parent's hash, you must write `__hash__ = Base.__hash__` explicitly. But that hash has to match the new equality. In the `Id` example, the hash from `object` is based on identity, while `__eq__` compares `name`, so equal objects get different hashes. In CPython, a `set` compares elements for equality only when their hashes match, so both objects remain in the set.

The same mechanism applies to dataclasses: if the class does not define `__hash__` itself, then with `eq=True` and `frozen=False` (the default values) it is set to `None`, while with `frozen=True` the dataclass generates a hash from its fields.[^py314-library-dataclasses-dataclass]

**Common mistakes:**
- overriding `__eq__` in a subclass and expecting the parent's hash to keep working without an explicit decision;
- copying `__hash__ = Base.__hash__` into a class with different equality, which breaks the rule shown in the example;
- hashing a mutable object by fields that change after it has been added to a `set` or `dict`.
