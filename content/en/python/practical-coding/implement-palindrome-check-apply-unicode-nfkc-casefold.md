---
id: py-prac-0007
title: "Implement a palindrome check: apply Unicode NFKC, `casefold()`, discard non-alphanumeric characters, and never build a reversed copy of the normalized string."
description: "Normalize and casefold once, then compare with two pointers."
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
---

## Task

Implement `is_palindrome(s)` using NFKC, then casefold, then ignoring non-alphanumeric code points. Do not allocate a reversed copy.

## Constraints

- Input is str.
- Empty or punctuation-only input is a palindrome.
- Compare code points, not grapheme clusters; do not strip accents.
- The normalized string may be allocated.

## Short answer

**Normalize and casefold once, then compare with two pointers.** Skip non-alphanumeric characters at both ends. This avoids a reversed copy but still allocates the normalized string.

## Detailed explanation

The scan maintains equal retained prefixes and suffixes. NFKC handles compatibility forms and casefold handles caseless matching; the exact sequence is part of this task, not a universal linguistic definition of a palindrome. [^py313-unicode] [^py313-types]

## Examples

```python
assert is_palindrome("Race car!")
```

## Solution

```python
import unicodedata

def is_palindrome(s):
    s = unicodedata.normalize("NFKC", s).casefold()
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
```

## Complexity

The two-pointer scan is O(m) time and O(1) extra scan storage for m normalized code points. Total storage includes O(m) for normalization; normalization and casefold costs are additional. [^py313-unicode] [^py313-types]

## Edge cases

Include empty input, punctuation, fullwidth letters, casefold expansion and unequal retained characters.

## Tests

Run after the Solution block with pytest installed.

```python
import pytest

assert is_palindrome("")
assert is_palindrome("!!!")
assert is_palindrome("A man, a plan, a canal: Panama!")
assert is_palindrome("ＡbＡ")
assert is_palindrome("ßs")
assert not is_palindrome("ab")
assert not is_palindrome("éa")
```

## Evaluation guide

### Expected signals

Explain the difference between O(1) scan storage and total normalization storage. Preserve the requested order of transformations.

### Red flags

The implementation misses a stated boundary case or its complexity claim omits allocated data.

### Level-up follow-up

How would grapheme-cluster comparison change this contract?

## Sources

<!-- generated from frontmatter -->
