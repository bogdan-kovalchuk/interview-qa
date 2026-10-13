---
id: py-stdlib-0014
title: "When is `bisect` useful for a sorted list, and why doesn't binary search make insertion cheap?"
description: "When is `bisect` useful for a sorted list, and why doesn't binary search make insertion cheap?"
track: python
section: standard-library
level: middle
type: practical
tags: [bisect]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-bisect
    title: "Python 3.14: Library/bisect"
    url: https://docs.python.org/3.14/library/bisect.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: bisect calls only __lt__; insort is O(n) because of the insert step; the key parameter was added in 3.10; the functions are not thread-safe; a dictionary is faster for locating specific values."
---

## Short answer

**`bisect` finds the insertion point in a logarithmic number of comparisons, but `insort()` costs O(n) because the `list.insert()` step shifts elements.**[^py314-library-bisect] The module is useful for range lookups in sorted data and for long lists with expensive comparisons; it calls only `__lt__`.[^py314-library-bisect] For frequent insertions into a large list, consider another structure, such as `SortedList` from the `sortedcontainers` package.

## Detailed explanation

`bisect` is a binary search over a sorted list: `bisect_left` gives the position before equal elements, and `bisect_right` the position after them. The functions call only `__lt__`, never `__eq__`, so equality must be checked separately.[^py314-library-bisect]

An example, illustrative and run on CPython 3.13 and 3.14:

```python
import bisect

# Range lookup: bisect_right returns the index of the first breakpoint above the score.
breakpoints = [60, 70, 80, 90]
grades = ["F", "D", "C", "B", "A"]
print(grades[bisect.bisect_right(breakpoints, 85)])   # B

# insort finds the position with a binary search, then list.insert shifts the tail.
data = [10, 20, 30, 40]
bisect.insort(data, 25)
print(data)                                           # [10, 20, 25, 30, 40]

# bisect never tests equality, so a membership check compares the found element.
def contains(sorted_items, x):
    i = bisect.bisect_left(sorted_items, x)
    return i < len(sorted_items) and sorted_items[i] == x

print(contains(data, 30), contains(data, 35))         # True False
```

`bisect_right(breakpoints, 85)` returns 3, so `grades[3]` is `'B'`. The search for `insort` is logarithmic, but `list.insert` shifts the tail of the list, and on a large list that shift dominates, which makes `insort` O(n).[^py314-library-bisect] The `contains` function makes the equality test explicit.

The module is useful when a sorted list already exists and most operations read from it: finding a position, range boundaries, or long lists whose comparisons are expensive. For locating specific values a dictionary is usually faster, and the documentation recommends it for that purpose.[^py314-library-bisect] The `key` parameter (added in Python 3.10) is applied to the list elements but not to `x`, so `x` must already be in the same key space.[^py314-library-bisect]

Limits: `bisect` does not check that the list is sorted, so on an unsorted list it silently returns a position that means nothing. The functions are not thread-safe: inserting into one list from several threads through `insort` can leave the list unsorted.[^py314-library-bisect]

**Common mistakes:**
- assuming that `insort` is O(log n) overall: only the search is logarithmic, while inserting into a list costs O(n);
- relying on `bisect` for a membership check without comparing `a[i] == x`;
- searching a list that was sorted by a different order or key: `bisect` returns a wrong position without raising an error.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
