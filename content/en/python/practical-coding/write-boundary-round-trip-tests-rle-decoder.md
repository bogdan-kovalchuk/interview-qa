---
id: py-prac-0025
title: "Write boundary and round-trip tests for an RLE decoder with the grammar `count:character|count:character`: count is a positive decimal, and a character can never be `:` or `|`; malformed input raises `ValueError`."
description: "Write boundary and round-trip tests for an RLE decoder with the grammar `count:character|count:character`: count is a positive decimal, and a character can never be `:` or `|`; malformed input raises `ValueError`."
track: python
section: practical-coding
level: middle
type: practical
tags: [count-character-count-character, valueerror]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-exceptions-valueerror
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html#ValueError
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: ValueError means an argument with the right type but an inappropriate value."
  - source_id: py314-library-functions-int
    title: "Python 3.14: Library/functions"
    url: https://docs.python.org/3.14/library/functions.html#int
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: int() accepts a string with surrounding whitespace, a sign and single underscores between digits; the values 0-9 can be any Unicode decimal digits."
---

## Short answer

**Boundary: minimal `count=1`, round-trip `decode(encode(s)) == s` for non-empty `s` without `:` or `|`; malformed input must raise `ValueError` (an argument of the right type with an inappropriate value).**[^py314-library-exceptions-valueerror] Valid: `"3:a|2:b|1:c" -> "aaabbc"`; `"1:x" -> "x"`; `"12:a" -> "a" * 12`. Malformed: `""`, `":a"`, `"0:a"`, `"-1:a"`, `" 3:a"`, `"1::"`, `"1:|"`, `"3:a|"`, `"12:ab"`.

## Detailed explanation

Tests for an RLE decoder fall into three groups: boundary, round-trip, and malformed input. The format is `count:character`, with runs separated by `|`. The minimal valid count is 1: `"1:x"` gives `"x"`. A multi-digit count must also work: `"12:a"` gives `"a" * 12`, so the parser cannot read only one digit. A count of `0`, an empty character, and `:` or `|` as the character are all malformed. Under this grammar, malformed input must raise `ValueError`.[^py314-library-exceptions-valueerror]

The subtlest trap is parsing the count. `int()` accepts whitespace around the string, a sign, and single underscores between digits; the values 0–9 can be any Unicode decimal digits.[^py314-library-functions-int] So `int(" 3")` gives 3, `int("1_0")` gives 10, and `int("١")` (the Arabic-Indic digit one, U+0661) gives 1. If the grammar means ASCII digits, check the count separately, for example with the regular expression `[0-9]+`, and only then call `int()`. A naive parser without that check accepts `" 3:a"`, and the test below catches it:

```python
import unittest


def count_of(run):
    # Naive parser: int() also accepts surrounding whitespace, a sign and underscores.
    count_text, _, _ = run.partition(":")
    return int(count_text)


class TestCount(unittest.TestCase):
    def test_count_is_plain_digits(self):
        # count_of(" 3:a") returns 3 instead of raising, so this test fails.
        with self.assertRaises(ValueError):
            count_of(" 3:a")


if __name__ == "__main__":
    unittest.main()
```

The round-trip checks that encode and decode agree: `encode("aabbc")` gives `"2:a|2:b|1:c"`, and decode returns `"aabbc"`. But a round-trip does not prove correctness if encode and decode make the same mistake, so fixed examples such as `"3:a|2:b|1:c" -> "aaabbc"` remain mandatory. An empty string is not part of the round-trip: under this grammar `decode("")` must raise `ValueError`, so encode of an empty `s` must refuse as well. encode also rejects `:` and `|`, because they are the grammar's separators.

**Common mistakes:**
- checking the count with `int()` without a separate check of the characters, so `" 3"` and `"1_0"` are accepted;
- testing only single-digit counts, without `12` and without `0`;
- assuming that the character can be a string longer than one character, for example `"12:ab"`.

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
