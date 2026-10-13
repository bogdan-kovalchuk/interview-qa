---
id: py-excpt-0009
title: "How does `raise ... from None` affect how the exception context is displayed, and when is that justified?"
description: "How does `raise ... from None` affect how the exception context is displayed, and when is that justified?"
track: python
section: exceptions
level: senior
type: practical
tags: [raise-from-none]
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

**`raise NewError(...) from None` sets `__cause__ = None` and `__suppress_context__ = True`, so the traceback does not show the implicit `__context__`.**[^py314-library-exceptions] The original exception stays in `__context__` for debugging, but the standard traceback does not print it. This is appropriate when the inner exception is an implementation detail, for example when a `KeyError` is converted to an `AttributeError` in a library API and the caller gets nothing useful from it.

## Detailed explanation

When a `raise` runs inside the handling of another exception, Python by default stores the handled exception in the new one’s `__context__`, and the standard traceback shows both. An explicit `from` replaces this behaviour with a stated cause: `raise NewError(...) from exc` shows `exc` as the cause. `from None` is the extreme choice: it sets `__cause__ = None` and `__suppress_context__ = True`, so the display of `__context__` is switched off.[^py314-library-exceptions] The documentation describes this as replacing the old exception with the new one for display purposes, while the old one stays in `__context__` for debugging.[^py314-library-exceptions]

Example: `get_field` converts a `KeyError` into its own `NotFound`. If the exception is not caught, the traceback shows only `NotFound`; the attributes are visible when the exception is caught:

```python
class NotFound(Exception):
    pass

def get_field(record, name):
    try:
        return record[name]
    except KeyError:
        raise NotFound(f"no field {name!r}") from None  # hides the KeyError in the traceback

try:
    get_field({}, "name")
except NotFound as err:
    print(repr(err.__cause__))       # None
    print(err.__suppress_context__)  # True
    print(repr(err.__context__))     # KeyError('name'), still available
```

The cost is that the traceback loses the original cause: the key that was not found, and the line where that happened. If the `KeyError` is a bug in your own code rather than an expected detail, `from None` makes diagnosis harder, because `__context__` has to be fetched by hand. It is appropriate in a narrow case: the inner exception is an implementation detail, its type would not help the caller fix the call, and the new exception fully describes the failure. If the original cause must be shown, `from exc` is the better choice: the traceback then contains both exceptions.[^py314-library-exceptions]

**Common mistakes:**
- using `from None` by default to make the traceback look cleaner, and losing the cause of a bug;
- assuming `from None` deletes `__context__`: the attribute stays, and only the display changes;
- choosing `from None` when the caller needs the cause for diagnosis: `from exc` shows both exceptions.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
