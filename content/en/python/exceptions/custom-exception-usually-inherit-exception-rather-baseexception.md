---
id: py-excpt-0011
title: "Why should a custom exception usually inherit from `Exception` rather than `BaseException`?"
track: python
section: exceptions
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
  - source_id: py314-library-asyncio-exceptions
    title: "Python 3.14: Library/asyncio-exceptions"
    url: https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError
---

## Short answer

**A custom exception should inherit from `Exception` so that an ordinary `except Exception` catches it without also catching the system-level exceptions `SystemExit`, `KeyboardInterrupt` and `GeneratorExit`.**[^py314-library-exceptions] These three classes, plus `BaseExceptionGroup`, inherit directly from `BaseException`, bypassing `Exception`.[^py314-library-exceptions] If a custom exception inherits from `BaseException` instead, a plain `except Exception` misses it, while `except BaseException` also catches the system signals, which is usually undesirable.[^py314-reference-compound-stmts-the-try-statement]

## Detailed explanation

The hierarchy of built-in exceptions starts at `BaseException`. Below it branch the system-level classes and `Exception`, and most errors belong to `Exception`. The classes `SystemExit`, `KeyboardInterrupt`, `GeneratorExit` and `BaseExceptionGroup` inherit directly from `BaseException`. The documentation gives the reason for `SystemExit`: it inherits from `BaseException` so that code catching `Exception` does not catch it by accident.[^py314-library-exceptions]

An `except X` clause matches when the exception is an instance of `X` or of a subclass of `X`.[^py314-reference-compound-stmts-the-try-statement] So `except Exception` catches any subclass of `Exception`, but not `SystemExit` or `KeyboardInterrupt`. A custom exception that derives from `Exception` automatically falls into the category of ordinary errors that a general handler deals with, while system-level signals stay outside it.

The consequences show up at the edge of a program. For example, a task-processing loop often has an `except Exception` that logs the error and moves on. If a library error derives from `Exception`, the loop sees it. If it derives from `BaseException`, the error passes the handler and the loop ends. Replacing that handler with `except BaseException` is a bad idea too: it also catches `KeyboardInterrupt`, so Ctrl+C can be swallowed if the handler keeps running, and the program does not stop.

The exception to the rule is control signals that a general handler must not swallow. In the standard library this is `asyncio.CancelledError`: since Python 3.8 it inherits from `BaseException` rather than `Exception`, and the documentation requires it to be re-raised in almost all situations.[^py314-library-asyncio-exceptions] For a custom exception of this kind, `BaseException` can be a justified choice, but then it has to be documented clearly for callers.

Example: `AppError` derives from `Exception`, `AppFatal` from `BaseException`. The output is the same on CPython 3.13 and 3.14.

```python
class AppError(Exception):
    pass

class AppFatal(BaseException):
    pass

def run(exc_type):
    try:
        raise exc_type("boom")
    except Exception:
        return "caught by except Exception"
    except BaseException:
        return "caught only by except BaseException"

print(run(AppError))  # caught by except Exception
print(run(AppFatal))  # caught only by except BaseException
```

**Common mistakes:**
- inheriting from `BaseException` to "catch everything": general `except Exception` handlers then miss such errors;
- writing `except BaseException` and not re-raising: this swallows `KeyboardInterrupt` and `SystemExit`;
- assuming `except Exception` catches everything: the system-level classes stay outside it.
