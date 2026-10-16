---
id: py-testing-0009
title: "How can a broad-scoped mutable fixture create order-dependent tests and state leakage?"
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
  - source_id: pytest-how-to-fixtures-scopes
    title: "pytest documentation: How-to guides, Fixtures, Fixture scopes"
    url: https://docs.pytest.org/en/stable/how-to/fixtures.html#fixture-scopes
  - source_id: pytest-how-to-fixtures-yield
    title: "pytest documentation: How-to guides, Fixtures, yield fixtures"
    url: https://docs.pytest.org/en/stable/how-to/fixtures.html#yield-fixtures-recommended
---

## Short answer

**A fixture with `scope="module"` or `scope="session"` creates one instance for the whole module or session, so a mutable value (dict, list, DB connection) changed by one test is seen by the later tests in that scope.**[^pytest-how-to-fixtures-scopes]

```python
import pytest

@pytest.fixture(scope="module")
def shared_cache():
    return {}  # one dict shared by every test in the module

def test_a(shared_cache):
    shared_cache["key"] = "value"

def test_b(shared_cache):
    assert "key" not in shared_cache  # AssertionError if test_a ran first
```

Such tests become order-dependent: run alone or in another order, they behave differently. For mutable state, use the `function` scope or reset the state after each test.

## Detailed explanation

A fixture is a function whose result pytest caches for a given scope. The default scope is `function`, so the fixture is created again for each test. The `module` and `session` scopes mean one instance for the whole module or the whole session: pytest creates it when a test first requests it and destroys it during the teardown after the last test in that scope.[^pytest-how-to-fixtures-scopes] Sharing is the effect of a wider scope: every test in the scope receives the same object, not a copy.

Sharing only causes harm when the object can change. A number, a string, a `frozenset`, or a `tuple` whose elements are immutable is safe to share, but a `dict`, a `list`, a `tuple` holding a list, or a database connection is not: a test that adds a key or a row hands the changed state to the tests that run after it. Example: `test_b` passes when run alone but fails when `test_a` ran before it.

```python
import pytest

@pytest.fixture(scope="module")
def shared_cache():
    return {}  # one dict shared by every test in the module

def test_a(shared_cache):
    shared_cache["key"] = "value"

def test_b(shared_cache):
    assert "key" not in shared_cache  # AssertionError if test_a ran first
```

This is an order-dependent test. Its result depends not on its own code but on what other tests did to the same object earlier. The bug appears only when the tests run together in a particular order, so a single run of `test_b` looks green.

The fix depends on what is stored. If the fixture is cheap to build, make it `function`-scoped so that each test gets its own dict. If creation is expensive (a database, a network connection), keep the wide scope for the resource and roll the state back after each test: for example, a function-scoped fixture opens a transaction and rolls it back at the end of the test. Code after `yield` runs in the teardown, when the fixture is destroyed.[^pytest-how-to-fixtures-yield] For `scope="module"` that happens once, after the module's last test, so it does not reset the state between the tests of the module; for a `function`-scoped fixture, destruction happens after every test.[^pytest-how-to-fixtures-scopes]

**Common mistakes:**
- assuming that `scope="module"` isolates tests: it isolates modules from each other, not the tests inside one module;
- calling the failure "flaky" and re-running the test instead of looking for the shared mutable state;
- widening the `scope` "for speed" without checking whether the tests write to the fixture's value.
