---
id: py-prac-0018
title: "Спроєктуйте thread-safe rate-limit decorator з injected monotonic clock: до X викликів за rolling T seconds, перевищення викликає явний exception."
track: python
section: practical-coding
sources:
  - source_id: py314-library-threading-lock-objects
    title: "Python 3.14: Library/threading, Lock Objects"
    url: https://docs.python.org/3.14/library/threading.html#lock-objects
  - source_id: py314-library-time-time-monotonic
    title: "Python 3.14: Library/time"
    url: https://docs.python.org/3.14/library/time.html#time.monotonic
  - source_id: py314-library-time-time-time
    title: "Python 3.14: Library/time, time.time"
    url: https://docs.python.org/3.14/library/time.html#time.time
  - source_id: py314-library-collections-collections-deque
    title: "Python 3.14: Library/collections, deque"
    url: https://docs.python.org/3.14/library/collections.html#collections.deque
---

## Short answer

**Rolling window тримає `timestamps` list під `threading.Lock`, а injected `clock` (default `time.monotonic`) дозволяє тестування: expired timestamps видаляються з початку list.** `threading.Lock` підтримує context management protocol, тож `with lock:` бере і відпускає його.[^py314-library-threading-lock-objects] <span class="warn">`time.time()` не підходить, бо системний годинник можна перевести назад.</span>[^py314-library-time-time-time] `time.monotonic()` не може йти назад.[^py314-library-time-time-monotonic] `clock()` читається всередині `with lock:`, щоб `timestamps` лишався впорядкованим.

```python
import threading
import time
import functools

class RateLimitExceeded(Exception):
    pass

def rate_limit(max_calls, period, clock=None):
    if clock is None:
        clock = time.monotonic
    def decorator(func):
        lock = threading.Lock()
        timestamps = []
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            with lock:
                now = clock()
                cutoff = now - period
                while timestamps and timestamps[0] <= cutoff:
                    timestamps.pop(0)
                if len(timestamps) >= max_calls:
                    raise RateLimitExceeded(
                        f"Rate limit: {max_calls} calls per {period}s"
                    )
                timestamps.append(now)
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

## Detailed explanation

Rate limit з вікном `T` секунд дозволяє до `X` викликів за останні `T` секунд. Реалізація зберігає моменти успішних викликів. Перед кожним викликом видаляються записи з `ts <= now - T`, і якщо залишилось `X`, піднімається виняток. Сам `func` викликається поза lock, щоб повільна функція не блокувала інші потоки.

`time.monotonic()` задокументовано як годинник, що не може йти назад і не залежить від оновлень системного годинника.[^py314-library-time-time-monotonic] Тому різниця між моментами виклику не стає від’ємною через переведення системного часу. `time.time()` для цього не підходить: він може повернути значення нижче за попереднє, якщо системний годинник перевели назад.[^py314-library-time-time-time] Injected `clock` дає тесту змогу підставити власний годинник і керувати часом без реального очікування.

Порядок читання `clock()` і взяття lock важливий. Якщо `now` читати до lock, два потоки можуть записати моменти не за зростанням: потік A прочитав `10.0` і призупинився, потік B прочитав `10.5` і записав його першим, потім A записав `10.0` у кінець. Тоді `timestamps[0]` дорівнює `10.5`, і цикл видалення зупиняється на ньому, хоча `10.0` уже не належить вікну. При примусово заданому порядку потоків на CPython 3.13 і 3.14 з `T = 1` і `X = 2` виклик у момент `11.2` отримує `RateLimitExceeded`, хоча у вікні `(10.2, 11.2]` лише один виклик (`10.5`). Тому `clock()` читається всередині `with lock:`.

У CPython `list.pop(0)` зсуває решту елементів, тобто коштує O(n); це деталь реалізації. Для великих вікон `collections.deque` дає приблизно однаковий O(1) для `popleft()` і `append()` з будь-якого боку.[^py314-library-collections-collections-deque]

**Типові помилки:**
- читати час до lock: порядок записів ламається, як показано вище;
- використовувати `time.time()` для вікна: перевід годинника назад затримує видалення записів, а перевід уперед видаляє їх передчасно;
- викликати `func` усередині lock: усі потоки чекають на один довгий виклик.
