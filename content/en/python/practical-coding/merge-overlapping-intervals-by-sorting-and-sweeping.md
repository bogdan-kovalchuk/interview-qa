---
id: py-prac-0001
title: "Merge a list of intervals so that no two of them overlap"
description: "Sort by start, then sweep once and extend the last kept interval while it still touches the next."
track: python
section: practical-coding
level: middle
type: coding
tags: [intervals, sorting, sweep, complexity]
status: published
updated: 2026-09-03
content_revision: 2
reconciled_with:
  uk: 2
see_also: [cs-cmplx-0001]
prerequisites: [cs-cmplx-0001]
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14.7"
  flags: []
applies_to:
  - product: CPython
    version: "3.14"
anki:
  export: true
sources:
  - source_id: cpython-listsort-notes
    title: "CPython Objects/listsort.txt: implementation notes for list.sort"
    url: https://github.com/python/cpython/blob/3.14/Objects/listsort.txt
    accessed: 2026-09-03
    kind: official
    version: "3.14"
    applicability: "The sorting algorithm used by list.sort and sorted in CPython; not a language guarantee."
  - source_id: py314-sorting-howto
    title: "Sorting Techniques (Python HOWTO)"
    url: https://docs.python.org/3.14/howto/sorting.html
    accessed: 2026-09-03
    kind: official
    version: "3.14"
    applicability: "Guaranteed stability of sorted and the semantics of the key argument."
---

## Task

Given a list of closed intervals `(start, end)` with `start <= end`, return the shortest list of
intervals that covers exactly the same set of points. Intervals that overlap or touch are merged into
one. The input is not sorted and must not be modified. The order of the result is by start.

## Constraints

- `0 <= len(intervals) <= 10**5`; coordinates are integers.
- Touching intervals count as overlapping: `(1, 2)` and `(2, 3)` merge into `(1, 3)`.
- The input list must be left unchanged.
- The result is sorted by start and contains no two intervals that overlap or touch.

## Short answer

**Sort the intervals by start, then sweep once, extending the last interval kept while the next one
starts at or before that interval's end.** Everything else is bookkeeping: a new interval is appended
only when it starts strictly after the current end. The sort dominates the cost at `O(n log n)`, and
the sweep adds `O(n)`.[^cpython-listsort-notes] Without sorting first, an interval can merge with one
seen much earlier, and a single pass is no longer enough.

## Detailed explanation

The problem belongs to a family that becomes easy after one ordering decision: sort by the coordinate
that makes the useful relation local. Once intervals are ordered by start, an interval can only
overlap the block that immediately precedes it, so a linear sweep with one piece of state, the current
merged interval, is sufficient. That is the whole idea, and the interviewer is looking for it rather
than for the loop.

Ordering by start is what makes the invariant true: every interval already emitted starts no later
than the one being examined, so if the new one begins after the current end, it also begins after the
end of everything emitted earlier, and the current block can be closed for good. Sorting by end
instead is a different, equally valid algorithm for a different problem, the maximum number of
non-overlapping intervals.

Tuple comparison already gives the right order, so no key function is needed; if intervals are
objects, `key` keeps the sort stable and avoids defining a comparison on the class.[^py314-sorting-howto]

## Examples

```text
[(1, 3), (2, 6), (8, 10), (15, 18)]  ->  [(1, 6), (8, 10), (15, 18)]
[(1, 4), (4, 5)]                     ->  [(1, 5)]
[(1, 10), (2, 3)]                    ->  [(1, 10)]
[]                                   ->  []
```

## Solution

```python
def merge_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    """Merge overlapping or touching intervals; the input list is not modified."""
    if not intervals:
        return []

    merged: list[tuple[int, int]] = []
    for start, end in sorted(intervals):
        if merged and start <= merged[-1][1]:
            last_start, last_end = merged[-1]
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))
    return merged
```

`sorted` returns a new list, so the caller's input is untouched. The `max` is what handles a fully
contained interval: without it, `(1, 10)` followed by `(2, 3)` would be truncated to `(1, 3)`.
Changing `start <= merged[-1][1]` to `<` implements the other convention, in which touching intervals
stay separate.

## Complexity

Time is `O(n log n)`: the sort dominates, and the sweep is a single linear pass with `O(1)` work per
interval.[^cpython-listsort-notes] Space is `O(n)` for the sorted copy and the result; the sweep
itself uses constant extra memory. On input that is already sorted, or built from a few sorted runs,
the sort in CPython is close to linear, so the practical cost drops without changing the bound.

## Edge cases

- Empty input returns an empty list.
- A single interval is returned unchanged.
- Fully contained interval: `(1, 10)` then `(2, 3)` returns `(1, 10)`.
- Touching intervals merge under this specification, and the boundary case is exactly where the
  requirement has to be confirmed rather than assumed.
- Degenerate interval where `start == end` is valid input and merges normally.
- Duplicated intervals collapse into one.
- The caller's list is unchanged after the call.

## Tests

```python
import pytest

from intervals import merge_intervals


@pytest.mark.parametrize(
    "given, expected",
    [
        ([], []),
        ([(1, 3)], [(1, 3)]),
        ([(1, 3), (2, 6), (8, 10), (15, 18)], [(1, 6), (8, 10), (15, 18)]),
        ([(1, 4), (4, 5)], [(1, 5)]),
        ([(1, 10), (2, 3)], [(1, 10)]),
        ([(5, 6), (1, 2)], [(1, 2), (5, 6)]),
        ([(1, 1), (1, 1)], [(1, 1)]),
    ],
)
def test_merge_intervals(given, expected):
    assert merge_intervals(given) == expected


def test_input_is_not_modified():
    given = [(3, 4), (1, 2)]
    merge_intervals(given)
    assert given == [(3, 4), (1, 2)]
```

## Evaluation guide

### Expected signals

- Sorts by start before sweeping, and can say why the sort is what makes one pass sufficient.
- States the complexity as `O(n log n)` time dominated by the sort, and `O(n)` extra space for the
  output.
- Handles the containment case, where the next interval ends before the current one, without
  shortening the result.
- Asks whether touching intervals such as `(1, 2)` and `(2, 3)` are to be merged, instead of guessing.

### Red flags

- A nested loop that compares every pair, presented as the intended solution.
- Mutates the caller's list with `intervals.sort()` and does not notice.
- Writes `merged[-1][1] = end` without the maximum, and so drops a contained interval.

### Level-up follow-up

Ask for the streaming version: intervals arrive one at a time, already ordered by start, and the
consumer must emit each merged block as soon as it can never grow again. It exposes whether the
candidate understands the invariant or only remembers the pattern.

## Sources

<!-- generated from frontmatter -->
