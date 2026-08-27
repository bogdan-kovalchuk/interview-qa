---
id: py-coll-0004
title: "Why can repeated concatenation of a list in a loop be worse than `append`/`extend`, even when the result is the same?"
description: "Why can repeated concatenation of a list in a loop be worse than `append`/`extend`, even when the result is the same?"
track: python
section: collections
level: middle
type: comparison
tags: [append, extend]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/sequences.md#L292-L321
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**The operation `lst = lst + [x]` creates a new list and copies all elements every time, which
gives O(n²) for n iterations.**[^py314-library-stdtypes] `lst.append(x)`, by contrast, runs in
amortized O(1), and `lst.extend(iterable)` or `lst += iterable` modify the list in place.
<span class="warn">It is specifically `lst = lst + [x]` (with rebinding) that is slow; `lst += [x]`
is an in-place operation, equivalent to `extend`.</span>

## Detailed explanation

The difference in behavior comes from the fact that a `list` is an array of pointers with capacity
pre-allocated beyond its current length. In the amortized case, `append(x)` simply writes a pointer
into an already-allocated slot; only when capacity runs out does CPython reallocate the array and
copy every element – but it does this progressively less often, so the total cost of n `append`
calls stays O(n), not O(n²).[^py314-library-stdtypes]

`lst = lst + [x]`, by contrast, creates a brand-new list every time: the `+` operator for a list
allocates memory for `len(lst) + 1` elements and copies all the existing pointers into it, plus the
new one. This happens on every loop iteration regardless of how much spare capacity the previous
list had – rebinding the name `lst` leaves no alternative. For n iterations, the sum of copies
1 + 2 + ... + n gives O(n²).

`extend(iterable)` avoids this problem differently than `append` does: if `iterable` supports
`__len__`, CPython can reallocate the list to the needed size up front and copy the elements once,
in O(k) for k new elements, instead of k separate reallocations.[^py314-howto-sorting]

The practical consequence: in a loop that adds one element per iteration, the choice is between
`append` (one at a time) and accumulating into a temporary list followed by a single `extend` –
both are linear. The mistake happens exactly when the code looks almost like `append` but uses `+`
instead of `+=`: `lst = lst + [x]` and `lst += [x]` produce the same result, but the first is
always O(n) per call, while the second is amortized O(1), because `+=` on a list calls `__iadd__`,
i.e. an in-place `extend`, not the creation of a new object.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
