---
id: py-funcs-0005
title: "Why can a wrapper with the signature `(*args, **kwargs)` accept a syntactically valid call that the wrapped function then rejects, and at what point does the `TypeError` occur?"
description: "Why can a wrapper with the signature `(*args, **kwargs)` accept a syntactically valid call that the wrapped function then rejects, and at what point does the `TypeError` occur?"
track: python
section: functions-and-scope
level: senior
type: mechanism
tags: [args-kwargs, typeerror]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-expressions-calls
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#calls
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-inspect-inspect-signature
    title: "Python 3.14: Library/inspect"
    url: https://docs.python.org/3.14/library/inspect.html#inspect.signature
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: functools.wraps adds a __wrapped__ attribute to the wrapper and copies metadata; it does not change which arguments the wrapper accepts."
  - source_id: py314-library-inspect-signature-bind
    title: "Python 3.14: Library/inspect"
    url: https://docs.python.org/3.14/library/inspect.html#inspect.Signature.bind
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: Signature.bind matches positional and keyword arguments to parameters and raises TypeError if they do not match the signature."
---

## Short answer

**The `(*args, **kwargs)` wrapper accepts any combination of arguments, so the signature is checked only when the wrapped function is called.**[^py314-reference-expressions-calls] For example, if the inner function is `def inner(a, b)` and the wrapper is called as `wrapper(1, 2, 3)`, the wrapper binds `args = (1, 2, 3)` without error, but unpacking `inner(*args)` raises `TypeError: inner() takes 2 positional arguments but 3 were given`. The error occurs inside the wrapper, at the call to inner, not on entry to the wrapper.

## Detailed explanation

When `wrapper(1, 2, 3)` is called, Python first matches the arguments against the wrapper's own parameters. The signature `(*args, **kwargs)` accepts any positional and keyword arguments: extra positional arguments go into the tuple `args`, and keyword arguments go into the dict `kwargs`. The rule "more positional arguments than parameters" applies to the function that is actually called. A wrapper with `*args` has no such limit, so it accepts the call.[^py314-reference-expressions-calls]

The error appears when the wrapper forwards the arguments. The call `inner(*args, **kwargs)` performs the same matching for `inner`: three positional values do not fit the parameters `a` and `b`, so a `TypeError` is raised. The error therefore occurs at the line in the wrapper that forwards the call, not on entry to the wrapper. The following example shows this:

```python
def inner(a, b):
    return a + b

def wrapper(*args, **kwargs):
    print('wrapper got', args, kwargs)
    return inner(*args, **kwargs)

wrapper(1, 2)            # prints: wrapper got (1, 2) {}
try:
    wrapper(1, 2, 3)     # prints: wrapper got (1, 2, 3) {}
except TypeError as error:
    print(error)         # inner() takes 2 positional arguments but 3 were given
```

The `print` line runs before the error, because the wrapper has already accepted the call and started work. This matters when a wrapper does something before the call: it counts calls, writes a log, limits the rate, or caches results. Such side effects happen before the error, so an invalid call can change program state and only then fail with an exception.

If the check must happen on entry, the arguments can be matched in advance: `inspect.signature(func).bind(*args, **kwargs)` creates a mapping from the arguments to the parameters and raises `TypeError` if they do not match the signature.[^py314-library-inspect-signature-bind] `functools.wraps` does something different: it copies metadata and adds a `__wrapped__` attribute,[^py314-library-functools-functools-wraps] so `inspect.signature(wrapper)` shows the signature of the wrapped function, for example `(a, b)`.[^py314-library-inspect-inspect-signature] This is only introspection: the call `wrapper(1, 2, 3)` is still accepted by the wrapper itself, and the error still occurs inside.

**Common mistakes:**
- expecting invalid arguments to be rejected on entry to the decorator, when the wrapper accepts them and forwards them;
- ignoring side effects of the wrapper that run before the `TypeError`;
- assuming that `functools.wraps` or `inspect.signature` makes the wrapper stricter.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
