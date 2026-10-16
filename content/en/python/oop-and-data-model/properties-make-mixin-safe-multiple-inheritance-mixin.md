---
id: py-oop-0020
title: "What properties make a mixin safe for multiple inheritance, and why does a mixin usually not own the object's primary state?"
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
  - source_id: py314-builtins-functions-super
    title: "Python 3.14: Built-in Functions/super"
    url: https://docs.python.org/3.14/builtins/functions.html#super
---

## Short answer

**A mixin adds behavior rather than owning the object's primary state: it usually has no required arguments in `__init__` and works with attributes that other classes provide.** It passes control on through `super()` with the same signature as the rest of the cooperative methods.[^py314-builtins-functions-super] <span class="warn">Two mixins that write to the same attribute can silently overwrite each other's data.</span> So a mixin should document the attributes and methods it expects from the other classes.

## Detailed explanation

A mixin is a class that adds reusable behavior to other classes through multiple inheritance. It is usually not created on its own: it sits in the MRO next to the class that creates the object and holds the main state. Hence the rule: a mixin adds methods, and leaves the data to the class that creates the instance. This is a design convention, not a restriction that Python enforces.

The reason is visible in the data model: an instance has a namespace stored as a dictionary, and every class in its MRO can write to that same dictionary.[^py314-reference-datamodel] Two mixins that use the same attribute name conflict, even if each is correct on its own. Example:

```python
class LoggingMixin:
    def __init__(self, *args, **kwargs):
        self.items = []                       # the mixin writes its own state
        super().__init__(*args, **kwargs)

class CacheMixin:
    def __init__(self, *args, **kwargs):
        self.items = {}                       # same attribute name: silent clash
        super().__init__(*args, **kwargs)

class Service(LoggingMixin, CacheMixin):
    pass

s = Service()
print(type(s.items).__name__)                 # dict: CacheMixin replaced the list
```

`Service()` first runs `LoggingMixin.__init__`, which creates a list, and then `CacheMixin.__init__`, which replaces it with a dictionary. No error is raised, so a clash like this is easy to miss.

The second condition is the signature. If a mixin's `__init__` requires a positional argument, everyone who creates a class with that mixin must pass it, so the mixin changes the constructor of the whole class. That is why a mixin accepts `*args, **kwargs` and passes them on, as the rest of the cooperative methods do.[^py314-builtins-functions-super]

The third condition is position. A mixin should not need to know which class comes before or after it. So it calls `super()` rather than `Base.method(self)`: `super()` searches for the next class in the MRO of the actual type, so the mixin does not depend on its neighbours as long as the attributes it needs are present in the combination.[^py314-builtins-functions-super] But the order of bases decides which override wins, so a mixin that must override a method is placed before the class that defines it, and that class may not call `super()`.[^py314-howto-mro]

**Common mistakes:**
- assuming that two mixins with the same attribute name are isolated because they are declared in different classes;
- adding a required `__init__` argument to a mixin that the other classes in the combination do not pass on;
- using an attribute that the mixin neither creates nor documents, and breaking a combination where that attribute is missing.
