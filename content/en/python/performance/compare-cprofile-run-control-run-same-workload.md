---
id: py-perf-0004
title: "How do you compare a `cProfile` run with a control run on the same workload, to tell instrumentation overhead apart from a real bottleneck?"
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
  - source_id: py314-library-profile-introduction
    title: "Python 3.14: Library/profile (Introduction to the profilers)"
    url: https://docs.python.org/3.14/library/profile.html#introduction-to-the-profilers
  - source_id: py314-library-profile-limitations
    title: "Python 3.14: Library/profile (Limitations)"
    url: https://docs.python.org/3.14/library/profile.html#limitations
  - source_id: py314-library-timeit-cli
    title: "Python 3.14: Library/timeit (Command-Line Interface)"
    url: https://docs.python.org/3.14/library/timeit.html#timeit-command-line-interface
---

## Short answer

**Run the same workload twice, once under `cProfile` and once without it, on deterministic inputs, and compare the total time and the relative shares of the functions.** If the profiled run is much slower than the control run, the overhead is significant. The overhead falls on Python code, so a C implementation looks faster under the profiler than it is.[^py314-library-profile-introduction] Functions with many calls accumulate error, so their `tottime` may be inflated.[^py314-library-profile-limitations] <span class="warn">For accurate timing use `timeit`, and treat the profiler only as a tool for finding hot spots.</span>[^py314-library-profile-introduction]

## Detailed explanation

The comparison has to answer two different questions: how much time the profiler itself adds, and whether a function is really the bottleneck. For this you need two runs of the same workload: a control run without the profiler and a profiled run under `cProfile`. The Python version, the machine, the code and the inputs must be the same, and the input must be deterministic: a fixed seed or fixed data.

Take the control run as repeats. The `timeit` documentation explains that measurements can be affected by other programs on the machine, so it is better to repeat the timing several times and take the best time. The `timeit` command line does this by default, with 5 repetitions.[^py314-library-timeit-cli]

The example measures the control time without the profiler, then the same call under `cProfile`. `pstats` shows how many events the profiler recorded for `leaf`:

```python
import cProfile
import pstats
import timeit

def leaf(x):
    return x * 2

def workload():
    return sum(leaf(i) for i in range(10_000))

# Control run: no profiler, best of 5 repeats, seconds per workload call.
control = min(timeit.repeat(workload, number=20, repeat=5)) / 20

# Profiled run: the same workload with the same input.
profiler = cProfile.Profile()
profiler.runcall(workload)
stats = pstats.Stats(profiler)
profiled = stats.total_tt         # seconds, including profiler overhead

for (filename, lineno, funcname), (cc, nc, tt, ct, callers) in stats.stats.items():
    if funcname == "leaf":
        print(nc)                 # 10000 recorded calls, each with profiler work
print(control > 0 and profiled > 0)   # True
```

The difference between `profiled` and `control` is the overhead, including the work the profiler does between events. It cannot simply be subtracted from the results of individual functions, because it is distributed unevenly. The documentation explains that the overhead falls on Python code, not on C-level functions, so a C implementation looks faster under the profiler than it is.[^py314-library-profile-introduction] The error also accumulates in functions that are called many times, so a small function with many calls can get an inflated `tottime`.[^py314-library-profile-limitations]

To tell overhead apart from a real bottleneck, check a change on the control run, not on the profile. If a function really dominates, optimising it reduces the control time by roughly its share of that time. If a function looks heavy only in the profile and the control time does not change, the profile overstated that function's share of the real time.

**Common mistakes:**
- treating a function as a hot spot only because of its `tottime` in the profile, without a control run;
- comparing a profiled run with a control run on different inputs or in different processes;
- taking a single control measurement instead of repeats.
