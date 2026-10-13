---
id: py-testing-0003
title: "How do you balance unit, integration, and end-to-end tests for feedback speed, fidelity, and maintenance cost?"
description: "How do you balance unit, integration, and end-to-end tests for feedback speed, fidelity, and maintenance cost?"
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
  - source_id: martinfowler-integration-test
    title: "Martin Fowler: Integration Test"
    url: https://martinfowler.com/bliki/IntegrationTest.html
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Essay by Martin Fowler (not official documentation): definition of integration tests, narrow and broad variants, contract tests for checking doubles."
  - source_id: martinfowler-test-pyramid
    title: "Martin Fowler: Test Pyramid"
    url: https://martinfowler.com/bliki/TestPyramid.html
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Essay by Martin Fowler (not official documentation): the test pyramid as a trade-off, broad-stack tests as slow, expensive and brittle, the limits of that assumption."
  - source_id: martinfowler-practical-test-pyramid
    title: "The Practical Test Pyramid (martinfowler.com, Ham Vocke)"
    url: https://martinfowler.com/articles/practical-test-pyramid.html
    accessed: 2026-10-13
    kind: book
    version: null
    applicability: "Article by Ham Vocke on martinfowler.com (not official documentation): pipeline stages by speed and scope, end-to-end scenarios, high maintenance cost and flaky tests."
---

## Short answer

**Keep most tests as fast unit tests, fewer integration tests, and the fewest end-to-end tests, because the higher the level, the slower and more brittle the test.**[^martinfowler-test-pyramid] Unit tests give faster feedback and cheaper upkeep, while Fowler regards end-to-end tests as costly to maintain and prone to non-determinism.[^martinfowler-test-pyramid][^martinfowler-practical-test-pyramid] <span class="warn">An inverted pyramid, with many end-to-end and few unit tests, slows CI and increases flaky tests.</span>[^martinfowler-test-pyramid][^martinfowler-practical-test-pyramid]

## Detailed explanation

Three criteria pull in different directions: feedback speed (how quickly a failure becomes visible), fidelity (how closely a test resembles the real system at work) and maintenance cost (what it costs to write and keep a test). The test pyramid is a heuristic that explains this trade-off: there should be many more low-level tests than broad UI tests, because broad tests are slow, expensive and brittle.[^martinfowler-test-pyramid]

The pyramid is not a fixed proportion. Its assumption is that broad tests are slow, expensive and brittle. Fowler explicitly notes that if high-level tests are fast, reliable and cheap to change, lower-level tests may not be needed.[^martinfowler-test-pyramid] There is also an opposite view: some writers prefer more integration tests and fewer unit tests, but according to Fowler the difference is probably illusory, caused by different definitions of "unit test".[^martinfowler-test-pyramid]

Each level has its own role. Unit tests check branch logic and boundary values, and can run often, on every commit. Integration tests check seams with databases, networks or other services, where doubles may not match reality.[^martinfowler-integration-test] Ham Vocke suggests keeping end-to-end tests to a few key user journeys, for example searching for a product, adding it to the basket and checking out.[^martinfowler-practical-test-pyramid]

The practical criterion is speed and scope, not the test type. Vocke writes that pipeline stages are defined by speed and scope, so fast, narrow integration tests can sit in the same stage as unit tests.[^martinfowler-practical-test-pyramid] When a high-level test finds a bug, it is worth first reproducing the bug with a unit test: the bug then stays under control at the lower level.[^martinfowler-test-pyramid]

**Common mistakes:**
- building the pyramid by test count rather than by run time and by how quickly a test shows the failure;
- covering logic with end-to-end tests: this is slow, and a failure shows up only as a broken scenario without a cause;
- treating any proportions as mandatory without measuring pipeline time and the share of flaky tests;
- writing no integration tests at all and relying on doubles that nobody has checked.

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
