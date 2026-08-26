---
id: py-gil-0023
title: "Коли `threading.local()` кращий за shared dictionary keyed by thread ID, а коли він приховує небажаний implicit state?"
description: "threading.local() кращий коли потрібна автоматична ізоляція даних між потоками й автоматичний cleanup при завершенні потоку; shared dictionary з ключем threading.get_ident() – коли потрібна явність і повний контроль над..."
track: python
section: concurrency-and-gil
level: middle
type: comparison
tags: [threading-local]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L987-L1043
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`threading.local()` кращий коли потрібна автоматична ізоляція даних між потоками й автоматичний cleanup при завершенні потоку; shared dictionary з ключем `threading.get_ident()` – коли потрібна явність і повний контроль над структурою.**[^py314-library-threading] Переваги `threading.local()`: не потребує lock для самого сховища, дані автоматично видаляються коли потік завершується, доступ через атрибути зручніший. <span class="warn">Небезпека implicit state:</span> значення виглядають як звичайні атрибути, але невидимі між потоками – це ускладнює debugging і може призвести до помилок якщо значення з `local` передати в інший потік. Shared dict потребує lock для оновлень і ручного видалення записів померлих потоків, інакше – витік пам'яті.

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
