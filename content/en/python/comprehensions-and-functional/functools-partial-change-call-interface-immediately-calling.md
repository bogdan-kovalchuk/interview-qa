---
id: py-compfn-0009
title: "How does `functools.partial` change the call interface without immediately calling the wrapped callable?"
description: "How does `functools.partial` change the call interface without immediately calling the wrapped callable?"
track: python
section: comprehensions-and-functional
level: middle
type: mechanism
tags: [functools-partial]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-howto-functional
    title: "Python 3.14: Howto/functional"
    url: https://docs.python.org/3.14/howto/functional.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-expressions-displays-for-lists-sets-and-dict
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**`functools.partial` returns a new callable object in which a subset of positional or keyword arguments is "frozen", but the original function is not invoked until the partial object is called.**[^py314-howto-functional] Additional arguments supplied at call time append to the frozen positional arguments; new keyword arguments take precedence over previously configured ones. For example, `functools.partial(pow, 2)` creates a function computing powers of two: `f(10)` -> `1024`.

## Detailed explanation

The `functools.partial` function returns a new instance of a dedicated `partial` type that wraps the underlying callable and freezes a portion of its positional and keyword arguments without executing it.[^py314-library-functools] The returned object stores three read-only attributes: `.func` (a reference to the original callable), `.args` (a tuple of frozen positional arguments), and `.keywords` (a dictionary or `None` containing frozen keyword arguments).

When the `partial` object is called as `partial(*more_args, **more_kwargs)`, argument merging takes place dynamically immediately prior to invoking the original function. Positional arguments are merged via tuple concatenation `self.args + more_args` (frozen arguments always come first), while keyword arguments are merged via dictionary union `{**self.keywords, **more_kwargs}`, where call-time keywords override earlier defaults. The original function is only executed when the `partial` object itself is called.

Because `partial` is a distinct built-in type rather than a standard Python function, it does not implement the standard descriptor protocol for instance method binding inside classes (use `functools.partialmethod` for class methods instead). Furthermore, `partial` does not automatically copy `__name__` and `__doc__` attributes, although the `inspect` module correctly reflects its updated call signature.

Creating a partially applied function and inspecting its internal attributes:

```python
from functools import partial


def greet(greeting: str, name: str, punctuation: str = "!") -> str:
    return f"{greeting}, {name}{punctuation}"


# Freeze the first positional argument 'greeting'
say_hello = partial(greet, "Hello")

# Attributes stored on the partial object
print(say_hello.func is greet)  # True
print(say_hello.args)  # ('Hello',)

# Calling the partial object with the remaining arguments
print(say_hello("Alice"))
# Output: Hello, Alice!

# Overriding a default keyword argument at call time
print(say_hello("Bob", punctuation="?"))
# Output: Hello, Bob?
```

**Nuances and common limitations of `functools.partial`:**
- positional arguments are always prepended: standard `partial` cannot freeze the second positional parameter while leaving the first unbound (use keyword arguments or a `lambda` instead);
- lack of descriptor support: for class methods, use `functools.partialmethod`, otherwise `partial` will not pass `self` automatically;
- `partial` objects do not automatically copy `__name__` and `__doc__` metadata; access them via the `.func` attribute instead.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
