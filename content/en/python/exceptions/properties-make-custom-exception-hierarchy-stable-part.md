---
id: py-excpt-0010
title: "What properties make a custom exception hierarchy a stable part of a library API?"
description: "What properties make a custom exception hierarchy a stable part of a library API?"
track: python
section: exceptions
level: middle
type: practical
tags: []
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

**A stable hierarchy usually starts with one library base class derived from `Exception` (a convention, not a language requirement).**[^py314-tutorial-errors] Intermediate classes for categories, such as `LookupError` for `KeyError` and `IndexError`, let callers catch a whole category.[^py314-library-exceptions] Concrete subclasses are usually named with an `Error` suffix, as most standard exceptions are.[^py314-tutorial-errors]

## Detailed explanation

The language does not define the rules for the stability of a library API, so what follows are conventions that come from how `except` works. An `except X` clause matches when the exception is an instance of `X` or of a subclass of `X`.[^py314-reference-compound-stmts-the-try-statement] So the name of a class and its place in the hierarchy are part of the contract: callers write `except` against a specific class, and changing its ancestors changes what they catch.

A root derived from `Exception` is meant for exactly these callers. The `Exception` documentation says that all user-defined exceptions should be derived from it.[^py314-library-exceptions] Then a single `except LibraryError` catches everything the library raises, without listing the classes one by one.

Intermediate classes give different levels of detail. The standard library shows this with `LookupError`: it is the base of `IndexError` and `KeyError`, so `except LookupError` catches both.[^py314-library-exceptions] A new subclass under an existing category does not break code that catches the category. Moving an existing class to another branch, by contrast, silently changes which `except` blocks catch it. That is why the stable part of an API is not only the names but also the place of each class in the hierarchy.

Error data is better passed in attributes than only in the message text. The caller then reads `err.key` instead of parsing a string that may change in the next version. The example below shows `except QueryError` catching a concrete `NotFoundError`, with the key taken from an attribute:

```python
class LibraryError(Exception):
    """Base class: callers can catch everything the library raises."""

class QueryError(LibraryError):
    """Category: the request itself is wrong."""

class NotFoundError(QueryError):
    """Specific condition with its own name."""
    def __init__(self, key):
        super().__init__(f"no record for key {key!r}")
        self.key = key  # data lives in an attribute, not in parsed message text

try:
    raise NotFoundError("user-42")
except QueryError as err:
    print(type(err).__name__, err.key)  # NotFoundError user-42
```

**Common mistakes:**
- having no library base class: callers must list every class to catch the library's errors;
- moving an existing class to another branch of the hierarchy: callers' `except` blocks change behaviour although the library code is still correct;
- parsing `str(err)` to find the cause: the message text is usually not regarded as part of the API.

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
