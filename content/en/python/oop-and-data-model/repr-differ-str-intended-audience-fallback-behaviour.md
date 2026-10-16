---
id: py-oop-0021
title: "How does `__repr__` differ from `__str__` in intended audience and fallback behaviour?"
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
  - source_id: py314-reference-datamodel-object-repr
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__repr__
  - source_id: py314-reference-datamodel-object-str
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__str__
---

## Short answer

**`__repr__` returns an "official" string for debugging, which should be unambiguous and, where possible, look like a valid Python expression.**[^py314-reference-datamodel-object-repr] `__str__` returns the "informal" string used by `str()` and `print()`, and it is not required to be a Python expression.[^py314-reference-datamodel-object-str] If a class defines only `__repr__`, `str()` uses it as a fallback.[^py314-reference-datamodel-object-repr] The default `object.__str__` itself calls `object.__repr__`.[^py314-reference-datamodel-object-str]

## Detailed explanation

`repr()` and `str()` are two separate ways to present an object, and their purposes differ. `repr(obj)` calls `__repr__` and returns the "official" string, meant mainly for debugging, so it should be informative and unambiguous. Where possible, the string should look like a Python expression that recreates an object with the same value; if that is not possible, the documentation suggests a form such as `<...some useful description...>`. The class `object` itself provides the default implementation.[^py314-reference-datamodel-object-repr]

`str(obj)` calls `__str__` and returns the "informal" string, meant to be readable by people. The documentation does not require it to be a Python expression, so a shorter or more convenient form is acceptable.[^py314-reference-datamodel-object-str] The method is used by `str()`, `print()` and the default `__format__`, so an f-string `{obj}` also shows `__str__` unless the class overrides `__format__`.[^py314-reference-datamodel-object-str]

The fallback works in one direction only. If a class defines only `__repr__`, then `str()` and `print()` show its result, because the default `object.__str__` calls `object.__repr__`.[^py314-reference-datamodel-object-str] There is no reverse rule: a class that has only `__str__` gets the default string for `repr()`, which does not recreate the value; in CPython this is, for example, `<__main__.Plain object at 0x...>`.

The example has one class with both methods and three calls, each using a different mechanism.

```python
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f"Money({self.amount!r}, {self.currency!r})"

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

m = Money(12.5, "USD")
print(repr(m))  # Money(12.5, 'USD'): unambiguous, valid Python expression
print(str(m))   # 12.50 USD: readable text for people
print([m])      # [Money(12.5, 'USD')]: containers show the repr of their items
```

In CPython, containers such as lists, tuples and dicts show the `repr` of their elements, so `print([m])` prints the `repr`, while `print(m)` prints the `str`.

**Common mistakes:**
- assuming that `print()` uses `__repr__`; it calls `__str__`, and falls back to `__repr__` only when `__str__` is missing;
- writing only human-friendly text in `__repr__`, so logs lack an unambiguous description of the state;
- defining only `__str__` and expecting `repr()` to show the object's contents.
