---
id: py-coll-0007
title: "Why must dictionary keys be hashable, and how does a dictionary use hash together with equality?"
description: "Why must dictionary keys be hashable, and how does a dictionary use hash together with equality?"
track: python
section: collections
level: middle
type: mechanism
tags: []
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L206-L242
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**A key must be hashable – it must have `__hash__()` and `__eq__()` – because a dict uses the
hash to determine the bucket, and equality to resolve collisions.**[^py314-library-stdtypes] First
`hash(key)` is computed to find the position; if the bucket already has entries, `__eq__()` is
called to compare against each of them. <span class="warn">Objects that compare as equal must
have the same hash – otherwise the key gets "lost".</span>

## Detailed explanation

CPython's `dict` is not a list of chains per bucket but uses open addressing: `hash(key)`, masked
to the table size, gives a starting slot, and if it is occupied by a different key, a
deterministic probing sequence (perturbation) that uses further bits of that same hash is
followed until an empty slot or a slot with an equal key is found.[^py314-library-stdtypes] So a
"bucket" here is not a container holding several elements but a single array slot, and lookup
speed depends on how rarely hash collisions occur.

The hashable-type contract – if `a == b` then `hash(a) == hash(b)` must hold – is critical
precisely because of this scheme: a lookup first narrows the search to slots with a matching
hash, and only then does `__eq__` confirm the final match. If this contract is broken (equal
objects with different hashes), a lookup by key may never even reach the slot where the "equal"
key lives, and `d[a]` will fail to find an entry that was made as `d[b] = ...`.

Mutable built-in types (`list`, `dict`, `set`) are deliberately unhashable, because if a `hash`
were computed for an object at insertion time and the object were then changed, its future hash
at lookup time would no longer match the stored slot – the key becomes "lost": it physically
stays in the table, visible during iteration, but unreachable through `d[key]`, because the hash
no longer leads to the right slot.

Another consequence is that defining `__eq__` on a class without an explicit `__hash__`
automatically makes its instances unhashable (Python sets `__hash__ = None`), because the
interpreter cannot guarantee consistency between hash and equality without an explicit
implementation of both. `tuple` and `frozenset` are hashable only when every one of their
elements is hashable – recursively.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
