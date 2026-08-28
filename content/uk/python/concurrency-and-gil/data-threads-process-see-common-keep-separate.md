---
id: py-gil-0003
title: "Які дані threads в одному process спільно бачать і які мають окремо?"
description: "Threads спільно бачать усі heap-об'єкти (global-змінні, модульний стан, мутабельні контейнери) та відкриті file descriptors, але кожен thread має власний стек викликів, локальні змінні та регістри."
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L3-L28
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Threads спільно бачать усі heap-об'єкти (global-змінні, модульний стан, мутабельні контейнери) та відкриті file descriptors, але кожен thread має власний стек викликів, локальні змінні та регістри.**[^py314-library-threading] Для ізольованого стану використовується `threading.local()` – значення прив'язані до конкретного thread і не видимі іншим. Відсутність явного розділення стану є основним джерелом race conditions.

## Detailed explanation

Threads в одному process виконуються всередині одного адресного простору, тому більшість стану
програми доступна їм спільно за замовчуванням. Це принципова відмінність від процесів, де кожен
має власну копію адресного простору й нічого не бачить автоматично.[^py314-library-threading]

Спільно видимі: усі об'єкти на heap – global-змінні модуля, атрибути класів та інстансів, елементи
списків і словників, а також відкриті file descriptors і сокети. Якщо один thread змінює список
або словник, зміну одразу бачать усі інші threads, що мають посилання на той самий об'єкт.

Окремі для кожного thread: власний стек викликів, локальні змінні функцій, які виконує саме цей
thread, і регістри процесора на момент виконання. Це те, що робить кожен thread незалежним потоком
керування, навіть попри спільну пам'ять.

```python
import threading

counter = 0  # shared across all threads

def worker():
    local_value = 0  # private stack-local variable
    global counter
    for _ in range(1000):
        local_value += 1
        counter += 1  # visible to every thread, not synchronized

threads = [threading.Thread(target=worker) for _ in range(4)]
```

У прикладі `local_value` існує окремо в кожному виклику `worker()`, тоді як `counter` – один
об'єкт, до якого звертаються всі чотири threads одночасно, без жодної гарантії атомарності.

Коли потрібен стан, приватний для thread, але без ручного передавання його через аргументи,
використовують `threading.local()` – кожен атрибут такого об'єкта прив'язаний до конкретного
thread і не видимий іншим, хоча сам об'єкт формально один на всю
програму.[^py314-library-threading]

**Типові джерела помилок через спільний стан:**
- вважати, що локальна змінна функції ізольована, тоді як насправді змінюється спільний
  mutable-об'єкт, переданий у функцію за посиланням;
- забувати, що модульні global-змінні й class-атрибути спільні для всіх threads без явної
  синхронізації;
- плутати ізоляцію процесів (`multiprocessing`) з ізоляцією threads – процеси не бачать спільний
  стан взагалі, threads бачать майже все, крім стека й локальних змінних.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
