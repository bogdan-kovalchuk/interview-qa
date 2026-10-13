---
id: py-perf-0016
title: "When does moving a hot loop to a vectorized or native implementation justify the boundary-crossing and data-conversion cost?"
description: "When does moving a hot loop to a vectorized or native implementation justify the boundary-crossing and data-conversion cost?"
track: python
section: performance
level: senior
type: practical
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-array
    title: "Python 3.14: Library/array"
    url: https://docs.python.org/3.14/library/array.html#module-array
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Description of the array module: a type that compactly represents an array of basic values of one type. Does not describe the cost of converting from a list."
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
---

## Short answer

**Moving a hot loop to a vectorized or native implementation is justified when, among other conditions, the work per element is high and there is enough data to offset the fixed cost of crossing from Python and converting the data.** First find the hot spot; the profile module exists for that.[^py314-faq-programming-performance] The threshold depends on code, data and machine, so measure at representative sizes. If each element carries little work, or the data is converted back and forth on every call, the boundary-crossing and data-conversion cost can consume the gain.

## Detailed explanation

Moving a loop into native code (a vectorized library or a C extension) makes sense when the loop itself is the bottleneck. The FAQ advises finding hot spots before optimizing anything, and the profile module is the tool for that.[^py314-faq-programming-performance] In profile, `tottime` is the time spent in the function itself, excluding calls to subfunctions, so it shows where the work is concentrated.[^py314-library-profile] If the loop takes only a small share of the time, moving it will not change the total time, even if the loop itself becomes much faster.

The crossing cost has three parts: the fixed cost of calling from Python, converting arguments and results, and the work itself. The gain appears when the work per element is large relative to the first two. Primitives written in C are usually faster than Python code you write yourself: the FAQ says a standard-library primitive is likely (though not guaranteed) to be faster than an alternative you write, and that this is doubly true for primitives written in C.[^py314-faq-programming-performance]

Conversion is often the hidden cost. The `array` module describes itself as a type that compactly represents an array of basic values,[^py314-library-array] so building an array from a list of Python objects means copying every value:

```python
from array import array

values = [float(i) for i in range(1_000_000)]  # 1,000,000 Python float objects
packed = array('d', values)                    # one O(n) conversion into C doubles
print(packed[:3])                              # array('d', [0.0, 1.0, 2.0])
```

If such an array is rebuilt on every call, the conversion repeats. With simple arithmetic per element it can equal the work or exceed it, so keep the data in native form between calls.

Compare variants with `timeit`, on the same data and sizes as in production. The documentation recommends repeating the timing and taking the best result, because other programs on the same machine can affect it.[^py314-library-timeit] Do not compare a Python loop profiled under cProfile with a C function: the profiler adds overhead to Python code but not to C-level functions, so the C code looks faster in that comparison than it really is.[^py314-library-profile]

**Common mistakes:**
- moving the loop without profiling, when the hot spot is elsewhere;
- measuring on small data, where the crossing takes most of the time, and drawing conclusions for large data;
- converting the data back and forth on every step;
- comparing time measured under a profiler with the time of a C function.

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
