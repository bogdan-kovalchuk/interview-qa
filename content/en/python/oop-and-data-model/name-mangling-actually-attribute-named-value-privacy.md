---
id: py-oop-0006
title: "What does name mangling actually do for an attribute named `__value`, and why is it not a privacy security mechanism?"
description: "What does name mangling actually do for an attribute named `__value`, and why is it not a privacy security mechanism?"
track: python
section: oop-and-data-model
level: middle
type: mechanism
tags: [value]
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
  - source_id: py314-reference-expressions-private-name-mangling
    title: "Python 3.14: Reference/expressions, Private name mangling"
    url: https://docs.python.org/3.14/reference/expressions.html#private-name-mangling
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the rule by which a private identifier (two or more leading `_`, no trailing `__`) is rewritten to a form with the class name before code is generated. Does not describe mangling as a security mechanism."
  - source_id: py314-tutorial-classes-private-variables
    title: "Python 3.14: Tutorial/classes, Private Variables"
    url: https://docs.python.org/3.14/tutorial/classes.html#private-variables
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the purpose of mangling (avoiding name clashes with names defined in subclasses); the rules are designed mostly to avoid accidents, and access and modification remain possible; a single leading underscore as a convention. Does not describe descriptors."
---

## Short answer

**Name mangling automatically renames `__value` to `_ClassName__value` to avoid name clashes with names defined in subclasses.**[^py314-tutorial-classes-private-variables] The transformation happens before code is generated: an identifier `__name` (two or more leading `_`, no trailing `__`) inside the definition of class `Foo` becomes `_Foo__name`.[^py314-reference-expressions-private-name-mangling] It does not block access: the mangled name can still be used directly, so the mechanism protects against accidental clashes, not deliberate access.[^py314-tutorial-classes-private-variables]

## Detailed explanation

Name mangling is a renaming that happens at compile time, not a mechanism that runs during execution. An identifier that begins with two or more `_` and does not end in two `_` is a private name of its class. Before code is generated, Python replaces it with a longer form: the class name with leading underscores removed, one `_` in front, and then the name itself.[^py314-reference-expressions-private-name-mangling] So `__value` in class `Base` becomes `_Base__value`, and in class `_Base` it also becomes `_Base__value`.

The purpose of the rule is to avoid name clashes with names defined in subclasses. If both `Base` and `Child` assign `self.__value`, the instance `__dict__` gets two different keys, and the subclass does not overwrite the base class's value.[^py314-tutorial-classes-private-variables] Check it:

```python
class Base:
    def __init__(self):
        self.__value = 'base'      # stored as _Base__value

class Child(Base):
    def __init__(self):
        super().__init__()
        self.__value = 'child'     # stored as _Child__value, no clash

c = Child()
print(vars(c))  # {'_Base__value': 'base', '_Child__value': 'child'}
```

So `__value` is not a way to hide data: it only changes the name under which the attribute is stored in `__dict__`. A mangled attribute is an ordinary attribute, and it can be read from anywhere in the program:

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance   # stored as _Account__balance

acc = Account(100)
print(acc._Account__balance)      # 100: the mangled name is an ordinary attribute
print(hasattr(acc, '__balance'))  # False: the string '__balance' is not mangled
print(vars(acc))                  # {'_Account__balance': 100}
```

A string passed to `hasattr`, `getattr` or `setattr` is not changed, because the rule applies to identifiers in the class text.[^py314-reference-expressions-private-name-mangling] The Python tutorial says the mangling rules are designed mostly to avoid accidents, not to protect data: access and modification remain possible even for an attribute that is meant to be private.[^py314-tutorial-classes-private-variables] For an attribute that is not meant for use outside the class, most Python code uses a single `_` prefix as a convention.[^py314-tutorial-classes-private-variables]

**Common mistakes:**
- assuming `__value` cannot be accessed from outside the class: it can be read as `obj._ClassName__value`;
- expecting a subclass to override the base class's `self.__value`: with mangling these are two different attributes;
- looking up the mangled attribute with `getattr(obj, '__value')`: the string is not changed.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
