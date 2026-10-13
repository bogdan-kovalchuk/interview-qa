---
id: py-testing-0018
title: "How do you tell a flaky test apart from a genuine product race, and how do you preserve evidence to reproduce it?"
description: "A flaky test is a nondeterministic test that fails without code changes; a product race is a real concurrency bug in the application. Isolated repeated runs and kept evidence tell them apart."
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
  - source_id: pytest-usage-node-ids
    title: "pytest documentation: Specifying which tests to run"
    url: https://docs.pytest.org/en/stable/how-to/usage.html#specifying-which-tests-to-run
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "Official pytest documentation: running a single test by node id in the form file::function."
  - source_id: pytest-output-junitxml
    title: "pytest documentation: Creating JUnitXML format files"
    url: https://docs.pytest.org/en/stable/how-to/output.html#creating-junitxml-format-files
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "Official pytest documentation: writing a JUnit XML report with --junit-xml."
  - source_id: pytest-logging
    title: "pytest documentation: How to manage logging"
    url: https://docs.pytest.org/en/stable/how-to/logging.html#how-to-manage-logging
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "Official pytest documentation: captured logs shown for failed tests; by default records of level WARNING and above."
---

## Short answer

**A flaky test is a nondeterministic test (time, order, shared state, `random`); a product race is a real race condition in the application.** Run the test alone by its node id, for example `tests/test_mod.py::test_func`.[^pytest-usage-node-ids] Repeated runs then separate the causes: failing only in the full set usually means shared state or order dependence; failing alone means test nondeterminism, a product race or a plain deterministic bug. To reproduce it, keep the command, the seed, the `--junit-xml` report and the logs.[^pytest-output-junitxml][^pytest-logging]

## Detailed explanation

Both phenomena look the same in CI: a red test that is green the next time. What tells them apart is the source of the nondeterminism. A flaky test is a problem in the test itself: it depends on real time, `random` without a seed, the network, the order of execution, or shared global state. A product race is a problem in the application: two threads or tasks change shared data without synchronization, and the result depends on how they interleave. The failure rate does not distinguish them, because both can fail rarely.

The most common confusion is a test that depends on order because of shared state. Here is a module with a global registry and two tests, which pytest runs in file order:

```python
_handlers: dict[str, object] = {}       # module-level state shared by all tests


def register(name: str, handler: object) -> None:
    _handlers[name] = handler


def handler_count() -> int:
    return len(_handlers)


def test_register_adds_handler() -> None:
    register("email", print)
    assert handler_count() == 1         # passes only if no earlier test registered a handler


def test_register_sms() -> None:
    register("sms", print)
    assert handler_count() == 1         # fails after test_register_adds_handler in file order
```

Running `test_register_sms` alone passes, while the whole file fails at that test. This is not a race: in a fixed order the failure is deterministic. But the same defect looks flaky when the order changes between runs, so the isolated run is the first step of diagnosis.

Diagnosis starts with repeated isolated runs, for example in a shell loop: `for i in $(seq 50); do pytest 'tests/test_mod.py::test_func' -q || break; done`. If the test fails in isolation too, first check the nondeterminism in the test itself: time, `random` without a seed, the network, timeouts. Only after that look for a race in the product. It is reproduced not by a `sleep` in the test but by forcing an interleaving: many threads or tasks at once, and an artificial delay at the point of shared access. If the test fails only within the set, look for shared state: global variables, fixtures with a wider scope, side effects that are not cleaned up.

To reproduce a failure later, keep the command with the node id, the seed of any random source, a `--junit-xml` report[^pytest-output-junitxml] and the failure logs. By default pytest shows, for a failed test, only records of level WARNING and above; INFO has to be enabled explicitly, for example with `--log-level=INFO`.[^pytest-logging] Without this the test can only be re-run, and the cause will not be found.

**Common mistakes:**
- adding `time.sleep()` to a test to make it "stable" instead of fixing the synchronization in the product;
- declaring a test flaky without checking whether it fails in isolation and whether shared state is involved;
- re-running a test until it is green without keeping evidence: the failure disappears and the cause remains.

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
