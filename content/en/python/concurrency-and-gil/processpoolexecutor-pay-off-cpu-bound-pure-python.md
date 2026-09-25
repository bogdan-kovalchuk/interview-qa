---
id: py-gil-0013
title: "When can `ProcessPoolExecutor` pay off for a CPU-bound pure-Python workload in GIL-enabled CPython?"
description: "When can `ProcessPoolExecutor` pay off for a CPU-bound pure-Python workload in GIL-enabled CPython?"
track: python
section: concurrency-and-gil
level: middle
type: practical
tags: [processpoolexecutor]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython with GIL"
    version: null
anki:
  export: true
sources:
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-multiprocessing
    title: "Python 3.14: Library/multiprocessing"
    url: https://docs.python.org/3.14/library/multiprocessing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-concurrent-futures
    title: "Python 3.14: Library/concurrent.futures"
    url: https://docs.python.org/3.14/library/concurrent.futures.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-free-threading-python
    title: "Python 3.14: Howto/free Threading Python"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-howto-free-threading-extensions
    title: "Python 3.14: Howto/free Threading Extensions"
    url: https://docs.python.org/3.14/howto/free-threading-extensions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**`ProcessPoolExecutor` provides genuine CPU parallelism in GIL-enabled CPython because each worker runs in an independent process with its own GIL.**[^py314-library-threading] A performance gain occurs when the computational workload significantly exceeds the overhead of IPC, pickle serialization of arguments and results, and process startup. Target functions and data arguments must be picklable; lambdas and locally defined closures from `__main__` cannot be serialized.

## Detailed explanation

In standard GIL-enabled CPython, threads cannot execute Python bytecode simultaneously across multiple CPU cores due to the Global Interpreter Lock.[^py314-library-threading] Consequently, attempting to parallelize a pure-Python CPU-bound workload using `ThreadPoolExecutor` provides zero speedup, often slowing execution down due to lock contention and continuous thread switching overhead. `ProcessPoolExecutor` from `concurrent.futures` bypasses this limitation by launching independent worker processes, each running its own CPython interpreter instance with a private GIL and isolated memory heap.[^py314-library-concurrent-futures]

However, coordinating separate OS processes introduces substantial baseline overhead. Spawning worker processes requires runtime initialization and module imports, while dispatching each task requires serializing arguments via `pickle.dumps`, transmitting them across an IPC pipe, and deserializing them in the worker process (`pickle.loads`), with an identical transfer sequence for the returned result.[^py314-library-multiprocessing] If task computation is brief relative to IPC and serialization latency (fine-grained tasks), the multiprocessing implementation will run considerably slower than a straightforward single-threaded loop.

`ProcessPoolExecutor` yields genuine speedup only when the computational granularity is coarse enough that pure CPU evaluation time completely dwarfs IPC and serialization overhead. For batch processing, specifying the `chunksize` parameter in `executor.map()` is essential because it groups multiple items into a single IPC payload, dramatically amortizing communication overhead across the workload.

Demonstration of `ProcessPoolExecutor` on a CPU-bound workload using batched execution with `chunksize`:

```python
from concurrent.futures import ProcessPoolExecutor
import math

def is_prime_heavy(n):
    # Pure-Python CPU-bound task with sufficient computational weight
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    numbers = [10_000_019, 10_000_079, 10_000_103, 10_000_121]

    # chunksize batches items to amortize pickle and IPC transfer overhead
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime_heavy, numbers, chunksize=2))

    print(results)  # [True, True, True, True]
```

**Practical consequences and requirements:**
- workloads must be coarse-grained: if an individual task completes in microseconds, IPC latency will eliminate any multicore performance advantage;
- configuring `chunksize > 1` in `executor.map()` is critical when iterating over large collections to minimize IPC transactions;
- all target functions, arguments, and return values must be picklable; lambdas, locally nested closures, generators, and open resource handles will fail to serialize;
- entry points that initialize the pool must be guarded by `if __name__ == '__main__':` to prevent runaway recursive process creation during module import under `spawn` or `forkserver`.

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
