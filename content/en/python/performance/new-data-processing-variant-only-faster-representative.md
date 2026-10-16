---
id: py-perf-0017
title: "A new data-processing variant is only 2% faster on a representative benchmark but noticeably more complex: how do you justify the choice based on latency budget and maintenance cost?"
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
---

## Short answer

**If a 2% improvement does not bring the system closer to its latency budget or change its scalability, the more complex variant is usually not worth adopting.** Criteria: (1) does it move the system closer to the SLO or latency target, (2) does throughput change enough to postpone scaling, (3) does the code get harder to read, test or debug. The FAQ recommends good test coverage before sophisticated optimizations, because they may hide regressions.[^py314-faq-programming-performance] Make sure 2% exceeds the spread of repeated runs: timeit recommends the best of several repeats.[^py314-library-timeit]

## Detailed explanation

A percentage alone decides nothing. A 2% gain matters only if it changes something the system cares about. A latency budget is the acceptable delay for a request or processing step. If the system already fits its budget, a 2% speed-up does not change whether it meets the target. So first record the budget and the current margin, and only then compare the variants.

Repeated measurement, not a single run, shows whether 2% is real. The timeit documentation notes that other programs on the same machine affect the result, so it is best to repeat the timing and take the best time.[^py314-library-timeit] Profiling modules are not meant for benchmarking: they provide an execution profile of a program, and for reasonably accurate timings there is timeit.[^py314-library-profile] Use the profiler to see where a gain came from, and timeit to get numbers you can compare.

Maintenance cost is concrete work: every extra branch, special case or invariant has to be understood during review, tested on each change and explained to a colleague. The FAQ recommends good test coverage before sophisticated optimizations, because they may hide regressions.[^py314-faq-programming-performance] So a 2% gain bought with obscure code can be a worse decision than making no change.

Example: processing takes 40 ms against a 50 ms budget. The variant gives 2%, that is `40 * 0.98 = 39.2` ms. The budget is already met, so the more complex code fixes nothing. If processing takes 52 ms instead, `52 * 0.98 = 50.96` ms: the budget is still exceeded by 0.96 ms, and a 2% gain does not close the gap. The percentage only means something together with the budget.

**Common mistakes:**
- treating 2% as a gain without repeated measurements and without comparing it with the budget;
- comparing variants with the profiler instead of timeit;
- not recording the latency budget, so "faster" becomes the goal in itself;
- ignoring maintenance cost when tests and review do not cover the complex variant.
