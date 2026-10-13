---
id: py-testing-0001
title: "What boundary does a unit test have, and why shouldn't it quietly turn into an integration test?"
description: "What boundary does a unit test have, and why shouldn't it quietly turn into an integration test?"
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
  - source_id: martinfowler-integration-test
    title: "Martin Fowler: Integration Test"
    url: https://martinfowler.com/bliki/IntegrationTest.html
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Essay by Martin Fowler (not official documentation): definition of integration tests, narrow and broad variants, solitary and sociable unit tests, contract tests."
  - source_id: martinfowler-test-pyramid
    title: "Martin Fowler: Test Pyramid"
    url: https://martinfowler.com/bliki/TestPyramid.html
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Essay by Martin Fowler (not official documentation): the test pyramid, broad-stack tests as slow, expensive and brittle, the limits of that assumption."
---

## Short answer

**A solitary unit test replaces its collaborators with test doubles and checks only the unit under test.**[^martinfowler-integration-test] A sociable unit test with real collaborators in the same process is still a unit test in Fowler's terms.[^martinfowler-integration-test] <span class="warn">When a test uses real external services, such as a database or a network, it becomes an integration test, and quietly replacing doubles with such services changes what the test means.</span>[^martinfowler-integration-test]

## Detailed explanation

The boundary of a unit test is the unit it checks: a function, method or class. Fowler calls a solitary unit test one in which all other program elements are replaced with test doubles, and a sociable unit test one in which real collaborators work together. He counts both as unit tests and distinguishes them by the adjective: solitary or sociable.[^martinfowler-integration-test] To replace collaborators, `unittest.mock` is the usual tool: it replaces parts of the system under test with mock objects and lets you check how they were called.[^py314-library-unittest-mock]

A test becomes an integration test when real external services take part in it: a database, a network, or the files of another system. Fowler distinguishes narrow integration tests, which use test doubles of such services, and broad ones, which need live versions of them and a suitable environment.[^martinfowler-integration-test] The term has blurred: some writers use integration test for sociable unit tests too, so the name alone does not tell you which kind a test is. The shift goes unnoticed when a real service is substituted for a double: the test stays green while the service works, and turns red for reasons unrelated to the logic of the unit.

The function below reads the clock directly. Without a replacement, the test checks the current time rather than the function, so its expected value cannot be set. When `time.time` is replaced with a test double, the test checks only the function and always gives the same result.

```python
import time
import unittest
from unittest import mock


def seconds_left(deadline: float) -> float:
    # Depends on the real clock, so the result changes on every run.
    return deadline - time.time()


class SecondsLeftUnitTest(unittest.TestCase):
    def test_returns_remaining_time(self):
        # The clock is a test double, so the unit under test is the only real code.
        with mock.patch("time.time", return_value=100.0):
            self.assertEqual(seconds_left(160.0), 60.0)


if __name__ == "__main__":
    unittest.main()
```

The practical conclusion: state the boundary explicitly – solitary or sociable, and which collaborators are replaced. Doubles belong where the test reaches the outside world (network, database, files), and the interaction with a real service is checked by a separate integration test with an explicit name. A unit test then usually remains faster than a broad one.[^martinfowler-test-pyramid]

**Common mistakes:**
- calling a test a unit test because it sits in a unit folder, even though it starts a real database or HTTP server;
- replacing some dependencies but not the network or files, so the test quietly becomes an integration test;
- checking only mock calls and not the module's behaviour: the test passes although the module is broken with a real dependency.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
