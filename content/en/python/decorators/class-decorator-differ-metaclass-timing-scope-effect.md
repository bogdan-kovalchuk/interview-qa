---
id: py-decor-0008
title: "How does a class decorator differ from a metaclass in the timing and scope of its effect on the class object?"
description: "How does a class decorator differ from a metaclass in the timing and scope of its effect on the class object?"
track: python
section: decorators
level: senior
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
  - source_id: py314-glossary-term-decorator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-decorator
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-compound-stmts-class-definitions
    title: "Python 3.14: Reference/compound Stmts, Class definitions"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#class-definitions
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Order of a class definition: the class body runs, then the class object is created, then decorators are applied to it; `@f1(arg) @f2 class Foo` is roughly equivalent to `Foo = f1(arg)(f2(Foo))`."
  - source_id: py314-reference-datamodel-creating-the-class-object
    title: "Python 3.14: Reference/datamodel, Creating the class object"
    url: https://docs.python.org/3.14/reference/datamodel.html#creating-the-class-object
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "The class object is created by calling metaclass(name, bases, namespace, **kwds) after the class body has run. It does not describe what a metaclass does with the namespace."
  - source_id: py314-reference-datamodel-customizing-class-creation
    title: "Python 3.14: Reference/datamodel, Customizing class creation"
    url: https://docs.python.org/3.14/reference/datamodel.html#customizing-class-creation
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "A class decorator affects only the class it is applied to; __init_subclass__ applies to future subclasses. It does not describe metaclass behaviour."
  - source_id: py314-reference-datamodel-metaclasses
    title: "Python 3.14: Reference/datamodel, Metaclasses"
    url: https://docs.python.org/3.14/reference/datamodel.html#metaclasses
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "A class inherits the metaclass of a base class that specifies one. It does not describe class decorators."
---

## Short answer

**A class decorator receives the class object that has already been built and can modify or replace it.**[^py314-reference-compound-stmts-class-definitions] A metaclass controls the creation of the class itself: it is called as `metaclass(name, bases, namespace)` before the class object exists.[^py314-reference-datamodel-creating-the-class-object] A decorator affects only the class it is applied to.[^py314-reference-datamodel-customizing-class-creation] A metaclass is inherited by subclasses, so it affects the whole hierarchy.[^py314-reference-datamodel-metaclasses] So a decorator is simpler and more local, while a metaclass is more powerful but has a wider reach.

## Detailed explanation

A class decorator is a callable that is applied after the `class` statement has run the class body and created the class object. The reference describes this as roughly equivalent to `Foo = f1(arg)(f2(Foo))`, so the decorator sees a finished class with its attributes and methods and may return a different object.[^py314-reference-compound-stmts-class-definitions] The syntax is the same as for function decorators, which the glossary describes as a function that returns another function and is usually applied with `@`.[^py314-glossary-term-decorator] This mechanism is convenient for registering, checking or adding attributes, but the decorator receives the result of class creation, not its inputs: `name`, `bases` and `namespace` are no longer passed to it as arguments.

A metaclass is a class whose instances are classes. When a class is created, Python calls the metaclass as `metaclass(name, bases, namespace)`, so its `__new__` receives the raw `name`, `bases` and `namespace` before the class exists.[^py314-reference-datamodel-creating-the-class-object] At that stage the metaclass can, for example, change the namespace, validate fields or register the class before it becomes available. The example below shows the timing and scope of both mechanisms: the metaclass records `meta:Base` before the decorator records `Base`.

```python
registry = []

def register(cls):                 # class decorator: runs after the class body
    registry.append(cls.__name__)
    return cls

class RegisterMeta(type):          # metaclass: runs while the class is being created
    def __new__(mcls, name, bases, namespace, **kwargs):
        registry.append("meta:" + name)
        return super().__new__(mcls, name, bases, namespace, **kwargs)

@register
class Base(metaclass=RegisterMeta):
    x = 1

class Child(Base):                 # the decorator is not re-applied; the metaclass is inherited
    pass

print(registry)   # ['meta:Base', 'Base', 'meta:Child']
```

The scope differs as well. A class decorator acts only on the class it is attached to, whereas `__init_subclass__` applies to future subclasses.[^py314-reference-datamodel-customizing-class-creation] A metaclass is inherited: a subclass gets the same metaclass from the base class that specifies it.[^py314-reference-datamodel-metaclasses] In the example, `Child` does not pass through the decorator again, but it appears in `registry` because of the metaclass.

In practice, a decorator suits a single class, while a metaclass suits a rule that must apply to a whole hierarchy. If you only need to react to subclass creation, `__init_subclass__` defined on the base class is usually simpler, with no separate metaclass.[^py314-reference-datamodel-customizing-class-creation]

**Common mistakes:**
- assuming a class decorator applies to subclasses: they do not receive it, as the example shows;
- writing a metaclass where a decorator or `__init_subclass__` is enough;
- expecting the decorator to change how the class was created: it receives an already finished class object.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
