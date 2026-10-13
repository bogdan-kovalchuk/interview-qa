---
id: py-funcs-0003
title: "How do you forward received `*args` and `**kwargs` to another function without losing positional and keyword arguments, and what mistake is easy to make while forwarding them?"
description: "How do you forward received `*args` and `**kwargs` to another function without losing positional and keyword arguments, and what mistake is easy to make while forwarding them?"
track: python
section: functions-and-scope
level: middle
type: mechanism
tags: [args, kwargs]
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
  - source_id: py314-faq-programming
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**Unpack them at the call site: `target(*args, **kwargs)`, not pass them as ordinary arguments.**[^py314-reference-expressions-calls] `*` expands `args` into additional positional arguments, and `**` expands `kwargs` into additional keyword arguments.[^py314-reference-expressions-calls] A common mistake is to write `target(args, kwargs)`: then `args` (a tuple) is passed as one positional argument and `kwargs` (a dict) as a second positional argument, not as keywords. Depending on the signature, the target either silently receives wrong values or raises `TypeError`.[^py314-reference-expressions-calls]

## Detailed explanation

Inside the function, `args` and `kwargs` are ordinary values: `args` is a tuple and `kwargs` is a dict. The documentation defines it this way: a `*identifier` parameter receives a tuple of the excess positional arguments, and a `**identifier` parameter receives a dict of the excess keyword arguments.[^py314-reference-expressions-calls] To forward them without loss, unpack them in the call: `*` expands the tuple into additional positional arguments, and `**` expands the dict into additional keyword arguments.[^py314-reference-expressions-calls]

The most common mistake is to pass `args` and `kwargs` as ordinary values. Positional arguments fill the slots in order, so `args` becomes the first argument `a` and the dict becomes the second argument `b`, and no keyword reaches `flag` or `options`.[^py314-reference-expressions-calls] Below, `forward` forwards the arguments correctly and `wrong` does not; both call the same `target`:

```python
def target(a, b, *rest, flag=False, **options):
    return a, b, rest, flag, options

def forward(*args, **kwargs):
    return target(*args, **kwargs)

def wrong(*args, **kwargs):
    return target(args, kwargs)

print(forward(1, 2, 3, flag=True, color='red'))
# (1, 2, (3,), True, {'color': 'red'})
print(wrong(1, 2, 3, flag=True, color='red'))
# ((1, 2, 3), {'flag': True, 'color': 'red'}, (), False, {})
```

In `wrong` the error is silent: the function runs and returns wrong values. If the target does not accept that many positional arguments, a `TypeError` is raised instead.

There are two more mistakes. A call with only `target(*args)` silently drops all keyword arguments. Adding a keyword that is already in `kwargs`, as in `target(*args, **kwargs, flag=True)` when `kwargs` has the key `flag`, raises `TypeError`, because the parameter has already received a value.[^py314-reference-expressions-calls]

**Common mistakes:**
- writing `target(args, kwargs)` or `target(*args, kwargs)`: then `kwargs` becomes a positional dict;
- passing only `*args` and forgetting `**kwargs`: keyword arguments disappear without an error;
- adding a keyword to the call that is already in `kwargs`: this is a `TypeError`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
