---
id: py-testing-0010
title: "For a repository that must behave like real in-memory storage, when should you choose a Fake, and when a Stub or an interaction-verifying Mock?"
description: "For a repository that must behave like real in-memory storage, when should you choose a Fake, and when a Stub or an interaction-verifying Mock?"
track: python
section: testing
level: middle
type: comparison
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
  - source_id: py314-library-unittest-mock-quick-guide
    title: "Python 3.14: Library/unittest.mock, Quick Guide"
    url: https://docs.python.org/3.14/library/unittest.mock.html#quick-guide
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: Mock and MagicMock store details of how they have been used."
  - source_id: py314-library-unittest-mock-assert-called-with
    title: "Python 3.14: Library/unittest.mock, Mock.assert_called_with"
    url: https://docs.python.org/3.14/library/unittest.mock.html#unittest.mock.Mock.assert_called_with
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: assert_called_with checks that the last call of a mock was made with the given arguments."
---

## Short answer

**Fake: a working but simplified contract implementation (an in-memory dict instead of a database); Stub: a passive object with fixed answers.** Mock records calls for interaction verification.[^py314-library-unittest-mock-quick-guide] For a repository that must behave like real storage, use a Fake: it implements the whole contract, while a Stub returns one fixed answer to any query. An interaction-verifying Mock (`mock.assert_called_with(...)`) fits when the call protocol matters, not the state.[^py314-library-unittest-mock-assert-called-with] <span class="warn">A Fake must pass the same interface tests as the real implementation, or mismatches go unnoticed.</span>

## Detailed explanation

Test doubles serve different purposes, and the choice depends on what the test checks. A Fake has a working but simplified implementation of the contract: for a repository, an in-memory dict where `save` really stores, `get` returns what was stored, and `delete` removes it. A test with a Fake checks the state after operations, so the simplification has to be correct for the whole contract, not for one scenario.

A Stub has no state: it returns prepared answers whatever the arguments. A Mock is configured in the same way (through `return_value`), but it also records how it was used: `unittest.mock.Mock` keeps details of its calls.[^py314-library-unittest-mock-quick-guide] A test can check them with `assert_called_with`.[^py314-library-unittest-mock-assert-called-with] That is why a Stub and a Mock can look identical in code; the difference lies in what the test checks.

For a repository that must behave like real storage, the choice is a Fake: the test checks the result (for example, `find` after `save`) and does not break when the internal implementation changes. A Stub is risky here, because it silently returns the same answer for any query. An interaction-verifying Mock fits when the protocol matters, for example that a message was sent exactly once, not the state of the storage.

Example: a Fake stores and returns real data, while a Stub gives one answer to any query.

```python
from unittest import mock

class InMemoryUserRepo:  # Fake: a working, simplified implementation
    def __init__(self):
        self._users = {}

    def save(self, user):
        self._users[user["id"]] = user

    def get(self, user_id):
        return self._users.get(user_id)

    def delete(self, user_id):
        self._users.pop(user_id, None)

    def find(self, name):
        return [u for u in self._users.values() if u["name"] == name]

user = {"id": 1, "name": "alice"}

fake = InMemoryUserRepo()
fake.save(user)
print(fake.find("alice"))  # [{'id': 1, 'name': 'alice'}]
print(fake.find("bob"))    # []

stub = mock.Mock()         # Stub: one fixed answer, whatever the query
stub.find.return_value = [user]
print(stub.find("bob"))    # [{'id': 1, 'name': 'alice'}]: the query is ignored
```

To keep a Fake from drifting away from the real storage, run the same contract tests against both the Fake and the real implementation, for example against SQLite. Then a behaviour mismatch shows up in the tests, not in production.

**Common mistakes:**
- a Fake that implements only part of the contract (for example, `find` without a filter), so tests pass on wrong behaviour;
- a Stub where the test reads back what was saved: it remembers nothing, so the mismatch stays hidden;
- checking `save` with `assert_called_with` where the stored result matters: such a test breaks on a refactoring that does not change behaviour.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
