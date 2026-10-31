---
id: py-async-0022
title: "Як вибрати між `asyncio.Lock`, `Event`, `Condition` та `Semaphore` для coordination protocol?"
track: python
section: asyncio
sources:
  - source_id: py314-library-asyncio-task
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html
  - source_id: py314-library-asyncio-eventloop
    title: "Python 3.14: Library/asyncio Eventloop"
    url: https://docs.python.org/3.14/library/asyncio-eventloop.html
  - source_id: py314-library-asyncio-dev
    title: "Python 3.14: Library/asyncio Dev"
    url: https://docs.python.org/3.14/library/asyncio-dev.html
---

## Short answer

**`Lock` – взаємне виключення; `Event` – сигнал «щось сталося» багатьом Task; `Condition` – очікування зміни стану під захистом lock; `Semaphore` – обмеження кількості одночасних доступів.**[^py314-library-asyncio-task] `Lock` підходить, коли одна Task наразі модифікує спільний ресурс. `Event` – коли одна Task має повідомити іншим про готовність (наприклад, ініціалізацію), а `set()` залишається до `clear()`. `Condition` потрібен, якщо Task має чекати певної умови над ресурсом і одразу після пробудження отримати ексклюзивний доступ – типовий producer/consumer. `Semaphore(N)` обмежує N одночасних користувачів ресурсу (connection pool, throttle API-запитів).

## Detailed explanation

Усі чотири примітиви побудовані на `Future` й не є thread-safe – вони призначені для координації
Task у межах одного event loop, а не потоків чи процесів; спроба поділити один об’єкт `Lock` між
двома event loop дає непередбачувані результати.[^py314-library-asyncio-task]

`Condition` фактично обгортає `Lock` (свій або переданий) і додає `wait()`/`notify()`: викликати
`wait()` можна лише утримуючи lock, після чого він тимчасово звільняється, а Task блокується, доки
хтось не викличе `notify()` або `notify_all()` – і lock автоматично повертається перед тим, як
`wait()` завершиться. Це відрізняє `Condition` від голого `Event`: `Event` не пов’язаний з жодним
ресурсом і не гарантує ексклюзивного доступу після пробудження, тоді як `Condition` гарантує його,
бо lock захоплюється знову перед поверненням з `wait()`.

`asyncio.Lock` не є reentrant: повторний `acquire()` тим самим Task, який уже утримує lock,
призводить до deadlock, на відміну від `threading.RLock`. Усі очікувачі `Lock` і `Semaphore`
обслуговуються у порядку FIFO, тому голодування (starvation) окремого Task теоретично неможливе,
доки інші Task коректно звільняють ресурс.

`BoundedSemaphore` – варіант `Semaphore`, який кидає `ValueError`, якщо `release()` викликано
більше разів, ніж було `acquire()`; це корисно для виявлення баги «зайвого release» під час
розробки connection pool або rate limiter, коли звичайний `Semaphore` просто мовчки дозволив би
лічильнику зрости понад початкове значення.
