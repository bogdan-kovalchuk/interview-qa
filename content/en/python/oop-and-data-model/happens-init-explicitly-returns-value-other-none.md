---
id: py-oop-0003
title: "What happens if `__init__` explicitly returns a value other than `None`, and why?"
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
  - source_id: py314-reference-datamodel-object-init
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__init__
---

## Short answer

**Python raises `TypeError: __init__() should return None, not '...'`.**[^py314-reference-datamodel-object-init] When a class is called, the interpreter checks what `__init__` returned: any value other than `None` (including `0` or `False`) is an error, because `__new__` and `__init__` work together to create an object, and `__init__` only configures an instance that already exists.[^py314-reference-datamodel-object-init]

## Detailed explanation

Calling a class, for example `Point(1, 2)`, creates the object through `__new__`, passes it to `__init__` for configuration, and returns that object. The value that `__init__` returns does not become the result of the class call. Instead, Python requires `None` and raises `TypeError` if it gets anything else.[^py314-reference-datamodel-object-init]

The example below shows both behaviours: returning `0` causes the error, while `return None` does not.

```python
class Bad:
    def __init__(self):
        return 0            # any value other than None

try:
    Bad()
except TypeError as e:
    print(e)                # __init__() should return None, not 'int'

class Good:
    def __init__(self):
        return None         # same as a bare return or no return at all

print(type(Good()).__name__)  # Good
```

The check applies to the class call itself. If you call `__init__` directly on an object that already exists, it is an ordinary function, and `obj.__init__()` returns `0` without an exception. So the rule about `None` applies when the interpreter creates an instance through a class call.[^py314-reference-datamodel-object-init]

If `__init__` needs to signal an error, the correct way is to raise an exception, for example `raise ValueError(...)`. The exception stops the object from being created and carries the message out, whereas a returned value in a class call only leads to `TypeError`.

**Common mistakes:**
- ending `__init__` with `return self`, which raises `TypeError` during the class call;
- returning `False` or an error code from `__init__` instead of using `raise`;
- expecting `Cls()` to return the value that `__init__` returned.
