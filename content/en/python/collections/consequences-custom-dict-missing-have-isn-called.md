---
id: py-coll-0012
title: "What consequences does a custom `dict.__missing__()` have, and why isn't it called the same way by every method of accessing a key?"
description: "What consequences does a custom `dict.__missing__()` have, and why isn't it called the same way by every method of accessing a key?"
track: python
section: collections
level: senior
type: mechanism
tags: [dict-missing]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L173-L190
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`__missing__(key)` is called only by the `__getitem__()` method when a key is absent; `get()`,
`pop()`, and `setdefault()` do not call it.**[^py314-library-stdtypes] This means `d[missing_key]`
triggers `__missing__`, while `d.get(missing_key)` returns `None` (or the given default) without
calling `__missing__`. This is exactly the mechanism `collections.defaultdict` is built on: its
`__missing__` calls `default_factory` and stores the result in the dictionary.

## Detailed explanation

The key distinction is that `__missing__` is a hook invoked by `dict.__getitem__()` itself at the
C level, not a universal interceptor for all dictionary access. So any code path that bypasses
`__getitem__` simply never sees this hook: `key in d` (i.e. `__contains__`) checks for the key
directly in the table and never calls `__missing__`, and likewise `pop(key, default)` and
`setdefault(key, default)` are implemented through their own C-level logic that does not delegate
to `__missing__`.[^py314-library-stdtypes]

The consequence is a possible inconsistency: if `__missing__` creates an entry (as in
`defaultdict`), then `key in d` returns `False` before the first `d[key]` but `True` right after
it, even though no explicit assignment appeared in the code. If `__missing__` does not mutate the
dictionary and only computes and returns a value (as `collections.Counter` does, where a missing
key is treated as `0` without being written to the table), then `d[key]` and `key in d` stay
consistent – the dictionary does not "grow" from reads alone.

Plain `dict` does not define `__missing__` at all, so the `KeyError` from `d[missing_key]` on an
ordinary dictionary is the standard behaviour of `__getitem__` with no delegation; the hook only
applies in subclasses where it is explicitly overridden.

One more practical trap – if `__missing__` itself accesses `self[key]` for the same key without a
base case, it leads to infinite recursion, because every miss calls `__missing__` again.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
