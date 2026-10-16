---
id: py-perf-0012
title: "Як спроєктувати cache invalidation та eviction, якщо source data можуть змінюватися?"
track: python
section: performance
sources:
  - source_id: py314-library-functools-functools-lru-cache
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.lru_cache
---

## Short answer

**Потрібно поєднати стратегію eviction (обмеження розміру) із механізмом invalidation (скасування застарілих записів за зміною source data).** `functools.lru_cache` дає LRU-eviction з `maxsize` і метод `cache_clear()`[^py314-library-functools-functools-lru-cache], але не відстежує source data. Для mutable source data застосовують TTL-cache (словник із timestamp і періодичним очищенням), versioned cache key (версію або хеш ресурсу додають до ключа) чи write-through cache з подіями invalidation. <span class="warn">Якщо `maxsize=None`, cache зростає без меж[^py314-library-functools-functools-lru-cache], а без invalidation він віддає застарілі значення.</span>

## Detailed explanation

Eviction і invalidation вирішують різні задачі. Eviction обмежує пам’ять: коли cache заповнений, видаляється найдавніше використаний запис. Invalidation означає, що після зміни source data застарілий запис більше не віддається. `lru_cache(maxsize=N)` дає перше, а `cache_clear()` очищає весь cache функції.[^py314-library-functools-functools-lru-cache] Окремого видалення одного ключа в `lru_cache` немає. Якщо `maxsize=None`, LRU вимкнено і cache може зростати без обмеження.[^py314-library-functools-functools-lru-cache]

Версія в ключі – один зі способів invalidation без подій. Версію беремо з source дешевим запитом (наприклад, `updated_at` або номер ревізії), а результат кешуємо за парою `(name, version)`:

```python
from functools import lru_cache


@lru_cache(maxsize=256)
def load_config(name, version):
    print(f"loading {name} v{version}")
    return {"name": name, "version": version}


load_config("db", 1)  # loading db v1
load_config("db", 1)  # no output: cache hit
load_config("db", 2)  # loading db v2: a new version is a new key
print(load_config.cache_info())  # CacheInfo(hits=1, misses=2, maxsize=256, currsize=2)
```

Новий ключ не віддає застарілий результат. Але запис `('db', 1)` лишається в cache, поки LRU його не витіснить: `cache_info()` показує `currsize=2`. Схема окупається, лише якщо перевірка версії коштує менше, ніж повторне читання даних; інакше cache нічого не дає.

Коли версії немає, використовують TTL: запис зберігає час завантаження і перечитується після спливу TTL. Це обмежує вік застарілих даних, але не гарантує актуальності: до спливу TTL запис може вже бути неактуальним. Точніша актуальність потребує подій змін: код, що змінює source data, видаляє відповідний ключ зі власного словника, бо `lru_cache` такого видалення не має.

Межі області дії. `lru_cache` живе в пам’яті процесу. Кожен worker у `ProcessPoolExecutor` має власний cache, тому `cache_clear()` в одному процесі не очищає інші; для кількох процесів або машин invalidation має йти через спільне сховище чи повідомлення. Сам cache потокобезпечний, але функція може виконатися більше одного разу, якщо інший потік викличе її з тими самими аргументами до завершення першого виклику.[^py314-library-functools-functools-lru-cache]

**Типові помилки:**
- взяти `functools.cache` для даних, які змінюються: ліміту немає, і застарілі значення лишаються до перезапуску процесу;
- очистити cache в одному процесі, вважаючи, що очистилися всі worker-и;
- зробити TTL довшим за допустиму затримку оновлення або перевіряти версію дорогим запитом, через що cache не дає виграшу.
