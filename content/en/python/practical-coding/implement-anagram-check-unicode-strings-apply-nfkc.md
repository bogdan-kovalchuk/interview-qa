---
id: py-prac-0013
title: "Implement an anagram check for Unicode strings: apply NFKC and `casefold()`, ignore whitespace, and take other code points into account."
description: "Build a Counter of non-whitespace characters after NFKC and casefold."
track: python
section: practical-coding
level: middle
type: coding
tags: [casefold]
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
- source_id: py313-unicode
  title: 'Python 3.13: Unicode normalization'
  url: https://docs.python.org/3.13/library/unicodedata.html#unicodedata.normalize
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-types
  title: 'Python 3.13: Built-in types'
  url: https://docs.python.org/3.13/library/stdtypes.html
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
- source_id: py313-counter
  title: 'Python 3.13: Counter and most_common ordering'
  url: https://docs.python.org/3.13/library/collections.html#collections.Counter
  accessed: '2026-10-04'
  kind: official
  version: '3.13'
  applicability: API semantics and language guarantees used by this solution.
---

## Task

Implement `is_anagram(s1, s2)`: apply NFKC, then casefold, ignore whitespace and compare multiplicities of all remaining code points.

## Constraints

- Both inputs are str.
- Punctuation and accents count; only whitespace is ignored.
- Compare code points rather than grapheme clusters.
- Do not apply additional normalization after casefold.

## Short answer

**Build a Counter of non-whitespace characters after NFKC and casefold.** Equality of Counters checks both characters and multiplicities. Unlike sorting, counting avoids ordering the whole character sequence.

## Detailed explanation

Normalization can compose canonically equivalent sequences and replace compatibility forms. Casefold can expand one character into several; counting must therefore happen after both transformations. Punctuation remains significant. [^py313-unicode] [^py313-types] [^py313-counter]

## Examples

```python
assert is_anagram("Dormitory", "Dirty room")
```

## Solution

```python
import unicodedata
from collections import Counter

def is_anagram(s1, s2):
    def counts(text):
        text = unicodedata.normalize("NFKC", text).casefold()
        return Counter(ch for ch in text if not ch.isspace())
    return counts(s1) == counts(s2)
```

## Complexity

Counting and comparison use expected O(m+n) operations for transformed lengths m and n. Storage includes the transformed strings and distinct-character counters; transformation costs are additional. [^py313-unicode] [^py313-types] [^py313-counter]

## Edge cases

Test canonical equivalence, fullwidth letters, casefold expansion, Unicode whitespace, unequal multiplicities and punctuation.

## Tests

Run after the Solution block with pytest installed.

```python
import pytest

assert is_anagram("Listen", "Silent")
assert is_anagram("é", "é")
assert is_anagram("Ａ b", "ba")
assert is_anagram("Straße", "strasse")
assert is_anagram("a b", "ba")
assert is_anagram("", " 	")
assert not is_anagram("aab", "abb")
assert not is_anagram("ab!", "ba")
```

## Evaluation guide

### Expected signals

Do not replace the Counter with a set, which loses multiplicity. Ignore whitespace only.

### Red flags

The implementation misses a stated boundary case or its complexity claim omits allocated data.

### Level-up follow-up

How would a grapheme-based anagram definition differ?

## Sources

<!-- generated from frontmatter -->
