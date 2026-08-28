---
id: py-syntax-0004
title: "How does extended iterable unpacking work in the assignment `head, *middle, tail = items`, and what happens if there are not enough elements?"
description: "How does extended iterable unpacking work in the assignment `head, *middle, tail = items`, and what happens if there are not enough elements?"
track: python
section: syntax-and-control-flow
level: middle
type: mechanism
tags: [head-middle-tail-items]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-simple-stmts
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-compound-stmts
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/syntax.md#L252-L352
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`*middle` collects all the intermediate elements into a `list`; at least 2 elements are needed for it to succeed (for `head` and `tail`).**[^py314-reference-expressions] For example, `head, *middle, tail = [1, 2, 3, 4, 5]` gives `head=1, middle=[2, 3, 4], tail=5`. With only one element - `head, *middle, tail = [1]` - it raises `ValueError: not enough values to unpack (expected at least 2, got 1)`.

## Detailed explanation

Extended unpacking splits the targets into two categories: ordinary names, each taking exactly one
element, and exactly one starred name, which takes whatever is
left.[^py314-reference-simple-stmts]

The algorithm is simple: Python counts the ordinary targets to the left and to the right of the
star, hands them one element each from the corresponding ends, and puts the middle into a **list** -
always a list, even when the source was a tuple or a string.

```python
head, *middle, tail = [1, 2, 3, 4, 5]
head      # 1
middle    # [2, 3, 4]   - always a list
tail      # 5

first, *rest = 'abc'
rest      # ['b', 'c']  - a list of characters, not a string
```

Hence the minimum number of elements: it equals the number of ordinary targets. For
`head, *middle, tail` that is two; with fewer elements you get a `ValueError`, not a silent
`None`.[^py314-reference-expressions]

```python
head, *middle, tail = [1]
# ValueError: not enough values to unpack (expected at least 2, got 1)

head, *middle, tail = [1, 2]
middle    # []  - exactly two is enough; the middle is simply empty
```

The star can sit in any position, not only in the middle - and that is what makes the construct
convenient for "take the first and the rest" or "take the last and the rest".

```python
*init, last = [1, 2, 3]     # init = [1, 2], last = 3
a, b, *rest = [1, 2]        # rest = []
```

**Limits and subtleties:**
- there can be only **one** star in a target: `*a, *b = ...` is a syntax error, because the split
  would be ambiguous;
- the source can be any iterable, a generator included - but it will be exhausted completely,
  because the middle has to be materialised;
- that makes `head, *rest = infinite_generator()` a trap: the construct will try to read everything;
- the same star in literals means something else - unpacking into a new collection (`[*a, *b]`) -
  and there several stars are allowed.

The most common use is taking apart a sequence of known shape without indices: `name, *aliases,
domain = parts` reads better than three lookups by
number.[^py314-reference-compound-stmts]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
