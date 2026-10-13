---
id: py-testing-0013
title: "How does over-mocking implementation details make a test suite brittle during behaviour-preserving refactoring?"
description: "How does over-mocking implementation details make a test suite brittle during behaviour-preserving refactoring?"
track: python
section: testing
level: senior
type: pitfall
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
  - source_id: py314-library-unittest-mock-assert-has-calls
    title: "Python 3.14: Library/unittest.mock, Mock.assert_has_calls"
    url: https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.assert_has_calls
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: assert_has_calls checks the mock_calls list; the order matters unless any_order is set."
---

## Short answer

**A test that checks the number and order of calls to internal mock objects, instead of the observable result, breaks under a behaviour-preserving refactoring that changes those calls.**[^py314-library-unittest-mock-assert-has-calls] For example, replacing a loop of `save` calls with one batch call to `save_many` keeps the result, but `assert_has_calls` on the `save` mock stops passing. The fix is to test the input and output of the public contract, and to use a mock for external dependencies where the call itself is the result, such as a sent email.

## Detailed explanation

A mock records implementation details when the test checks not the result but the protocol: how many times and in what order a dependency was called. `assert_has_calls` checks the `mock_calls` list: unless `any_order` is set, the expected calls must appear consecutively, while extra calls before or after them are allowed.[^py314-library-unittest-mock-assert-has-calls] So changing the number or the order of calls breaks the test, even when nothing changed for the user of the service.

The service used to call `save` once per row; after the refactoring it calls `save_many`. The storage ends up the same. `BehaviourTest` checks the state of a Fake and passes for both versions of the service. `BrittleTest` checks the calls to `save` and fails after the refactoring.

```python
import unittest
from unittest import mock

class UserServiceBatched:
    def __init__(self, repo):
        self.repo = repo

    def import_users(self, rows):
        self.repo.save_many(rows)  # refactored: one batch call, same stored rows
        return len(rows)

class InMemoryRepo:  # Fake
    def __init__(self):
        self.rows = []

    def save(self, row):
        self.rows.append(row)

    def save_many(self, rows):
        self.rows.extend(rows)

class BrittleTest(unittest.TestCase):
    def test_import_calls_save_per_row(self):
        repo = mock.Mock()
        UserServiceBatched(repo).import_users(["alice", "bob"])
        # Fails: the code now calls save_many, so save has no calls
        repo.save.assert_has_calls([mock.call("alice"), mock.call("bob")])

class BehaviourTest(unittest.TestCase):
    def test_import_stores_rows(self):
        repo = InMemoryRepo()
        UserServiceBatched(repo).import_users(["alice", "bob"])
        self.assertEqual(repo.rows, ["alice", "bob"])  # passes for both service versions

if __name__ == "__main__":
    unittest.main(verbosity=1)
```

A mock is appropriate when the call itself is the result: an email was sent exactly once, a payment was charged once. For internal dependencies that have behaviour of their own (a storage, a cache), prefer a Fake and check the state: then a refactoring that preserves behaviour does not break the test.

**Common mistakes:**
- checking every internal call when the test should check the result;
- assuming that more mocks make a test more isolated: isolation is needed from the outside world, not from your own code that the test runs anyway;
- adjusting the test's expectations to a new sequence of calls, after which the test checks nothing useful.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
