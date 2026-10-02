---
id: py-prac-0012
title: "Implement top-3 words for ASCII text: a token matches `[A-Za-z]+`, comparison is case-insensitive, and ties are sorted lexicographically."
description: "Count lowercase regex matches and sort by (-count, word)."
track: python
section: practical-coding
level: middle
type: coding
tags: [a-za-z]
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
- source_id: py313-counter
  title: 'Python 3.13: Counter and most_common ordering'
  url: https://docs.python.org/3.13/library/collections.html#collections.Counter
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-regex
  title: 'Python 3.13: Regular expression iteration'
  url: https://docs.python.org/3.13/library/re.html#re.finditer
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-sorting
  title: 'Python 3.13: Sorting techniques'
  url: https://docs.python.org/3.13/howto/sorting.html
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
---

## Task

Implement `top3_words(text)`: extract tokens matching `[A-Za-z]+`, lowercase them and return up to three distinct words by descending frequency, breaking ties lexicographically.

## Constraints

- Input is an ASCII str.
- Digits, punctuation and apostrophes separate tokens.
- Return fewer than three words when necessary; no tokens means an empty list.

## Short answer

**Count lowercase regex matches and sort by `(-count, word)`.** Take the first three entries. `Counter.most_common()` resolves ties by first encounter, so it does not implement this lexicographic contract.

## Detailed explanation

The regex defines the words, so an apostrophe splits a token. A compound sorting key makes both ordering rules explicit and independent of encounter order. [^py313-counter] [^py313-regex] [^py313-sorting]

## Examples

```python
assert top3_words("b a B") == ["b", "a"]
```

## Solution

```python
import re
from collections import Counter

def top3_words(text):
    counts = Counter(match.group().lower()
                     for match in re.finditer(r"[A-Za-z]+", text))
    return sorted(counts, key=lambda word: (-counts[word], word))[:3]
```

## Complexity

For text length L and u distinct words, token scanning processes O(L) characters and sorting uses O(u log u) comparisons. String comparison may inspect multiple characters; storage includes the distinct word text and counts. [^py313-counter] [^py313-regex] [^py313-sorting]

## Edge cases

Test no words, fewer than three words, mixed case, punctuation, and ties whose encounter order differs from alphabetic order.

## Tests

Run after the Solution block with pytest installed.

```python
import pytest

assert top3_words("") == []
assert top3_words("123 !!!") == []
assert top3_words("Z z a A b B") == ["a", "b", "z"]
assert top3_words("cat cat dog") == ["cat", "dog"]
assert top3_words("Hello world hello World foo bar foo bar baz") == ["bar", "foo", "hello"]
assert top3_words("can't can't") == ["can", "t"]
```

## Evaluation guide

### Expected signals

A frequency-only sort or most_common is insufficient. Follow the exact token grammar.

### Red flags

The implementation misses a stated boundary case or its complexity claim omits allocated data.

### Level-up follow-up

How would you avoid sorting every distinct word?

## Sources

<!-- generated from frontmatter -->
