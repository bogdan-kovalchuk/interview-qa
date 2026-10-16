---
id: py-perf-0013
title: "How can task batching and `chunksize` reduce serialization and scheduling overhead in a process pool, while worsening load balancing?"
track: python
section: performance
sources:
  - source_id: py314-library-concurrent-futures
    title: "Python 3.14: Library/concurrent.futures"
    url: https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Executor.map
---

## Short answer

**`chunksize` in `ProcessPoolExecutor.map()` groups the elements of the iterable into chunks, which are submitted to the pool as separate tasks.**[^py314-library-concurrent-futures] For very long iterables, a large `chunksize` can significantly improve performance,[^py314-library-concurrent-futures] because there are fewer tasks. With `chunksize=1` (the default), each element is a separate task: balancing is better, but the overhead is paid for every task. <span class="warn">`chunksize` has no effect on `ThreadPoolExecutor.map()`, where it is ignored.</span>[^py314-library-concurrent-futures]

## Detailed explanation

`ProcessPoolExecutor` sends each task to another process: the function and its arguments must be serialized, and the result must be sent back. The fixed costs (messages between processes, scheduling) are paid per task, not per element. The documentation describes the mechanism: `Executor.map()` splits the iterable into chunks that are submitted to the pool as separate tasks, and `chunksize` sets the approximate size of a chunk.[^py314-library-concurrent-futures]
The chunk size changes the number of tasks:

```python
from concurrent.futures import ProcessPoolExecutor


def square(x):
    return x * x


if __name__ == '__main__':
    with ProcessPoolExecutor(max_workers=4) as pool:
        # chunksize=1 (default): 10 000 items -> 10 000 separate tasks
        list(pool.map(square, range(10_000)))
        # chunksize=500: 10 000 items -> 20 tasks of up to 500 items each
        list(pool.map(square, range(10_000), chunksize=500))
```

Choosing the size is a trade-off. A large chunk reduces the number of tasks, but makes each unit of work coarser. Suppose there are 1000 elements, 4 workers and `chunksize=250`: there will be 4 chunks, one per worker. If all the slow elements land in the first chunk, one worker runs for a long time while the other three sit idle after finishing their chunks. With `chunksize=1`, the same 1000 tasks are taken by free workers, so balancing is better, but the overhead is paid 1000 times.

The gain depends on the ratio of the element cost to the fixed costs. If an element costs much more than the transfer, `chunksize` barely changes anything; if element durations vary a lot, a large chunk hurts. There is no universal number, so measure on real data. `ThreadPoolExecutor` ignores chunksize. Since 3.14, `map()` accepts `buffersize`, which limits the number of submitted tasks whose results have not yet been yielded; it is not a way to group tasks, but a limit on how many can wait.[^py314-library-concurrent-futures]

**Common mistakes:**
- looking for a `chunksize` parameter in `submit()`: it is not there, so batches are built by hand;
- setting a large `chunksize` for uneven tasks and getting idle workers at the end;
- measuring on a short iterable, where pool startup and process start dominate.
