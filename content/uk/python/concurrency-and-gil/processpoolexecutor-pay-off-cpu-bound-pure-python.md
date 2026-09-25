---
id: py-gil-0013
title: "Коли `ProcessPoolExecutor` може дати виграш для CPU-bound pure-Python workload у GIL-enabled CPython?"
description: "ProcessPoolExecutor дає справжній CPU-паралелізм у GIL-enabled CPython, оскільки кожен worker працює в окремому процесі з власним GIL."
track: python
section: concurrency-and-gil
level: middle
type: practical
tags: [processpoolexecutor]
status: published
updated: 2026-09-27
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
---

## Short answer

**`ProcessPoolExecutor` дає справжній CPU-паралелізм у GIL-enabled CPython, оскільки кожен worker працює в окремому процесі з власним GIL.**[^py314-library-threading] Виграш з'являється, коли обчислювальна робота суттєво перевищує накладні витрати на pickle-серіалізацію аргументів/результатів та старт процесів. Функції та дані мають бути picklable; лямбди та замикання з `__main__` не працюють.

## Detailed explanation

У стандартній збірці CPython із увімкненим GIL потоки виконання не можуть паралельно виконувати байткод Python на кількох ядрах CPU через дію глобального блокування інтерпретатора.[^py314-library-threading] Тому спроба розпаралелити чисто обчислювальну задачу (pure-Python CPU-bound) через `ThreadPoolExecutor` не приносить прискорення, а навпаки збільшує час виконання через постійну конкуренцію за GIL та витрати на перемикання контексту потоків. `ProcessPoolExecutor` із модуля `concurrent.futures` долає це обмеження, створюючи окремі процеси-робітники, кожен із яких запускає власний інтерпретатор CPython з ізольованим екземпляром GIL та незалежною пам'яттю.[^py314-library-concurrent-futures]

Однак використання окремих процесів пов'язане з суттєвими накладними витратами. Запуск нових процесів вимагає ініціалізації середовища CPython та імпорту модулів, а кожен виклик завдання потребує серіалізації аргументів через `pickle.dumps`, їх передачі через IPC-канал і десеріалізації у worker-процесі (`pickle.loads`), з аналогічною процедурою для поверненого результату.[^py314-library-multiprocessing] Якщо тривалість самих обчислень менша або співмірна з часом на серіалізацію та передачу даних (fine-grained tasks), багатопроцесна версія буде працювати значно повільніше за простий послідовний цикл.

`ProcessPoolExecutor` починає давати реальний виграш лише тоді, коли обчислювальна гранулярність завдань достатньо велика (coarse-grained workload), тобто час чистого виконання функції на CPU на порядки перевищує накладні витрати на IPC. Для пакетних обчислень критично використовувати параметр `chunksize` у методі `executor.map()`, що дозволяє передавати елементи пачками в одному IPC-повідомленні, радикально знижуючи накладні витрати на серіалізацію для кожного елемента.

Приклад використання `ProcessPoolExecutor` для CPU-bound обчислень із групуванням завдань через `chunksize`:

```python
from concurrent.futures import ProcessPoolExecutor
import math

def is_prime_heavy(n):
    # Pure-Python CPU-bound task with sufficient computational weight
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    numbers = [10_000_019, 10_000_079, 10_000_103, 10_000_121]

    # chunksize batches items to amortize pickle and IPC transfer overhead
    with ProcessPoolExecutor() as executor:
        results = list(executor.map(is_prime_heavy, numbers, chunksize=2))

    print(results)  # [True, True, True, True]
```

**Практичні наслідки та вимоги:**
- завдання повинні бути coarse-grained: якщо операція триває мікросекунди, витрати на IPC нівелюють будь-яку вигоду від додаткових ядер;
- використання `chunksize > 1` у `executor.map()` є обов'язковим при обробці великих послідовностей для зменшення кількості IPC round trip;
- усі аргументи, функції та значення повернення мають бути picklable; не можна передавати замикання, локальні функції, lambda чи відкриті дескриптори ресурсів;
- блок створення пулу обов'язково захищається перевіркою `if __name__ == '__main__':`, щоб уникнути нескінченної рекурсії при імпорті модуля дочірніми процесами на платформах із `spawn` або `forkserver`.

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
