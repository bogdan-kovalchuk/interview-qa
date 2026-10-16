---
id: py-perf-0019
title: "Чому один positive `tracemalloc` snapshot diff після workload ще не доводить leak і як repeated steady-state measurements відрізняють cache growth від unbounded retention?"
track: python
section: performance
sources:
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
  - source_id: py314-library-functools-functools-lru-cache
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.lru_cache
---

## Short answer

**tracemalloc відстежує блоки, виділені Python, а порівняння двох snapshots призначене для пошуку leaks.**[^py314-library-tracemalloc] Один позитивний diff ще не доводить leak: це може бути прогрівання кешу або lazy initialization. Щоб відрізнити bounded cache від unbounded retention, прогрівають workload, роблять кілька snapshots однакового workload і дивляться на пізні кроки: `lru_cache` з `maxsize` не росте без меж, а з `maxsize=None` може рости без меж.[^py314-library-functools-functools-lru-cache] <span class="warn">У CPython tracemalloc не бачить пам’ять, яку C-код виділяє напряму через malloc(), тому чистий diff не гарантує відсутність leak у C extension.</span>

## Detailed explanation

tracemalloc відстежує блоки пам’яті, які виділив Python, а не весь RSS процесу. Snapshot фіксує блоки, що живі в певний момент, а `Snapshot.compare_to()` показує різницю між двома snapshots.[^py314-library-tracemalloc] Tracing треба ввімкнути до вимірюваних раундів: snapshot не містить блоків, виділених до того, як tracemalloc почав відстежувати пам’ять.[^py314-library-tracemalloc] Прогрів (warm-up) може піти до старту, бо порівнюються лише виміряні раунди.

Одна позитивна різниця може відображати легітимний ріст: lazy initialization, прогрівання кешу або тимчасову структуру, що ще жива під час другого snapshot. Вона не каже, чи ці блоки будуть звільнені пізніше, тож один результат не відрізняє cache growth від retention.

Метод: прогнати workload до steady state, зробити кілька snapshots однакового workload і порівняти пізні пари. `functools.lru_cache` з `maxsize` не росте без меж, а з `maxsize=None` може рости без меж.[^py314-library-functools-functools-lru-cache] Тому плато вказує на обмеження, а ріст на кожному кроці того самого workload – на retention, яку треба шукати (хто тримає посилання на об’єкти).

Приклад порівнює кеш з `maxsize=100` і необмежений кеш на однаковому workload: після прогріву кожен крок додає 1000 нових ключів (ілюстративний приклад):

```python
import tracemalloc
from functools import lru_cache

@lru_cache(maxsize=100)  # bounded: at most 100 entries are kept
def bounded(key):
    return f"{key}:" + "x" * 1000

@lru_cache(maxsize=None)  # unbounded: every new key is kept
def unbounded(key):
    return f"{key}:" + "x" * 1000

next_key = 0

def workload(func):  # one round of 1000 calls, each with a new key
    global next_key
    for _ in range(1000):
        func(next_key)
        next_key += 1

def growth_per_round(func):
    workload(func)                  # warm-up before tracing: the cache fills up to its limit
    tracemalloc.start()
    s2 = tracemalloc.take_snapshot()
    workload(func)
    s3 = tracemalloc.take_snapshot()
    workload(func)
    s4 = tracemalloc.take_snapshot()
    tracemalloc.stop()
    return sum(x.size_diff for x in s4.compare_to(s3, "filename"))

print("bounded:", growth_per_round(bounded) // 1024, "KiB per round")
print("unbounded:", growth_per_round(unbounded) // 1024, "KiB per round")
# Output:
# bounded: 0 KiB per round
# unbounded: 1125 KiB per round
```

Межі: tracemalloc відстежує аллокації, які робить Python (domain 0), а C extensions можуть використовувати інші domains для власних ресурсів.[^py314-library-tracemalloc] У CPython пам’ять, яку C-код виділяє напряму через malloc(), у snapshot не потрапляє, тож чистий diff не доводить відсутність leak у C extension.

**Типові помилки:**
- робити висновок про leak з одного snapshot diff;
- запускати tracemalloc після вимірюваних раундів, тож їхні блоки не потраплять у snapshot;
- вважати плато доказом відсутності leak, зокрема в пам’яті C extension;
- порівнювати snapshots з різним обсягом роботи між ними і приймати різницю за retention.
