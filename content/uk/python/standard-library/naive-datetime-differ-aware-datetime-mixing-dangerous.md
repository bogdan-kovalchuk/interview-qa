---
id: py-stdlib-0011
title: "Чим naive `datetime` відрізняється від aware `datetime` і чому їх небезпечно змішувати?"
track: python
section: standard-library
sources:
  - source_id: py314-library-datetime-determining-aware-or-naive
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html#determining-if-an-object-is-aware-or-naive
  - source_id: py314-library-datetime-aware-and-naive-objects
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html#aware-and-naive-objects
  - source_id: py314-library-datetime-objects
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html#datetime-objects
---

## Short answer

**Naive `datetime` не має інформації про часову зону (`tzinfo is None` або `utcoffset()` повертає `None`), тоді як aware має `tzinfo` з визначеним зсувом.**[^py314-library-datetime-determining-aware-or-naive] Порядкове порівняння (`<`, `>`) і віднімання між naive й aware об’єктами піднімають `TypeError`.[^py314-library-datetime-objects] Порівняння на рівність помилки не викликає, але naive і aware об’єкти ніколи не рівні, тож помилка тиха.[^py314-library-datetime-objects]

## Detailed explanation

У `datetime` поняття aware і naive визначено формально: об’єкт `d` є aware, якщо `d.tzinfo` не `None` і `d.tzinfo.utcoffset(d)` не повертає `None`; інакше він naive.[^py314-library-datetime-determining-aware-or-naive] Naive значення не каже, чи це UTC, локальний час або інша зона: це вирішує програма. Aware значення позначає конкретний момент, який не залежить від інтерпретації.[^py314-library-datetime-aware-and-naive-objects]

Небезпека в тому, що помилка проявляється по-різному. Порядкове порівняння й віднімання між naive та aware кидають `TypeError` одразу. Рівність такої помилки не викликає: `==` дає `False`, а `!=` дає `True`, бо naive й aware об’єкти ніколи не рівні. Тому код, який лише перевіряє рівність, наприклад пошук значення в списку, мовчки не знайде збігу.[^py314-library-datetime-objects]

Приклад показує обидві поведінки. Вивід однаковий на CPython 3.13 і 3.14:

```python
from datetime import datetime, timezone

naive = datetime(2026, 10, 13, 12, 0)                       # no tzinfo: naive
aware = datetime(2026, 10, 13, 12, 0, tzinfo=timezone.utc)  # fixed offset: aware

print(naive == aware, naive != aware)  # False True, no exception
print(naive < aware)                   # TypeError: can't compare offset-naive and offset-aware datetimes
```

Надійніше тримати час aware з самого початку і порівнювати моменти в UTC. `datetime.now(timezone.utc)` повертає aware значення, тоді як `datetime.now()` повертає naive локальний час.[^py314-library-datetime-objects] Метод `replace(tzinfo=timezone.utc)` не конвертує годину, а лише позначає її як UTC. Якщо насправді це був локальний час, отриманий момент зміщений на зсув зони.

**Типові помилки:**
- порівнювати `datetime.now()` (naive, локальний час) з `datetime.now(timezone.utc)` (aware);
- трактувати `False` від `==` як «різні моменти»: для naive й aware це лише несумісність типів;
- додавати `tzinfo=timezone.utc` до naive значення, яке було локальним часом;
- зберігати naive datetime без позначки зони в базі даних або API.
