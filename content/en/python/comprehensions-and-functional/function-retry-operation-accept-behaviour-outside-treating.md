---
id: py-compfn-0008
title: "The function `retry(operation)` must accept behaviour from the outside: how does treating it as a first-class function let you pass the operation without calling it immediately?"
description: "The function `retry(operation)` must accept behaviour from the outside: how does treating it as a first-class function let you pass the operation without calling it immediately?"
track: python
section: comprehensions-and-functional
level: middle
type: practical
tags: [retry-operation]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-howto-functional
    title: "Python 3.14: Howto/functional"
    url: https://docs.python.org/3.14/howto/functional.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-expressions-displays-for-lists-sets-and-dict
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**In Python, functions are first-class objects: you can pass a reference to a function (without parentheses `()`), and `retry` will call it internally when needed.**[^py314-howto-functional] For example, `retry(fetch_data)` passes a callable, whereas `retry(fetch_data())` would pass an already-computed result. The `retry` function can accept `operation: Callable[[], T]` and invoke `operation()` inside a retry loop.

## Detailed explanation

In Python, functions are first-class citizens (first-class objects), meaning they can be assigned to variables, stored in data structures, returned from other functions, and passed as arguments just like any other value.[^py314-howto-functional] When passing a function by its identifier without parentheses `()`, you pass a reference to the callable object itself rather than the result of its evaluation. This defers execution (deferred or lazy execution) and delegates control over the invocation to the receiving function, such as `retry`.

If a caller accidentally invokes the function at the call site – `retry(operation())` – the interpreter evaluates it immediately before control is transferred to `retry`. In that scenario, `retry` receives an already-evaluated return value or fails to catch an exception raised on the first attempt, entirely undermining the retry mechanism. By receiving the callable object, `retry` can invoke `operation()` within a `try...except` block, manage backoff delays between attempts, track attempt counts, and catch only expected exception classes.

When the target operation requires its own arguments, first-class functions combine cleanly with closures, `functools.partial`, or `lambda` expressions, such as `retry(lambda: fetch_user(user_id))` or by forwarding `*args` and `**kwargs` directly through the signature of `retry`.

Implementation of the `retry` pattern by passing a callable object:

```python
import time
from typing import Callable, TypeVar

T = TypeVar("T")


def retry(operation: Callable[[], T], max_attempts: int = 3, delay: float = 0.1) -> T:
    for attempt in range(1, max_attempts + 1):
        try:
            return operation()  # Called only when retry decides
        except Exception as exc:
            if attempt == max_attempts:
                raise
            time.sleep(delay)
    raise RuntimeError("Unreachable")


# Passing the function reference without parentheses
call_count = 0


def unstable_network_call() -> str:
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError("Temporary glitch")
    return "success"


result = retry(unstable_network_call)
print(result)
# Output: success
```

**Common mistakes and practical recommendations:**
- accidentally invoking the function at the call site: `retry(fetch())` instead of `retry(fetch)`;
- losing operation arguments: if the operation requires arguments, pass `functools.partial(fetch, url)` or `lambda: fetch(url)` rather than calling it eagerly;
- swallowing system exceptions: catch only expected operational exceptions rather than `except BaseException:`, which suppresses `KeyboardInterrupt` and `SystemExit`.

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
