---
id: py-perf-0014
title: "Why can adding more workers hurt throughput because of contention, context switching, and downstream saturation?"
track: python
section: performance
sources:
  - source_id: py314-glossary-term-parallelism
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-parallelism
  - source_id: py314-howto-free-threading
    title: "Python 3.14: Howto/free-threading"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
  - source_id: py314-library-concurrent-futures-threadpoolexecutor
    title: "Python 3.14: Library/concurrent.futures"
    url: https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
  - source_id: py314-library-concurrent-futures-processpoolexecutor
    title: "Python 3.14: Library/concurrent.futures"
    url: https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor
---

## Short answer

**Workers beyond the saturation point add no throughput: they compete for shared resources, add context switches, and can overload the downstream system.** In a regular GIL build of CPython, only one thread runs Python bytecode at a time, so CPU-bound tasks in threads do not run in parallel; for several cores, use processes.[^py314-glossary-term-parallelism] Too many processes add OS-level context switching and RAM use per process. Even for I/O-bound work, too many concurrent connections can exhaust file descriptors or overload a remote server, so latency grows and throughput may fall.

## Detailed explanation

Throughput is the amount of completed work per unit of time. An extra worker helps as long as there is spare capacity: I/O wait time, idle cores, free connections. Once a bottleneck is saturated (CPU cores, the GIL, a disk, a connection pool, a remote API's rate limit), new workers queue for the same resource: throughput may stay flat or fall, while latency grows. Saturation depends on the workload and the resources, not on the number of workers alone.

For CPU-bound code this is clearest. In a regular GIL build of CPython, only one thread runs bytecode at a time,[^py314-glossary-term-parallelism] so 8 threads running a pure Python loop do not produce more computation per second than one thread. For parallelism across several cores, use processes. Since 3.13, CPython has a free-threaded build in which the GIL is disabled,[^py314-howto-free-threading] but it is a separate interpreter build, not a replacement for the regular one.

The limit on a downstream service belongs on the resource itself, not on the number of workers. In the example below there are 32 workers, but no more than 4 calls to the remote service run at once:

```python
import threading
import time
from concurrent.futures import ThreadPoolExecutor

limit = threading.BoundedSemaphore(4)  # at most 4 calls to the remote service at once
state_lock = threading.Lock()
active = 0
max_active = 0


def call_service(item):
    global active, max_active
    with limit:
        with state_lock:
            active += 1
            max_active = max(max_active, active)
        time.sleep(0.05)  # stands in for a network call
        with state_lock:
            active -= 1
    return item


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=32) as pool:
        list(pool.map(call_service, range(32)))
    print("max concurrent service calls:", max_active)  # prints 4: the semaphore limits it, not the 32 workers
```

The default values are only a starting point. Since 3.13, `ThreadPoolExecutor` takes `max_workers = min(32, (os.process_cpu_count() or 1) + 4)` (before 3.13 it was `os.cpu_count() + 4`),[^py314-library-concurrent-futures-threadpoolexecutor] and `ProcessPoolExecutor` takes `os.process_cpu_count()`.[^py314-library-concurrent-futures-processpoolexecutor] The documentation describes these values as defaults, not as the optimal number of workers for your workload. Too many processes on the same cores add OS-level context switching and RAM use per process.

Find the limit by measuring: increase the workers while throughput grows. When throughput stops growing and latency and error counts (timeouts, HTTP 429 responses from an API) rise, you have reached saturation. Measure throughput and latency together: throughput alone will not show that the downstream service is already struggling.

**Common mistakes:**
- increasing `max_workers` for CPU-bound code in a thread pool "for speed";
- setting the number of workers above the downstream limit (connection pool, rate limit) instead of limiting that resource;
- assuming the default `max_workers` is optimal;
- measuring only throughput, without latency and errors.
