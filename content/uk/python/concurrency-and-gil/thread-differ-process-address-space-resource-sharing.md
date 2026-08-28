---
id: py-gil-0002
title: "Чим thread відрізняється від process за address space, resource sharing та failure isolation?"
description: "Thread виконується всередині батьківського process і має той самий address space; process має власний ізольований address space."
track: python
section: concurrency-and-gil
level: middle
type: comparison
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L29-L64
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Thread виконується всередині батьківського process і має той самий address space; process має власний ізольований address space.**[^py314-library-threading] Threads спільно використовують heap, модулі, відкриті file descriptors, тоді як кожен process отримує власну копію пам'яті та потребує IPC (pickle через `Queue`/`Pipe`, shared memory через `Value`/`Array`). Crash одного thread (необроблений exception) завершує весь process; crash окремого process ізольований – батьківський process продовжує роботу.

## Detailed explanation

Thread – це одиниця виконання всередині одного process; кілька threads одного process ділять один і
той самий address space, тоді як кожен process отримує власний, ізольований address space – окреме
адресне відображення пам'яті, яке керує операційна система.[^py314-library-threading]

Через спільний address space threads бачать одні й ті самі об'єкти в пам'яті: змінна, список чи
dict, створені в одному thread, доступні з іншого без жодного копіювання чи серіалізації. Це дешево
й швидко, але саме тому вимагає explicit синхронізації для спільного mutable стану.

Process, навпаки, ізольований на рівні пам'яті операційною системою: два process не можуть просто
прочитати змінну одне одного. Обмін даними між ними йде через IPC – `multiprocessing.Queue`,
`Pipe`, або shared memory (`Value`, `Array`), і в більшості випадків дані серіалізуються (`pickle`)
перед передачею.[^py314-library-multiprocessing]

Приклад: створення worker-а як thread і як process виглядає майже однаково в коді, але поведінка
пам'яті різна:

```python
import threading
import multiprocessing

def worker(shared_list):
    shared_list.append(1)  # visible to the parent immediately for a thread,
                            # needs a Manager/shared memory for a process

t = threading.Thread(target=worker, args=([],))
p = multiprocessing.Process(target=worker, args=([],))
```

Різниця виявляється і при збої. Необроблений exception у неголовному thread завершує лише цей
thread; решта process продовжує роботу, хоча стан спільної пам'яті може лишитися неконсистентним.
Process, який впав чи був вбитий (наприклад, OOM killer), не зачіпає пам'ять батьківського чи інших
process – ОС просто звільняє його адресний простір.

**Головні наслідки цієї різниці:**
- threads дешевші за створення й перемикання, але вимагають locks чи queues для безпечного доступу
  до спільних даних;
- processes дорожчі й потребують серіалізації для обміну даними, але дають справжню ізоляцію
  відмов і обхід GIL для CPU-bound роботи;[^py314-library-multiprocessing]
- вибір між ними – це компроміс між дешевизною спільного стану і безпекою ізоляції.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
