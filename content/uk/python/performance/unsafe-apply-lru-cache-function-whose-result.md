---
id: py-perf-0021
title: "Чому `lru_cache` небезпечно застосовувати до function, result якої залежить від current time, randomness, external mutable state чи side effects?"
description: "lru_cache зберігає результат виключно за комбінацією аргументів, тому для non-pure function повертає застаріле або некоректне значення, а side effects на cache hit взагалі пропускаються."
track: python
section: performance
level: middle
type: pitfall
tags: [lru-cache]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-library-profile
    title: "Python 3.14: Library/profile"
    url: https://docs.python.org/3.14/library/profile.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-timeit
    title: "Python 3.14: Library/timeit"
    url: https://docs.python.org/3.14/library/timeit.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
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
  - source_id: py314-faq-programming-performance
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#performance
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools-functools-lru-cache
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.lru_cache
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-stdtypes-common-sequence-operations
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#common-sequence-operations
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/standard_library.md#L666-L695
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`lru_cache` зберігає результат виключно за комбінацією аргументів, тому для non-pure function повертає застаріле або некоректне значення, а side effects на cache hit взагалі пропускаються.**[^py314-library-profile] Декоратор припускає, що функція є детермінованою: однакові аргументи -> однаковий результат. Якщо результат залежить від `time.time()`, `random`, глобального мутабельного стану або зовнішнього I/O, кешований return value більше не відповідає поточному виклику. Функції з side effects (запис у файл, логування, мутація аргументів) при повторному виклику з тими самими аргументами взагалі не виконуються – тіло функції пропускається, і side effect зникає.

```python
from functools import lru_cache
import time

@lru_cache()
def fetch_now():
    return time.time()

first = fetch_now()
time.sleep(0.1)
print(fetch_now() == first)  # True - stale cached value
```

<span class="warn">Попередження:</span> `lru_cache` також зберігає strong references на аргументи й return values доки вони не будуть evicted, що може подовжити життя великих об'єктів.

## Detailed explanation

TODO

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
