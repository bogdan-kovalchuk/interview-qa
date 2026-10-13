---
id: py-excpt-0008
title: "When is a bare `raise` used inside a handler, and why can `raise exc` change how the traceback is presented?"
description: "When is a bare `raise` used inside a handler, and why can `raise exc` change how the traceback is presented?"
track: python
section: exceptions
level: middle
type: mechanism
tags: [raise-exc]
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
  - source_id: py314-reference-simple-stmts-the-raise-statement
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#the-raise-statement
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the raise statement, bare raise re-raising the active exception, and the 3.11 change for a modified traceback."
---

## Short answer

**A bare `raise` inside an `except` block re-raises the active exception.**[^py314-reference-simple-stmts-the-raise-statement] In CPython a bare `raise` adds no entry for its own line, so the traceback keeps the place where the exception was first raised. `raise exc`, even with the same object, adds an entry for the `raise exc` line in front of the original traceback, so the same function appears twice in the report.

## Detailed explanation

A bare `raise` without arguments re-raises the exception that is currently being handled (the active exception). This is the usual pattern of “log it or clean up, then pass it on”: the handler does not create a new object, it raises the same one.[^py314-reference-simple-stmts-the-raise-statement] Outside handling there is no active exception, and then a bare `raise` itself raises `RuntimeError`.

A traceback is a chain of entries, one for each frame the exception has passed through. In CPython a bare `raise` does not create an entry for its own line: the exception continues along its path with the existing chain, so the report shows where the exception was first raised. The documentation also records the 3.11 change: if the traceback of the active exception is modified in an `except` clause, a later `raise` re-raises the exception with the modified traceback; previously it used the traceback that existed when the exception was caught.[^py314-reference-simple-stmts-the-raise-statement]

`raise exc` is treated as an ordinary raise of an object that already has a `__traceback__`. In CPython an entry for the current line is added, and the older entries stay behind it. So the report contains both the `raise exc` line and the line of the original call to the same function, and it looks as if the error passed through the handler twice, although it happened once. The type and value of the exception do not change; only what the reader of the report sees changes.

Example: both functions call `inner()`, which raises a `ValueError`. The result is printed with `traceback.extract_tb`; it is the same on CPython 3.13 and 3.14.

```python
import traceback

def inner():
    raise ValueError("original")

def bare():
    try:
        inner()
    except ValueError:
        raise  # re-raises the active exception, adds no entry for this line

def same_object():
    try:
        inner()
    except ValueError as exc:
        raise exc  # adds an entry for this line in front of the original frames

for fn in (bare, same_object):
    try:
        fn()
    except ValueError as err:
        print(fn.__name__, [(f.name, f.lineno) for f in traceback.extract_tb(err.__traceback__)])
# bare [('<module>', 20), ('bare', 8), ('inner', 4)]
# same_object [('<module>', 20), ('same_object', 16), ('same_object', 14), ('inner', 4)]
```

**Common mistakes:**
- writing `raise err` instead of `raise` in a handler that only logs: this adds an extra traceback entry;
- seeing one function twice in the report and looking for a second error: there is only one error, and the second entry was added by `raise exc`;
- calling a bare `raise` outside `except`: you get `RuntimeError: No active exception to reraise`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
