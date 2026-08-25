# Topic brief: 15_gil_threads_processes

## Goal and scope

Test selection and correctness across threads processes and executors, explicitly covering both
GIL-enabled and supported free-threaded CPython 3.14 builds.

## Sources

- Official: https://docs.python.org/3.14/library/threading.html
- Official: https://docs.python.org/3.14/library/multiprocessing.html
- Official: https://docs.python.org/3.14/library/concurrent.futures.html
- Official: https://docs.python.org/3.14/howto/free-threading-python.html
- Official: https://docs.python.org/3.14/howto/free-threading-extensions.html
- Candidate Q&A: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md

## Coverage plan

| Cluster | Retrieval operation | Middle | Senior | Total |
|---|---|---:|---:|---:|
| Thread and process isolation | contrast and choose | 2 | 1 | 3 |
| GIL-enabled CPython behavior | explain and diagnose | 2 | 2 | 4 |
| Free-threaded CPython support | qualify and assess | 1 | 2 | 3 |
| CPU-bound vs I/O-bound selection | choose and justify | 2 | 1 | 3 |
| Locks races deadlocks and visibility | diagnose and design | 2 | 2 | 4 |
| Executors and worker pools | select and handle failure | 1 | 1 | 2 |
| IPC and process start methods | design and qualify | 1 | 1 | 2 |
| Thread-local state | choose | 1 | 0 | 1 |

Planned total: 22 fronts, all Middle+.

## Sensitive boundaries

- Do not state that Python universally has a GIL.
- Atomic-looking CPython operations are not a substitute for synchronization contracts.
