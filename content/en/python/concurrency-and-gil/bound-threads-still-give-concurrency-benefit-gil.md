---
id: py-gil-0006
title: "Why can I/O-bound threads still give a concurrency benefit in GIL-enabled CPython?"
description: "Why can I/O-bound threads still give a concurrency benefit in GIL-enabled CPython?"
track: python
section: concurrency-and-gil
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-05
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L689-L849
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**CPython releases the GIL for the duration of blocking I/O operations (system calls, network,
file operations), letting other threads execute bytecode.**[^py314-library-threading] While one
thread waits for a response from the network or disk, another thread can acquire the GIL and run
computation. So threads are effective for I/O-bound workloads but not for CPU-bound ones (those
need `multiprocessing` or a free-threaded build).

## Detailed explanation

The GIL is a mutex that lets only one thread execute Python bytecode at a time within one process.
This might seem to rule out any concurrency, but the GIL protects only the interpreter, not the
thread itself at the operating-system level – when a thread is waiting on something external, it
can give up the GIL without holding up the others.[^py314-library-threading]

The key point is exactly in blocking I/O calls. Functions such as `socket.recv()`, `file.read()`,
or `time.sleep()` are implemented so that the interpreter explicitly releases the GIL before
calling into the operating system, and reacquires it after returning. While one thread is
"parked" in a system call, the GIL is free, and the CPython scheduler can hand it to another
thread that is meanwhile doing computation or its own I/O.

Example: in a network client with several threads, each waiting for a response from the server,
the total run time is close to the slowest single request rather than the sum of all requests,
because the waits overlap:

```python
import threading

def fetch(url):
    response = session.get(url)  # GIL released while waiting on the socket
    process(response)

threads = [threading.Thread(target=fetch, args=(u,)) for u in urls]
```

For CPU-bound code the situation is the opposite: bytecode that computes something in a loop does
not voluntarily release the GIL (only periodically, on a switch-interval timer), so threads
effectively run one after another and give no extra speedup.[^py314-howto-free-threading-python]

**Common mistakes in judging the benefit of threads:**
- expecting a speedup from threads for CPU-bound work (parsing, computation) – that needs
  `multiprocessing` or a free-threaded build;
- forgetting that C extensions also have to explicitly release the GIL around blocking or
  long-running operations – if an extension does not do this, threads give no benefit;
- confusing "a thread does not block the whole process during I/O" with "the GIL does not exist" –
  the GIL still serializes bytecode, just not while a thread is waiting.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
