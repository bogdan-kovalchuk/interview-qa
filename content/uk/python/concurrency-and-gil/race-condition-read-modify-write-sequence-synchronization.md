---
id: py-gil-0015
title: "Що таке race condition на read-modify-write sequence і чому потрібен synchronization primitive?"
description: "Race condition виникає, коли кілька потоків виконують read-modify-write для спільного ресурсу без синхронізації, і результат залежить від порядку interleaving операцій."
track: python
section: concurrency-and-gil
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L559-L688
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Race condition виникає, коли кілька потоків виконують read-modify-write для спільного ресурсу без синхронізації, і результат залежить від порядку interleaving операцій.**[^py314-library-threading] Наприклад, `counter += 1` – це три операції: читання, інкремент, запис. Якщо два потоки одночасно читають однакове значення, один інкремент буде втрачено. Навіть у CPython з GIL bytecode-інструкції можуть перериватися між операціями, тому потрібен `Lock` або інший synchronization primitive для атомарності на рівні додатку.

## Detailed explanation

Race condition – це ситуація, коли результат виконання залежить від того, у якому порядку
interleave-яться операції кількох потоків (чи процесів) над одним спільним ресурсом, і принаймні
один з них цей ресурс змінює.[^py314-library-threading]

Найчастіше вона виникає на послідовності read-modify-write: прочитати значення, обчислити нове,
записати назад. Це три окремі кроки, навіть коли в коді вони виглядають як один вираз, і scheduler
може перемкнути потік між будь-якими двома з них.

Приклад race condition на простому лічильнику без синхронізації:

```python
counter = 0

def increment():
    global counter
    for _ in range(100_000):
        counter += 1  # read, add 1, write - not atomic
```

Якщо два потоки одночасно викликають `increment()`, підсумкове значення `counter` майже напевно
буде меншим за 200000: обидва потоки встигають прочитати старе значення до того, як інший запише
нове, і один інкремент губиться.

У CPython є GIL, який гарантує, що одна bytecode-інструкція виконується атомарно, але вираз
`counter += 1` компілюється в кілька bytecode-інструкцій (завантаження, додавання, запис), і GIL
може перемкнути потік між ними.[^py314-howto-free-threading-python] Тому GIL рятує від пошкодження
внутрішньої структури об'єкта, але не рятує від логічних race condition на рівні застосунку.

**Як лікувати race condition на read-modify-write:**
- обгорнути всю послідовність читання, зміни й запису в `threading.Lock` (або `RLock`), щоб
  зробити її атомарною на рівні застосунку;
- замінити спільний mutable стан на структуру, яка вже гарантує атомарність потрібної операції,
  наприклад `queue.Queue`, або винести стан у окремий процес;
- пам'ятати, що у free-threaded build (без GIL) ця проблема стає ще актуальнішою: зникає навіть
  випадковий захист від переривання між bytecode-інструкціями.[^py314-howto-free-threading-python]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
