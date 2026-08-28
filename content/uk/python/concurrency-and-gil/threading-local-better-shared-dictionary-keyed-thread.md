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
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
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

`threading.local()` – це клас, що дає кожному thread власну, ізольовану копію своїх атрибутів:
запис `local.value = 1` в одному thread ніяк не впливає на те, що бачить `local.value` в
іншому.[^py314-library-threading]

Функціонально це схоже на shared dictionary, ключем якого є `threading.get_ident()`, а значенням –
дані конкретного потоку. Різниця – у тому, хто відповідає за ізоляцію і за прибирання. У
`threading.local()` ізоляція вбудована: не потрібен lock, щоб читати чи писати «своє» значення, і
запис автоматично прибирається, коли thread завершується. У shared dict усе це доводиться робити
руками: lock навколо кожного доступу за ключем і явне видалення запису мертвого потоку, інакше
словник росте назавжди.

Приклад двох еквівалентних за призначенням, але різних за витратами реалізацій:

```python
# threading.local: isolation and cleanup are automatic
local_data = threading.local()
local_data.connection = get_connection()

# shared dict keyed by thread id: isolation and cleanup are manual
connections = {}
connections[threading.get_ident()] = get_connection()
```

**Коли `threading.local()` виграє:**
- дані справді потрібні лише в межах одного потоку (наприклад, per-thread DB connection чи request
  context) і не повинні «протікати» між потоками;
- важливий автоматичний cleanup при завершенні потоку без ручного видалення записів.

**Коли shared dict з явним ключем кращий:**
- потрібно з іншого thread (наприклад, для моніторингу чи graceful shutdown) переглянути чи
  завершити стан усіх потоків одразу – `threading.local()` цього просто не дає, бо кожен thread
  бачить лише своє;
- важлива явність: код, що читає `connections[tid]`, одразу показує, що це саме per-thread
  структура з lock-ом, тоді як атрибути `local_data` виглядають як звичайні атрибути, і це і є
  ризик.

Небезпека тут саме в implicit state: значення `threading.local()` виглядають як прості атрибути
об'єкта, тому легко забути, що вони невидимі з інших потоків, і випадково передати посилання на
`local_data` в інший thread, очікуючи побачити там ті самі дані.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
