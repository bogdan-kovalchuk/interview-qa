---
id: py-gil-0004
title: "How does process isolation change the model for exchanging data and handling a worker crash, compared to threads?"
description: "How does process isolation change the model for exchanging data and handling a worker crash, compared to threads?"
track: python
section: concurrency-and-gil
level: senior
type: comparison
tags: []
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
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

**Process isolation requires data serialization (pickle) for IPC, but provides crash isolation – a worker crash does not terminate the parent process.**[^py314-library-threading] Data exchange occurs via `Queue`/`Pipe` (pickle), `Value`/`Array` (shared memory for C types), or `Manager` (proxy objects managed by a server process). In threads, exchange is virtually free due to shared memory address space, but an unhandled exception or crash in a thread can terminate the entire process. The primary trade-off is process isolation and failure safety against serialization overhead and increased memory footprint.

## Detailed explanation

Process isolation is rooted in distinct virtual address spaces enforced by the operating system: each child process receives its own private heap, file descriptor table, and dedicated CPython interpreter instance with its own independent GIL.[^py314-library-multiprocessing] In contrast, threads (`threading`) run within a single shared address space where reading and writing shared objects occurs directly via memory pointers, requiring synchronization primitives (`Lock`, `RLock`) to prevent race conditions.

Because processes cannot directly read each other's memory, exchanging data requires inter-process communication (IPC). When utilizing `multiprocessing.Queue` or `Pipe`, data must undergo full serialization (`pickle.dumps`) in the sender process and deserialization (`pickle.loads`) in the receiving process, incurring substantial CPU overhead and demanding that all transferred objects be picklable. Alternative approaches include shared memory (`multiprocessing.shared_memory`, `Value`, `Array`), which transfers raw bytes without pickle serialization, and `Manager` server processes, which expose proxy objects across socket connections at the expense of high IPC latency.

The worker crash model highlights the primary reliability advantage of process isolation. A fatal thread failure at the OS level – such as a segmentation fault inside a C extension, stack overflow, or an OS OOM kill – immediately terminates the entire host process and all coexisting threads without cleanup. In a multiprocessing architecture, the OS memory protection boundary confines catastrophic failures: an abrupt crash of a child process leaves the parent process unharmed, allowing the supervisor to detect the non-zero exitcode or handle a `BrokenProcessPool` exception in `concurrent.futures` and trigger recovery or worker replacement.[^py314-library-concurrent-futures]

The distinction between data isolation via IPC serialization and parent process survival upon worker failure:

```python
import multiprocessing as mp
import os

def worker(queue):
    # IPC requires serialization (pickle) over pipes/sockets
    item = queue.get()
    item["value"] += 1
    queue.put(item)
    # Abrupt worker crash does not kill parent process
    os._exit(1)

if __name__ == "__main__":
    q = mp.Queue()
    data = {"value": 10}
    q.put(data)

    p = mp.Process(target=worker, args=(q,))
    p.start()
    p.join()

    # Data in parent remains unchanged due to isolated memory space
    print(data["value"])         # 10 (isolated from child modifications)
    print(q.get()["value"])      # 11 (received through IPC)
    print(p.exitcode)            # 1 (child terminated abnormally, parent survives)
```

**Practical consequences and architectural trade-offs:**
- transferring large datasets (such as multi-gigabyte DataFrames) across queues introduces severe serialization bottlenecks; high-throughput workloads should leverage `SharedMemory` or file-system paths;
- not all Python objects can be pickled: generators, open file handles, database connections, and lambda functions cannot be transmitted over standard IPC queues;
- unlike threads, a worker crash caused by a segmentation fault or an OOM killer does not crash the supervisor process, which is essential for fault-tolerant architectures;
- abrupt worker termination while holding an IPC synchronization lock or mid-write to a pipe can cause deadlocks in reading processes unless timeouts and broken process pool detection are configured.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
