---
id: py-testing-0008
title: "When is parametrization better than copying one test body for several cases?"
description: "When is parametrization better than copying one test body for several cases?"
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
  - source_id: pytest-how-to-parametrize
    title: "pytest documentation: @pytest.mark.parametrize"
    url: https://docs.pytest.org/en/stable/how-to/parametrize.html#pytest-mark-parametrize-parametrizing-test-functions
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "Official pytest documentation, section @pytest.mark.parametrize: the function runs once for each set of values, values are passed without copying, and default IDs are built from the values, for example test_eval[6*9-42]."
  - source_id: pytest-ref-param
    title: "pytest documentation: pytest.param"
    url: https://docs.pytest.org/en/stable/reference/reference.html#pytest.param
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "Official pytest reference, pytest.param: specifies a parameter set for parametrize, with its id and marks."
---

## Short answer

**Parametrization is better when the test logic is identical and only the inputs and the expected result differ.**[^pytest-how-to-parametrize] `@pytest.mark.parametrize` runs one body for each set of values, and `pytest.param(..., id="empty_input")` gives a set a readable ID such as `test_parse[empty_input]`.[^pytest-ref-param] Copying the body duplicates the logic, so changing an assertion means editing every copy. <span class="warn">When the logic differs between cases, separate test functions are usually easier to read, because the shared body starts to fill up with conditions.</span>

## Detailed explanation

`@pytest.mark.parametrize` runs one test body for each set of values. Pytest creates a separate test item for each set, and each one is reported separately.[^pytest-how-to-parametrize] This fits when the logic is identical and only the inputs and the expected result differ: then the check is changed in one place.

Copying the body also gives separate tests, but each copy is a separate function with its own duplicate of the logic. Nothing guarantees that the copies stay in sync, and the function names have to be invented by hand. Parametrize builds IDs from the values or from `pytest.param(..., id=...)`.[^pytest-ref-param] Without an explicit `id`, the ID is made of the values, for example `test_eval[6*9-42]` in the documentation example.[^pytest-how-to-parametrize]

Example: one check function and three sets with readable IDs:

```python
import pytest


def parse_port(text):
    return int(text.strip())


@pytest.mark.parametrize(
    "text, expected",
    [
        pytest.param("8080", 8080, id="typical_port"),
        pytest.param(" 1 ", 1, id="min_port_with_spaces"),
        pytest.param("65535", 65535, id="max_port"),
    ],
)
def test_parse_port(text, expected):
    assert parse_port(text) == expected
```

`pytest -v` shows `test_parse_port[typical_port]`, `test_parse_port[min_port_with_spaces]` and `test_parse_port[max_port]`, so a failure is visible by its case name at once.

Limits: when the sets need different setup, different checks or different mocks, the shared body starts to fill up with `if` statements on the parameters, and separate test functions read better. Parameter values are passed as-is, without copying: if the same mutable object appears in several sets, a change made in one test is visible to the next ones.[^pytest-how-to-parametrize]

**Common mistakes:**
- parametrizing tests with different logic, so the test body fills up with conditions per case;
- keeping default IDs for complex values, so the report does not show which case failed;
- putting the same mutable object into several parametrize sets, which the test changes, and creating a dependency between cases.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
