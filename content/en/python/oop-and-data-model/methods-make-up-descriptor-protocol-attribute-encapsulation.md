---
id: py-oop-0010
title: "Which methods make up the descriptor protocol, and what attribute-encapsulation problem does it solve?"
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
  - source_id: py314-reference-datamodel-invoking-descriptors
    title: "Python 3.14: Reference/datamodel, Invoking Descriptors"
    url: https://docs.python.org/3.14/reference/datamodel.html#invoking-descriptors
  - source_id: py314-reference-datamodel-implementing-descriptors
    title: "Python 3.14: Reference/datamodel, Implementing Descriptors"
    url: https://docs.python.org/3.14/reference/datamodel.html#implementing-descriptors
  - source_id: py314-reference-datamodel-object-set-name
    title: "Python 3.14: Reference/datamodel, object.__set_name__"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__set_name__
  - source_id: py314-howto-descriptor-validator-class
    title: "Python 3.14: Howto/descriptor, Validator class"
    url: https://docs.python.org/3.14/howto/descriptor.html#validator-class
  - source_id: py314-tutorial-classes-private-variables
    title: "Python 3.14: Tutorial/classes, Private Variables"
    url: https://docs.python.org/3.14/tutorial/classes.html#private-variables
---

## Short answer

**The descriptor protocol consists of `__get__`, `__set__` and `__delete__`; a class that defines at least one of them is a descriptor, and it lets you move attribute-access logic (validation, computation, logging) into a separate object while keeping ordinary dot syntax.**[^py314-reference-datamodel-invoking-descriptors] Instead of requiring callers to write `get_x()` / `set_x()`, a descriptor intercepts `obj.x` when it is found in the class. This lets you change the internal storage without changing the public interface, but the descriptor itself does not make the attribute private.[^py314-tutorial-classes-private-variables]

## Detailed explanation

The descriptor protocol is three methods: `__get__` for reading, `__set__` for assignment, and `__delete__` for `del`. Any object that defines at least one of them is a descriptor. Python uses it when it finds such an object as a class attribute during `obj.x`.[^py314-reference-datamodel-invoking-descriptors] The descriptor must be in the class dictionary or in the dictionary of a base class, so a descriptor stored as an instance attribute is not called.[^py314-reference-datamodel-implementing-descriptors]

The problem it solves is clearer when you look at the alternatives. A plain attribute gives no place for control: if validation is needed later, every place that assigns the attribute must change. Methods `get_x()` and `set_x()` give a place for control, but they change the API: every call site has to be rewritten. A descriptor gives both control and ordinary syntax: the class declares it once, and users write `obj.x = value`. This is exactly how a descriptor manages attribute access and checks a value before storing it.[^py314-howto-descriptor-validator-class]

An example: the descriptor `Positive` checks a value before storing it, and `Box` uses plain assignment syntax:

```python
class Positive:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name   # where the value is stored on the instance

    def __get__(self, obj, objtype=None):
        if obj is None:                  # accessed on the class, e.g. Box.width
            return self
        return obj.__dict__[self.private_name]

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f'{self.private_name[1:]} must be positive')
        obj.__dict__[self.private_name] = value

    def __delete__(self, obj):
        del obj.__dict__[self.private_name]

class Box:
    width = Positive()
    height = Positive()

    def __init__(self, width, height):
        self.width = width    # calls Positive.__set__
        self.height = height

b = Box(3, 4)
print(b.width * b.height)   # 12: call sites keep plain attribute syntax
print(b.__dict__)           # {'_width': 3, '_height': 4}: the storage is still reachable
try:
    b.width = -1
except ValueError as e:
    print(e)                # width must be positive
```

`__set_name__` is called when the class is created, and it gives the descriptor the name of the attribute it was assigned to. That is how `Positive` knows to store the value under `_width`.[^py314-reference-datamodel-object-set-name] A descriptor does not make data private: the value sits in `b.__dict__` under the name `_width` and can be read directly. Python has no true private instance variables, so encapsulation here means controlled access through the attribute name, not hiding the storage.[^py314-tutorial-classes-private-variables]

**Common mistakes:**
- putting a descriptor in `__init__` as an instance attribute (`self.width = Positive()`): its `__get__` and `__set__` are never called;
- not checking `obj is None` in `__get__`: access through the class (`Box.width`) then fails with `AttributeError`;
- assuming a descriptor makes data private: `b._width` and `b.__dict__` remain accessible.
