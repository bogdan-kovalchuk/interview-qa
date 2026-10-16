---
id: py-testing-0016
title: "When does property-based testing with generated examples and shrinking find edge cases better than hand-picked examples alone?"
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
  - source_id: hypothesis-api-reference
    title: "Hypothesis 6.169.0: API reference"
    url: https://hypothesis.readthedocs.io/en/latest/reference/api.html
  - source_id: hypothesis-tutorial-introduction
    title: "Hypothesis 6.169.0: Introduction to Hypothesis"
    url: https://hypothesis.readthedocs.io/en/latest/tutorial/introduction.html
---

## Short answer

**Hypothesis generates many input examples for a property (100 by default) and shrinks a failing case to a minimal one.**[^hypothesis-api-reference] This helps where the input space is large and the property is easy to state. On CPython 3.14, for the property `split_fields(join_fields(fields)) == fields`, Hypothesis finds `['']`, which is absent from hand-picked examples such as `['a', 'b']`.

## Detailed explanation

Hand-picked examples check only the inputs their author thought of. Property-based testing changes the approach: you describe a property that must hold for any input from a given strategy, and the library generates the inputs itself. In Hypothesis this is `@given` with a strategy; by default a test runs on 100 examples (`settings.max_examples`).[^hypothesis-api-reference] Generation is random, so finding a failure is likely but not guaranteed in every run.[^hypothesis-tutorial-introduction] The advantage is greatest where the input space is large and edge cases are not obvious: an author rarely guesses all of them.

An example. The pair `join_fields` and `split_fields` should return the same list. The author added a guard for an empty string, and this guard broke one case. The hand-picked test passes, while the property fails:

```python
from hypothesis import given, strategies as st


def join_fields(fields: list[str]) -> str:
    return ",".join(fields)


def split_fields(line: str) -> list[str]:
    return line.split(",") if line else []   # BUG: [""] joins to "" and comes back as []


def test_hand_picked_example() -> None:
    assert split_fields(join_fields(["a", "b"])) == ["a", "b"]


@given(st.lists(st.text()))
def test_split_inverts_join(fields: list[str]) -> None:
    assert split_fields(join_fields(fields)) == fields
```

Hypothesis reduces the failure to a minimal input: `fields=['']`. One empty string becomes an empty list. Shrinking matters because the developer sees the simplest input that breaks the property, not a large random list.[^hypothesis-api-reference] To keep this case, put `@example([''])` above the test: explicit examples run in a separate phase, do not count towards `max_examples`, and do not shrink.[^hypothesis-api-reference]

Property-based testing does not replace examples from the requirements. It needs a property that can be written down. If the correct result is known only for a specific input, for example exact numbers from business rules or an expected error text, a hand-picked example is more honest and easier to read. A weak property, such as `len(result) >= 0`, passes for any code that returns a list. A property that repeats the implementation only checks that the code agrees with itself.

**Common mistakes:**
- assuming property-based testing always finds every edge case: random generation gives a probability, not a guarantee;
- writing a property that copies the implementation instead of an independent invariant;
- leaving a weak property such as `len(result) >= 0` and believing it checks something.
