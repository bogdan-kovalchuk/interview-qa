---
id: py-perf-0001
title: "How does a deterministic profiler measure call counts and time, and why must its instrumentation overhead be taken into account when interpreting results?"
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
  - source_id: py314-library-profile-deterministic
    title: "Python 3.14: Library/profile (What Is Deterministic Profiling?)"
    url: https://docs.python.org/3.14/library/profile.html#what-is-deterministic-profiling
  - source_id: py314-library-profile-stats
    title: "Python 3.14: Library/profile (Analysis of the Profile Data)"
    url: https://docs.python.org/3.14/library/profile.html#profile-stats
  - source_id: py314-library-profile-limitations
    title: "Python 3.14: Library/profile (Limitations)"
    url: https://docs.python.org/3.14/library/profile.html#limitations
  - source_id: py314-library-profile-introduction
    title: "Python 3.14: Library/profile (Introduction to the profilers)"
    url: https://docs.python.org/3.14/library/profile.html#introduction-to-the-profilers
---

## Short answer

**A deterministic profiler (for example `cProfile`) records call, return and exception events and measures the intervals between them: `ncalls` is the number of calls, `tottime` the time in the function itself, and `cumtime` the time including subfunctions.**[^py314-library-profile-deterministic] The delay between an event and the clock reading accumulates in functions that are called many times.[^py314-library-profile-limitations] `cProfile` has moderate overhead, while `profile` (pure Python) adds significantly more.[^py314-library-profile-introduction] The profiler gives an execution profile, not an accurate benchmark.[^py314-library-profile-introduction]

## Detailed explanation

Deterministic profiling does not sample; it follows the execution. The interpreter reports every call, return and exception event to the profiler, and the time between events is attributed to functions.[^py314-library-profile-deterministic] This gives three report columns that are usually read together. `ncalls` is how many times a function was called. `tottime` is the time spent in the function itself, without subfunctions, and `cumtime` includes the subfunctions.[^py314-library-profile-stats] So `tottime` shows where time is spent directly, and `cumtime` shows how much work a call covers.

The call counter is easiest to see in an example. The function `leaf` is called 10,000 times from a generator expression, and each call is recorded as a separate event:

```python
import cProfile
import pstats

def leaf(x):
    return x * 2

def workload():
    return sum(leaf(i) for i in range(10_000))

profiler = cProfile.Profile()
profiler.runcall(workload)
stats = pstats.Stats(profiler)
for (filename, lineno, funcname), (cc, nc, tt, ct, callers) in stats.stats.items():
    if funcname == "leaf":
        print(nc)                 # 10000: every call is recorded
        print(cc == nc)           # True: leaf is not recursive
```

Overhead matters more than the counter. The profiler runs its own code between events, and that work ends up in the measured time. The documentation explains that the delay from an event until the clock is read accumulates in functions that are called many times or that call many functions, so their times can be inflated.[^py314-library-profile-limitations] For typical applications, the overhead of deterministic profiling is small.[^py314-library-profile-deterministic] For small functions with many calls, the distortion is noticeable.[^py314-library-profile-limitations]

The choice of tool also matters. `cProfile` is a C extension with reasonable overhead and is recommended for most users, while `profile`, a pure Python module, adds significantly more.[^py314-library-profile-introduction] For accurate timing, the documentation points to `timeit`, because the profilers are meant for an execution profile, not for benchmarking.[^py314-library-profile-introduction] Read the absolute numbers from a profile as inflated. The relative order of functions and the call counts are useful for finding candidates, but they must be confirmed with a control measurement.

**Common mistakes:**
- taking `tottime` or `cumtime` from a profile as the exact time of a function;
- confusing `tottime` with `cumtime` and looking for the bottleneck among top-level calls, which cover almost the whole run;
- ignoring that small functions with many calls are the most distorted by overhead.
