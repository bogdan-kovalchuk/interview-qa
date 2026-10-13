---
id: py-stdlib-0011
title: "How does a naive `datetime` differ from an aware `datetime`, and why is mixing them dangerous?"
description: "How does a naive `datetime` differ from an aware `datetime`, and why is mixing them dangerous?"
track: python
section: standard-library
level: middle
type: comparison
tags: [datetime]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-datetime-determining-aware-or-naive
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html#determining-if-an-object-is-aware-or-naive
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: the formal definition of aware and naive datetime objects (tzinfo is not None and utcoffset(d) does not return None)."
  - source_id: py314-library-datetime-aware-and-naive-objects
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html#aware-and-naive-objects
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, Aware and naive objects section: a naive object does not say whether it is UTC or local time; an aware object represents a specific moment."
  - source_id: py314-library-datetime-objects
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html#datetime-objects
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation, datetime objects section: order comparison and subtraction between naive and aware raise TypeError; naive and aware are never equal; now(tz) and replace()."
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

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
