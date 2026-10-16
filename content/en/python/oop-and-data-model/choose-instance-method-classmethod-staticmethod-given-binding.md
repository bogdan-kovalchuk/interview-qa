---
id: py-oop-0014
title: "When should you choose an instance method, `@classmethod`, or `@staticmethod`, given the binding and polymorphism you need?"
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
  - source_id: py314-howto-descriptor-class-methods
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#class-methods
  - source_id: py314-howto-descriptor-static-methods
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#static-methods
---

## Short answer

**Instance method when you need access to the state of a specific object; `@classmethod` when you need access to the class with polymorphism; `@staticmethod` when the method depends on neither the instance nor the class.**[^py314-howto-descriptor-class-methods] A `@classmethod` receives the class the method was called through, so factory methods return an instance of the subclass when inherited. A `@staticmethod` receives neither `self` nor `cls`.[^py314-howto-descriptor-static-methods] So it does not know which class it was called through; it can be overridden in a subclass, like any class attribute.

## Detailed explanation

The three variants differ in their first implicit argument. An instance method receives `self`: accessed through an instance, it is a bound method. A `@classmethod` receives the class whether it is called through the class or through an instance (for an instance, this is `type(obj)`).[^py314-howto-descriptor-class-methods] A `@staticmethod` receives nothing: its `__get__` returns the underlying function unchanged.[^py314-howto-descriptor-static-methods]

The choice depends on what the method actually needs:

- instance method: when the method reads or changes the state of a specific object, for example `self.n`;
- `@classmethod`: when it needs the class itself: an alternative constructor, access to class-level settings, or creating an instance of the class the call went through;
- `@staticmethod`: when the method needs neither state nor the class. A module-level function is often better: a staticmethod only groups it in the class namespace.

The example: `create` uses `cls` and returns an instance of the subclass, while `create_static` always returns `Shape`. The comments show the output (CPython 3.14):

```python
class Shape:
    @classmethod
    def create(cls):
        return cls()                  # an instance of the class the call went through

    @staticmethod
    def create_static():
        return Shape()                # always Shape: there is no cls to choose from

class Square(Shape):
    pass

print(type(Square.create()).__name__)          # Square
print(type(Square().create()).__name__)        # Square: works through an instance too
print(type(Square.create_static()).__name__)   # Shape
```

Polymorphism has limits here. A `@classmethod` selects behaviour by the class the method was called through, and it does so via `cls`. A `@staticmethod` also takes part in overriding: if a base method calls `self.kind()`, a subclass with its own `kind` gets the call, because the lookup goes by name. But the staticmethod itself does not know which class it was called through, so it cannot build the correct type.[^py314-howto-descriptor-static-methods]

The limits of `@classmethod`: it has no access to instance state, because `cls` is a class, not `self`. The class is determined by the call, not by where the method is declared: `Square.create()` returns a `Square`, although the method is defined in `Shape`.[^py314-howto-descriptor-class-methods]

**Common mistakes:**
- writing a factory with `@staticmethod` and a hard-coded class name: subclasses get the base type;
- using `@classmethod` when no class is needed, only because the method does not use `self`;
- believing that a `@staticmethod` cannot be overridden in a subclass.
