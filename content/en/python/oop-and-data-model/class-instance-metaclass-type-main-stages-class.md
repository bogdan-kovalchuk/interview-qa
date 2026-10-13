---
id: py-oop-0029
title: "Why is a class an instance of the metaclass `type`, and what main stages does a class statement go through before the class object is created?"
description: "A class is an instance of its metaclass, which is `type` by default; the class statement picks the metaclass, prepares the namespace, runs the body and calls the metaclass."
track: python
section: oop-and-data-model
level: middle
type: mechanism
tags: [type]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-descriptor
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-mro
    title: "Python 3.14: Howto/mro"
    url: https://docs.python.org/3.14/howto/mro.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-datamodel-metaclasses
    title: "Python 3.14: Reference/datamodel (Metaclasses)"
    url: https://docs.python.org/3.14/reference/datamodel.html#metaclasses
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: by default a class is constructed by type(name, bases, namespace); the sequence of steps for creating a class."
  - source_id: py314-reference-datamodel-creating-the-class-object
    title: "Python 3.14: Reference/datamodel (Creating the class object)"
    url: https://docs.python.org/3.14/reference/datamodel.html#creating-the-class-object
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the class object is created by calling metaclass(name, bases, namespace); after creation type.__new__ calls __set_name__ and __init_subclass__, then class decorators are applied."
  - source_id: py314-reference-datamodel-object-new
    title: "Python 3.14: Reference/datamodel (object.__new__)"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__new__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: __init__ is invoked after __new__ if it returns an instance of cls; otherwise __init__ is not invoked."
  - source_id: py314-reference-datamodel-resolving-mro-entries
    title: "Python 3.14: Reference/datamodel (Resolving MRO entries)"
    url: https://docs.python.org/3.14/reference/datamodel.html#resolving-mro-entries
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: __mro_entries__ substitutes the result of the method for a non-class base; related to generic types in the typing module."
---

## Short answer

**A class is an instance of its metaclass; if no metaclass is given, it is `type`, so `type(MyClass)` gives `type`.**[^py314-reference-datamodel-metaclasses] The stages are: resolving MRO entries for the bases, determining the metaclass, `__prepare__` for the namespace, executing the class body and, finally, calling `metaclass(name, bases, namespace)`.[^py314-reference-datamodel-metaclasses] That call creates the class object; `__init__` runs after `__new__` if `__new__` returned an instance of this metaclass.[^py314-reference-datamodel-creating-the-class-object][^py314-reference-datamodel-object-new]

## Detailed explanation

A class is an object too, so it has a type, and that type is its metaclass. When no metaclass is given and no base specifies another, Python uses `type`: the class body runs in a new namespace, and the name is bound to the result of `type(name, bases, namespace)`.[^py314-reference-datamodel-metaclasses] So `class C` is an instance of `type`, and `isinstance(C, type)` gives `True`. The base class `Base` defines the behaviour of instances of `C`, not of the class itself.

The order of the stages is visible in a trace. The metaclass prints a message in `__prepare__`, `__new__` and `__init__`, and the base class has `__init_subclass__`:

```python
class Meta(type):
    @classmethod
    def __prepare__(mcls, name, bases, **kwargs):
        print("prepare")  # printed 1st
        return {}

    def __new__(mcls, name, bases, namespace, **kwargs):
        print("new")  # printed 3rd
        return super().__new__(mcls, name, bases, namespace)

    def __init__(cls, name, bases, namespace, **kwargs):
        print("init")  # printed 5th
        super().__init__(name, bases, namespace)


class Base:
    def __init_subclass__(cls, **kwargs):
        print("init_subclass")  # printed 4th, inside type.__new__
        super().__init_subclass__(**kwargs)


class Demo(Base, metaclass=Meta):
    print("body")  # printed 2nd, after __prepare__ and before __new__
```

Before the body is run, Python resolves bases that are not classes: if a base has `__mro_entries__`, it is replaced by the result of that method. This is how non-class bases work, for example `list[int]`, which is replaced by `list`.[^py314-reference-datamodel-resolving-mro-entries] After the class object is created, `type.__new__` calls `__set_name__` for descriptors in the namespace, and then `__init_subclass__` of the nearest parent in the MRO. Class decorators are applied last, to the finished class object.[^py314-reference-datamodel-creating-the-class-object] So a decorator never sees the class body as a namespace; it receives only the result of class creation.

**Common mistakes:**
- confusing bases with the metaclass: `Base` defines the behaviour of instances of `Demo`, while `Meta` defines the behaviour of the class `Demo` itself;
- assuming that a class decorator sees the class body namespace rather than the created class object;
- expecting the metaclass `__init__` to run before `__init_subclass__`: in the trace it runs after.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
