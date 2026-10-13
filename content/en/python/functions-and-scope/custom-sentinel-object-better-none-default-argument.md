---
id: py-funcs-0008
title: "When is a custom sentinel object better than `None` as a default argument in a public API?"
description: "When is a custom sentinel object better than `None` as a default argument in a public API?"
track: python
section: functions-and-scope
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
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-expressions-calls
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#calls
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: parameters left unfilled by a call are filled with the default value from the function definition; the source describes argument matching at call time, not the choice between None and a sentinel."
  - source_id: py314-reference-expressions-is-not
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#is-not
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: is and is not test identity; x is y is true if and only if x and y are the same object."
---

## Short answer

**A sentinel is worth using when `None` is a valid parameter value that must be told apart from "argument not passed".** An omitted argument receives the default in the same parameter, so the function sees only the value.[^py314-reference-expressions-calls] With `def get(key, default=_MISSING)`, `get(key, None)` returns `None` when the key is missing, while `get(key)` raises `KeyError`. The sentinel is a private `object()` compared with `is`, so an ordinary argument does not match it.[^py314-reference-expressions-is-not] If `None` has no separate meaning, a plain `default=None` is simpler.

## Detailed explanation

A default value is an ordinary value that Python substitutes into the parameter when the argument is not passed.[^py314-reference-expressions-calls] Inside the function there is only the object in the parameter, with no record of whether the caller passed it. So if `None` has a meaning of its own (for example, `ttl=None` means "never expires"), then `default=None` cannot distinguish "the caller passed nothing" from "the caller explicitly passed `None`".

A sentinel separates these cases. It is a unique object that an ordinary call does not have; the default value is evaluated once, during `def`, so every call sees the same object.[^py314-reference-compound-stmts-function-definitions] The function checks it by identity:

```python
_MISSING = object()   # private sentinel: callers do not have it by accident

def get(key, default=_MISSING):
    values = {'host': 'localhost'}
    if key in values:
        return values[key]
    if default is _MISSING:
        raise KeyError(key)
    return default

print(get('host'))          # localhost
print(get('port', None))    # None: explicit None is a valid answer
print(get('port', 8080))    # 8080
try:
    get('port')
except KeyError as error:
    print('KeyError', error)  # KeyError 'port'
```

In the example, `get('port', None)` returns `None` because the explicit `None` is the answer, while `get('port')` raises `KeyError` because the sentinel shows that no `default` was given. The test uses `is` because `x is y` is true if and only if both names refer to the same object.[^py314-reference-expressions-is-not] A test with `==` is unreliable: an object with its own `__eq__` can compare equal to the sentinel, and the function then takes the wrong branch.

A public API has a cost. `inspect.signature` shows a plain `object()` sentinel as `<object object at 0x…>`, which says little in documentation. A small class with a readable `__repr__` solves this. The sentinel also adds a name that users must learn. So it pays off when `None` has a meaning of its own, not merely as a style choice.

**Common mistakes:**
- using a sentinel where `None` has no separate value, which adds complexity to the API for no benefit;
- testing the sentinel with `==` instead of `is`;
- leaving a plain `object()` sentinel with no readable `repr` in a public signature, so the documentation shows a memory address.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
