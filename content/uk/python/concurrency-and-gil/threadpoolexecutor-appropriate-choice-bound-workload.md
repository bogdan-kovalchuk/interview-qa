---
id: py-gil-0012
title: "Коли `ThreadPoolExecutor` є доречним вибором для I/O-bound workload?"
description: "ThreadPoolExecutor доречний, коли задача проводить більшу частину часу в очікуванні зовнішніх відповідей (мережа, диск, БД), а не в обчисленнях."
track: python
section: concurrency-and-gil
level: middle
type: practical
tags: [threadpoolexecutor]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L940-L986
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`ThreadPoolExecutor` доречний, коли задача проводить більшу частину часу в очікуванні зовнішніх відповідей (мережа, диск, БД), а не в обчисленнях.**[^py314-library-threading] У GIL-enabled CPython threads можуть паралельно чекати I/O, бо GIL звільняється під час системних викликів. Default кількість workers – `min(32, os.process_cpu_count() + 4)`, що розрахована саме на I/O-bound навантаження. Для CPU-bound задач threads не дають справжнього паралелізму через GIL.

## Detailed explanation

`ThreadPoolExecutor` – це пул воркер-потоків з `concurrent.futures`, який виконує callable-и з
черги задач і повертає `Future` для кожного виклику.[^py314-library-concurrent-futures]

Він доречний саме для I/O-bound навантаження, тому що GIL звільняється на час системних викликів:
поки один thread чекає відповіді мережі, диска чи бази даних, GIL може перейти до іншого thread, і
кілька I/O-операцій фактично виконуються одночасно навіть у звичайному GIL-enabled
CPython.[^py314-howto-free-threading-python]

Приклад типового використання – паралельні мережеві запити:

```python
from concurrent.futures import ThreadPoolExecutor

def fetch(url):
    ...  # a blocking network call; the GIL is released while waiting

with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(fetch, urls))
```

Default кількість workers, якщо `max_workers` не задано, – `min(32, os.process_cpu_count() + 4)`.
Це число явно розраховане на I/O-bound задачі: воно суттєво більше за кількість ядер, бо потоки
здебільшого простоюють в очікуванні, а не рахують.[^py314-library-concurrent-futures]

Для CPU-bound роботи той самий пул не дає прискорення: GIL не звільняється під час обчислень у
чистому Python-коді, тож потоки виконують bytecode по черзі, а накладні витрати на перемикання
контексту тільки додаються. Для такої роботи натомість підходить `ProcessPoolExecutor`, який обходить
GIL ціною окремого процесу і серіалізації даних для кожного виклику.

**Ознаки, що `ThreadPoolExecutor` – правильний вибір:**
- задача здебільшого чекає (мережа, диск, БД, зовнішній процес), а не рахує;
- потрібен спільний доступ до пам'яті процесу без IPC чи серіалізації;
- кількість одночасних задач помірна, і накладні витрати на потоки не критичні.

**Ознаки, що варто обрати інше:**
- обчислення завантажують CPU – тоді потрібен `ProcessPoolExecutor` або free-threaded build;
- задач дуже багато, і вони переважно чекають на мережу – тоді `asyncio` масштабується краще за
  потоки з їхньою фіксованою кількістю workers.

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
