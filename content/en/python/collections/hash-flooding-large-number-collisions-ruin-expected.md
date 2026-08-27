---
id: py-coll-0024
title: "Why can hash flooding or a large number of collisions ruin the expected O(1) lookup, and why doesn't that change the dictionary's logical contract?"
description: "Why can hash flooding or a large number of collisions ruin the expected O(1) lookup, and why doesn't that change the dictionary's logical contract?"
track: python
section: collections
level: senior
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython"
    version: null
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L441-L511
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Hash flooding is a situation where many keys land in the same hash table bucket, and lookup
degrades from average O(1) to O(n) because of long probe sequences.**[^py314-library-stdtypes] In
CPython, `dict` and `set` use open addressing, so collisions force the interpreter to search for
a free slot by probing. The dictionary's logical contract is not broken by this: `__eq__` is
checked against every candidate in the bucket, so the right key is still found – only speed
changes, not correctness.

## Detailed explanation

Average O(1) for `dict`/`set` is a statistical statement: it holds when keys are evenly
distributed across buckets and the load factor is kept low by automatic table resizing. If many
keys share the same or a nearby `hash()`, they compete for the same slots, and CPython is forced
to walk a longer probe sequence (linear probing perturbed by a `perturb` value) before finding a
free slot or an `__eq__` match. In the worst case, when all keys collide, every operation
degenerates to O(n).[^py314-library-stdtypes]

Collisions come in two flavours. Accidental ones follow from the birthday paradox: even with an
even hash distribution, some pairs are bound to coincide, but resizing keeps their share small.
Deliberate ones are hash flooding proper: an attacker crafts input strings so that their
`hash()` values coincide or land in the same bucket, then sends a mass of such keys (a classic
example is field names in a POST request that a server stores in a `dict`). This turns a normally
O(1) service into O(n) per request, i.e. a denial of service.

CPython's defence is randomising the hash of strings and bytes via SipHash with a secret
`PYTHONHASHSEED`, regenerated for every process unless it is explicitly pinned. Without knowing
the seed, an attacker cannot predict which strings will produce the same `hash()`, so preparing a
colliding set of keys in advance is not possible.[^py314-library-collections]

Crucially, none of these scenarios break correctness: `__eq__` is called against every candidate
in the probe sequence until an exact match or an empty slot is found, so the requested key (or
its absence) is always determined correctly. Only performance degrades, while the logical
contract – "keys equal by `__eq__` and `__hash__` are found" – stays intact.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
