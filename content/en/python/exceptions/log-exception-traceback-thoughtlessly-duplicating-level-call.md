---
id: py-excpt-0016
title: "How do you log an exception with its traceback without thoughtlessly duplicating it at every level of the call stack?"
description: "How do you log an exception with its traceback without thoughtlessly duplicating it at every level of the call stack?"
track: python
section: exceptions
level: senior
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
  - source_id: py314-library-logging-logger-exception
    title: "Python 3.14: Library/logging"
    url: https://docs.python.org/3.14/library/logging.html#logging.Logger.exception
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: exception() adds exception information and should be called from an exception handler."
  - source_id: py314-library-logging-logger-debug
    title: "Python 3.14: Library/logging"
    url: https://docs.python.org/3.14/library/logging.html#logging.Logger.debug
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the exc_info parameter; if it is true and no exception is passed explicitly, the current exception from sys.exc_info() is used."
  - source_id: py314-reference-simple-stmts-raise
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#raise
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: raise ... from attaches the original exception as __cause__; an unhandled exception is printed together with its cause."
---

## Short answer

**Log an exception with its traceback once, where it is finally handled and no longer re-raised.** This is a practice, not a rule of the `logging` module. Write the traceback with `logger.exception()` or `logger.error(..., exc_info=True)`.[^py314-library-logging-logger-exception][^py314-library-logging-logger-debug] Lower levels that only add context can raise a new exception with `raise ... from exc`, which stores the original as `__cause__`.[^py314-reference-simple-stmts-raise] Logging at every level produces duplicates.

## Detailed explanation

Duplicates appear because `logger.exception()` adds information about the exception currently being handled, and each such call writes a separate record with a traceback. For `logger.error(..., exc_info=True)` the rule is the same: if `exc_info` is true and no exception is passed explicitly, the current exception from `sys.exc_info()` is used.[^py314-library-logging-logger-exception][^py314-library-logging-logger-debug] So if every level of the stack logs in its own `except` block, one failure appears in the logs as many times as there are levels that logged it.

The right place to log is where the exception stops propagating: the level that answered the user, returned a fallback result or ended the process. Lower levels that only add context do not log; they raise a new exception with `from exc`. This stores the original as `__cause__`, and when the exception is not handled, both are printed together.[^py314-reference-simple-stmts-raise] In the example below, `read_config()` logs nothing, `load_settings()` adds context, and `main()` logs once:

```python
import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(name)s: %(message)s")
logger = logging.getLogger("app")

def read_config(path):
    with open(path) as f:               # no logging here: the caller decides
        return f.read()

def load_settings(path):
    try:
        text = read_config(path)
    except OSError as exc:
        raise RuntimeError(f"cannot load settings from {path}") from exc
    return text.split()

def main():
    try:
        load_settings("missing.cfg")
    except RuntimeError:
        logger.exception("startup failed")  # one record, with the whole chain
        # ERROR app: startup failed
        # Traceback: ... FileNotFoundError ... "The above exception was the direct cause ..."
        # RuntimeError: cannot load settings from missing.cfg

main()
```

Two clarifications. First, `logger.exception()` belongs in an exception handler: the documentation says it should be called from one.[^py314-library-logging-logger-exception] Outside an `except` block there is no current exception, and in CPython 3.13 and 3.14 it prints `NoneType: None`. Second, if a lower level really recovers and the exception does not propagate further, log it once at the level where that happened. The rule is one: the level that stops the propagation of the exception is the one that logs it.

**Common mistakes:**
- calling `logger.exception()` in every `except` along the call path: one failure then appears in the logs several times;
- logging an exception and re-raising it with a bare `raise`, then logging it again higher up: the same duplicates again;
- writing `logger.error(str(exc))` without `exc_info`: the message text is there, but the traceback is lost.

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
