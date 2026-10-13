---
id: py-stdlib-0002
title: "How does `Counter` simplify frequency analysis, and how does it behave with missing keys?"
description: "How does `Counter` simplify frequency analysis, and how does it behave with missing keys?"
track: python
section: standard-library
level: middle
type: mechanism
tags: [counter]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-datetime
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-re
    title: "Python 3.14: Library/re"
    url: https://docs.python.org/3.14/library/re.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-collections-counter
    title: "Python 3.14: Library/collections, Counter objects"
    url: https://docs.python.org/3.14/library/collections.html#collections.Counter
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the Counter objects section on the zero count for missing elements, most_common(), subtract(), and arithmetic operations on Counter."
---

## Short answer

**`Counter` returns `0` for missing keys instead of raising `KeyError`, so you can count elements without checking whether a key exists.**[^py314-library-collections-counter] It is initialized from an iterable or a mapping, provides `most_common(n)` for the top N elements and `subtract()` for subtracting counts, and supports the arithmetic operators `+`, `-`, `&`, and `|` between `Counter` objects.[^py314-library-collections-counter]

## Detailed explanation

A `Counter` is a `dict` subclass for counting hashable objects: its keys hold the elements and its values hold their counts.[^py314-library-collections-counter] Frequency analysis typically passes once over an iterable and increments the count of each element. The constructor `Counter(iterable)` does this in one call, and `most_common(n)` returns the `n` most frequent elements from most to least common. Elements with equal counts keep the order in which they were first encountered, so `Counter('abracadabra').most_common(3)` returns `a`, then `b` and `r`, both with a count of 2.[^py314-library-collections-counter]

The main difference from a plain `dict` is the behaviour with missing keys. The count of a missing element is zero, so `counts['dog']` returns `0` instead of raising `KeyError`.[^py314-library-collections-counter] In CPython this is implemented by the `__missing__` method, which only returns `0` and does not store the key in the dictionary. A read therefore changes nothing: `'dog' in counts` is still `False`. A key appears only on a write, for example `counts['dog'] += 1`.

Example: count words, then read a missing key:

```python
from collections import Counter

words = "the cat and the hat and the bat".split()
freq = Counter(words)
print(freq.most_common(2))  # [('the', 3), ('and', 2)]
print(freq['dog'])          # 0: a missing key gives 0, no KeyError
print('dog' in freq)       # False: the read did not insert the key
freq['dog'] += 1
print('dog' in freq, freq['dog'])  # True 1: a write does insert the key
```

Arithmetic operations return only results with positive counts: `c - d` drops elements whose count is zero or negative, while `subtract()` updates the counts in place and allows zero and negative values.[^py314-library-collections-counter] An explicitly stored zero count also stays in the `Counter` until you remove it with `del`.[^py314-library-collections-counter]

**Common mistakes:**
- assuming that reading `counts[key]` creates an entry, and building a key-existence check on that;
- expecting negative counts from `+` or `-`: they are dropped, and negative values come from `subtract()`;
- confusing `Counter` with `defaultdict(int)`: both give `0` for a missing key, but `defaultdict` inserts the key on read (see qid:py-stdlib-0003).

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
