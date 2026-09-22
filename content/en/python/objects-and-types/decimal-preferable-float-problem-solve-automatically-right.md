---
id: py-objtypes-0015
title: "When is `Decimal` preferable to `float`, and what problem does it not solve automatically without the right precision and rounding policy?"
description: "When is `Decimal` preferable to `float`, and what problem does it not solve automatically without the right precision and rounding policy?"
track: python
section: objects-and-types
level: middle
type: comparison
tags: [decimal, float]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L444-L497
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`Decimal` is preferable when exact base-10 representation is required: financial calculations, monetary values, and preserving significant trailing zeros (`1.30 + 1.20 = 2.50`).**[^py314-reference-datamodel] It eliminates binary floating-point representation errors (`Decimal('0.1') + Decimal('0.2') == Decimal('0.3')` is strictly `True`), but it does not automatically solve round-off errors with insufficient precision: the arithmetic context (`decimal.getcontext()`) defaults to 28 digits of precision, and whenever an operation exceeds that limit, rounding occurs according to the active rounding policy.

## Detailed explanation

The `Decimal` type from the `decimal` module implements fixed-point and floating-point arithmetic based on the IEEE 854/754-2008 standard, eliminating binary representation errors inherent to `float`.[^py314-library-stdtypes] Unlike `float`, which stores numbers in base 2, `Decimal` operates directly in base 10. This precision is essential in financial and accounting domains where values such as `0.10` or `0.05` must be exact, and where regulatory standards require preserving significant trailing zeros (for example, currency amounts requiring explicit cents or pence).

However, adopting `Decimal` does not automatically eliminate round-off errors. Fractions that cannot be represented finitely in base 10 (such as $1/3 = 0.3333...$) still cannot be stored without truncation in a finite number of digits. Arithmetic is evaluated within an active arithmetic context (`decimal.getcontext()`), which defines overall precision (`prec=28` by default) and rounding behaviour (such as `ROUND_HALF_EVEN`). When an operation yields more digits than `prec` allows, trailing digits are rounded according to the context policy, meaning `(Decimal(1) / Decimal(3)) * Decimal(3)` results in `0.999999...` rather than exactly `1`.

Furthermore, a common mistake is instantiating `Decimal` from a `float`: calling `Decimal(0.1)` copies the inaccurate binary floating-point approximation into the decimal object, forfeiting its advantages.[^py314-reference-datamodel] Instances should always be created from strings, integers, or tuples, using `Decimal.from_float()` only when explicitly converting an existing binary float.

An example showing string initialization, repeating decimal truncation, and explicit quantization:

```python
from decimal import Decimal, getcontext, ROUND_HALF_UP

# 1. Exact string initialization vs float conversion pitfall
d1 = Decimal("0.1")
d2 = Decimal("0.2")
print(d1 + d2 == Decimal("0.3"))  # True

d_float = Decimal(0.1)  # Pitfall: imports binary float inaccuracy
print(f"{d_float:.25s}")  # 0.1000000000000000055511...

# 2. Precision limit on non-terminating decimals (1/3 in base 10)
getcontext().prec = 6
third = Decimal(1) / Decimal(3)
print(third)                 # 0.333333 (truncated to prec=6)
print(third * Decimal(3))    # 0.999999 (round-off error still occurs)

# 3. Explicit monetary rounding via quantize
price = Decimal("19.995")
final_price = price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(final_price)           # 20.00
```

**Practical recommendations and pitfalls:**
- always initialize from strings: write `Decimal('0.1')` instead of `Decimal(0.1)`;
- manage arithmetic context: adjust `getcontext().prec` for high-precision workflows or use `decimal.localcontext()` for isolated blocks;
- enforce rounding explicitly: use `.quantize()` to round domain results to specific decimal places using rules like `ROUND_HALF_UP` or `ROUND_HALF_EVEN`;
- performance trade-offs: `Decimal` arithmetic is noticeably slower than hardware-accelerated `float` operations and requires more memory.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
