---
id: py-prac-0022
title: "For `is_prime(n)`, which checks divisors up to `int(sqrt(n))`, write tests that kill the mutants `<` vs `<=` at the square boundary and the bug for `n < 2`."
track: python
section: practical-coding
sources:
  - source_id: py314-tutorial-controlflow-the-range-function
    title: "Python 3.14: Tutorial/control flow, The range() Function"
    url: https://docs.python.org/3.14/tutorial/controlflow.html#the-range-function
  - source_id: py314-library-math-math-nan
    title: "Python 3.14: Library/math, math.nan"
    url: https://docs.python.org/3.14/library/math.html#math.nan
  - source_id: py314-library-math-math-isqrt
    title: "Python 3.14: Library/math, math.isqrt"
    url: https://docs.python.org/3.14/library/math.html#math.isqrt
---

## Short answer

**Three test groups: the base case `n < 2`, a perfect square (kills the `<` vs `<=` mutant), and ordinary prime and composite numbers.** For the mutant on `is_prime(4)`: `int(sqrt(4)) == 2`; if the bound is exclusive, `range(2, r)` does not include `r`,[^py314-tutorial-controlflow-the-range-function] the range is empty and the mutant returns `True`, while the correct code (`range(2, r + 1)`) finds `4 % 2 == 0` and returns `False`. For `n < 2`: `is_prime(0)`, `is_prime(1)`, `is_prime(-7)` -> `False`. Additionally: `is_prime(9)` -> `False`, `is_prime(2)` -> `True`.

## Detailed explanation

A mutant with `<` instead of `<=` in the loop bound differs from the correct function only when the smallest divisor equals `int(sqrt(n))`. These are the composite numbers `4`, `6`, `8`, `9`, `15`, `25`, `35`, `49` and similar ones; among them are the squares `4`, `9`, `25`, `49`. For `n = 4` the correct function finds the divisor `2`, while the mutant never checks `2` and returns `True`. Prime numbers do not kill the mutant, because both functions return `True` for them:

```python
from math import sqrt


def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(sqrt(n)) + 1):
        if n % d == 0:
            return False
    return True


def is_prime_mutant(n):  # mutant: the inclusive upper bound became exclusive
    if n < 2:
        return False
    for d in range(2, int(sqrt(n))):
        if n % d == 0:
            return False
    return True


print(is_prime(4), is_prime_mutant(4))  # False True: the test on 4 kills the mutant
print(is_prime(6), is_prime_mutant(6))  # False True
print(is_prime(7), is_prime_mutant(7))  # True True: a prime does not kill it
```

The cause is that `range(2, r)` does not include `r`.[^py314-tutorial-controlflow-the-range-function] With `r = 2` the range is empty, so the test on `4` (and on `9`, where `r = 3`) must expose exactly this error.

The `n < 2` branch is needed separately. For `0` and `1` without it, the range is empty and the function returns `True`. For `-7` without a guard, `math.sqrt` raises `ValueError`: CPython raises `ValueError` for invalid operations such as `sqrt(-1.0)`.[^py314-library-math-math-nan] So the test on `-7` checks the guard itself, with the expected `False`. For a reference value in a test, `math.isqrt(n)` can be used: it returns the floor of the exact square root of an integer.[^py314-library-math-math-isqrt]

The test set has three groups: (1) `n < 2`: `0`, `1`, `-7` give `False`; (2) numbers whose smallest divisor is `int(sqrt(n))`, including squares: `4`, `9`, `15`, `25`, `49` give `False`, and the mutant returns `True` for them; (3) ordinary numbers on which the mutant behaves like the correct function: `2` and `97` give `True`, and `91` (its smallest divisor `7` is less than `int(sqrt(91)) = 9`) gives `False`. Each group checks a separate branch: the guard, the loop bound and the main path.

**Common mistakes:**
- testing only ordinary prime and composite numbers: the mutant passes on `7` and `91`;
- not testing `n < 2`: `0` and `1` give `True`, and nobody notices the error;
- not testing negative numbers: without a guard the test fails with `ValueError`, not with a logic error.
