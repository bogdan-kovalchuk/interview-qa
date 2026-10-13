---
id: py-stdlib-0007
title: "Чим `cached_property` відрізняється від `property` за caching, attribute writes та invalidation?"
description: "cached_property обчислює значення при першому зверненні й зберігає його в __dict__ інстансу, тоді як property викликає getter при кожному зверненні."
track: python
section: standard-library
level: middle
type: comparison
tags: [cached-property, property]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-functools-cached-property
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.cached_property
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, розділ cached_property: кешування, запис в атрибут, видалення для скидання кешу, race condition, вимога mutable __dict__."
---

## Short answer

**`cached_property` обчислює значення при першому зверненні й зберігає його в `__dict__` інстансу, тоді як `property` викликає getter при кожному зверненні.**[^py314-library-functools-cached-property] Запис у `cached_property` замінює збережене значення; запис у `property` викликає його setter, а без setter кидає `AttributeError`. Інвалідація – через `del instance.attr`, після чого наступне звернення знову обчислить значення. Потребує mutable `__dict__`, тому не працює з `__slots__` без `__dict__`.[^py314-library-functools-cached-property]

## Detailed explanation

`cached_property` відрізняється від `property` тим, що зберігає результат getter. Перше звернення викликає функцію і записує результат у `instance.__dict__` під іменем атрибута. Наступні звернення знаходять значення там і до descriptor не доходять. Документація каже, що після цього атрибут з тим самим іменем має перевагу над `cached_property`: читання й записи йдуть до нього.[^py314-library-functools-cached-property] У CPython `cached_property` визначає `__get__` і `__set_name__`, але не `__set__`, тобто це non-data descriptor.

`property` навпаки викликає getter при кожному зверненні. Без setter присвоєння такому атрибуту кидає `AttributeError`. `cached_property` запис дозволяє: присвоєння замінює збережене значення, і наступне читання повертає його без обчислення. Це зручно для ручного заповнення кешу, але тоді значення може розійтися з тим, що повернув би getter.[^py314-library-functools-cached-property]

Приклад порівнює обидва descriptors. Вивід однаковий на CPython 3.13 і 3.14:

```python
from functools import cached_property

class Report:
    def __init__(self, rows):
        self.rows = rows

    @cached_property
    def total(self):
        print("computing total")
        return sum(self.rows)

    @property
    def count(self):
        print("computing count")
        return len(self.rows)

r = Report([1, 2, 3])
print(r.total)   # computing total, then 6
print(r.total)   # 6, no recomputation
print(r.count)   # computing count, then 3
print(r.count)   # computing count again, then 3
r.total = 100    # cached_property allows the write
print(r.total)   # 100
del r.total      # clears the cache
print(r.total)   # computing total, then 6
r.count = 5      # AttributeError: property 'count' of 'Report' object has no setter
```

Інвалідація – це `del instance.attr`: наступне звернення знову викличе getter. Документація каже, що кешоване значення можна очистити видаленням атрибута.[^py314-library-functools-cached-property] Сам кеш не оновлюється, коли змінюються дані getter: після зміни `self.rows` `r.total` повертає старе значення, доки атрибут не видалено.

Два обмеження важливі. По-перше, до Python 3.12 `cached_property` мав недокументований lock, який гарантував один запуск getter на інстанс; з 3.12 lock прибрано. Тепер у багатопотоковому коді getter може виконатися більше одного разу, а останній запуск запише кешоване значення. Якщо це шкідливо, синхронізацію треба додати всередині getter.[^py314-library-functools-cached-property] По-друге, потрібен mutable `__dict__`, тож метакласи й класи з `__slots__` без `__dict__` не підтримуються.[^py314-library-functools-cached-property] У CPython звернення до такого атрибута кидає `TypeError`.

**Типові помилки:**
- вважати, що getter у `cached_property` виконується один раз за будь-яких умов;
- присвоювати значення кешованому атрибуту й забувати, що воно може не збігатися з результатом getter;
- очікувати оновлення після зміни `rows` без `del`;
- застосувати `cached_property` до класу з `__slots__` без `__dict__`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
