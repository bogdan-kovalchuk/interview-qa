---
id: py-oop-0012
title: "How should a reusable validation descriptor store values separately for each instance, without creating shared state between objects?"
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
  - source_id: py314-reference-datamodel-object-set-name
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__set_name__
  - source_id: py314-howto-descriptor-managed-attributes
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#managed-attributes
  - source_id: py314-howto-descriptor-automatic-name-notification
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#automatic-name-notification
---

## Short answer

**The descriptor stores data not in itself (it is one per class), but in `instance.__dict__` under a private key whose name is defined through `__set_name__`.**[^py314-howto-descriptor-managed-attributes] `__set_name__` is called automatically when the class is created and passes the descriptor the attribute name; the descriptor computes the private name (for example, `'_' + name`) and stores and reads the value through `setattr(obj, self.private_name, value)` and `getattr(obj, self.private_name)`.[^py314-reference-datamodel-object-set-name] This way one descriptor object per class serves many instances without shared mutable state.

## Detailed explanation

The main trap is where the descriptor lives. It is one per class, because it sits in `class.__dict__`. If it stored a value in `self.value`, all instances would share one value. So the descriptor keeps the rules (name, limits, check) and stores each value in its own instance.

`__set_name__` supplies the name for the key. When the class is created, `type.__new__` finds the descriptors that define this method and calls it with the owning class and the attribute name.[^py314-reference-datamodel-object-set-name] The descriptor then builds a private key (here `_price`) and stores the value in `obj.__dict__` through `setattr`. The public attribute is a descriptor in the class, while the actual data lives in the instance dictionary.[^py314-howto-descriptor-managed-attributes] The key `_price` is only a convention: `a._price` is reachable by anyone, because Python does not enforce privacy.

Example: a descriptor checks that a value is positive and stores it separately for each instance. The comments show the output (CPython 3.14):

```python
class Positive:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name       # key used in the instance __dict__

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self                      # accessed on the class
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.public_name} must be positive")
        setattr(obj, self.private_name, value)

class Item:
    price = Positive()
    qty = Positive()

a = Item()
b = Item()
a.price = 10
b.price = 20
print(a.price, b.price)              # 10 20: each instance keeps its own value
print(a.__dict__)                    # {'_price': 10}: the data lives on the instance
try:
    b.qty                            # no value has been stored yet
except AttributeError:
    print("qty is not set")          # qty is not set
```

Limits. `__set_name__` runs only when the class is created: a descriptor added later through `setattr` gets no name until you call `__set_name__` manually.[^py314-howto-descriptor-automatic-name-notification] The same descriptor object placed in two classes receives two `__set_name__` calls, and the last one overwrites `public_name` and `private_name`, so each attribute needs its own descriptor. Also, `getattr` for a value that has not been set yet raises `AttributeError`, so `__get__` must either return a default or report the absence explicitly.

**Common mistakes:**
- storing the value in the descriptor's `self.value`: one value for the whole class;
- using the same descriptor object for several attributes or classes;
- treating `_name` as private: it can be accessed directly, and the name may clash with another attribute.
