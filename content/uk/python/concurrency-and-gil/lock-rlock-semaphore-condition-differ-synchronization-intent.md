---
id: py-gil-0016
title: "Чим `Lock`, `RLock`, `Semaphore` та `Condition` відрізняються за synchronization intent?"
description: "Lock – взаємовиключення (один потік у критичній секції); RLock – reentrant lock, той самий потік може захоплювати повторно; Semaphore – лічильник, що обмежує кількість одночасних входів; Condition – очікування зміни..."
track: python
section: concurrency-and-gil
level: middle
type: comparison
tags: [lock, rlock, semaphore, condition]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-multiprocessing
    title: "Python 3.14: Library/multiprocessing"
    url: https://docs.python.org/3.14/library/multiprocessing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-concurrent-futures
    title: "Python 3.14: Library/concurrent.futures"
    url: https://docs.python.org/3.14/library/concurrent.futures.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-free-threading-python
    title: "Python 3.14: Howto/free Threading Python"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-free-threading-extensions
    title: "Python 3.14: Howto/free Threading Extensions"
    url: https://docs.python.org/3.14/howto/free-threading-extensions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L126-L420
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`Lock` – взаємовиключення (один потік у критичній секції); `RLock` – reentrant lock, той самий потік може захоплювати повторно; `Semaphore` – лічильник, що обмежує кількість одночасних входів; `Condition` – очікування зміни стану з notify/notify_all.**[^py314-library-threading] `Lock` може звільнити будь-який потік; `RLock` – лише owning thread із відповідною кількістю `release()`. `Semaphore` підходить для пулів ресурсів (наприклад, connection pool). `Condition` потрібен для producer-consumer патернів, де один потік чекає сигналу від іншого.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
