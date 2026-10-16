---
id: py-perf-0007
title: "Why isn't Big O enough to predict latency without the input size, constants, and memory-access behaviour?"
track: python
section: performance
sources:
  - source_id: py314-library-profile
    title: "Python 3.14: Library/profile"
    url: https://docs.python.org/3.14/library/profile.html
  - source_id: py314-library-array
    title: "Python 3.14: Library/array"
    url: https://docs.python.org/3.14/library/array.html#module-array
  - source_id: cpython-listobject-h
    title: "CPython 3.14: Include/cpython/listobject.h"
    url: https://github.com/python/cpython/blob/v3.14.6/Include/cpython/listobject.h
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
---

## Short answer

**Big O describes only growth at large `n` and drops constant factors, so on practical sizes it does not decide which code is faster.** Two algorithms of the same complexity can differ several times over because of interpreter overhead, and the layout of data in memory changes latency. For measurement use `timeit`, not a profiler, because a profiler adds overhead itself.[^py314-library-profile]

## Detailed explanation

Big O is an upper bound on growth as `n` tends to infinity, and the multipliers are deliberately dropped. For a specific `n` the time is the multiplier times each step plus overhead, so two algorithms of the same complexity can differ several times over. Example: both variants search for the last value in a list of 100 000 items and both are O(n), but the Python loop runs every iteration through the interpreter, while `list.index` runs in C:

```python
def python_find(seq, value):
    for index, item in enumerate(seq):   # every step runs through the interpreter
        if item == value:
            return index
    return -1

data = list(range(100_000))
print(python_find(data, 99_999))   # 99999
print(data.index(99_999))          # 99999: same O(n) scan, but the loop runs in C
```

Constants can also change the order between different classes. Suppose one algorithm takes about `50*n*log2(n)` arbitrary units and another takes `2*n**2`. At `n = 100` the quadratic one is faster (about 20 000 against 33 200), and at `n = 1000` the `n log n` one is faster (about 498 000 against 2 000 000). These are arithmetic values of an assumed model, not measurements; in your code they have to be measured.

The second factor is memory. A `list` in CPython stores a vector of pointers to its elements, so walking the list also touches the objects themselves, which sit at separate places in memory.[^cpython-listobject-h] The `array` module compactly represents an array of basic values.[^py314-library-array] This usually fits the processor cache better, but the effect depends on size, platform and access pattern, so it must be measured rather than assumed. For the volume of allocations, `tracemalloc` shows statistics per line of code.[^py314-library-tracemalloc]

In practice, `profile` first shows where time goes in the whole workload,[^py314-library-profile] and then candidates are compared with `timeit` at the real `n` and on real data. Big O stays useful as `n` grows: for a large enough `n` the asymptotics outweigh any constant. For decisions at specific sizes it does not replace measurement.

**Common mistakes:**
- assuming that the same Big O means the same latency;
- choosing an algorithm without estimating the real size `n`;
- explaining a difference by cache effects where interpreter overhead dominates.
