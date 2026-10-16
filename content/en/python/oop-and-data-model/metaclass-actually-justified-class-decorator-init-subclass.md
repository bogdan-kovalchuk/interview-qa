---
id: py-oop-0030
title: "When is a metaclass actually justified, and when does a class decorator or `__init_subclass__` give a simpler solution?"
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
  - source_id: py314-reference-datamodel-preparing-the-class-namespace
    title: "Python 3.14: Reference/datamodel (Preparing the class namespace)"
    url: https://docs.python.org/3.14/reference/datamodel.html#preparing-the-class-namespace
  - source_id: py314-reference-datamodel-creating-the-class-object
    title: "Python 3.14: Reference/datamodel (Creating the class object)"
    url: https://docs.python.org/3.14/reference/datamodel.html#creating-the-class-object
  - source_id: py314-reference-datamodel-customizing-class-creation
    title: "Python 3.14: Reference/datamodel (Customizing class creation)"
    url: https://docs.python.org/3.14/reference/datamodel.html#customizing-class-creation
  - source_id: py314-reference-datamodel-determining-the-appropriate-metaclass
    title: "Python 3.14: Reference/datamodel (Determining the appropriate metaclass)"
    url: https://docs.python.org/3.14/reference/datamodel.html#determining-the-appropriate-metaclass
  - source_id: py314-reference-datamodel-special-method-lookup
    title: "Python 3.14: Reference/datamodel (Special method lookup)"
    url: https://docs.python.org/3.14/reference/datamodel.html#special-method-lookup
  - source_id: py314-reference-datamodel-customizing-instance-and-subclass-checks
    title: "Python 3.14: Reference/datamodel (Customizing instance and subclass checks)"
    url: https://docs.python.org/3.14/reference/datamodel.html#customizing-instance-and-subclass-checks
---

## Short answer

**A metaclass is justified when you must intervene in class creation itself, for example to change the namespace through `__prepare__` or to reject a definition before the class object exists.**[^py314-reference-datamodel-preparing-the-class-namespace][^py314-reference-datamodel-creating-the-class-object] `__init_subclass__` is called for each new subclass and suits registration or checks of subclasses without a metaclass.[^py314-reference-datamodel-customizing-class-creation] A class decorator affects only the class it is applied to, so it is simpler for a one-off change to a single class.[^py314-reference-datamodel-customizing-class-creation]

## Detailed explanation

The metaclass intervenes earlier than the others: `__prepare__` creates the namespace in which the class body runs.[^py314-reference-datamodel-preparing-the-class-namespace] `__init_subclass__` is called inside `type.__new__` after the class object has been created, and a class decorator is applied even after that.[^py314-reference-datamodel-creating-the-class-object]

Registration through `__init_subclass__` covers all subclasses, while a decorator affects only the class it is explicitly applied to:

```python
REGISTRY = []


class Plugin:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        REGISTRY.append(cls.__name__)


class CsvPlugin(Plugin):
    pass


class JsonPlugin(Plugin):
    pass


print(REGISTRY)  # ['CsvPlugin', 'JsonPlugin']: every subclass is registered


DECORATED = []


def register(cls):
    DECORATED.append(cls.__name__)
    return cls


@register
class XmlPlugin:
    pass


class SubXmlPlugin(XmlPlugin):  # not decorated, so register() never runs for it
    pass


print(DECORATED)  # ['XmlPlugin']
```

`__init_subclass__` is not called for the class where it is declared, only for future subclasses.[^py314-reference-datamodel-customizing-class-creation] A metaclass, however, can reject a duplicate while the class body runs, which `__init_subclass__` cannot do, because it sees the attribute already overwritten:

```python
class NoDuplicates(dict):
    def __setitem__(self, key, value):
        if key in self and not key.startswith("__"):
            raise TypeError(f"duplicate definition of {key!r}")
        super().__setitem__(key, value)


class StrictMeta(type):
    @classmethod
    def __prepare__(mcls, name, bases, **kwargs):
        return NoDuplicates()


try:
    class Strict(metaclass=StrictMeta):
        def run(self):
            return 1

        def run(self):
            return 2
except TypeError as error:
    print(error)  # duplicate definition of 'run'
```

A metaclass is also needed when you must define the behaviour of the class itself. Implicit calls to `__call__`, `__iter__`, `__getitem__` or `__instancecheck__` are looked up on `type(cls)`, not on the class: assigning `C.__iter__` does not change `for x in C`. This is how `ABCMeta` (`__instancecheck__`) and `Enum` (`__iter__`, `__getitem__`) work.[^py314-reference-datamodel-special-method-lookup][^py314-reference-datamodel-customizing-instance-and-subclass-checks] A decorator and `__init_subclass__` cannot do this, because they do not change `type(cls)`.

In practice, consider a decorator or `__init_subclass__` first. A metaclass complicates composition: if the bases have incompatible metaclasses, the class definition fails with `TypeError`.[^py314-reference-datamodel-determining-the-appropriate-metaclass]

**Common mistakes:**
- reaching for a metaclass for registration that `__init_subclass__` handles;
- expecting `__init_subclass__` or a decorator to intercept the class body or replace the metaclass;
- assuming that a class decorator acts on subclasses, or that `__init_subclass__` is called for the class where it is defined.
