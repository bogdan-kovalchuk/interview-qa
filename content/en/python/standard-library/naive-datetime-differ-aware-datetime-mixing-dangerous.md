---
id: py-stdlib-0011
title: "How does a naive `datetime` differ from an aware `datetime`, and why is mixing them dangerous?"
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

**A naive `datetime` carries no time zone information (`tzinfo is None` or `utcoffset()` returns `None`), whereas an aware one has a `tzinfo` with a defined offset.**[^py314-library-datetime-determining-aware-or-naive] Order comparisons (`<`, `>`) and subtraction between naive and aware objects raise `TypeError`.[^py314-library-datetime-objects] Equality comparisons (`==`, `!=`) raise no error, but naive and aware objects are never equal, so the mistake is silent.[^py314-library-datetime-objects]

## Detailed explanation

For `datetime`, awareness is defined formally: an object `d` is aware if `d.tzinfo` is not `None` and `d.tzinfo.utcoffset(d)` does not return `None`; otherwise it is naive.[^py314-library-datetime-determining-aware-or-naive] A naive value does not say whether it is UTC, local time, or another zone: that is up to the program. An aware value represents a specific moment that is not open to interpretation.[^py314-library-datetime-aware-and-naive-objects]

The danger is that the mistake shows up differently. Order comparison and subtraction between naive and aware objects raise `TypeError` immediately. Equality does not raise: `==` gives `False` and `!=` gives `True`, because naive and aware objects are never equal. So code that only checks equality, such as searching a list for a value, silently finds no match.[^py314-library-datetime-objects]

The example shows both behaviours. The output is the same on CPython 3.13 and 3.14:

```python
from datetime import datetime, timezone

naive = datetime(2026, 10, 13, 12, 0)                       # no tzinfo: naive
aware = datetime(2026, 10, 13, 12, 0, tzinfo=timezone.utc)  # fixed offset: aware

print(naive == aware, naive != aware)  # False True, no exception
print(naive < aware)                   # TypeError: can't compare offset-naive and offset-aware datetimes
```

It is safer to keep time aware from the start and compare instants in UTC. `datetime.now(timezone.utc)` returns an aware value, whereas `datetime.now()` returns naive local time.[^py314-library-datetime-objects] The method `replace(tzinfo=timezone.utc)` does not convert the hour; it only labels it as UTC. If the value was really local time, the resulting instant is off by the zone's offset.

**Common mistakes:**
- comparing `datetime.now()` (naive, local time) with `datetime.now(timezone.utc)` (aware);
- reading `False` from `==` as "different moments": for naive and aware values it only means the types are incompatible;
- adding `tzinfo=timezone.utc` to a naive value that was local time;
- storing naive datetimes without a zone marker in a database or an API.
