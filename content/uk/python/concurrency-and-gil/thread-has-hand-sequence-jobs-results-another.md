---
id: py-gil-0018
title: "Коли один thread має передати іншому послідовність jobs і results, чому `queue.Queue` дає чіткіший hand-off contract, ніж shared list без lock?"
description: "queue.Queue реалізує внутрішнє блокування для всіх операцій put()/get(), забезпечуючи thread-safe hand-off без потреби в явних locks."
track: python
section: concurrency-and-gil
level: senior
type: comparison
tags: [queue-queue]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L126-L420
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`queue.Queue` реалізує внутрішнє блокування для всіх операцій `put()`/`get()`, забезпечуючи thread-safe hand-off без потреби в явних locks.**[^py314-library-threading] Shared list без lock вимагає від розробника самостійно синхронізувати доступ; навіть окремі операції типу `list.append()` не гарантують атомарності на рівні додатку для складних протоколів. `Queue` також підтримує `maxsize` для backpressure, блокуючи producer коли черга переповнена, та надає чіткий контракт: кожен item отримує рівно один consumer.

## Detailed explanation

`queue.Queue` – це FIFO-черга з потокобезпечним інтерфейсом: усередині кожного виклику `put()` і
`get()` вона сама бере і звільняє внутрішній lock, тож зовнішньому коду не потрібна жодна додаткова
синхронізація.[^py314-library-threading]

Shared list без lock натомість не дає жодного контракту. Окремі виклики на кшталт `list.append()`
чи `list.pop(0)` самі по собі безпечні, але послідовність із кількох таких викликів – ні. Якщо один
потік перевіряє `if my_list:` перед `pop(0)`, а інший встигає забрати останній елемент між
перевіркою і `pop`, виникає race condition і `IndexError`.

Приклад hand-off без і з `Queue`:

```python
# fragile: check-then-act on a shared list
if job_list:
    job = job_list.pop(0)  # another thread may empty the list in between

# robust: Queue blocks and hands off exactly one item per get()
job = job_queue.get()
```

`Queue` додає й те, чого немає у списку: `put()` може блокуватися, коли черга досягла `maxsize`, а
це дає простий backpressure – producer сповільнюється, коли consumer не встигає. Є також
`task_done()` і `join()`, які дозволяють producer дочекатися, поки всі поставлені jobs будуть
оброблені.[^py314-library-threading]

**Чого не дає shared list без явного протоколу:**
- гарантії, що кожен job дістанеться рівно одному consumer, а не нулю чи двом одразу;
- сигналу «черга порожня, чекай» замість busy-wait циклу з перевіркою довжини списку;
- backpressure, коли producer працює швидше за consumer;
- єдиної точки, де видно весь контракт hand-off, замість розкиданих перевірок і locks навколо
  списку.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
