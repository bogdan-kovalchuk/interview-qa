---
id: py-prac-0018
title: "Design a thread-safe rate-limit decorator with an injected monotonic clock: up to X calls per rolling T seconds, raising an explicit exception on excess."
description: "threading.Lock protects the timestamps list, the injected clock (default time.monotonic) allows testing, and the rolling window is implemented by removing expired timestamps from the front of the list."
track: python
section: practical-coding
level: senior
type: practical
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14.7"
  flags: []
anki:
  export: true
sources:
  - source_id: py314-library-threading-lock-objects
    title: "Python 3.14: Library/threading, Lock Objects"
    url: https://docs.python.org/3.14/library/threading.html#lock-objects
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, Lock Objects: Lock supports the context management protocol. Does not describe rate limiting or guarantee the order of writes to data structures."
  - source_id: py314-library-time-time-monotonic
    title: "Python 3.14: Library/time"
    url: https://docs.python.org/3.14/library/time.html#time.monotonic
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, time.monotonic(): a monotonic clock that cannot go backwards and is not affected by system clock updates; only the difference between the results of two calls is valid, because the reference point is undefined. Does not describe time.time()."
  - source_id: py314-library-time-time-time
    title: "Python 3.14: Library/time, time.time"
    url: https://docs.python.org/3.14/library/time.html#time.time
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, time.time(): may return a lower value than a previous call if the system clock has been set back. Does not describe monotonic clocks."
  - source_id: py314-library-collections-collections-deque
    title: "Python 3.14: Library/collections, deque"
    url: https://docs.python.org/3.14/library/collections.html#collections.deque
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, deque: appends and pops from either side with approximately the same O(1) performance. Does not describe rate limiting."
---

## Short answer

**A rolling window keeps the `timestamps` list under a `threading.Lock`, and the injected `clock` (default `time.monotonic`) allows testing: expired timestamps are removed from the front of the list.** `threading.Lock` supports the context management protocol, so `with lock:` acquires and releases it.[^py314-library-threading-lock-objects] <span class="warn">`time.time()` is not suitable, because the system clock can be set back.</span>[^py314-library-time-time-time] `time.monotonic()` cannot go backwards.[^py314-library-time-time-monotonic] `clock()` is read inside `with lock:` so that `timestamps` stays in order.

```python
import threading
import time
import functools

class RateLimitExceeded(Exception):
    pass

def rate_limit(max_calls, period, clock=None):
    if clock is None:
        clock = time.monotonic
    def decorator(func):
        lock = threading.Lock()
        timestamps = []
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with lock:
                now = clock()
                cutoff = now - period
                while timestamps and timestamps[0] <= cutoff:
                    timestamps.pop(0)
                if len(timestamps) >= max_calls:
                    raise RateLimitExceeded(
                        f"Rate limit: {max_calls} calls per {period}s"
                    )
                timestamps.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

## Detailed explanation

A rate limit with a window of `T` seconds allows up to `X` calls in the last `T` seconds. The implementation stores the moments of successful calls. Before each call it removes the records with `ts <= now - T`, and if `X` remain, it raises an exception. `func` itself is called outside the lock, so a slow function does not block other threads.

`time.monotonic()` is documented as a clock that cannot go backwards and is not affected by system clock updates.[^py314-library-time-time-monotonic] So the difference between two call moments does not become negative because the system time was changed. `time.time()` is not suitable for this: it can return a value lower than a previous call if the system clock has been set back.[^py314-library-time-time-time] The injected `clock` lets a test substitute its own clock and control time without real waiting.

The order of reading `clock()` and taking the lock matters. If `now` is read before the lock, two threads can record moments out of order: thread A reads `10.0` and is paused, thread B reads `10.5` and records it first, then A records `10.0` at the end. Now `timestamps[0]` is `10.5`, and the removal loop stops at it even though `10.0` is already outside the window. With an order of threads forced by hand, on CPython 3.13 and 3.14 with `T = 1` and `X = 2`, a call at the moment `11.2` gets `RateLimitExceeded`, although the window `(10.2, 11.2]` holds only one call (`10.5`). So `clock()` is read inside `with lock:`.

In CPython, `list.pop(0)` shifts the remaining elements, so it costs O(n); this is an implementation detail. For large windows, `collections.deque` gives approximately the same O(1) performance for `popleft()` and `append()` from either side.[^py314-library-collections-collections-deque]

**Common mistakes:**
- reading the time before the lock: the order of records breaks, as shown above;
- using `time.time()` for the window: a clock set back delays the removal of records, and a clock set forward removes them too early;
- calling `func` inside the lock: all threads wait for one long call.

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
