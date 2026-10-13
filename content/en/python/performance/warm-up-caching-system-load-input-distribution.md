---
id: py-perf-0003
title: "How can warm-up, caching, system load, and input distribution skew a microbenchmark result?"
description: "Warm-up, caches, background load and unrepresentative inputs can skew a microbenchmark: the first run pays for warm-up, caches return stored results, and synthetic inputs may not match real ones."
track: python
section: performance
level: senior
type: pitfall
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-profile
    title: "Python 3.14: Library/profile"
    url: https://docs.python.org/3.14/library/profile.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-timeit
    title: "Python 3.14: Library/timeit"
    url: https://docs.python.org/3.14/library/timeit.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-faq-programming-performance
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#performance
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-functools-functools-lru-cache
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.lru_cache
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-timeit-repeat
    title: "Python 3.14: Library/timeit (Timer.repeat)"
    url: https://docs.python.org/3.14/library/timeit.html#timeit.Timer.repeat
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: timeit.Timer.repeat and its note that the minimum is the lower bound and that other processes cause higher values. Does not describe caches or warm-up."
  - source_id: py314-howto-sorting
    title: "Python 3.14: Sorting HOWTO (Sort Stability and Complex Sorts)"
    url: https://docs.python.org/3.14/howto/sorting.html#sort-stability-and-complex-sorts
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: Timsort, the sorting algorithm used in Python, takes advantage of any ordering already present in the data. Does not state a number of comparisons."
---

## Short answer

**Warm-up, caching, system load, and input distribution change what a benchmark measures, not only the code's pure performance.** Background processes add time, so higher values in repeats are usually caused by them.[^py314-library-timeit-repeat] `lru_cache` keeps the results of the most recent calls, so a repeated call with the same arguments may not run the function at all.[^py314-library-functools-functools-lru-cache] Input data matters too: Timsort, the sorting algorithm used in Python, takes advantage of any ordering already present in the data.[^py314-howto-sorting] <span class="warn">Tip: take `min()` over repeats and test on several input distributions.</span>

## Detailed explanation

A benchmark measures execution under specific conditions, not an abstract property of the code. The first run may include importing a module, if the import sits in the measured code, and cold CPU caches, so it is usually slower than the runs that follow. Repeats with `min()` cut such runs off: the smallest value in the series is the closest to the cost of the code without these effects.

A cache changes the very work being measured. `functools.lru_cache` stores the results of up to `maxsize` most recent calls, and it can save time when an expensive function is periodically called with the same arguments.[^py314-library-functools-functools-lru-cache] If the first call fills the cache and the repeats take the result from it, the smallest timing describes a cache lookup rather than the computation. Caching at the OS or application level can have the same effect; it is visible only when you compare against a run with the cache disabled.

System load adds noise unevenly: background processes, the OS scheduler and other programs on the machine shift individual timings. The `timeit` documentation describes this directly: higher values in repeats are usually caused by other processes interfering with the timing accuracy.[^py314-library-timeit-repeat]

The input also changes the execution path itself. Timsort, the sorting algorithm used in Python, takes advantage of any ordering already present in the data.[^py314-howto-sorting] A comparison counter shows the difference on lists of the same size (in CPython):

```python
class Counted:
    count = 0

    def __init__(self, value):
        self.value = value

    def __lt__(self, other):
        Counted.count += 1
        return self.value < other.value

n = 1000
already_sorted = [Counted(i) for i in range(n)]
permuted = [Counted((i * 7919) % n) for i in range(n)]   # a permutation of 0..999

Counted.count = 0
sorted(already_sorted)
print(Counted.count)              # 999: one comparison per adjacent pair (CPython)

Counted.count = 0
sorted(permuted)
print(Counted.count)              # 8532: about 8.5 times more on the same-size input (CPython)
```

The same `sorted()` call makes 999 comparisons on an already sorted list and 8532 on a permutation of 1000 elements. A synthetic input that looks typical but does not match the real distribution can show faster or slower work than the application will see.

In practice: repeat the measurement and take `min()`, separate warm-up from the timed part, test several input distributions, and state what is cached. These do not replace one another: repetition does not remove the effect of a cache, and a cache does not remove noise.

**Common mistakes:**
- treating one measurement after the import as a stable estimate;
- comparing a cached variant with an uncached one without accounting for the cache;
- testing only on inputs that favour the implementation (already sorted or uniform ones).

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
