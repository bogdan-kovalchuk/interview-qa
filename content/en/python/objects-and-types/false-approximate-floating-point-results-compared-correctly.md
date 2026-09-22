---
id: py-objtypes-0014
title: "Why can `0.1 + 0.2 == 0.3` be `False`, and how should approximate floating-point results be compared correctly?"
description: "Why can `0.1 + 0.2 == 0.3` be `False`, and how should approximate floating-point results be compared correctly?"
track: python
section: objects-and-types
level: middle
type: pitfall
tags: [0-1-0-2-0-3]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L401-L443
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`0.1 + 0.2 == 0.3` evaluates to `False` because Python's `float` uses IEEE 754 binary64, where decimal fractions like 0.1 and 0.2 have no exact binary representation.**[^py314-reference-datamodel] The expression `0.1 + 0.2` produces `0.30000000000000004`. For correct comparisons, use `math.isclose(a, b, rel_tol=1e-9, abs_tol=0.0)`, which tests whether `abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)`. <span class="warn">When comparing against zero, always specify `abs_tol > 0`, otherwise `rel_tol` alone cannot match.</span>

## Detailed explanation

The inequality `0.1 + 0.2 == 0.3` stems from the fact that hardware floating-point numbers conforming to IEEE 754 binary64 represent numbers in base 2, where fractions like $1/10$ and $2/10$ become infinitely recurring binary decimals.[^py314-library-stdtypes] Because the significand is limited to 53 bits (roughly 15–17 decimal digits of precision), the value is rounded to the nearest representable binary float. The literal `0.1` is stored as `0.10000000000000000555...`, and `0.2` as `0.20000000000000001110...`. Their sum evaluates to `0.30000000000000004440...`, whereas `0.3` rounds to `0.29999999999999998889...`. Because `==` performs strict bitwise equality, the comparison yields `False`.

Floating-point results should never be compared using the `==` operator. The standard library provides `math.isclose(a, b, rel_tol=1e-09, abs_tol=0.0)`, which verifies whether the difference between numbers falls within an acceptable relative (`rel_tol`) or absolute (`abs_tol`) tolerance. Relative tolerance automatically scales with the magnitude of the inputs, allowing both large and small values to be evaluated accurately without manual epsilon calculation.

Comparing values against zero represents a subtle pitfall. The `math.isclose` algorithm evaluates `abs(a - b) <= max(rel_tol * max(abs(a), abs(b)), abs_tol)`. When either operand is `0.0`, the relative term reduces to `rel_tol * abs(a)`, which mathematically cannot satisfy the condition for any standard `rel_tol < 1.0`.[^py314-reference-datamodel] For comparisons involving zero or values very close to zero, setting a non-zero `abs_tol` is mandatory.

An example showing approximate comparison and the zero-threshold pitfall:

```python
import math

a = 0.1 + 0.2
b = 0.3

print(a == b)         # False (exact bitwise inequality)
print(f"{a:.17f}")    # 0.30000000000000004
print(f"{b:.17f}")    # 0.29999999999999999

# Correct comparison with relative tolerance
print(math.isclose(a, b))  # True (rel_tol=1e-09 by default)

# Near-zero comparison pitfall: rel_tol alone always fails against 0.0
diff = 1e-11
print(math.isclose(diff, 0.0))                 # False (rel_tol * diff < diff)
print(math.isclose(diff, 0.0, abs_tol=1e-9))   # True (abs_tol handles zero bounds)
```

**Common mistakes and recommendations:**
- using strict `==` or `!=`: never apply exact equality operators to `float` variables after arithmetic operations;
- neglecting `abs_tol` near zero: calling `math.isclose(val, 0.0)` without setting `abs_tol` always evaluates to `False` for any non-zero value;
- relying on `round()` for comparisons: expressions like `round(a, 2) == round(b, 2)` are vulnerable to boundary rounding artifacts;
- financial domain modeling: for monetary or accounting calculations, adopt the `decimal` module to prevent binary representation discrepancies.

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
