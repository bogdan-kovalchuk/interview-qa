---
id: py-perf-0021
title: "Чому `lru_cache` небезпечно застосовувати до function, result якої залежить від current time, randomness, external mutable state чи side effects?"
track: python
section: performance
sources:
  - source_id: py314-library-functools-functools-lru-cache
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.lru_cache
---

## Short answer

**`lru_cache` повертає збережений результат лише для повторного виклику з тими самими аргументами, поки запис є в кеші, тому для функції, яка залежить від часу, випадковості чи зовнішнього стану, він дає застаріле значення, а side effects на cache hit пропускаються.**[^py314-library-functools-functools-lru-cache] Документація прямо каже, що не має сенсу кешувати функції з side effects і impure функції, як `time()` чи `random()`.[^py314-library-functools-functools-lru-cache]

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

<span class="warn">Попередження:</span> кеш тримає посилання на аргументи й результати, доки вони не виселені; з `maxsize=None` він може рости без обмеження.[^py314-library-functools-functools-lru-cache]

## Detailed explanation

`lru_cache` обгортає функцію і зберігає її результати у словнику, ключем якого є аргументи виклику. Тому аргументи мають бути hashable.[^py314-library-functools-functools-lru-cache] Коли той самий набір аргументів приходить удруге, поки його запис є в кеші, декоратор повертає збережене значення без нового виклику функції.[^py314-library-functools-functools-lru-cache] Саме це робить кеш корисним для дорогих обчислень і небезпечним для всього, що залежить від стану поза аргументами.

Декоратор не бачить нічого, крім аргументів. Якщо результат залежить від `time.time()`, `random`, глобального словника, файлу чи бази даних, кеш віддає значення, яке вже не відповідає стану. Документація прямо каже, що не має сенсу кешувати функції з side effects, функції, які мають створювати окремі mutable-об’єкти на кожному виклику (наприклад, генератори й async-функції), та impure функції, як `time()` чи `random()`.[^py314-library-functools-functools-lru-cache]

Side effects на cache hit не відбуваються, бо тіло функції не виконується. У прикладі другий виклик не додає запис до `calls`:

```python
from functools import lru_cache

calls = []

@lru_cache(maxsize=None)
def save(name):
    calls.append(name)   # side effect: runs only on a cache miss
    return len(calls)

print(save("a"), save("a"))  # 1 1 : second call is a cache hit, body skipped
print(calls)  # ['a']
```

Збережене значення може бути mutable. Той самий об’єкт повертається кожному виклику з тими самими аргументами, тому зміна, зроблена через одне посилання, видна через усі інші:

```python
from functools import lru_cache


@lru_cache(maxsize=None)
def new_bucket(name):
    return []  # a new list on each call without the cache


first = new_bucket("a")
first.append("x")
second = new_bucket("a")  # cache hit: the same list object is returned
print(second)  # ['x']
print(first is second)  # True
```

Кеш тримає посилання на аргументи й результати, доки записи не виселено або кеш не очищено. З `maxsize=None` LRU-виселення вимикається, і кеш може рости без обмеження.[^py314-library-functools-functools-lru-cache] Безпечний випадок – чиста функція з hashable аргументами, чий результат дорогий і не залежить від стану поза аргументами. Якщо потрібна свіжість, кеш очищують викликом `cache_clear()`,[^py314-library-functools-functools-lru-cache] або функцію взагалі не кешують.

**Типові помилки:**
- кешувати функцію, яка читає `time.time()`, `random` або файл, і вважати, що повторний виклик перевіряє стан знову;
- очікувати, що логування чи лічильник усередині кешованої функції спрацьовують на кожен виклик;
- повертати з кешованої функції mutable-об’єкт і змінювати його в місці виклику.
