---
id: py-gil-0014
title: "Чому паралелізація дрібних CPU tasks через processes може бути повільнішою за sequential execution?"
description: "Накладні витрати на створення процесів, pickle-серіалізацію аргументів і результатів, а також IPC-комунікацію через pipes перевищують час самих обчислень для дрібних задач."
track: python
section: concurrency-and-gil
level: senior
type: practical
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/gil_threads_processes.md#L1082-L1090
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Накладні витрати на створення процесів, pickle-серіалізацію аргументів і результатів, а також IPC-комунікацію через pipes перевищують час самих обчислень для дрібних задач.**[^py314-library-threading] Кожен виклик `submit()` у `ProcessPoolExecutor` вимагає серіалізації callable та аргументів через `pickle` і передачі їх через pipe. Якщо задача виконується мікросекунди, а серіалізація та комунікація – мілісекунди, сукупний overhead домінує. Рішення – групувати задачі в більші батчі.

## Detailed explanation

Паралелізація через процеси має фіксовані витрати на кожну задачу, які не залежать від самої
роботи; якщо задача маленька, ці витрати домінують над часом обчислення, і паралельна версія
виявляється повільнішою за звичайний послідовний цикл.[^py314-library-concurrent-futures]

Витрати складаються з кількох кроків, і кожен `submit()` (або елемент у `map()`) платить за них
окремо: серіалізація callable та аргументів через `pickle` у батьківському процесі, запис байтів у
pipe, десеріалізація у worker-процесі, виконання, серіалізація результату назад і десеріалізація в
батьківському процесі. Сам запуск worker-процесів амортизується на весь час життя `pool`, але цей
цикл серіалізація/IPC - ні, він повторюється для кожної задачі.

За порядком величини pickle і IPC round trip для навіть простих об'єктів займають десятки-сотні
мікросекунд, тоді як обчислення на кшталт множення двох чисел - наносекунди. Тобто накладні витрати
можуть перевищувати корисну роботу в тисячі разів.

```python
from concurrent.futures import ProcessPoolExecutor

def square(x):
    return x * x

# naive: one task per element - overhead dominates for cheap work
with ProcessPoolExecutor() as pool:
    results = list(pool.map(square, range(1_000_000)))

# batched: fewer, larger tasks amortize the per-submit overhead
def square_batch(chunk):
    return [x * x for x in chunk]
```

Найпростіший спосіб зменшити overhead - групувати роботу в більші батчі: замість мільйона окремих
задач передати worker-у список елементів і повернути список результатів одним pickle-циклом.
`ProcessPoolExecutor.map()` частково робить це сам через параметр `chunksize`, який об'єднує кілька
елементів ітерабла в одну задачу.[^py314-library-multiprocessing]

**Коли варто занепокоїтись:**
- задача виконується мікросекунди, а не мілісекунди чи довше;
- аргументи або результат - великі чи складні об'єкти, що дорого серіалізуються;
- кількість викликів `submit()`/елементів у `map()` набагато більша за кількість worker-процесів.

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
