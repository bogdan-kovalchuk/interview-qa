---
id: py-coll-0008
title: "How do `d[key]`, `d.get(key)`, and `setdefault()` differ in behaviour when the key is missing, and in their possible side effects?"
description: "How do `d[key]`, `d.get(key)`, and `setdefault()` differ in behaviour when the key is missing, and in their possible side effects?"
track: python
section: collections
level: middle
type: comparison
tags: [d-key, d-get-key, setdefault]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L118-L138
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`d[key]` raises `KeyError`; `d.get(key)` returns `None` (or a supplied default) with no side
effects; `d.setdefault(key, default)` inserts `default` into the dictionary if the key is
missing, and returns it.**[^py314-library-stdtypes] <span class="warn">The `setdefault()` method
always evaluates the `default` argument, even when the key already exists – this can be an
unwanted side effect if constructing the default is expensive.</span>

## Detailed explanation

`d[key]` is implemented through `__getitem__`, which, when the key is missing, calls the
`__missing__` hook instead of raising `KeyError` directly.[^py314-library-stdtypes] The base
`dict` defines `__missing__` to simply raise `KeyError`, but this exact hook is what makes
`collections.defaultdict` possible: it overrides `__missing__` so that it calls
`default_factory()`, inserts the result into the dictionary under that key, and returns it. So
`d[key]` on a `defaultdict` is not a different operation – it is the same protocol with a
different implementation of the hook.

`d.get(key, default)` does not use `__missing__` at all: it is a method that checks for the
key's presence itself and returns the ready-made `default` value with no write to the dictionary
and no mutation whatsoever – the safest option for read-only access, when a missing key is a
normal, expected case.

`d.setdefault(key, default)` combines a read with a potential write, but with an important trap:
the `default` expression is evaluated on every call, before the key's presence is even checked.
In the common grouping pattern `d.setdefault(key, []).append(x)`, this means a new empty list is
created on every call, even when the key already exists and that list is immediately discarded as
unneeded. For a cheap `default` (a number, `None`), this does not matter, but for an expensive
one it is wasted work on every call, not just the first.

That is exactly why `collections.defaultdict(list)` is usually better than `setdefault` for the
"groupby into a dict" pattern: `default_factory()` is called only inside `__missing__`, i.e.
exactly when the key is genuinely absent, not on every access. Syntactically both approaches look
equally compact, but semantically `defaultdict` avoids the unnecessary object creation on the
"hot" path where the key already exists.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
