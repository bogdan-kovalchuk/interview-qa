---
id: py-excpt-0015
title: "When should a library emit a warning instead of raising an exception?"
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
  - source_id: py314-library-warnings-module
    title: "Python 3.14: Library/warnings"
    url: https://docs.python.org/3.14/library/warnings.html#module-warnings
  - source_id: py314-library-warnings-categories
    title: "Python 3.14: Library/warnings"
    url: https://docs.python.org/3.14/library/warnings.html#warning-categories
  - source_id: py314-library-warnings-warn
    title: "Python 3.14: Library/warnings"
    url: https://docs.python.org/3.14/library/warnings.html#warnings.warn
  - source_id: py314-library-warnings-filter
    title: "Python 3.14: Library/warnings"
    url: https://docs.python.org/3.14/library/warnings.html#the-warnings-filter
---

## Short answer

**A library should emit a warning when a condition is not fatal but the user should know about it.**[^py314-library-warnings-module] Typical cases are a deprecated API (`DeprecationWarning`) and dubious runtime behavior (`RuntimeWarning`).[^py314-library-warnings-categories] `warnings.warn()` reports the condition without interrupting execution, and the user controls the reaction through filters, including `error`, which turns a warning into an exception.[^py314-library-warnings-filter] An exception is appropriate when continuing would produce an incorrect result.

## Detailed explanation

The boundary is simple: an exception means the call cannot be carried out correctly, while a warning means the call was carried out, but the caller should know something important. The `warnings` module documentation puts it this way: warnings are issued where a condition normally does not warrant raising an exception and terminating the program.[^py314-library-warnings-module] So a deprecated parameter that still works calls for a warning, while an argument the function cannot turn into a result calls for an exception.

The category matters because it determines whether the user sees the message at all. `DeprecationWarning` is meant for other Python developers and is ignored by default unless the code that triggered it runs in `__main__`; `UserWarning` is the default category for `warn()`; `RuntimeWarning` is for dubious runtime behavior.[^py314-library-warnings-categories] The parameter `stacklevel=2` makes `warn()` point at the caller's line instead of a line inside the library.[^py314-library-warnings-warn]

Below, `connect()` accepts the deprecated `legacy_port`, warns about it and carries on. A port outside the valid range raises an exception, because continuing would be wrong:

```python
import warnings

def connect(host, *, port=None, legacy_port=None):
    if legacy_port is not None:
        warnings.warn("legacy_port is deprecated; use port",
                      DeprecationWarning, stacklevel=2)  # point at the caller's line
        port = legacy_port
    if port is None:
        port = 443
    if not 0 < port < 65536:
        raise ValueError(f"port out of range: {port}")  # continuing would be wrong
    return f"{host}:{port}"

print(connect("example.org", legacy_port=8443))
# stderr: <file>:14: DeprecationWarning: legacy_port is deprecated; use port
# stderr:   print(connect("example.org", legacy_port=8443))
# example.org:8443

with warnings.catch_warnings():
    warnings.simplefilter("error", DeprecationWarning)  # the user turns the warning into an error
    try:
        connect("example.org", legacy_port=8443)
    except DeprecationWarning as exc:
        print("turned into exception:", exc)
# turned into exception: legacy_port is deprecated; use port

try:
    connect("example.org", port=0)
except ValueError as exc:
    print("raised:", exc)
# raised: port out of range: 0
```

The filter stays in the user's hands: the library decides what to report, and the program decides what to do with it, including whether to turn a warning into an error.[^py314-library-warnings-filter]

**Common mistakes:**
- raising a warning where continuing will produce an incorrect result: the user sees a message, but the data is already corrupted;
- omitting `stacklevel=2` in a library's `DeprecationWarning`: the message points at a line inside the library, and this category is ignored by default there, so the user never sees it;[^py314-library-warnings-categories]
- changing the global `warnings` filters from library code: this affects the whole process, not only the library's own calls.
