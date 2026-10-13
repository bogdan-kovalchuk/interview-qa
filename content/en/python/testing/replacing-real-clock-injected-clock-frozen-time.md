---
id: py-testing-0015
title: "How does replacing the real clock with an injected clock or frozen time make timeout and expiry tests deterministic?"
description: "Instead of time.sleep() and real waiting, the test controls a clock abstraction, so timeout, TTL and expiry are checked instantly and without flakiness."
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
  - source_id: py314-library-time
    title: "Python 3.14: Library/time"
    url: https://docs.python.org/3.14/library/time.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: time.monotonic() and time.time()."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: default parameter values are evaluated when def runs."
---

## Short answer

**Instead of `time.sleep()` and real waiting, the code receives its clock from outside and the test moves time to the needed point; timeout and expiry are then checked instantly.** For in-process timeouts and TTLs use `time.monotonic()`: it cannot go backwards and is not affected by system clock updates, but its reference point is undefined, so only differences between two calls are valid.[^py314-library-time] Expiry that survives a restart or crosses processes (cookie, JWT `exp`) needs wall-clock time.

## Detailed explanation

Timeouts, TTLs and expiry depend on the current time. A test that waits for real time with `time.sleep()` is slow and can fail or pass at random on a loaded CI machine. An injected clock removes this dependency: the code receives the clock as a parameter, a callable that returns seconds. In production the real clock is passed in; in the test, a controlled object that the test moves forward.

Below is a token cache with a 30-second TTL and a test of the boundary itself, not just "a moment later" and "much later". The test crosses the boundary in two steps: 29 seconds, when the entry is still valid, then one more second, when it is expired. `get` compares `now < expires_at`, so a check at "60 seconds later" cannot tell `<` from `<=`.

```python
from collections.abc import Callable


class TokenCache:
    def __init__(self, ttl_seconds: float, clock: Callable[[], float]) -> None:
        self._ttl = ttl_seconds
        self._clock = clock                 # injected: production passes time.monotonic
        self._values: dict[str, str] = {}
        self._expires_at: dict[str, float] = {}

    def put(self, key: str, value: str) -> None:
        self._values[key] = value
        self._expires_at[key] = self._clock() + self._ttl

    def get(self, key: str) -> str | None:
        if key in self._values and self._clock() < self._expires_at[key]:
            return self._values[key]
        self._values.pop(key, None)
        self._expires_at.pop(key, None)
        return None


class FakeClock:
    def __init__(self, now: float = 0.0) -> None:
        self.now = now

    def __call__(self) -> float:
        return self.now

    def advance(self, seconds: float) -> None:
        self.now += seconds


def test_entry_expires_exactly_at_ttl() -> None:
    clock = FakeClock()
    cache = TokenCache(ttl_seconds=30, clock=clock)
    cache.put("token", "abc")
    clock.advance(29)
    assert cache.get("token") == "abc"  # 29 s < 30 s: still valid
    clock.advance(1)
    assert cache.get("token") is None   # now == expiry: the entry is gone
```

For in-process timeouts and TTLs use a monotonic clock. `time.monotonic()` cannot go backwards and is not affected by system clock updates, so production code passes exactly that. Its reference point is undefined, so only the difference between two values is meaningful.[^py314-library-time] The value itself must not be stored across processes or restarts: expiry that has to survive them needs wall-clock time. `time.time()` can return a lower value than a previous call if the system clock has been set back.[^py314-library-time]

Frozen time also works without an injected clock. If the code calls `time.monotonic()` inside a method body, `unittest.mock.patch("time.monotonic")` changes the object that this name points to, so the call sees the substituted value.[^py314-library-unittest-mock] The trap is the default value: `clock=time.monotonic` in a signature is evaluated when `def` runs,[^py314-reference-compound-stmts-function-definitions] so a later `patch` does not replace it. Pass the clock explicitly, or read `time.monotonic()` inside the method body.

**Common mistakes:**
- `time.sleep(0.5)` in a test instead of a controlled clock: the test is slow and depends on machine load;
- `time.time()` for timeouts and TTLs: setting the system clock back breaks the comparison;
- `clock=time.monotonic` in a signature combined with a later `patch`: the substitution does not happen and the code uses the real clock;
- checking only far from the boundary, for example 60 seconds with a 30-second TTL: this misses a `<` versus `<=` mistake.

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
