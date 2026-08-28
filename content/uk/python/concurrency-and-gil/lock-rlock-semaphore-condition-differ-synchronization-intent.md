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

**`Lock` – взаємовиключення (один потік у критичній секції); `RLock` – reentrant lock, той самий потік може захоплювати повторно; `Semaphore` – лічильник, що обмежує кількість одночасних входів; `Condition` – очікування зміни стану з notify/notify_all.**[^py314-library-threading] `Lock` може звільнити будь-який потік; `RLock` – лише owning thread із відповідною кількістю `release()`. `Semaphore` підходить для пулів ресурсів (наприклад, connection pool). `Condition` потрібен для producer-consumer патернів, де один потік чекає сигналу від іншого.

## Detailed explanation

У модулі `threading` кожен примітив синхронізації виражає інший намір (synchronization intent), а
не просто інший API: вони відрізняються тим, яку властивість спільного ресурсу захищають, а не лише
деталями виклику.[^py314-library-threading]

`Lock` і `RLock` обидва реалізують взаємне виключення, але для різних сценаріїв. `Lock` дозволяє
захопити себе лише один раз - повторний `acquire()` з того самого потоку призводить до deadlock.
`RLock` веде внутрішній лічильник захоплень і власника (owning thread): той самий потік може
захопити його повторно без блокування, але має викликати `release()` стільки ж разів. `RLock`
потрібен саме для рекурсивних функцій або методів, які викликають один одного, утримуючи один і той
самий lock.

`Semaphore` виражає інший намір - не "один потік одночасно", а "не більше N потоків одночасно". Це
природний вибір для обмеження доступу до пулу ресурсів фіксованого розміру (наприклад, пул
з'єднань). `BoundedSemaphore` додає перевірку: якщо `release()` викликається частіше, ніж
`acquire()`, він кидає виняток, тоді як звичайний `Semaphore` мовчки дозволить лічильнику вирости
понад початкове значення, приховуючи баг.

`Condition` вирішує інше завдання - очікування зміни стану, а не просто захоплення ресурсу. Він
будується поверх `Lock` (або `RLock`) і додає `wait()`/`notify()`/`notify_all()`: потік, що чекає,
атомарно звільняє внутрішній lock на час очікування і повторно захоплює його при пробудженні. Це
основа producer-consumer патерну:

```python
condition = threading.Condition()
queue = []

def consumer():
    with condition:
        while not queue:
            condition.wait()
        item = queue.pop(0)
```

**Типові помилки:**
- використовувати `Lock` там, де рекурсивний виклик того самого потоку вимагає `RLock`, і
  отримувати self-deadlock;
- брати звичайний `Semaphore` для пулу ресурсів там, де потрібен `BoundedSemaphore`, щоб виявляти
  зайві `release()` як помилку, а не мовчки;
- викликати `notify()` або `wait()` поза блоком `with condition`, що призводить до `RuntimeError`;
- перевіряти умову через `if` замість `while` навколо `condition.wait()`, ігноруючи spurious
  wakeup.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
