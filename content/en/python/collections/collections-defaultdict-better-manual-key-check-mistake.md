---
id: py-coll-0009
title: "When is `collections.defaultdict` better than a manual key check, and what mistake can a wrong default factory hide?"
description: "When is `collections.defaultdict` better than a manual key check, and what mistake can a wrong default factory hide?"
track: python
section: collections
level: middle
type: comparison
tags: [collections-defaultdict]
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

**`defaultdict` is better when you need to group or accumulate values by key: it automatically
creates a default value through `default_factory` when accessed via
`__getitem__`.**[^py314-library-stdtypes] <span class="warn">Any access `d[key]` for a missing key
silently creates an entry, so an accidental lookup grows the dictionary with spurious entries. The
`d.get(key)` method does not call `default_factory` and does not create the key.</span>

## Detailed explanation

The mechanism `defaultdict` is built on is an overridden `__missing__`: when `__getitem__` cannot
find a key, instead of raising `KeyError` it calls `default_factory()` with no arguments, and the
result is immediately stored in the dictionary and returned.[^py314-library-collections] This is
what distinguishes `defaultdict` from `dict.setdefault(key, default)`: `setdefault` evaluates the
default expression on every call, even when the key already exists and the default is not used,
whereas `default_factory` is only invoked on an actual miss.

A typical use is grouping: `d = defaultdict(list); d[key].append(item)` avoids the manual
`if key not in d: d[key] = []`. For counters the natural choice is `defaultdict(int)`, because
`int()` returns `0`. For nested structures you can pass a callable instead of a plain type:
`defaultdict(lambda: defaultdict(int))` builds a tree of dictionaries on the fly.

A mistake that is easy to hide is a wrong factory that takes arguments or has side effects:
`default_factory` is called with no parameters, so `defaultdict(list.append)` or any factory that
expects a key will fail on the first miss with a `TypeError`. Another trap is confusing
`defaultdict(list)` with `defaultdict(list())`: the second passes an already-created list as
`default_factory` rather than the type itself, and calling `list()(...)` fails with a `TypeError`,
because a list is not callable.

The mechanism is closely tied to `__missing__` on plain dictionaries qid:py-coll-0012 –
`defaultdict` is, in essence, the simplest example of using it.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
