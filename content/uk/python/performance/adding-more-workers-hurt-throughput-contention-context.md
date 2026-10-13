---
id: py-perf-0014
title: "Чому більше workers може погіршити throughput через contention, context switching та downstream saturation?"
description: "Workers понад точку насичення конкурують за спільні ресурси (GIL у звичайній збірці CPython, I/O-дескриптори, downstream-сервіс), додають context switches і не підвищують throughput."
track: python
section: performance
level: senior
type: pitfall
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-glossary-term-parallelism
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-parallelism
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: у збірках з GIL лише один thread виконує bytecode в певний момент, тож багатоядерність зазвичай дають процеси або native extensions, що звільняють GIL."
  - source_id: py314-howto-free-threading
    title: "Python 3.14: Howto/free-threading"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: починаючи з 3.13 CPython має збірку free threading, у якій GIL вимкнено."
  - source_id: py314-library-concurrent-futures-threadpoolexecutor
    title: "Python 3.14: Library/concurrent.futures"
    url: https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: max_workers за замовчуванням з 3.13 – min(32, (os.process_cpu_count() or 1) + 4), до 3.13 – min(32, os.cpu_count() + 4); документація описує значення за замовчуванням, а не оптимальну кількість workers."
  - source_id: py314-library-concurrent-futures-processpoolexecutor
    title: "Python 3.14: Library/concurrent.futures"
    url: https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: max_workers за замовчуванням – os.process_cpu_count() (з 3.13); документація описує значення за замовчуванням, а не оптимальну кількість workers."
---

## Short answer

**Workers понад точку насичення не додають throughput: вони конкурують за спільні ресурси, додають context switches і можуть перевантажити downstream-систему.** У звичайній збірці CPython з GIL лише один thread виконує Python bytecode в певний момент, тож CPU-bound задачі в threads не виконуються паралельно; для кількох ядер беруть processes.[^py314-glossary-term-parallelism] Надмірна кількість processes додає context switching на рівні ОС і витрати RAM на кожен process. Навіть для I/O-bound роботи забагато одночасних з’єднань може вичерпати file descriptors або перевантажити віддалений сервер, тож latency зростає, а throughput може падати.

## Detailed explanation

Throughput – це обсяг завершеної роботи за одиницю часу. Додатковий worker дає приріст, поки є незайнята потужність: час очікування I/O, вільні ядра, вільні з’єднання. Щойно вузьке місце насичене (CPU-ядра, GIL, диск, пул з’єднань, rate limit віддаленого API), нові workers стають у чергу за тим самим ресурсом: throughput може лишатися сталим або падати, а latency зростає. Насичення залежить від навантаження і ресурсів, а не лише від кількості workers.

Для CPU-bound коду це видно найясніше. У звичайній збірці CPython лише один thread виконує bytecode в певний момент,[^py314-glossary-term-parallelism] тому 8 threads, що виконують чистий Python-цикл, не дають більше обчислень за секунду, ніж один thread. Для паралелізму на кількох ядрах беруть processes. З 3.13 CPython має збірку free threading, у якій GIL вимкнено,[^py314-howto-free-threading] але це окрема збірка інтерпретатора, а не заміна звичайної.

Ліміт на downstream ставимо на сам ресурс, а не на число workers. У прикладі 32 workers, але до віддаленого сервісу одночасно йде не більше 4 викликів:

```python
import threading
import time
from concurrent.futures import ThreadPoolExecutor

limit = threading.BoundedSemaphore(4)  # at most 4 calls to the remote service at once
state_lock = threading.Lock()
active = 0
max_active = 0


def call_service(item):
    global active, max_active
    with limit:
        with state_lock:
            active += 1
            max_active = max(max_active, active)
        time.sleep(0.05)  # stands in for a network call
        with state_lock:
            active -= 1
    return item


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=32) as pool:
        list(pool.map(call_service, range(32)))
    print("max concurrent service calls:", max_active)  # prints 4: the semaphore limits it, not the 32 workers
```

Значення за замовчуванням – лише стартова точка. `ThreadPoolExecutor` з 3.13 бере `max_workers = min(32, (os.process_cpu_count() or 1) + 4)` (до 3.13 було `os.cpu_count() + 4`),[^py314-library-concurrent-futures-threadpoolexecutor] а `ProcessPoolExecutor` – `os.process_cpu_count()`.[^py314-library-concurrent-futures-processpoolexecutor] Документація описує ці значення як default, а не як оптимальну кількість workers для вашого навантаження. Надмірна кількість processes на тих самих ядрах додає context switching на рівні ОС і витрати RAM на кожен process.

Межу шукають вимірюванням: збільшуйте workers, поки throughput росте. Коли throughput перестає рости, а latency і кількість помилок (timeouts, відповіді 429 від API) зростають, це насичення. Міряти треба throughput і latency разом: сам throughput не покаже, що downstream уже страждає.

**Типові помилки:**
- збільшувати `max_workers` для CPU-bound коду в thread pool «для швидкості»;
- ставити кількість workers вище ліміту downstream (пул з’єднань, rate limit) замість того, щоб обмежувати саме ресурс;
- вважати default `max_workers` оптимальним;
- міряти лише throughput без latency і помилок.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
