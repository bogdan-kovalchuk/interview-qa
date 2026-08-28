---
id: py-gil-0006
title: "Чому I/O-bound threads можуть давати concurrency benefit в GIL-enabled CPython?"
description: "CPython звільняє GIL на час блокуючих I/O-операцій (системні виклики, мережа, файлові операції), дозволяючи іншим threads виконувати bytecode."
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L689-L849
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**CPython звільняє GIL на час блокуючих I/O-операцій (системні виклики, мережа, файлові операції), дозволяючи іншим threads виконувати bytecode.**[^py314-library-threading] Поки один thread чекає на відповідь від мережі або диска, інший thread може захопити GIL і виконувати обчислення. Тому для I/O-bound навантаження threads ефективні, а для CPU-bound – ні (потрібен `multiprocessing` або free-threaded build).

## Detailed explanation

GIL – це mutex, який дозволяє лише одному thread одночасно виконувати Python bytecode всередині
одного process. Здавалося б, це має унеможливити будь-яку паралельність, але GIL захищає лише
інтерпретатор, а не сам thread на рівні операційної системи – коли thread чекає на щось зовнішнє,
він може віддати GIL і не заважати іншим.[^py314-library-threading]

Ключовий момент саме в блокуючих I/O-викликах. Функції на кшталт `socket.recv()`, `file.read()`
або `time.sleep()` реалізовані так, що перед зверненням до операційної системи інтерпретатор
явно звільняє GIL, а після повернення захоплює його знову. Поки один thread «зависає» в
системному виклику, GIL вільний, і планувальник CPython може передати його іншому thread, який
у цей час виконує обчислення або робить власний I/O.

Приклад: у мережевому клієнті з кількома threads, кожен з яких очікує відповіді від сервера,
загальний час виконання близький до часу найповільнішого запиту, а не до суми всіх запитів,
бо очікування перекриваються:

```python
import threading

def fetch(url):
    response = session.get(url)  # GIL released while waiting on the socket
    process(response)

threads = [threading.Thread(target=fetch, args=(u,)) for u in urls]
```

Для CPU-bound коду ситуація протилежна: bytecode, що обчислює щось у циклі, не звільняє GIL
добровільно (лише періодично, за таймером перемикання), тому threads фактично виконуються по
черзі й додаткового прискорення не дають.[^py314-howto-free-threading-python]

**Типові помилки в оцінці вигоди від threads:**
- очікувати прискорення від threads для CPU-bound задач (парсинг, обчислення) – тут потрібен
  `multiprocessing` або free-threaded build;
- забувати, що C-розширення теж мають явно звільняти GIL навколо блокуючих або довгих операцій –
  якщо розширення цього не робить, вигоди від threads не буде;
- плутати «thread не блокує весь process під час I/O» з «GIL взагалі не існує» – GIL і далі
  серіалізує bytecode, просто не в момент очікування.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
