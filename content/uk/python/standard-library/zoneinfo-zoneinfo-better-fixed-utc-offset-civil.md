---
id: py-stdlib-0012
title: "Чому `zoneinfo.ZoneInfo` краще за фіксований UTC offset для civil time з daylight-saving transitions?"
description: "ZoneInfo обчислює зсув від UTC для кожного моменту за правилами IANA-бази, тому фіксований зсув не може коректно пройти перехід на літній час."
track: python
section: standard-library
level: middle
type: comparison
tags: [zoneinfo-zoneinfo]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-zoneinfo
    title: "Python 3.14: Library/zoneinfo"
    url: https://docs.python.org/3.14/library/zoneinfo.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: ZoneInfo за базою IANA, datetime-арифметика через DST, fold і джерела даних (системна база або пакет tzdata)."
  - source_id: py314-library-datetime
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: timezone має фіксований зсув від UTC; додавання timedelta до aware datetime зберігає tzinfo без коригування часового поясу; віднімання для однакового tzinfo ігнорує tzinfo."
---

## Short answer

**`ZoneInfo` зберігає правила часового поясу з IANA-бази, тому обчислює зсув від UTC для кожного конкретного моменту, включно з переходами DST.**[^py314-library-zoneinfo] Фіксований `timezone(timedelta(hours=-5))` має один зсув назавжди, тож влітку його wall clock розходиться з місцевим часом.[^py314-library-datetime] Для неоднозначних моментів під час переходу з літнього часу на стандартний `ZoneInfo` розрізняє два варіанти через `fold`.[^py314-library-zoneinfo]

## Detailed explanation

Перехід на літній час (DST) змінює зсув від UTC. `ZoneInfo` читає правила зони з IANA-бази.[^py314-library-zoneinfo] Фіксований `timezone(timedelta(hours=-5))` описує один зсув і правил не знає, тож для місцевого часу міста з DST він правильний лише частину року.[^py314-library-datetime]

Арифметика `timedelta` з aware datetime зберігає tzinfo і не виконує коригувань часового поясу.[^py314-library-datetime] Зсув результату обчислюється заново за його wall clock.[^py314-library-zoneinfo] Тому `timedelta(days=1)` означає «та сама місцева година наступного дня», а `timedelta(hours=N)` додає N до wall clock, а не N реальних годин.

Приклад (виконано на CPython 3.13 і 3.14):

```python
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

NY = ZoneInfo("America/New_York")

# A fixed offset stays -05:00 all year, so its local time in summer is one hour off.
fixed = timezone(timedelta(hours=-5))
print((datetime(2026, 3, 7, 9, tzinfo=fixed) + timedelta(days=1)).astimezone(NY))  # 2026-03-08 10:00:00-04:00

# ZoneInfo recomputes the offset for the result's wall-clock time.
print(datetime(2026, 3, 7, 9, tzinfo=NY) + timedelta(days=1))  # 2026-03-08 09:00:00-04:00

# Fall back: wall-clock arithmetic and elapsed time differ.
start = datetime(2026, 11, 1, 0, 30, tzinfo=NY)  # 00:30 EDT
end = start + timedelta(hours=2)                  # wall clock now 02:30, EST
print(end - start)                                # 2:00:00 (same tzinfo: wall-clock difference)
print(end.astimezone(timezone.utc) - start.astimezone(timezone.utc))  # 3:00:00 (real elapsed time)
```

Фіксований зсув дає 10:00 у Нью-Йорку, а `ZoneInfo` – 09:00 з `-04:00`. При відкаті `start + timedelta(hours=2)` дає 02:30, але `end - start` для одного tzinfo дорівнює `2:00:00`, хоча минуло три реальні години; для реального інтервалу переведіть значення в UTC.[^py314-library-datetime] Неоднозначний 01:30 у день відкату має `fold=0` (зсув до переходу) або `fold=1` (після).[^py314-library-zoneinfo]

Доступність даних – окрема умова: без системних даних часових поясів і пакета `tzdata` кожен `ZoneInfo(...)` викидає `ZoneInfoNotFoundError`.[^py314-library-zoneinfo]

**Типові помилки:**
- вважати, що `timedelta(hours=N)` для ZoneInfo-часу завжди дає N реальних годин: при зміні зсуву між моментами різниця інша;
- обчислювати тривалість через `-` для datetime з одним tzinfo і отримувати wall-clock різницю;
- зберігати зсув як `-05:00` замість назви зони `America/New_York`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
