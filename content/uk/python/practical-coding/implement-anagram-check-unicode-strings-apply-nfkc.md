---
id: py-prac-0013
title: "Реалізуйте anagram check для Unicode strings: застосуйте NFKC та `casefold()`, ігноруйте whitespace, а інші code points враховуйте."
description: "Побудуйте Counter non-whitespace символів після NFKC та casefold."
track: python
section: practical-coding
level: middle
type: coding
tags: [casefold]
status: published
updated: 2026-10-04
content_revision: 3
reconciled_with:
  en: 3
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

Реалізуйте `is_anagram(s1, s2)`: застосуйте NFKC, потім casefold, ігноруйте whitespace й порівняйте multiplicities решти code points.

## Constraints

- Обидва inputs – str.
- Punctuation та accents враховуються; ігнорується лише whitespace.
- Порівнюйте code points, а не grapheme clusters.
- Не додавайте нормалізацію після casefold.

## Short answer

**Побудуйте Counter non-whitespace символів після NFKC та casefold.** Рівність Counters перевіряє і символи, і multiplicities. На відміну від sorting, counting не впорядковує всю послідовність символів.

## Detailed explanation

Нормалізація може compose canonically equivalent sequences і замінювати compatibility forms. Casefold може розгорнути один символ у кілька; counting має відбуватися після обох transformations. Punctuation залишається значущою. [^py313-unicode] [^py313-types] [^py313-counter]

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

Counting та comparison потребують expected O(m+n) операцій для transformed lengths m і n. Пам’ять включає transformed strings та distinct-character counters; вартість transformations додається. [^py313-unicode] [^py313-types] [^py313-counter]

## Edge cases

Перевірте canonical equivalence, fullwidth letters, casefold expansion, Unicode whitespace, нерівні multiplicities та punctuation.

## Tests

Виконайте після блока Solution із встановленим pytest.

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

Не замінюйте Counter на set, яка втрачає multiplicity. Ігноруйте лише whitespace.

### Red flags

Implementation пропускає зазначений boundary case або complexity claim не враховує allocated data.

### Level-up follow-up

Чим відрізнятиметься grapheme-based означення anagram?

## Sources

<!-- generated from frontmatter -->
