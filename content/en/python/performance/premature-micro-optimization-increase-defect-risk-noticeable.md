---
id: py-perf-0018
title: "Why can premature micro-optimization increase defect risk without a noticeable user-level benefit?"
track: python
section: performance
sources:
  - source_id: py314-library-profile
    title: "Python 3.14: Library/profile"
    url: https://docs.python.org/3.14/library/profile.html
  - source_id: py314-library-timeit
    title: "Python 3.14: Library/timeit"
    url: https://docs.python.org/3.14/library/timeit.html
  - source_id: py314-faq-programming-performance
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#performance
  - source_id: py314-library-functools-functools-lru-cache
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.lru_cache
---

## Short answer

**Micro-optimization changes working code before profiling has shown that this exact spot is the bottleneck.**[^py314-faq-programming-performance] Such a change often does not change user-visible latency: a cache whose arguments never repeat never hits, yet adds memory and code, and a hand-written replacement or a premature C extension adds places for bugs and makes testing harder. <span class="warn">Profile first, then find the hot spot, then optimize exactly that; otherwise the effort goes into code that does not determine the user experience.</span>

## Detailed explanation

Micro-optimization is a local change that speeds up a small piece of code: another way to compute the same thing, a hand-written replacement for a standard function, a cache, or a C extension. The trap is making such a change blind. The FAQ advises finding the hot spots in the program first, and says that making algorithms faster can yield much larger benefits than sprinkling micro-optimization tricks across the code.[^py314-faq-programming-performance] To locate hot spots, use `profile`: its internal time statistics can identify hot loops that are worth optimizing.[^py314-library-profile]

Defect risk grows with complexity: more complex code has more branches and edge cases that need tests, and without tests an optimization can silently break behaviour that nobody checks. This is why the FAQ recommends good test coverage before introducing sophisticated optimizations.[^py314-faq-programming-performance]

An example is a cache where no argument repeats. `lru_cache(maxsize=None)` disables the size limit, and the cache can grow without bound.[^py314-library-functools-functools-lru-cache] In the code below every argument is new, so the cache never hits and only accumulates entries:

```python
from functools import lru_cache

@lru_cache(maxsize=None)  # unbounded: every new argument adds an entry
def parse_id(raw):
    return int(raw)

for i in range(5):
    parse_id(str(i))         # every argument is new, so the cache never hits
print(parse_id.cache_info())
# CacheInfo(hits=0, misses=5, maxsize=None, currsize=5)
```

The code is correct, but for these calls the cache gave no benefit: only memory and an extra decorator line remain.

Even a genuinely faster piece of code does not change the end-to-end time if the bottleneck is elsewhere, for example in I/O, the network or SQL. So profile first, then optimize exactly the hot spot. Otherwise the effort goes into code that does not determine the user experience, and the regression risk remains.

**Common mistakes:**
- optimizing a function because it "looks slow" without profiling;
- adding a cache without checking whether arguments will repeat;
- rewriting code for a micro-gain without tests for its behaviour;
- assuming that a faster local piece automatically makes the request faster.
