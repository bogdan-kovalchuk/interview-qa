---
id: py-prac-0010
title: "Implement a retry decorator with a tuple of transient exception types and `max_attempts`: it must preserve metadata and re-raise the last exception with its traceback."
description: "Wrap the callable with functools.wraps and catch only the configured exception tuple."
track: python
section: practical-coding
level: senior
type: coding
tags: [max-attempts]
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.13.15"
  flags: []
anki:
  export: true
sources:
- source_id: py313-functools
  title: 'Python 3.13: Wrapper metadata'
  url: https://docs.python.org/3.13/library/functools.html#functools.wraps
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-raise
  title: 'Python 3.13: The raise statement'
  url: https://docs.python.org/3.13/reference/simple_stmts.html#the-raise-statement
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
---

## Task

Implement `retry(max_attempts, exceptions)` for synchronous functions. Retry only the supplied transient exception types and re-raise the final failure while retaining its traceback.

## Constraints

- max_attempts includes the initial call and must be a positive int excluding bool. exceptions is a tuple of Exception subclasses; an empty tuple means no retries.
- Calls must tolerate repetition; no delay or backoff is included.

## Short answer

**Wrap the callable with `functools.wraps` and catch only the configured exception tuple.** Return immediately on success and use bare `raise` in the final handler. Validate the attempt count before creating the wrapper.

## Detailed explanation

A successful result stops the loop, including None. Non-transient failures bypass the handler; bare raise retains the active exception and its originating frames. Retrying side effects is safe only when the operation supports repetition. [^py313-functools] [^py313-raise]

## Examples

```python
assert retry(2, (OSError,))(lambda: 4)() == 4
```

## Solution

```python
from functools import wraps

def retry(max_attempts, exceptions):
    if type(max_attempts) is not int:
        raise TypeError("max_attempts must be int")
    if max_attempts < 1:
        raise ValueError("max_attempts must be positive")
    if not isinstance(exceptions, tuple) or any(
        not isinstance(t, type) or not issubclass(t, Exception) for t in exceptions
    ):
        raise TypeError("exceptions must be Exception subclasses")
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except exceptions:
                    if attempt == max_attempts - 1:
                        raise
        return wrapper
    return decorate
```

## Complexity

For at most a attempts, wrapper overhead is O(a) with a fixed exception tuple, plus the costs of the attempted calls. Auxiliary loop state is O(1); exception traceback storage depends on the call stack. [^py313-functools] [^py313-raise]

## Edge cases

Cover eventual success, exhausted attempts, immediate non-transient failure, empty exceptions and invalid configuration.

## Tests

Run after the Solution block with pytest installed.

```python
import pytest

calls = []
@retry(3, (OSError,))
def flaky(value):
    """Return after two transient failures."""
    calls.append(value)
    if len(calls) < 3:
        raise OSError("temporary")
    return value
assert flaky(9) == 9 and calls == [9, 9, 9]
assert flaky.__name__ == "flaky" and flaky.__doc__
assert flaky.__wrapped__.__name__ == "flaky"
failure = OSError("permanent")
calls.clear()
def fail():
    calls.append(1)
    raise failure
with pytest.raises(OSError) as caught:
    retry(2, (OSError,))(fail)()
assert caught.value is failure and len(calls) == 2
frames = []
tb = caught.value.__traceback__
while tb:
    frames.append(tb.tb_frame.f_code.co_name)
    tb = tb.tb_next
assert "fail" in frames
calls.clear()
with pytest.raises(OSError):
    retry(3, (ValueError,))(fail)()
assert len(calls) == 1
calls.clear()
with pytest.raises(OSError):
    retry(3, ())(fail)()
assert len(calls) == 1
with pytest.raises(ValueError):
    retry(0, (OSError,))
for bad in ([OSError], (BaseException,), (1,)):
    with pytest.raises(TypeError):
        retry(1, bad)
assert retry(1, (OSError,))(lambda: None)() is None
```

## Evaluation guide

### Expected signals

Check exact call counts, metadata and original traceback frames. Never catch BaseException broadly.

### Red flags

The implementation misses a stated boundary case or its complexity claim omits allocated data.

### Level-up follow-up

How would you add bounded backoff with an injected sleep function?

## Sources

<!-- generated from frontmatter -->
