---
id: py-prac-0007
title: "Реалізуйте palindrome check: застосуйте Unicode NFKC, `casefold()`, відкиньте non-alphanumeric characters і не створюйте reversed copy normalized string."
description: "Виконайте normalize та casefold один раз, потім порівнюйте двома pointers."
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
---

## Task

Реалізуйте `is_palindrome(s)`: NFKC, потім casefold, потім ігнорування non-alphanumeric code points. Не створюйте reversed copy.

## Constraints

- Вхід – str.
- Порожній рядок або лише punctuation вважається palindrome.
- Порівнюйте code points, а не grapheme clusters; accents не видаляйте.
- Нормалізований рядок можна створити.

## Short answer

**Виконайте normalize та casefold один раз, потім порівнюйте двома pointers.** Пропускайте non-alphanumeric символи з обох країв. Це уникає reversed copy, але нормалізований рядок усе одно займає пам’ять.

## Detailed explanation

Обхід підтримує рівність збережених prefixes та suffixes. NFKC обробляє compatibility forms, а casefold – caseless matching; саме така послідовність є контрактом задачі, а не універсальним мовним означенням palindrome. [^py313-unicode] [^py313-types]

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

Two-pointer scan має O(m) часу й O(1) додаткової пам’яті обходу для m нормалізованих code points. Загальна пам’ять включає O(m) на нормалізацію; її час і час casefold враховуються додатково. [^py313-unicode] [^py313-types]

## Edge cases

Включіть порожній вхід, punctuation, fullwidth letters, casefold expansion та нерівні збережені символи.

## Tests

Виконайте після блока Solution із встановленим pytest.

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

Поясніть різницю між O(1) пам’яті обходу та загальною пам’яттю нормалізації. Збережіть заданий порядок transformations.

### Red flags

Implementation пропускає зазначений boundary case або complexity claim не враховує allocated data.

### Level-up follow-up

Як comparison grapheme clusters змінить цей contract?

## Sources

<!-- generated from frontmatter -->
