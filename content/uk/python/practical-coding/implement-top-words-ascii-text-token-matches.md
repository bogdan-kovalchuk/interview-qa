---
id: py-prac-0012
title: "Реалізуйте top-3 words для ASCII text: token матчить `[A-Za-z]+`, comparison є case-insensitive, а ties сортуються lexicographically."
description: "Порахуйте lowercase regex matches і сортуйте за (-count, word)."
track: python
section: practical-coding
level: middle
type: coding
tags: [a-za-z]
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

Реалізуйте `top3_words(text)`: виділіть tokens за `[A-Za-z]+`, перетворіть на lowercase й поверніть до трьох distinct words за спаданням frequency та lexicographic ties.

## Constraints

- Вхід – ASCII str.
- Digits, punctuation та apostrophes розділяють tokens.
- За потреби поверніть менше трьох слів; без tokens – порожній list.

## Short answer

**Порахуйте lowercase regex matches і сортуйте за `(-count, word)`.** Візьміть перші три entries. `Counter.most_common()` вирішує ties за першим входженням, тому не реалізує цей lexicographic contract.

## Detailed explanation

Regex визначає слова, тому apostrophe розділяє token. Compound sorting key явно задає обидва правила порядку незалежно від encounter order. [^py313-counter] [^py313-regex] [^py313-sorting]

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

Для довжини тексту L та u distinct words token scanning обробляє O(L) символів, а сортування – O(u log u) порівнянь. String comparison може переглядати кілька символів; пам’ять включає текст distinct words і counts. [^py313-counter] [^py313-regex] [^py313-sorting]

## Edge cases

Перевірте відсутність слів, менше трьох слів, mixed case, punctuation і ties з encounter order, що відрізняється від alphabetic order.

## Tests

Виконайте після блока Solution із встановленим pytest.

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

Сортування лише за frequency або most_common недостатнє. Дотримуйтеся точної token grammar.

### Red flags

Implementation пропускає зазначений boundary case або complexity claim не враховує allocated data.

### Level-up follow-up

Як уникнути sorting кожного distinct word?

## Sources

<!-- generated from frontmatter -->
