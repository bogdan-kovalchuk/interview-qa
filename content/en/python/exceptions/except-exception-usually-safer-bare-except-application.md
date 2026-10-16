---
id: py-excpt-0001
title: "Why is `except Exception` usually safer than a bare `except` for application-level handling?"
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
  - source_id: py314-library-exceptions-exception-hierarchy
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html#exception-hierarchy
  - source_id: py314-tutorial-errors-handling-exceptions
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html#handling-exceptions
  - source_id: py314-reference-expressions-generator-iterator-methods
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-iterator-methods
---

## Short answer

**A bare `except` catches every `BaseException`, including `SystemExit` and `KeyboardInterrupt`, whereas `except Exception` lets them pass.**[^py314-library-exceptions-exception-hierarchy] These exceptions signal exit, interruption or generator shutdown, not a failure to handle: `sys.exit()`, Ctrl-C, and closing a generator with `close()`. So a bare `except` can swallow a shutdown request, while `except Exception` lets it reach the top level.[^py314-library-exceptions-exception-hierarchy]

## Detailed explanation

A bare `except:` is a handler without an expression. It must come last in the list of handlers, and it catches everything raised in the `try` block.[^py314-reference-compound-stmts-the-try-statement] In the exception hierarchy, `BaseException` is the root. All built-in exceptions except `BaseExceptionGroup`, `GeneratorExit`, `KeyboardInterrupt` and `SystemExit` derive from `Exception`, that is, from program errors such as `ValueError` and `KeyError`. These four classes sit next to `Exception`, not under it.[^py314-library-exceptions-exception-hierarchy]

The example below shows that `except Exception` does not catch a request to exit:

```python
import sys

def run_job():
    sys.exit(3)                  # SystemExit: a request to stop, not a job failure

try:
    run_job()
except Exception as error:       # SystemExit is not an Exception, so it passes through
    print('job failed:', error)
print('not reached')             # the process exits with status 3 before this line
```

If `except Exception as error:` is replaced by a bare `except:`, and the `print` by `print('job failed')`, the program prints `job failed` and continues after the block (exit status 0 instead of 3): the exit is swallowed.

`KeyboardInterrupt` deliberately inherits from `BaseException`, so that ordinary code catching `Exception` does not catch it by accident.[^py314-library-exceptions] `GeneratorExit` is raised by `close()` and is also a `BaseException`, so a bare `except` inside a generator catches it too.[^py314-library-exceptions-exception-hierarchy] If the generator then yields a value, `close()` raises `RuntimeError`.[^py314-reference-expressions-generator-iterator-methods]

`except Exception` does not mean "handle everything". The tutorial describes `Exception` as a wildcard that catches almost everything, and it advises being as specific as possible about the exception types.[^py314-tutorial-errors-handling-exceptions] So the safer approach is a narrow list of expected exceptions, with a broad `except Exception` kept at the boundary where the error is logged or re-raised, not silently swallowed.

**Common mistakes:**
- writing a bare `except:` "just in case" and swallowing `SystemExit` and `KeyboardInterrupt`;
- assuming that `except Exception` catches everything: it catches almost everything, but not `SystemExit`, `KeyboardInterrupt` or `GeneratorExit`;
- catching `Exception` and silently continuing, which hides bugs in the code.
