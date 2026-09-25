---
id: py-gil-0021
title: "In Python 3.14, which process start method is the default on POSIX and on Windows, and when do you need to explicitly choose `spawn`, `fork`, or `forkserver`?"
description: "In Python 3.14, which process start method is the default on POSIX and on Windows, and when do you need to explicitly choose `spawn`, `fork`, or `forkserver`?"
track: python
section: concurrency-and-gil
level: senior
type: comparison
tags: [spawn, fork, forkserver]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython"
    version: "3.14"
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

**In Python 3.14, the default on POSIX is `forkserver`, and on Windows it is `spawn`.**[^py314-library-threading] <span class="warn">The POSIX default changed from `fork` to `forkserver` in 3.14 to prevent multithreaded `fork()` issues.</span> `spawn` is the safest (fresh interpreter) but slower; `fork` is fast but unsafe if the parent has threads (risking crash or deadlock); `forkserver` balances both: one server process starts via `spawn`, and subsequent workers fork from it. Choose `fork` only for legacy code without threads; choose `spawn` when maximum isolation is needed.

## Detailed explanation

Historically on POSIX systems (Linux and other Unix derivatives), CPython defaulted to `fork` because the `fork()` system call creates a child process nearly instantaneously via OS copy-on-write memory cloning without re-initializing the runtime or re-importing modules.[^py314-library-multiprocessing] However, calling `fork()` inside a multithreaded process duplicates only the calling thread into the child; all other threads abruptly vanish. If any background thread held a synchronization lock (such as a memory allocator mutex, a logging lock, or a database connection lock) at the moment of the fork, that lock remains acquired permanently in the child, inevitably resulting in deadlocks or heap corruption.

Because modern Python environments frequently run background threads in third-party extensions (such as OpenMP, C runtime runtimes, and newer CPython internals), Python 3.14 officially switched the default start method on POSIX from `fork` to `forkserver`.[^py314-library-multiprocessing] On Windows, `spawn` has always been the sole native start method because the Windows kernel lacks a POSIX `fork` syscall. On macOS, the default was transitioned to `spawn` earlier in Python 3.8 due to system crashes within Cocoa and CoreFoundation frameworks.

The three start methods represent distinct architectural trade-offs:
- `spawn`: launches a completely fresh interpreter process (`python`), re-executing the entry script up to the `if __name__ == '__main__':` guard and passing state strictly via pickle. It guarantees clean-slate isolation and immunity from inherited thread deadlocks, but incurs the highest startup latency and memory overhead;
- `fork`: clones the existing process directly via OS `fork()`, inheriting full address space state. It is fast but structurally unsafe in any application that employs threads;
- `forkserver`: an optimal balance designed to resolve multithreaded fork safety. An auxiliary server process is spawned once upon initial demand and remains strictly single-threaded. All subsequent worker processes are forked from this clean forkserver process, delivering thread safety alongside much lower creation latency than full `spawn`.

Inspecting the active start method and explicitly managing execution using a `spawn` context:

```python
import multiprocessing as mp

def task(name):
    # Retrieve current active context method
    method = mp.get_start_method()
    print(f"Task '{name}' executed under start method: {method}")

if __name__ == "__main__":
    # In Python 3.14: POSIX defaults to 'forkserver', Windows defaults to 'spawn'
    default_method = mp.get_start_method()
    print(f"System default start method: {default_method}")

    # Best practice: use explicit contexts rather than global set_start_method()
    # 'spawn' guarantees a clean interpreter and identical behavior across OSes
    spawn_ctx = mp.get_context("spawn")
    p = spawn_ctx.Process(target=task, args=("worker-1",))
    p.start()
    p.join()
```

**Practical consequences and method selection:**
- choose `spawn` for cross-platform applications requiring identical execution semantics across Windows, macOS, and Linux, or when integrating with runtimes (CUDA, PyTorch, GUI toolkits) that forbid forking;
- select `forkserver` on POSIX servers that repeatedly create short-lived worker processes; preloading heavy dependencies via `mp.set_forkserver_preload(['numpy', 'torch'])` shares memory efficiently;
- restrict `fork` strictly to legacy single-threaded POSIX utilities where the complete absence of secondary threads is guaranteed and minimal spawn overhead is paramount;
- avoid mutating global process state via `mp.set_start_method()`, which can collide across independent libraries; prefer explicit context instances obtained via `mp.get_context('...')`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
