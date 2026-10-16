---
id: py-testing-0007
title: "How does fixture lifecycle help set up state, yield a resource, and tear it down after the test?"
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
  - source_id: pytest-how-to-fixtures-yield
    title: "pytest documentation: How to use fixtures (yield fixtures)"
    url: https://docs.pytest.org/en/stable/how-to/fixtures.html#yield-fixtures-recommended
  - source_id: pytest-how-to-fixtures-errors
    title: "pytest documentation: Handling errors for yield fixture"
    url: https://docs.pytest.org/en/stable/how-to/fixtures.html#handling-errors-for-yield-fixture
  - source_id: pytest-how-to-fixtures-scopes
    title: "pytest documentation: Fixture scopes"
    url: https://docs.pytest.org/en/stable/how-to/fixtures.html#fixture-scopes
---

## Short answer

**A fixture runs the code before `yield` as setup, passes the resource to the test as the `yield` value, and runs the code after `yield` as teardown once the test finishes.**[^pytest-how-to-fixtures-yield]

```python
@pytest.fixture
def db_conn():
    conn = create_connection()  # setup, runs before the test
    yield conn  # the test receives conn here
    conn.close()  # teardown, runs after the test
```

The scope sets how long the resource lives: `function` (the default) creates it for each test, while `module` or `session` share one resource, which reduces overhead but needs care with mutable state.[^pytest-how-to-fixtures-scopes]

## Detailed explanation

A fixture is a function marked with `@pytest.fixture`. A test requests it by naming a parameter after it, and pytest calls it before the test. If the fixture uses `yield`, the code before `yield` is setup, and the value that `yield` produces is what the test receives. The code after `yield` is teardown: pytest runs it when the test is finished, in reverse order to the setup.[^pytest-how-to-fixtures-yield]

Teardown belongs to the same fixture, so it does not run if the setup fails before `yield`. Fixtures that have already set up successfully for that test are still torn down.[^pytest-how-to-fixtures-errors] So place `yield` right after the resource is opened: risky steps before it can leave the resource open.

Example: a fixture that keeps a log, and a test that checks that setup ran before the test:

```python
import pytest

LOG = []


@pytest.fixture
def db_conn():
    LOG.append("setup")  # runs before the test
    yield "connection"  # the test receives this value
    LOG.append("teardown")  # runs after the test


def test_query_uses_connection(db_conn):
    assert db_conn == "connection"
    assert LOG == ["setup"]
```

The test passes because setup has already been recorded. When a test fails, teardown still runs: checked on pytest 9.1.1 with a fixture that prints in setup and teardown and a test with `assert False`; running with `pytest -s` printed `setup`, then `F`, then `teardown`.

The scope decides when pytest destroys a fixture: `function` at the end of each test (the default), `module` after the last test in the module, `session` at the end of the session.[^pytest-how-to-fixtures-scopes] A wider scope means the resource is created less often, but tests share its state, so a change left by one test reaches the next.

Teardown is not an absolute guarantee: if the process is killed hard, the code after `yield` does not run. Cleanup written after an `assert` in the test body also does not run when that `assert` fails, which is why it belongs in a fixture.

**Common mistakes:**
- putting cleanup at the end of a test body instead of in fixture teardown, so it does not run when the test fails;
- using `scope="session"` for a resource with mutable state that tests change;
- assuming teardown runs when setup failed before `yield`.
