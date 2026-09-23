---
id: py-objtypes-0002
title: "Why is `is None` used to check for `None` instead of relying on `== None`?"
description: "Why is `is None` used to check for `None` instead of relying on `== None`?"
track: python
section: objects-and-types
level: middle
type: mechanism
tags: [is-none]
status: published
updated: 2026-09-27
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
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**`None` is a singleton: only one instance of `None` exists in the process, so checking for identity via `is` is the correct approach.**[^py314-reference-datamodel] The `is` operator cannot be overloaded and guarantees comparison against that exact object. The `==` operator may be overridden in any class via `__eq__`, which can yield misleading results.

## Detailed explanation

In Python, `None` is the sole instance of the built-in `NoneType` class and serves as a singleton representing the absence of a value.[^py314-reference-datamodel]

Because exactly one `None` object exists throughout the entire lifetime of an interpreter process, the expression `val is None` directly compares the pointer of `val` with the address of this singleton. In CPython bytecode, this check translates into a dedicated instruction (`IS_OP`) that runs at the C-structure level without invoking any Python-level methods.

In contrast, the expression `val == None` invokes the method `val.__eq__(None)`. Any user-defined class or third-party library can implement `__eq__` in a way that returns `True` for an object that is not actually `None`, or raises an exception.[^py314-library-stdtypes] Furthermore, in some libraries (such as array-based structures), `== None` returns a container of booleans, which causes an exception when evaluated in a conditional statement like `if val == None:`.

Beyond safety and reliability, checking via `is` avoids unwanted computational overhead and guarantees the exact semantics mandated by PEP 8.

An example demonstrating the difference between `== None` and `is None`:

```python
class MisbehavingSentinel:
    def __eq__(self, other):
        # Flawed equality that claims match with everything
        return True

class FragileObject:
    def __eq__(self, other):
        # Some proxy objects or custom types reject direct equality
        raise TypeError("Direct equality comparison is unsupported")

sentinel = MisbehavingSentinel()
fragile = FragileObject()

# Equality invokes __eq__ and can produce false positives or errors:
print(sentinel == None)  # True: misleading result caused by custom __eq__
# fragile == None        # raises TypeError

# Identity check tests the memory address directly without calling __eq__:
print(sentinel is None)  # False: distinct object from the singleton
print(fragile is None)   # False: safe, fast, and never raises
```

**Practical consequences and common mistakes:**
- using `val == None` when checking default arguments: objects with non-standard `__eq__` implementations can be falsely treated as missing values;
- substituting `is None` with a truthiness check `if not val:`: empty containers or falsy values (`[]`, `""`, `0`, `False`) evaluate to false, causing subtle defects when `0` or an empty string are valid inputs;
- performance degradation: `val is None` is a fast pointer comparison, whereas `val == None` requires full dynamic lookup and invocation of the `__eq__` method.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
