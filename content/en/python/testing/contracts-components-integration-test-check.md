---
id: py-testing-0002
title: "What contracts between components does an integration test check?"
description: "What contracts between components does an integration test check?"
track: python
section: testing
level: middle
type: mechanism
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
  - source_id: martinfowler-integration-test
    title: "Martin Fowler: Integration Test"
    url: https://martinfowler.com/bliki/IntegrationTest.html
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Essay by Martin Fowler (not official documentation): definition of integration tests, narrow and broad variants, contract tests for checking doubles."
---

## Short answer

**An integration test checks the seam between components: that code calling another component works correctly with it under that component's contract.**[^martinfowler-integration-test] For example, an SQL query must match the real database schema, and an HTTP response must parse into the expected data type. A double used in such a test must be checked separately against the real component, which is what contract tests are for.[^martinfowler-integration-test]

## Detailed explanation

An integration test answers a different question from a unit test: whether independently developed units work correctly when they are connected.[^martinfowler-integration-test] The object of the check is the place where the code crosses the boundary between components: a call into another module, a database query, an HTTP client or a message queue. The contract at that boundary is the agreement about what passes through it: the table schema, the fields and types of a response, the message format, error codes and the order of calls.

Fowler distinguishes narrow and broad integration tests. A narrow one checks only the code of its own service that talks to an external component, and uses test doubles of that component; a broad one uses live versions of all services and runs through them. Fowler suggests considering the narrow style when only broad tests exist: it is likely to improve testing speed, ease of use and resiliency significantly.[^martinfowler-integration-test]

The example shows why a double is risky without a check. The first test uses a `Mock`, which accepts any call and creates attributes on access, so the real schema does not constrain it.[^py314-library-unittest-mock] The second works with the real SQLite engine and schema, and the error in the query becomes visible.

```python
import sqlite3
from unittest import mock


def find_email(conn, user_id):
    row = conn.execute("SELECT email FROM users WHERE id = ?", (user_id,)).fetchone()
    return row[0] if row else None


# Unit test with a double: passes, although the real schema has no 'email' column.
fake = mock.Mock()
fake.execute.return_value.fetchone.return_value = ("a@example.com",)
print(find_email(fake, 1))  # a@example.com

# Integration test with the real engine and schema: the query is wrong.
conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, mail TEXT)")  # the column is 'mail'
try:
    find_email(conn, 1)
except sqlite3.OperationalError as error:
    print(error)  # no such column: email
```

To keep a double from drifting away from reality, it is checked separately: Fowler proposes contract tests for this.[^martinfowler-integration-test] He describes the combination of narrow integration tests with doubles and contract tests as a way to integrate with an external service without running tests against its live instance. Broad tests with all live services then remain as a thin final smoke test with a small number of scenarios.[^martinfowler-integration-test]

**Common mistakes:**
- testing SQL or HTTP code only with a `Mock`: the test passes with any schema or response;
- assuming an integration test must start all services: a narrow variant with doubles is an integration test too;
- trusting a double that nobody has checked against the real component.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
