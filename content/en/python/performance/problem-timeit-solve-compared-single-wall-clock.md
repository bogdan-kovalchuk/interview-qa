---
id: py-perf-0002
title: "What problem does `timeit` solve compared to a single wall-clock time measurement?"
description: "Repeats in timeit give a smallest value that is a lower bound on the code's speed; larger values are usually caused by other processes that disturb the timing."
track: python
section: performance
level: middle
type: mechanism
tags: [timeit]
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
  - source_id: py314-library-timeit-repeat
    title: "Python 3.14: Library/timeit (Timer.repeat)"
    url: https://docs.python.org/3.14/library/timeit.html#timeit.Timer.repeat
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: timeit.Timer.repeat and its note that the minimum is the lower bound and that higher values are caused by other processes. Does not describe setup or GC."
  - source_id: py314-library-timeit-timeit
    title: "Python 3.14: Library/timeit (Timer.timeit)"
    url: https://docs.python.org/3.14/library/timeit.html#timeit.Timer.timeit
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: timeit.Timer.timeit runs setup once, returns the time of the main statement, turns off garbage collection during timing, and defaults number to 1000000."
  - source_id: py314-library-timeit-autorange
    title: "Python 3.14: Library/timeit (Timer.autorange)"
    url: https://docs.python.org/3.14/library/timeit.html#timeit.Timer.autorange
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: timeit.Timer.autorange increases the number of loops until the total time is at least 0.2 seconds."
  - source_id: py314-library-timeit-default-timer
    title: "Python 3.14: Library/timeit (default_timer)"
    url: https://docs.python.org/3.14/library/timeit.html#timeit.default_timer
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the default timer is always time.perf_counter(). Does not describe other timers."
  - source_id: py314-library-timeit-cli
    title: "Python 3.14: Library/timeit (Command-Line Interface)"
    url: https://docs.python.org/3.14/library/timeit.html#timeit-command-line-interface
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the command-line interface picks the number of loops automatically, repeats the timing 5 times by default, and recommends the best time."
  - source_id: py314-library-time-time
    title: "Python 3.14: Library/time (time.time)"
    url: https://docs.python.org/3.14/library/time.html#time.time
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: time.time can return a lower value than a previous call if the system clock has been set back. It is not a monotonic clock."
  - source_id: py314-library-profile-introduction
    title: "Python 3.14: Library/profile (Introduction to the profilers)"
    url: https://docs.python.org/3.14/library/profile.html#introduction-to-the-profilers
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the profilers are meant for an execution profile, not for benchmarking; for reasonably accurate results it refers to timeit."
---

## Short answer

**`timeit` addresses measurement noise through repetition: the smallest value from repeats is a lower bound on how fast the code can run, because larger values are usually caused by other processes.**[^py314-library-timeit-repeat] While timing, it turns off the garbage collector,[^py314-library-timeit-timeit] and the command line picks the number of loops itself and repeats the timing 5 times by default.[^py314-library-timeit-cli] A single measurement with `time.time()` has none of these safeguards, and its value can also drop if the system clock is set back.[^py314-library-time-time]

## Detailed explanation

A single measurement (the difference of two `time.time()` readings) records everything that the OS and other processes did in that interval. `time.time()` can also return a lower value than a previous call if the system clock has been set back.[^py314-library-time-time] Noise from other processes only adds time, so the smallest of several repeats is closer to the real cost of the code. The `timeit` documentation explains it this way: the lowest value gives a lower bound, higher values are usually caused by other processes, so the mean and the standard deviation are not very useful.[^py314-library-timeit-repeat]

`timeit` automates part of the work, but not all of it. The setup runs once, `timeit()` returns the time of the main statement only, and the garbage collector is turned off during timing so that the timings are more comparable. The number of loops (`number`) defaults to 1,000,000 and is set by you.[^py314-library-timeit-timeit] The default timer is `time.perf_counter()`.[^py314-library-timeit-default-timer] `autorange()` provides the automatic choice of the count: it increases it until the total time is at least 0.2 s.[^py314-library-timeit-autorange]

The example shows that the GC is off during timing, and that `repeat()` returns a list of 5 timings, from which the smallest is taken:

```python
import gc
import timeit

# The statement runs with the garbage collector turned off.
timer = timeit.Timer('print(gc.isenabled())', setup='import gc')
timer.timeit(1)                   # prints False: timeit disables GC while timing
print(gc.isenabled())             # True: the state is restored afterwards

times = timeit.repeat('sum(range(1000))', number=1000, repeat=5)
print(len(times))                 # 5: one total time per repeat
best = min(times)                 # the lower bound; higher values are usually noise
```

The smallest timing is an estimate for this code on this machine, with this Python version and this load, not a universal constant. Compare variants in the same way and with the same `setup`. For accurate timing, a profiler is the wrong tool: the profiling documentation refers to `timeit` for that.[^py314-library-profile-introduction]

**Common mistakes:**
- taking the mean of a single measurement or of the repeats instead of `min()`;
- assuming that `Timer.timeit()` returns the minimum by itself: it returns the time of one run of `number` iterations;
- running in `stmt` what belongs in `setup` (for example, creating data), because it is repeated on every iteration.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
