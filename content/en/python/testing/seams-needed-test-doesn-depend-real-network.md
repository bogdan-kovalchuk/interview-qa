---
id: py-testing-0004
title: "What seams are needed so a test doesn't depend on a real network, clock, or external service?"
track: python
section: testing
sources:
  - source_id: py314-library-unittest
    title: "Python 3.14: Library/unittest"
    url: https://docs.python.org/3.14/library/unittest.html
  - source_id: py314-library-unittest-mock
    title: "Python 3.14: Library/unittest.mock"
    url: https://docs.python.org/3.14/library/unittest.mock.html
  - source_id: pytest-docs
    title: "pytest documentation"
    url: https://docs.pytest.org/en/stable/
  - source_id: hypothesis-docs
    title: "Hypothesis documentation"
    url: https://hypothesis.readthedocs.io/en/latest/
  - source_id: mutmut-docs
    title: "mutmut documentation"
    url: https://mutmut.readthedocs.io/en/latest/
  - source_id: py314-library-unittest-mock-patch
    title: "Python 3.14: Library/unittest.mock (patch)"
    url: https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.patch
  - source_id: py314-library-unittest-mock-where-to-patch
    title: "Python 3.14: Library/unittest.mock (where to patch)"
    url: https://docs.python.org/3.14/library/unittest.mock.html#where-to-patch
  - source_id: freezegun-readme
    title: "FreezeGun README (Usage)"
    url: https://github.com/spulec/freezegun#usage
  - source_id: vcrpy-docs
    title: "VCR.py documentation"
    url: https://vcrpy.readthedocs.io/en/latest/
  - source_id: respx-guide
    title: "RESPX User Guide"
    url: https://lundberg.github.io/respx/guide/
---

## Short answer

**Keep tests independent of the real network, clock and external services by replacing each dependency with a controlled test double at a seam.** For the network, substitute the HTTP client with `unittest.mock.patch`[^py314-library-unittest-mock-patch] or a fixture; for time, use `freezegun`[^freezegun-readme] or an injectable clock; for an external service, use a fake, a stub, record-replay (`vcrpy`[^vcrpy-docs]), or `respx`[^respx-guide] to mock HTTPX requests. <span class="warn">Without seams a test depends on its environment: a network timeout, a changed clock or an unavailable service can make it flaky or break CI.</span>

## Detailed explanation

A seam is a place in the code where a dependency can be replaced without changing the logic. A test's nondeterminism usually comes from the network, the current time or an external service: the result depends on state outside the code, so the same test can pass today and fail tomorrow.

For the network, the simplest option is to replace the HTTP client. `unittest.mock.patch` temporarily replaces the object that a name points to.[^py314-library-unittest-mock-patch] Patch the name where the code looks it up, not where it is defined: if a module has already imported the function, a patch on the source module has no effect.[^py314-library-unittest-mock-where-to-patch]

For time, `freezegun` freezes `datetime.datetime.now()`, `time.time()` and other time functions inside a decorator or context manager.[^freezegun-readme] Without a library, a `clock` parameter gives the same effect: the test passes a fixed value.

For an external service, a fake is a simplified working implementation, a stub returns canned answers, and record-replay plays back recorded HTTP interactions: `vcrpy` writes them to a cassette and, on later runs, reads the responses without HTTP traffic.[^vcrpy-docs] `respx` captures requests sent by HTTPX and returns the responses you define.[^respx-guide]

Example without `patch`:

```python
import datetime as dt
from unittest.mock import Mock


def fetch_rate(client, clock):
    response = client.get("/rates")  # network seam: any object with get()
    return {"rate": response["rate"], "fetched_at": clock()}  # clock seam


def test_fetch_rate_without_network_or_real_clock():
    client = Mock()  # the Mock records the call; no socket is opened
    client.get.return_value = {"rate": 1.25}
    fixed_now = dt.datetime(2026, 1, 1, tzinfo=dt.timezone.utc)

    result = fetch_rate(client, clock=lambda: fixed_now)

    assert result == {"rate": 1.25, "fetched_at": fixed_now}
    client.get.assert_called_once_with("/rates")
```

Seams do not make a test truthful by themselves: a fake or mock shows how the code reacts to the response you gave it, not whether the real service returns that response. After an API change the cassette must be recorded again, or the test keeps checking a stale response.[^vcrpy-docs]

**Common mistakes:**
- patching a name in the module where it is defined, not where the code uses it;
- leaving `datetime.now()` or `time.time()` directly in the logic you test;
- assuming that a fake or mock proves the behaviour of the real service.
