---
id: py-gil-0020
title: "Як коректно зібрати exceptions та результати з executor futures, не втративши worker failure?"
description: "Future.result() повертає значення або повторно викидає exception worker-а; Future.exception() повертає exception-об'єкт або None."
track: python
section: concurrency-and-gil
level: senior
type: practical
tags: []
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L940-L986
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`Future.result()` повертає значення або повторно викидає exception worker-а; `Future.exception()` повертає exception-об'єкт або `None`.**[^py314-library-threading] Для збору результатів кількох futures використовуйте `concurrent.futures.as_completed(fs)`, який yield-ить futures у порядку завершення – це дозволяє обробити кожну помилку індивідуально. `Executor.map()` повертає результати у порядку викликів, але exception піднімається лише при зверненні до нього. <span class="warn">Якщо не викликати `result()` або не обробити future через `as_completed`, exception worker-а буде silently lost.</span>

## Detailed explanation

`Future` – це об'єкт-обіцянка результату асинхронної задачі, надісланої в executor. Він завжди
переходить в один із трьох станів: успішно завершений з результатом, завершений з exception, або
скасований. Проблема на практиці не в тому, що результат втрачається технічно – `Future`
зберігає exception усередині, – а в тому, що код може просто ніколи не перевірити цей
стан.[^py314-library-concurrent-futures]

`future.result()` повертає значення, якщо задача завершилась успішно, і повторно піднімає той
самий exception, якщо worker впав. `future.exception()` дає доступ до exception-об'єкта без
повторного підняття, повертаючи `None` при успіху. Обидва методи блокують виклик до завершення
задачі (з опційним `timeout`).

Приклад коректного збору результатів і помилок з кількох futures:

```python
from concurrent.futures import as_completed

futures = [executor.submit(worker, item) for item in items]
for future in as_completed(futures):
    try:
        result = future.result()
    except Exception as exc:
        log_failure(future, exc)
    else:
        process(result)
```

`as_completed()` yield-ить futures у порядку завершення, а не подання, тому обробка кожного
результату або помилки відбувається щойно вони готові, без очікування на найповільніший.
`Executor.map()` натомість зберігає порядок виклику й піднімає exception лише в момент ітерації по
відповідному елементу – якщо ітерацію перервати раніше, помилки решти задач залишаться непобаченими.

**Типові способи silently втратити worker failure:**
- надіслати задачі через `submit()` і ніколи не викликати `result()` або `exception()` на
  отриманих futures – виконання завершиться, а exception просто зникне;
- пройтись по списку futures у порядку подання замість `as_completed()`, тоді як `map()`
  застосований без обробки exception на кожному кроці ітерації;
- використати `executor.map()` і зберегти лише сам generator, не ітеруючи по ньому повністю –
  exception на пізньому елементі ніколи не підніметься.

Явна перевірка кожного `Future` – через `result()`, `exception()` або `add_done_callback()` –
єдиний спосіб гарантовано побачити помилку worker-а.[^py314-library-concurrent-futures]

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
