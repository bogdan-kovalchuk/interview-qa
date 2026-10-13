---
id: py-prac-0024
title: "Write tests for a maximum-overlapping-intervals function: intervals are closed `[start, end]`, so start and end at the same instant count as overlapping."
description: "Write tests for a maximum-overlapping-intervals function: intervals are closed `[start, end]`, so start and end at the same instant count as overlapping."
track: python
section: practical-coding
level: middle
type: practical
tags: [start-end]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-tutorial-controlflow-the-range-function
    title: "Python 3.14: Tutorial/control flow"
    url: https://docs.python.org/3.14/tutorial/controlflow.html#the-range-function
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: range() never includes its end point, and its start point is included."
  - source_id: py314-reference-expressions-value-comparisons
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#value-comparisons
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: tuples and other sequences compare by their first unequal element."
---

## Short answer

**The key boundary is closed intervals: touching `[1,5]` and `[5,10]` give overlap == 2 at point 5.** Unlike `range(1, 5)`, which does not contain 5,[^py314-tutorial-controlflow-the-range-function] a closed interval contains both ends. Tests: full nesting `[(1,10),(2,9),(3,8)] -> 3`; no intersection `[(1,3),(5,7)] -> 1`; empty list -> 0; one interval -> 1; all identical `[(1,5)]*4 -> 4`; degenerate `[(3,3),(3,3)] -> 2`.

## Detailed explanation

The function `max_overlap` takes a list of closed intervals `[start, end]` and returns the largest number of intervals that share a common point. Closed means that both ends belong to the interval. So `[1, 5]` and `[5, 10]` share the point 5, and their overlap is 2. This boundary should be tested first, because it breaks easily with a wrong comparison.

Python's built-in `range` uses a different, half-open, model: the end point is not part of the sequence.[^py314-tutorial-controlflow-the-range-function] If you carry this model over to intervals, `[1, 5]` and `[5, 10]` stop intersecting, and the function returns 1. To prevent this, a sweep-line algorithm handles events with the same coordinate in this order: start before end. The events are stored as tuples `(coordinate, kind)`, and `events.sort()` sorts them lexicographically, so `(5, 0)` (a start) comes before `(5, 1)` (an end).[^py314-reference-expressions-value-comparisons]

The implementation and two tests are below. A half-open variant, in which an end is handled before a start at the same coordinate, gives `AssertionError: 1 != 2` on the touching test, so touching must be checked explicitly.

```python
import unittest


def max_overlap(intervals):
    # Closed intervals: at the same coordinate, starts are handled before ends.
    events = []
    for start, end in intervals:
        events.append((start, 0))  # 0 = start
        events.append((end, 1))    # 1 = end
    events.sort()
    best = current = 0
    for _, kind in events:
        if kind == 0:
            current += 1
            best = max(best, current)
        else:
            current -= 1
    return best


class TestMaxOverlap(unittest.TestCase):
    def test_touching_closed_intervals(self):
        # [1, 5] and [5, 10] both contain the point 5.
        self.assertEqual(max_overlap([(1, 5), (5, 10)]), 2)

    def test_degenerate_intervals(self):
        self.assertEqual(max_overlap([(3, 3), (3, 3)]), 2)


if __name__ == "__main__":
    unittest.main()
```

The degenerate case `[(3, 3), (3, 3)]` gives 2: both intervals contain the point 3, so the test checks that equal starts and ends do not cancel each other out. An empty list gives 0, one interval gives 1, and `[(1, 5)] * 4` gives 4. These cases check that the counter goes up and down correctly.

**Limits.** Fixed cases do not prove correctness for every interval. For random data, a reference implementation based on a simpler algorithm or property-based tests are useful.

**Common mistakes:**
- testing only disjoint and nested intervals and skipping the touching case;
- assuming that `[1, 5]` and `[5, 10]` do not intersect because `range(1, 5)` does not contain 5;
- sorting events without a rule for equal coordinates, which changes the answer.

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
