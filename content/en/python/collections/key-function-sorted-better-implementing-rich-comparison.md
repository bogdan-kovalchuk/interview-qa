---
id: py-coll-0021
title: "When is a key function in `sorted()` better than implementing rich comparison methods on a domain class?"
description: "When is a key function in `sorted()` better than implementing rich comparison methods on a domain class?"
track: python
section: collections
level: senior
type: comparison
tags: [sorted]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-sorting
    title: "Python 3.14: Howto/sorting"
    url: https://docs.python.org/3.14/howto/sorting.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**A key function is better when the sort order depends on context or external data, rather than
on the type's own natural order.**[^py314-library-stdtypes] Rich comparison methods (`__lt__`,
for instance) define a single canonical order for the class; a key function lets you sort by any
derived key without changing the class. For example, `sorted(users, key=lambda u: scores[u.id])`
sorts by an external dictionary, which cannot be expressed through `__lt__`.

## Detailed explanation

Rich comparison ties the order to the class itself: `__lt__` is a single, canonical answer to
"what is less". If the same `User` objects need to be sorted sometimes by `age`, sometimes by
`name`, sometimes by a `score` from an external dictionary, you would either need several
versions of `__lt__` (impossible – there is only one method) or switch the class's state before
every sort, which is both fragile and not thread-safe. A key function removes this constraint:
every call to `sorted(data, key=...)` carries its own ordering logic local to that call, and the
class does not need to know such an order even exists.

Performance also favours a key function when computing the key is expensive: `sorted()` calls
`key(x)` exactly once per element (known as decorate-sort-undecorate, or the Schwartzian
transform), then compares the already-computed keys. If the order were defined via `__lt__`, that
same expensive logic would run again on every pairwise comparison during the sort – O(n log n)
times instead of O(n).[^py314-howto-sorting]

A key function is also the only way to sort data that is not an instance of your own class and
cannot be given an `__lt__` at all (for instance, `dict`, a `tuple` from an external source, or an
object from a third-party library): `sorted(records, key=lambda r: r["score"])` works without any
change to the type of `records`.

Rich comparison, on the other hand, is justified when the domain genuinely has one natural, stable
order that is part of the type's own meaning – for example, `Decimal` or `datetime`, where "less
than" means the same thing in any context of use; then `__lt__` (together with
`functools.total_ordering`, so you do not have to write all six methods by hand) makes the order
part of the type's public API, rather than a detail of one particular `sorted()` call.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
