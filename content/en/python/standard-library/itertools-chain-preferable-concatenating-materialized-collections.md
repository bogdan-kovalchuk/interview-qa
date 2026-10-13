---
id: py-stdlib-0004
title: "When is `itertools.chain()` preferable to concatenating materialized collections?"
description: "When is `itertools.chain()` preferable to concatenating materialized collections?"
track: python
section: standard-library
level: middle
type: comparison
tags: [itertools-chain]
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
  - source_id: py314-library-itertools-chain
    title: "Python 3.14: Library/itertools, chain"
    url: https://docs.python.org/3.14/library/itertools.html#itertools.chain
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: itertools.chain and chain.from_iterable (sequential traversal of iterables, the yield from equivalent, lazy evaluation)."
  - source_id: py314-library-stdtypes-common-sequence-operations
    title: "Python 3.14: Library/stdtypes, common sequence operations"
    url: https://docs.python.org/3.14/library/stdtypes.html#common-sequence-operations
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the concatenation operation s + t for sequence types; does not cover iterables that are not sequences."
---

## Short answer

**`chain()` yields the elements of its input iterables one after another, lazily and without an intermediate list, so it is preferable when the combined result is only iterated once: `chain` itself builds no new list, even when the inputs are `list` objects.**[^py314-library-itertools-chain] Concatenation of two `list` objects with `a + b` creates a new list of length `len(a) + len(b)`.[^py314-library-stdtypes-common-sequence-operations] For generators, `+` does not work at all. If one iterable contains other iterables, use `chain.from_iterable()`.[^py314-library-itertools-chain]

## Detailed explanation

`chain()` takes several iterables and returns a single iterator. It yields the elements of the first iterable until that one is exhausted, then moves on to the next. The documentation describes this as equivalent to `for iterable in iterables: yield from iterable`.[^py314-library-itertools-chain] So `chain` does not build a list: each element is produced when it is requested, and no extra copy of the data is made. Input collections that already exist remain in memory unchanged.

The comparison with concatenation is the key point. For two `list` objects, `a + b` creates a new list into which references to all elements of both operands are copied, so the extra memory is proportional to `len(a) + len(b)`. For a generator the `+` operator does not work at all, because a generator is not a sequence and has no `len()`:

```python
from itertools import chain

a = [1, 2, 3]
b = (x * 10 for x in range(3))  # a generator: no len(), no +
try:
    a + b
except TypeError as error:
    print('TypeError:', error)  # can only concatenate list (not "generator") to list
print(list(chain(a, b)))        # [1, 2, 3, 0, 10, 20]
```

Laziness is visible when the inputs produce data with side effects. The first `next()` starts only the first generator, and the second one is not touched until the first is exhausted:

```python
from itertools import chain

def produce(label, n):
    for i in range(n):
        print(f'{label} produces {i}')
        yield i

it = chain(produce('first', 2), produce('second', 1))
print('chain created')   # no item has been produced yet
print(next(it))          # first produces 0, then 0
print(list(it))          # first produces 1, second produces 0, then [1, 0]
```

A second `list()` of the same `chain` gives an empty list, because the result can be traversed only once (this is iterator behaviour). For repeated passes, `len()`, or indexing, a sequence is needed. `chain` fits when the inputs are iterables without `len()` or indexing (generators, the results of `map` or `filter`, lines of a file), the result is consumed in a single pass, and an intermediate list would be expensive. If the result must be stored as a `list` anyway, `list(chain(a, b))` also creates a new list, and nothing is saved.

**Common mistakes:**
- assuming that `chain` creates a copy of the data: it only iterates over the inputs, and `list(chain(...))` is what makes a copy;
- expecting indexing, `len()`, or a second pass over a `chain`;
- expecting `chain(['AB', 'CD'])` to split strings into characters: it yields `'AB'` and `'CD'` whole; to flatten one iterable of iterables, use `chain.from_iterable()`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
