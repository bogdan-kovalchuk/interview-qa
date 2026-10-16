---
id: py-perf-0005
title: "How do you verify that an asymptotically better algorithm actually wins on representative input sizes and distributions?"
track: python
section: performance
sources:
  - source_id: py314-library-profile
    title: "Python 3.14: Library/profile"
    url: https://docs.python.org/3.14/library/profile.html
  - source_id: py314-library-timeit
    title: "Python 3.14: Library/timeit"
    url: https://docs.python.org/3.14/library/timeit.html
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
---

## Short answer

**You can check this with a benchmark on input sizes `n` close to production and on several input distributions, comparing the best time of several `timeit` repeats.**[^py314-library-timeit] An asymptotically better complexity (for example `O(n log n)` versus `O(n²)`, where the first is the classic bound for comparison sorting) does not guarantee a win at a specific `n`, because larger constants can dominate at small sizes. First use `profile` to see where the workload spends its time, and `tracemalloc` to see how much memory each variant allocates.[^py314-library-profile][^py314-library-tracemalloc]

## Detailed explanation

Asymptotic complexity describes how the running time grows as `n` increases, but it does not say which of two algorithms is faster at a specific `n`. The running time is roughly `c*f(n)` plus overhead, where the constants `c` depend on the implementation, the data structures and the Python version. So an algorithm with a better asymptotic class can lose at small sizes. The check has to establish which `n` the system actually runs at and which input distributions occur there.

For each variant, take the best time of several repeats, because single measurements are noisy; the `timeit` documentation recommends exactly this.[^py314-library-timeit] The example below compares two ways to remove duplicates: sorting, which is O(n log n) (the classic bound for comparison sorting; no source is cited here), and scanning a list of unique values, which costs O(n*u), where `u` is the number of distinct values. The code prints the winner for each `n`:

```python
import random
import timeit

def unique_sorted(xs):
    # O(n log n): sort first, then drop neighbouring duplicates
    out = []
    for x in sorted(xs):
        if not out or out[-1] != x:
            out.append(x)
    return out

def unique_scan(xs):
    # O(n*u), u = number of distinct values: each test scans the list so far
    out = []
    for x in xs:
        if x not in out:
            out.append(x)
    return out

random.seed(1)
for n in (8, 64, 512, 4096):
    data = [random.randrange(n) for _ in range(n)]
    number = max(1, 1000 // n)
    # best of 5 repeats, as the timeit docs recommend
    a = min(timeit.repeat(lambda: unique_sorted(data), number=number, repeat=5))
    b = min(timeit.repeat(lambda: unique_scan(data), number=number, repeat=5))
    print(n, 'scan' if b < a else 'sort')

# expected output (CPython 3.13 and 3.14):
# 8 scan
# 64 sort
# 512 sort
# 4096 sort
```

The winner depends on the distribution, not only on `n`: the scan can win when `u` is much smaller than `n`, because it then runs in nearly linear time; when the values are mostly distinct, as in the example above, sorting wins. So a benchmark needs random, nearly sorted and heavily duplicated data. The conclusion holds only for the sizes, distributions, Python version and machine that were measured.

`timeit` turns off the garbage collector during timing by default, so GC costs of the real program may not show up in the number.[^py314-library-timeit] `profile` is for finding where time goes, not for benchmarking: it adds overhead to Python code, so compare the variants with `timeit`.[^py314-library-profile]

**Common mistakes:**
- comparing at one `n`, for example 1000, and extending the conclusion to other sizes;
- testing only random data while production has many duplicates or nearly sorted data;
- taking one measurement or an average instead of the best time of several repeats;
- benchmarking a function in isolation when its cost in the system is set by other code.
