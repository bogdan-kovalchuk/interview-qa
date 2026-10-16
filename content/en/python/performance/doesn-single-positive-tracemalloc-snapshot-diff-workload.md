---
id: py-perf-0019
title: "Why doesn't a single positive `tracemalloc` snapshot diff after a workload prove a leak, and how do repeated steady-state measurements tell cache growth apart from unbounded retention?"
track: python
section: performance
sources:
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
  - source_id: py314-library-functools-functools-lru-cache
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.lru_cache
---

## Short answer

**tracemalloc tracks memory blocks allocated by Python, and comparing two snapshots is meant to find leaks.**[^py314-library-tracemalloc] One positive diff does not prove a leak: it can come from cache warm-up or lazy initialization. Warm the workload up, take several snapshots and compare the later steps: a bounded `lru_cache` does not grow without bound, but `maxsize=None` can.[^py314-library-functools-functools-lru-cache] <span class="warn">In CPython, tracemalloc does not see memory C code allocates directly with malloc(), so a clean diff does not rule out a leak in a C extension.</span>

## Detailed explanation

tracemalloc tracks memory blocks allocated by Python, not the whole process memory. A snapshot records the blocks that are alive at a given moment, and `Snapshot.compare_to()` returns the differences between two snapshots.[^py314-library-tracemalloc] Start tracing before the measured rounds: a snapshot does not include blocks allocated before tracemalloc began tracing.[^py314-library-tracemalloc] The warm-up may run before that, because only the measured rounds are compared.

A single positive difference can reflect legitimate growth: lazy initialization, cache warm-up, or a temporary structure still alive during the second snapshot. The diff does not say whether those blocks will be freed later, so one result cannot separate cache growth from retention.

The method: run the workload to steady state, take several snapshots of identical workload and compare the later pairs. `functools.lru_cache` with a `maxsize` does not grow without bound, but with `maxsize=None` it can.[^py314-library-functools-functools-lru-cache] So a plateau points to a bound, while growth at every step of the same workload points to retention that has to be traced (who holds references to the objects).

The example compares a cache with `maxsize=100` and an unbounded cache under the same workload: after warm-up, each step adds 1000 new keys (illustrative):

```python
import tracemalloc
from functools import lru_cache

@lru_cache(maxsize=100)  # bounded: at most 100 entries are kept
def bounded(key):
    return f"{key}:" + "x" * 1000

@lru_cache(maxsize=None)  # unbounded: every new key is kept
def unbounded(key):
    return f"{key}:" + "x" * 1000

next_key = 0

def workload(func):  # one round of 1000 calls, each with a new key
    global next_key
    for _ in range(1000):
        func(next_key)
        next_key += 1

def growth_per_round(func):
    workload(func)                  # warm-up before tracing: the cache fills up to its limit
    tracemalloc.start()
    s2 = tracemalloc.take_snapshot()
    workload(func)
    s3 = tracemalloc.take_snapshot()
    workload(func)
    s4 = tracemalloc.take_snapshot()
    tracemalloc.stop()
    return sum(x.size_diff for x in s4.compare_to(s3, "filename"))

print("bounded:", growth_per_round(bounded) // 1024, "KiB per round")
print("unbounded:", growth_per_round(unbounded) // 1024, "KiB per round")
# Output:
# bounded: 0 KiB per round
# unbounded: 1125 KiB per round
```

Limits: tracemalloc follows the allocations made by Python (domain 0), while C extensions can use other domains for their own resources.[^py314-library-tracemalloc] In CPython, memory that C code allocates directly with malloc() does not appear in the snapshot, so a clean diff does not prove the absence of a leak in a C extension.

**Common mistakes:**
- drawing a leak conclusion from one snapshot diff;
- starting tracemalloc after the measured rounds, so their blocks never reach the snapshot;
- treating a plateau as proof that there is no leak, including memory of C extensions;
- comparing snapshots taken around different amounts of work and reading the difference as retention.
