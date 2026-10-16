---
id: py-testing-0019
title: "What does a surviving mutant after an artificial change to the code's behaviour mean, and how does that reveal weak assertions or missing cases?"
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
  - source_id: mutmut-docs-workflow
    title: "mutmut documentation: Workflow"
    url: https://mutmut.readthedocs.io/en/latest/#workflow
  - source_id: mutmut-docs-type-checker
    title: "mutmut documentation: Filter generated mutants with type checker"
    url: https://mutmut.readthedocs.io/en/latest/#filter-generated-mutants-with-type-checker
---

## Short answer

**A surviving mutant is an artificial change to the code (a mutant, for example `>=` replaced by `>`) after which no test fails.** If the tests do not notice such a change, an assertion or a boundary case, such as `age == 18`, is usually missing. Not every survivor is a gap, because a mutant may not change the behaviour. `mutmut browse` shows the mutants, and for a chosen one you write a test that should kill it.[^mutmut-docs-workflow]

## Detailed explanation

Mutation testing checks not whether a line ran, but whether the tests notice a change in behaviour. The tool creates a mutant: a copy of the code with one small change (an operator, a literal, a condition) that is still valid Python. A mutant is **killed** if at least one test fails, and **surviving** if no test fails. A surviving mutant shows that the set of tests does not tell the changed behaviour apart from the original.

Take the function `is_adult`, where the mutant replaces `>=` with `>`. A weak test checks only `30` and `5`: the original and the mutant give the same results for these values, so the mutant survives even though the changed line runs. Adding the boundary case `18` kills the mutant. The example runs both checks:

```python
def is_adult(age):
    return age >= 18          # original code

def is_adult_mutant(age):
    return age > 18           # mutant: '>=' replaced by '>'

def weak_test(fn):
    assert fn(30) is True
    assert fn(5) is False

def stronger_test(fn):
    weak_test(fn)
    assert fn(18) is True     # boundary case

def survives(test, fn):
    try:
        test(fn)
    except AssertionError:
        return False          # a test failed: the mutant is killed
    return True               # no test failed: the mutant survives

print(survives(weak_test, is_adult_mutant))      # True: the mutant survives
print(survives(stronger_test, is_adult_mutant))  # False: the mutant is killed
```

This difference is the same one that separates coverage from verification: a line that runs does not mean that its behaviour is checked. Mutmut describes a similar case, where a type checker could reject the change (for example, `x: str = 'foo'` to `x: str = None`): if the tests do not detect it, the value of `x` is not properly tested.[^mutmut-docs-type-checker] So a survivor is a reason to inspect a specific case and decide what is missing: an assertion, a boundary value, or a test altogether.

Not every survivor is a gap. A change may not affect the result for any input (for example, `x + 0` instead of `x`); such a mutant cannot be killed, so it should be marked rather than covered by a test written at random. In the mutmut workflow, the mutants are reviewed with `mutmut browse`, a test is written for the chosen mutant to try to kill it, and the mutant is rerun.[^mutmut-docs-workflow]

**Common mistakes:**
- treating 100% line coverage as proof that the tests check behaviour;
- adding tests that only call the code without checking the result or boundary values;
- writing a test for every survivor without checking whether it is equivalent to the original.
