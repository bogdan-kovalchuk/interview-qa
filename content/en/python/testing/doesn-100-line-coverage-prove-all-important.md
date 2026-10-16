---
id: py-testing-0017
title: "Why doesn't 100% line coverage prove that all important behaviours and assertions have been checked?"
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
  - source_id: coverage-branch
    title: "Coverage.py 7.16.2: Branch coverage measurement"
    url: https://coverage.readthedocs.io/en/latest/branch.html#branch-coverage-measurement
---

## Short answer

**Line coverage shows only which lines ran.**[^coverage-branch] It does not say whether the correct behaviour is checked: a test without assertions or with `assert True` can execute every line of the function and report 100% line coverage, and a bug then goes unnoticed. Branch coverage shows whether both branches of each `if` were taken,[^coverage-branch] and mutation testing checks whether the tests catch deliberately introduced changes to the code.[^mutmut-docs]

## Detailed explanation

Coverage measures execution, not verification. Line (statement) coverage records which lines ran during the tests, and nothing more. A test that only calls the function executes the same lines as a test with a correct `assert`, so coverage cannot tell them apart.

The function with a conditional discount, file `billing.py`:

```python
def apply_discount(price, is_member):
    if is_member:
        price = price * 0.9
    return price
```

And two tests, file `test_billing.py`. The first only calls the function, the second checks the result:

```python
from billing import apply_discount


def test_runs_without_checking() -> None:
    apply_discount(100, True)           # executes every line, checks nothing


def test_member_price() -> None:
    assert apply_discount(100, True) == 90
```

If only the first runs, `billing.py` gets 100% line coverage, although no result is checked. The complete set still has a gap. A branch is a possible jump between lines. `if is_member:` has two jumps: into line 3, and past the body to line 4. Both tests call the function with `is_member=True`, so the jump past the body never runs. Line coverage does not see this, because every line still executes. `coverage run --branch` marks this `if` as partially covered (`2->4`) and that lowers the coverage percentage.[^coverage-branch]

Mutation testing checks something else: it introduces a deliberate change (a mutant) and checks whether a test fails. A mutant that no test catches "survives". If `0.9` becomes `0.8`, the test without an assertion lets it pass, while `assert ... == 90` catches it. A mutant that removes `if is_member:` and gives everyone the discount survives this set of tests: no test calls the branch without the discount, and branch coverage shows the same gap.[^mutmut-docs]

Coverage does not know what the correct result is, so 100% does not prove correctness. A practical order: first assertions on the result and side effects, then branch coverage for critical `if` statements, and only then mutation testing for important modules.

**Common mistakes:**
- treating 100% line coverage as proof that all branches and behaviour are checked;
- writing tests without assertions "for coverage";
- not noticing that an `if` without `else` needs a test with both values of the condition.
