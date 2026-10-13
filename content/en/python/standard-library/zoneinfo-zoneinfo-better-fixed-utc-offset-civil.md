---
id: py-stdlib-0012
title: "Why is `zoneinfo.ZoneInfo` better than a fixed UTC offset for civil time with daylight-saving transitions?"
description: "Why is `zoneinfo.ZoneInfo` better than a fixed UTC offset for civil time with daylight-saving transitions?"
track: python
section: standard-library
level: middle
type: comparison
tags: [zoneinfo-zoneinfo]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-zoneinfo
    title: "Python 3.14: Library/zoneinfo"
    url: https://docs.python.org/3.14/library/zoneinfo.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: ZoneInfo with the IANA database, datetime arithmetic across DST, fold, and data sources (system data or the tzdata package)."
  - source_id: py314-library-datetime
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: timezone has a fixed offset from UTC; adding a timedelta to an aware datetime keeps tzinfo without time zone adjustment; subtraction of datetimes with the same tzinfo ignores tzinfo."
---

## Short answer

**`ZoneInfo` holds the time zone rules from the IANA database, so it computes the UTC offset for each specific moment, including DST transitions.**[^py314-library-zoneinfo] A fixed `timezone(timedelta(hours=-5))` has one offset forever, so in summer its wall clock differs from local time.[^py314-library-datetime] For ambiguous moments during the switch from daylight time to standard time, `ZoneInfo` tells the two apart with `fold`.[^py314-library-zoneinfo]

## Detailed explanation

Daylight saving time (DST) changes the UTC offset. `ZoneInfo` reads the zone's rules from the IANA database.[^py314-library-zoneinfo] A fixed `timezone(timedelta(hours=-5))` describes one offset and knows no rules, so for a city's local clock that observes DST it is right only part of the year.[^py314-library-datetime]

Arithmetic with `timedelta` on an aware datetime keeps the tzinfo and makes no time zone adjustment.[^py314-library-datetime] The result's offset is then recomputed from its wall clock.[^py314-library-zoneinfo] So `timedelta(days=1)` means "the same local time on the next day", while `timedelta(hours=N)` adds N to the wall clock, not N real hours.

An example, run on CPython 3.13 and 3.14:

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

The fixed offset gives 10:00 in New York, while `ZoneInfo` gives 09:00 with `-04:00`. On fall back, `start + timedelta(hours=2)` gives 02:30, but `end - start` for one tzinfo returns `2:00:00`, although three real hours have passed; convert both values to UTC to get the real interval.[^py314-library-datetime] The ambiguous 01:30 on the fall-back day has `fold=0` (the offset before the transition) or `fold=1` (the offset after it).[^py314-library-zoneinfo]

Data availability is a separate requirement: without system time zone data and the `tzdata` package, every `ZoneInfo(...)` call raises `ZoneInfoNotFoundError`.[^py314-library-zoneinfo]

**Common mistakes:**
- assuming that `timedelta(hours=N)` on ZoneInfo time always covers N real hours: an offset change between the two moments alters the real difference;
- computing a duration with `-` for datetimes that share one tzinfo and getting a wall-clock difference;
- storing an offset such as `-05:00` instead of the zone name `America/New_York`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
