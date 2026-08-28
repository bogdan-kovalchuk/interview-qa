---
id: py-gil-0017
title: "Які умови створюють deadlock і як lock ordering зменшує ризик?"
description: "Deadlock виникає, коли два або більше потоків блокуються назавжди, кожен чекаючи ресурс, утримуваний іншим; класична умова – циклічне очікування locks у різному порядку."
track: python
section: concurrency-and-gil
level: senior
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L421-L483
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Deadlock виникає, коли два або більше потоків блокуються назавжди, кожен чекаючи ресурс, утримуваний іншим; класична умова – циклічне очікування locks у різному порядку.**[^py314-library-threading] Якщо потінок A захоплює Lock1 і чекає Lock2, а потінок B захоплює Lock2 і чекає Lock1 – жоден не продовжить роботу. Lock ordering зменшує ризик: якщо всі потоки захоплюють locks у єдиному глобальному порядку (наприклад, завжди спочатку Lock1, потім Lock2), цикл неможливий. Додатково використовуйте `with` для гарантованого звільнення та timeout на `acquire()`.

## Detailed explanation

Deadlock – це стан, коли кілька потоків чекають один на одного назавжди й жоден не може
продовжити роботу. Класично для цього потрібні чотири умови одночасно: взаємне виключення
(ресурс належить лише одному власнику), утримання й очікування (потік тримає один lock, чекаючи
іншого), відсутність витіснення (lock не можна відібрати ззовні) і циклічне очікування.
Прибрати будь-яку з цих умов – достатньо, щоб deadlock став неможливим.[^py314-library-threading]

На практиці найлегше усунути саме циклічне очікування, тому воно й дає назву типовому сценарію:
два потоки захоплюють два locks у протилежному порядку.

```python
import threading

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread_1():
    with lock_a:
        with lock_b:  # waits for lock_b, held by thread_2
            ...

def thread_2():
    with lock_b:
        with lock_a:  # waits for lock_a, held by thread_1
            ...
```

Якщо `thread_1` встигає захопити `lock_a`, а `thread_2` – `lock_b`, кожен чекає на ресурс, який
тримає інший, і жоден не звільнить свій. Ні timeout за замовчуванням, ні GIL цьому не заважають –
GIL керує лише виконанням bytecode, а не порядком захоплення locks.

Lock ordering прибирає можливість циклу: якщо всі потоки в програмі захоплюють кілька locks
завжди в одному й тому самому глобальному порядку (наприклад, за id об'єкта або за наперед
визначеним списком), цикл очікування не може утворитися, бо потік ніколи не чекатиме на lock, який
йде «раніше» за той, що вже утримує.

**Додаткові способи знизити ризик deadlock:**
- використовувати `with lock:` замість ручних `acquire()`/`release()`, щоб lock завжди звільнявся,
  навіть при exception;
- передавати `timeout` в `acquire()` і обробляти відмову замість нескінченного очікування;
- мінімізувати кількість locks, які потрібно тримати одночасно, звужуючи critical section;
- де можливо, замінювати кілька дрібних locks одним, що покриває весь пов'язаний стан.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
