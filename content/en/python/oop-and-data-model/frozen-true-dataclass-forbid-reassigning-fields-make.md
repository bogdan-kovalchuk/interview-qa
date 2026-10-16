---
id: py-oop-0031
title: "Why does `frozen=True` on a `@dataclass` forbid reassigning fields, but not make a nested mutable object immutable?"
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
---

## Short answer

**`frozen=True` generates `__setattr__` and `__delattr__`, which raise `FrozenInstanceError` when you try to rebind a field.**[^py314-library-dataclasses] But this does not make nested objects immutable: `__setattr__` covers only assignment to the field itself, so `obj.mutable_list.append(1)` runs without error, and the change is visible through every reference to that list.[^py314-reference-datamodel] The dataclasses documentation states: "It is not possible to create truly immutable Python objects".[^py314-library-dataclasses]

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    items: list[int]

c = Config([1, 2])
c.items = [3]        # raises FrozenInstanceError
c.items.append(3)    # OK - c.items == [1, 2, 3]
```

## Detailed explanation

`@dataclass(frozen=True)` does not make an object immutable in the full sense. It adds `__setattr__` and `__delattr__` methods to the class, and they raise `FrozenInstanceError` on assignment to a field. In CPython, trying to add a new attribute to an instance of the same class, such as `c.y = 5`, raises `FrozenInstanceError` too (observed on CPython 3.12 to 3.14). The protection therefore covers the instance's own attributes, not the objects those attributes refer to.

The blocking is implemented with ordinary class methods, so it is a convention of use rather than strict protection. `__init__` must also write the fields through `object.__setattr__()`, because the documentation says that simple assignment cannot be used to initialize fields in `__init__()` of a frozen class.[^py314-library-dataclasses] The same call is available to outside code: `object.__setattr__(c, 'items', [3])` bypasses the check.

The field `items` holds a reference to a `list` object. The frozen class forbids replacing the reference `c.items` itself, but the list stays mutable. The documentation describes this as a difference between immutability of references and immutability of value: when an immutable container holds a mutable object, the container's value changes along with that object.[^py314-reference-datamodel] The example below shows an assignment that is blocked, a mutation that goes through, and a hash that fails:

```python
from dataclasses import dataclass, FrozenInstanceError

@dataclass(frozen=True)
class Config:
    items: list[int]

c = Config([1, 2])
try:
    c.items = [3]
except FrozenInstanceError:
    print("reassignment blocked")
c.items.append(3)        # OK: the list object itself is still mutable
print(c.items)           # [1, 2, 3]
try:
    hash(c)              # frozen + eq generate __hash__, which hashes the list
except TypeError as e:
    print(e)             # unhashable type: 'list'
```

By default, `eq=True` and `frozen=True` together make `@dataclass` generate a `__hash__()` method.[^py314-library-dataclasses] In CPython that hash is computed from the fields, so a `list` field makes `hash(c)` impossible. A frozen instance that holds a list therefore cannot go into a `set` or be used as a `dict` key. For values that must really stay unchanged, make the fields hashable: `tuple` instead of `list`, `frozenset` instead of `set`. A `tuple` still fixes only its direct elements, though; if one of them is a mutable object, that object can be changed.[^py314-reference-datamodel]

**Common mistakes:**
- assuming that `frozen=True` makes the whole state immutable, including nested `list` and `dict` fields;
- passing the same `list` to another place and changing it there: the change is visible in `c.items`;
- putting a frozen class with a list field into a `dict` key or a `set` element and getting a `TypeError` from `hash()`.
