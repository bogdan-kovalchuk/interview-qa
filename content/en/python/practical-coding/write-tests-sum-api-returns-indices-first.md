---
id: py-prac-0023
title: "Write tests for a Two Sum API that returns the indices of the first pair in lexicographic order, never uses an element twice, and returns `None` when there is no solution."
track: python
section: practical-coding
sources:
  - source_id: py314-reference-expressions-value-comparisons
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#value-comparisons
  - source_id: py314-library-unittest-assertequal
    title: "Python 3.14: Library/unittest"
    url: https://docs.python.org/3.14/library/unittest.html#unittest.TestCase.assertEqual
---

## Short answer

**The tests check four properties: the pair's sum equals target, the pair `(i, j)` with `i < j` is the lexicographically smallest, no index is used twice, and `None` is returned when there is no solution.** Tuples in Python compare by their first unequal element.[^py314-reference-expressions-value-comparisons] Cases: `[2,7,11,15], target=9 -> (0,1)`; `[3,2,4], target=6 -> (1,2)`, not `(0,0)`; `[1,2,3], target=100 -> None`; an empty list, negative numbers, duplicate values.

## Detailed explanation

Tests for `two_sum` check the function's contract, not its current implementation. The contract is this: the function returns a pair `(i, j)` with `i < j` for which `nums[i] + nums[j] == target`. Among all such pairs it returns the lexicographically smallest one, and `None` if there is no pair. Each case checks one property, so a failing test points directly to the broken rule.

**Lexicographic order** is the most subtle requirement. Tuples compare by their first unequal element.[^py314-reference-expressions-value-comparisons] So `(0, 3)` is smaller than `(1, 2)`: the first elements, `0` and `1`, differ, and they decide the result. For `[1, 2, 3, 4]` and `target=5` there are two pairs with sum 5: `(0, 3)` and `(1, 2)`. The correct answer is `(0, 3)`. An implementation with the outer loop over `j` finds `(1, 2)` first, and the test with this input catches that mistake.

**Reusing an index.** An inner loop that starts at `0` allows `j == i`. For `[3, 2, 4]` and `target=6`, the pair `(0, 0)` gives `3 + 3 == 6`, although the element is used twice. Below is a faulty implementation and the test that catches it. The test expects `(1, 2)`. `assertEqual` compares the expected value with the result and fails when they are not equal.[^py314-library-unittest-assertequal]

```python
import unittest


def two_sum_reuse(nums, target):
    # Bug: j may equal i, so one element is used twice.
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None


class TestTwoSum(unittest.TestCase):
    def test_element_not_reused(self):
        # Fails with: AssertionError: Tuples differ: (0, 0) != (1, 2)
        self.assertEqual(two_sum_reuse([3, 2, 4], 6), (1, 2))


if __name__ == "__main__":
    unittest.main()
```

A correct implementation starts the inner loop at `i + 1`, so `j` is always greater than `i`.

**Edge cases.** An empty list and a list with one element return `None`, because a pair must consist of two different indices. Negative numbers: `[-3, 4, 3, 90]` with `target=0` gives `(0, 2)`, so the test does not rely on positive values. Duplicates: `[3, 3]` with `target=6` gives `(0, 1)`: two different indices with the same value form a legal pair.

**Limits.** A few fixed cases do not prove correctness for every input. For larger inputs you can compare the function with a simple brute-force search as a reference, or use property-based tests. The reference must be obviously correct, otherwise two identical mistakes would pass the check together.

**Common mistakes:**
- checking only `sum == target`, without the order and without forbidding index reuse;
- writing the expected result without working out which pair is lexicographically smallest;
- not testing `None` and the empty input, so an implementation that raises an exception instead of returning `None` goes unnoticed.
