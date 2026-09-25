---
id: py-compfn-0004
title: "Why must the groups returned by `itertools.groupby()` be consumed or materialized before moving on to the next group?"
description: "Why must the groups returned by `itertools.groupby()` be consumed or materialized before moving on to the next group?"
track: python
section: comprehensions-and-functional
level: middle
type: pitfall
tags: [itertools-groupby]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-howto-functional
    title: "Python 3.14: Howto/functional"
    url: https://docs.python.org/3.14/howto/functional.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-expressions-displays-for-lists-sets-and-dict
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**Each group is an iterator that shares the underlying iterable with `groupby()`; advancing to the next group exhausts the previous iterator.**[^py314-howto-functional] Therefore, storing the group object without materialising it (for example, into a `list`) leads to an empty result when consumed later. <span class="warn">A common mistake is `groups = [(k, g) for k, g in groupby(data, key)]`, after which all `g` iterators are already exhausted.</span>

## Detailed explanation

Each group returned by `itertools.groupby()` is an independent iterator (`_grouper`) that references the shared data stream of the underlying iterable.[^py314-library-itertools] When the outer loop advances to the next group by invoking `next()` on the `groupby` object, the algorithm must step through the internal cursor until a new key appears. If the elements of the current group were not already consumed, `groupby` consumes them automatically to reach the start of the next group, leaving the previous iterator permanently exhausted.

This behaviour is an intentional design trade-off in favor of memory efficiency (streaming processing). `groupby()` is designed to process infinite or very large sequences with `O(1)` auxiliary memory, so it never caches group elements or buffers input values. If concurrent access to multiple groups or repeated iteration over a group is required, each group must be materialized (for example, by calling `list(group)`) immediately in the loop body before the next iteration of `groupby`.

It is also important to remember the core contract of `groupby`: it groups only consecutive identical keys (run-length grouping). Unlike SQL `GROUP BY`, it does not aggregate identical keys from different parts of a collection unless the input iterable is sorted by that key beforehand.

Demonstration of group exhaustion and how to handle it correctly:

```python
from itertools import groupby

data = ["ant", "ape", "bat", "bear", "cat"]

# Pitfall: storing iterators without materialization
broken = [(k, g) for k, g in groupby(data, key=lambda s: s[0])]
print([(k, list(g)) for k, g in broken])
# Output: [('a', []), ('b', []), ('c', [])]

# Correct: materialize each group immediately
correct = [(k, list(g)) for k, g in groupby(data, key=lambda s: s[0])]
print(correct)
# Output: [('a', ['ant', 'ape']), ('b', ['bat', 'bear']), ('c', ['cat'])]
```

**Common mistakes and practical consequences:**
- storing `(key, group)` pairs in a list or dictionary without calling `list(group)` during iteration;
- calling `groupby()` on unsorted data expecting global aggregation across the entire collection;
- attempting to re-read a `group` iterator after exiting the loop or generator context.

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
