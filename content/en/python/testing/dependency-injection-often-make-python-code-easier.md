---
id: py-testing-0005
title: "Why does dependency injection often make Python code easier to test deterministically?"
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
  - source_id: py314-tutorial-defining-functions
    title: "Python 3.14: Tutorial/Defining Functions"
    url: https://docs.python.org/3.14/tutorial/controlflow.html#defining-functions
  - source_id: py314-library-unittest-mock-where-to-patch
    title: "Python 3.14: Library/unittest.mock (where to patch)"
    url: https://docs.python.org/3.14/library/unittest.mock.html#where-to-patch
---

## Short answer

**Dependency injection (DI) passes dependencies as arguments, so a test substitutes a fake or mock by passing it in.** A function that takes `http_client` and `clock` gets a `StubClient` and a `FrozenClock` in its test: no network, no real time. When a dependency is imported inside the function, substituting it requires `patch`, which temporarily replaces the object a name points to.[^py314-library-unittest-mock-patch] DI is a design pattern, not a Python rule, so its benefit depends on passing in every input that the result depends on.

## Detailed explanation

Dependency injection (DI) is a design convention, not a language feature. The code receives its dependencies (an HTTP client, a clock, a store) as function or constructor parameters instead of creating them or importing them inside. Python does not require this, but the call mechanism works exactly that way: at call time the arguments are bound to the local parameter names, so the body uses the object the caller passed in.[^py314-tutorial-defining-functions]

A hidden dependency is an `import` or a call to `datetime.now()` inside the function. To substitute it, you have to patch an attribute of a module. `patch` works by temporarily replacing the object that a name points to, so the patch must sit where the code looks the name up.[^py314-library-unittest-mock-where-to-patch] A patch applied in a neighbouring module changes nothing, and the test may silently run the real dependency.

Example: `make_report` reads neither the network nor a clock, so the test passes a fake and a fixed time as arguments, with no patch:

```python
import datetime as dt


def make_report(fetch_rate, now):
    rate = fetch_rate("USD")  # collaborator passed in, not imported
    return f"{now:%Y-%m-%d}: USD={rate:.2f}"


def test_make_report_is_deterministic():
    fixed_now = dt.datetime(2026, 1, 1)
    report = make_report(lambda currency: 41.5, fixed_now)  # fake, no network
    assert report == "2026-01-01: USD=41.50"
```

The result is deterministic because every input is set in the test itself. The same logic with hidden dependencies would need two patches in the module where `make_report` lives.

DI does not make code deterministic by itself. If `random.random()`, `datetime.now()` or a global cache is still used inside the function, that input is still hidden. A fake must match the contract of the real object: a test with the wrong method passes but proves nothing. For one function with one call, DI can be unnecessary complexity.

**Common mistakes:**
- assuming DI makes code deterministic while `datetime.now()` or `random` remain inside;
- passing a fake whose methods or signature the real object does not have, so the test passes against the wrong interface;
- converting every function to DI when a single `patch` is simpler.
