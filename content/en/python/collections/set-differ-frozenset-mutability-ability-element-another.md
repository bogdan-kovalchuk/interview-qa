---
id: py-coll-0014
title: "How does `set` differ from `frozenset` in mutability and in the ability to be an element of another set?"
description: "How does `set` differ from `frozenset` in mutability and in the ability to be an element of another set?"
track: python
section: collections
level: middle
type: comparison
tags: [set, frozenset]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L36-L70
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`set` is mutable and not hashable, so it cannot be an element of another set; `frozenset` is
immutable and hashable, so it can.**[^py314-library-stdtypes] Trying to add a `set` to another set
raises `TypeError: unhashable type: 'set'`. `frozenset` supports the same set operations (union,
intersection, subset), but has no `add()` or `remove()` methods.

## Detailed explanation

The reason for the restriction is not an arbitrary rule but a necessary condition for the
correctness of a hash table: an object's hash determines which bucket it is placed in, and that
bucket must not change while the object sits inside the hash table. If `set` were hashable and
could be mutated after being added to another structure, changing its contents would also change
its hash – the object would stay in its old bucket, but a lookup by the new hash would no longer
find it; the hash table would become inconsistent.[^py314-library-stdtypes] That is why Python
deliberately does not define `__hash__` for a mutable `set`, and trying to use `{1, 2}` as an
element of another set immediately raises `TypeError: unhashable type: 'set'`, instead of silently
corrupting the structure.

`frozenset` solves this by fixing its contents at creation time: after construction, no element can
be added or removed, so its hash can be computed once and relied on forever. This makes `frozenset`
usable both as an element of another set and as a dict key – wherever a set-valued value needs to
participate in a hashed structure itself.

Operationally, `frozenset` supports all the same binary operations as `set` – `union`,
`intersection`, `difference`, `symmetric_difference`, as well as the `|`, `&`, `-`, `^` operators and
the subset/superset comparisons – but each of them returns a new `frozenset` rather than modifying
the existing one.[^py314-library-collections] The in-place mutating methods (`add`, `remove`,
`discard`, `update`, `pop`, `clear`) simply do not exist on `frozenset` – consistent with
immutability being a guarantee of the type, not a recommendation.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
