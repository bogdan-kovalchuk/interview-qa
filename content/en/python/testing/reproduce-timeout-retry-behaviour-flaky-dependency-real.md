---
id: py-testing-0006
title: "How do you reproduce timeout and retry behaviour without a flaky dependency on a real external service?"
description: "How do you reproduce timeout and retry behaviour without a flaky dependency on a real external service?"
track: python
section: testing
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
  - source_id: py314-library-unittest
    title: "Python 3.14: Library/unittest"
    url: https://docs.python.org/3.14/library/unittest.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-unittest-mock
    title: "Python 3.14: Library/unittest.mock"
    url: https://docs.python.org/3.14/library/unittest.mock.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: pytest-docs
    title: "pytest documentation"
    url: https://docs.pytest.org/en/stable/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official pytest documentation."
  - source_id: hypothesis-docs
    title: "Hypothesis documentation"
    url: https://hypothesis.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Hypothesis (property-based testing) documentation."
  - source_id: mutmut-docs
    title: "mutmut documentation"
    url: https://mutmut.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official mutmut (mutation testing) documentation."
  - source_id: py314-library-unittest-mock-side-effect
    title: "Python 3.14: Library/unittest.mock (Mock.side_effect)"
    url: https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.side_effect
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, section Mock.side_effect: an iterable must yield a value on every call; an exception element is raised instead of returned."
---

## Short answer

**A mock HTTP client with `side_effect` reproduces a sequence of errors followed by success, and the test checks the number of calls and the result without a real network.**[^py314-library-unittest-mock-side-effect]

```python
call = Mock(side_effect=[TimeoutError(), TimeoutError(), "ok"])
assert fetch_with_retry(call, sleep=lambda seconds: None) == "ok"
assert call.call_count == 3
```

Dependency injection passes the mock in place of the real client, and an injectable `sleep` removes the real waiting. <span class="warn">Real sleep calls in retry logic should be replaced with an injectable delay function, or the test becomes slow.</span>

## Detailed explanation

A real timeout is hard to reproduce against a live service: it depends on load and the network, so the test becomes slow or flaky. Instead, reproduce the sequence of results itself. A `Mock` with `side_effect` as an iterable returns the next element on each call, and an element that is an exception is raised instead of returned.[^py314-library-unittest-mock-side-effect]

The retry logic receives the client as a parameter (the same technique as DI), so the mock is substituted without patches. The delay is also a parameter: with `time.sleep` the test would wait 1 + 2 seconds, while `delays.append` records the delays and checks the backoff instantly. A complete example that passes without a network and without waiting:

```python
import time
from unittest.mock import Mock


def fetch_with_retry(call, max_attempts=3, sleep=time.sleep):
    for attempt in range(1, max_attempts + 1):
        try:
            return call()
        except TimeoutError:
            if attempt == max_attempts:
                raise
            sleep(2 ** (attempt - 1))  # backoff: 1 s, then 2 s


def test_retries_twice_then_succeeds():
    call = Mock(side_effect=[TimeoutError(), TimeoutError(), "ok"])
    delays = []  # the injected sleep records the delays instead of waiting

    assert fetch_with_retry(call, sleep=delays.append) == "ok"
    assert call.call_count == 3
    assert delays == [1, 2]
```

The test checks three things: the number of calls, the result, and the delays between attempts. The give-up path is separate: if the client always raises `TimeoutError`, `fetch_with_retry` re-raises it after the last attempt, and that deserves its own test with `Mock(side_effect=TimeoutError())`.

An iterable in `side_effect` must yield a value on every call.[^py314-library-unittest-mock-side-effect] After the last element the mock raises `StopIteration` (checked on CPython 3.13 and 3.14). A mock reproduces only the exceptions you give it, so take the exception types from the documentation of the real client, not from memory.

**Common mistakes:**
- testing retry with a real `time.sleep`, so the test waits for seconds;
- checking only the number of calls, without the result and without the behaviour after the attempts run out;
- giving a `side_effect` list shorter than the number of calls, so the test fails with `StopIteration`.

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
