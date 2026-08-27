---
id: py-coll-0016
title: "Why can an incorrect `__eq__` on custom objects lead to unexpected results for set membership?"
description: "Why can an incorrect `__eq__` on custom objects lead to unexpected results for set membership?"
track: python
section: collections
level: senior
type: pitfall
tags: [eq]
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L388-L440
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**A set first looks up an element by `hash()` (the bucket), then compares with `__eq__`; if
`__eq__` and `__hash__` are inconsistent, membership gives wrong results.**[^py314-library-stdtypes]
The contract is: `a == b` -> `hash(a) == hash(b)`. If `__eq__` returns `True` but `hash()`
differs, the set will not find the object in the right bucket – `b in {a}` returns `False` even
though `a == b`. <span class="warn">Always define `__hash__` and `__eq__` together, using the
same fields.</span>

## Detailed explanation

The most common trap appears before anyone even breaks the contract itself: if a class defines
only `__eq__` and does not define `__hash__`, Python automatically sets `__hash__ = None`, and
the class becomes unhashable – trying to put such an object into a `set` or use it as a `dict`
key raises `TypeError` before any membership test even runs.[^py314-library-stdtypes] This
prevents a silent bug, but it often surprises people who expected to inherit the default hash
from `object` (which is based on `id()` and also works, but breaks the contract "equal objects
have the same hash" once a custom `__eq__` is added).

A second, quieter case is when `__hash__` is computed from the same fields as `__eq__`, but those
fields are mutable and the object is still placed into a `set`. Example: `hash()` is computed
from a `name` field, the object is added to a `set`, and then `name` is changed in place. The
bucket the object lives in stays the old one – the one it was placed into under the previous
`hash()` – so a later lookup by the new `name` value will not find that object, `in` returns
`False`, even though the object is physically present in the set. This is exactly why mutable
fields should not be included in `__hash__`.

A third case is asymmetric comparison: if `A.__eq__` returns `True` for `B`, but `B.__eq__` does
not return `True` for `A` (for example, `B` is a different type with its own, incompatible
logic), the behaviour of `in` depends on which side of the comparison is invoked inside the
bucket, and the result becomes unpredictable depending on insertion order.

The practical takeaway is to use only fields that stay unchanged for as long as the object lives
in a collection for `__hash__` (ideally a frozen `dataclass` or `NamedTuple`, where `__eq__` and
`__hash__` are generated consistently and automatically), and never to rely on comparisons
against objects of other types without an explicit, symmetric check.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
