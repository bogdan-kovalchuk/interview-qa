---
id: py-itergen-0007
title: "Why can a generator pipeline reduce peak memory but not necessarily total execution time?"
track: python
section: iterators-and-generators
sources:
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
---

## Short answer

**Each stage yields one item per `next()` call.**[^py314-library-stdtypes-iterator-types] So a generator pipeline builds no intermediate lists and lowers peak memory: in the measurement in the explanation, the peak fell from about 81 MB to about 0.001 MB. The amount of work is unchanged: every item still passes through every stage, so total execution time is not reduced automatically and must be measured. Peak memory still includes whatever the source holds and whatever is collected into a list.

## Detailed explanation

A pipeline built from generators is a chain of iterators. The consumer calls `next()` on the last stage, which calls `next()` on the previous one, and so on back to the source.[^py314-library-stdtypes-iterator-types] So at any moment only one item moves through the chain, and no intermediate list is needed. Peak memory is determined by what the stages hold at the same time, plus the source and the result if they are complete lists.

Below are two versions of the same computation: one with intermediate lists and one with a chain of generator expressions.

```python
import tracemalloc

N = 1_000_000

def peak_mb(fn):
    tracemalloc.start()
    fn()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return round(peak / 1e6, 3)

def eager():
    a = [x * 2 for x in range(N)]      # intermediate list
    b = [x + 1 for x in a]             # second intermediate list
    return sum(b)

def lazy():
    a = (x * 2 for x in range(N))      # generator, no list
    b = (x + 1 for x in a)
    return sum(b)

print(peak_mb(eager))                  # 80.889
print(peak_mb(lazy))                   # 0.001
```

In this run on CPython 3.14, the eager version held about 81 MB, while the chain over `range` held about 0.001 MB. When the source is already a finished list of a million items, the list itself takes about 40 MB (building `list(range(1_000_000))` under tracemalloc gives a peak of 39.992 MB), and the pipeline over it adds about 0.001 MB. The saving concerns intermediate sequences, not everything that is in memory.

Time is a separate question. A pipeline does not reduce the amount of work: every item passes through every stage. In CPython, the switches between generator frames add overhead, while the large intermediate lists disappear. So total execution time depends on the balance of these effects, and there is no guarantee that it decreases. The timings were taken with the `eager` and `lazy` functions above, the best of 5 runs with `time.perf_counter`, `N = 1_000_000`. On CPython 3.14 the eager version took about 0.09–0.10 s and the lazy one about 0.05 s; on CPython 3.13 the eager version took about 0.10 s and the lazy one 0.06–0.09 s. In these runs the lazy version was faster, but the exact numbers depend on the machine, so measure on your own data.

**Common mistakes:**
- assuming a generator pipeline is always faster because it builds no lists;
- forgetting that a source which is already a list keeps all its items in memory;
- collecting the result with `list(...)` and expecting a low peak memory.
