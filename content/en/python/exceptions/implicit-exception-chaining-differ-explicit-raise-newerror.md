---
id: py-excpt-0007
title: "How does implicit exception chaining differ from an explicit `raise NewError(...) from original`?"
description: "How does implicit exception chaining differ from an explicit `raise NewError(...) from original`?"
track: python
section: exceptions
level: middle
type: comparison
tags: [raise-newerror-from-original]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**Implicit chaining automatically sets `__context__` when a new exception is raised while another one is being handled (usually inside an `except` block); an explicit `from` sets `__cause__`.**[^py314-library-exceptions] Implicit chaining appears in the traceback as “During handling of the above exception, another exception occurred”, and explicit chaining as “The above exception was the direct cause of the following exception”.[^py314-tutorial-errors] Setting `__cause__` also sets `__suppress_context__ = True`, so the traceback shows `__cause__` and not `__context__`.[^py314-library-exceptions]

## Detailed explanation

Both mechanisms store the causal link on the exception object itself, not only in the text of the traceback. Implicit chaining needs no separate decision from the author: if a new exception is raised while another one is already being handled, Python stores the handled exception in the new one’s `__context__`.[^py314-library-exceptions] The link is therefore a side effect of where the `raise` sits, not a separate action.

Explicit chaining is the author’s decision: `raise NewError(...) from original` stores `original` in `__cause__` and immediately sets `__suppress_context__ = True`. The standard traceback then shows the chain through `__cause__` and does not show `__context__`. The `__context__` itself is not erased; it stays available for debugging.[^py314-library-exceptions]

Example: in both functions `NewError` is raised inside an `except` block, but only the second one uses `from`. The values below were checked on CPython 3.13 and 3.14, and they are the same on both.

```python
class NewError(Exception):
    pass

def implicit():
    try:
        {}["key"]
    except KeyError:
        raise NewError("lookup failed")  # __context__ is set automatically

def explicit():
    try:
        {}["key"]
    except KeyError as original:
        raise NewError("lookup failed") from original  # __cause__ is set

try:
    implicit()
except NewError as err:
    print(type(err.__context__).__name__)  # KeyError
    print(err.__cause__)                   # None
    print(err.__suppress_context__)        # False

try:
    explicit()
except NewError as err:
    print(type(err.__context__).__name__)  # KeyError, still set
    print(type(err.__cause__).__name__)    # KeyError
    print(err.__suppress_context__)        # True
```

The standard traceback handler marks the two cases with different phrases: for implicit chaining “During handling of the above exception, another exception occurred”, for explicit chaining “The above exception was the direct cause of the following exception”.[^py314-tutorial-errors]

In practice, `from` fits when a function translates a low-level error into an error of its own API and the cause should be kept. `from None` sets `__cause__ = None` and hides `__context__` from the display, but does not delete it.[^py314-library-exceptions]

**Common mistakes:**
- assuming implicit chaining has to be switched on: it happens by itself when a `raise` runs while another exception is being handled;
- assuming `from` erases `__context__`: the attribute stays, and only the traceback display changes;
- assuming `from` catches the exception: it only names the cause of the new exception, and `except` is what catches it.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
