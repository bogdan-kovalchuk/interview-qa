---
id: py-prac-0006
title: "Implement FizzBuzz for integers 1..N with ordered rules `[(3, \"Fizz\"), (5, \"Buzz\")]`, so that a new rule never requires a new branch."
description: "Store rules as data and join the labels whose divisors divide each number."
track: python
section: practical-coding
level: middle
type: coding
tags: [3-fizz-5-buzz]
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  uk: 3
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.13.15"
  flags: []
anki:
  export: true
sources:
- source_id: py313-types
  title: 'Python 3.13: Built-in types'
  url: https://docs.python.org/3.13/library/stdtypes.html
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-expressions
  title: 'Python 3.13: Expressions: arithmetic operations'
  url: https://docs.python.org/3.13/reference/expressions.html#binary-arithmetic-operations
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
---

## Task

Implement `fizzbuzz(n, rules=None)` returning strings for integers 1 through n. Concatenate all matching labels in rule order; use the number when no rule matches.

## Constraints

- n is a non-negative int, excluding bool.
- Rules are a finite iterable of positive integer divisors and non-empty string labels.
- Invalid types raise TypeError; invalid values raise ValueError.
- An empty rule set is allowed.

## Short answer

**Store rules as data and join the labels whose divisors divide each number.** Preserve rule order and use `str(i)` when nothing matches. Validate the configuration before generating results.

## Detailed explanation

Modulo selects matching rules; joining their labels handles combined matches without another branch. Materializing rules once also supports one-shot iterables. The empty-string fallback is unambiguous because labels cannot be empty. [^py313-types] [^py313-expressions]

## Examples

```python
assert fizzbuzz(3) == ["1", "2", "Fizz"]
```

## Solution

```python
def fizzbuzz(n, rules=None):
    if type(n) is not int:
        raise TypeError("n must be int")
    if n < 0:
        raise ValueError("n must be non-negative")
    rules = tuple([(3, "Fizz"), (5, "Buzz")] if rules is None else rules)
    for divisor, label in rules:
        if type(divisor) is not int or not isinstance(label, str):
            raise TypeError("invalid rule type")
        if divisor <= 0 or not label:
            raise ValueError("invalid rule value")
    return ["".join(label for d, label in rules if i % d == 0) or str(i)
            for i in range(1, n + 1)]
```

## Complexity

For n numbers and r rules, there are O(n*r) divisibility checks. Time also includes writing the output characters; storage is O(r) plus the returned strings. This assumes unit-cost integer arithmetic. [^py313-types] [^py313-expressions]

## Edge cases

Test n=0, no rules, simultaneous matches, rule order, one-shot rules and invalid divisors.

## Tests

Run after the Solution block with pytest installed.

```python
import pytest

assert fizzbuzz(5) == ["1", "2", "Fizz", "4", "Buzz"]
assert fizzbuzz(15)[-1] == "FizzBuzz"
assert fizzbuzz(0) == []
assert fizzbuzz(3, []) == ["1", "2", "3"]
assert fizzbuzz(6, iter([(3, "A"), (2, "B")]))[-1] == "AB"
for rules in ([(0, "A")], [(-1, "A")], [(2, "")]):
    with pytest.raises(ValueError):
        fizzbuzz(1, rules)
with pytest.raises(TypeError):
    fizzbuzz(True)
with pytest.raises(ValueError):
    fizzbuzz(-1)
```

## Evaluation guide

### Expected signals

Adding a rule must require only another data item. Reject zero divisors before any modulo operation.

### Red flags

The implementation misses a stated boundary case or its complexity claim omits allocated data.

### Level-up follow-up

How would you stream results instead of collecting the output?

## Sources

<!-- generated from frontmatter -->
