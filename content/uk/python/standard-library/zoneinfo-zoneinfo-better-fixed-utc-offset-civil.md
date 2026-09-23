---
id: py-stdlib-0012
title: "Чому `zoneinfo.ZoneInfo` краще за фіксований UTC offset для civil time з daylight-saving transitions?"
description: "ZoneInfo використовує базу даних IANA з повною історією переходів DST, тому автоматично коректує зсув під час арифметики datetime."
track: python
section: standard-library
level: middle
type: comparison
tags: [zoneinfo-zoneinfo]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-datetime
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-re
    title: "Python 3.14: Library/re"
    url: https://docs.python.org/3.14/library/re.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: owasp-regular-expression-denial-of-service-redos
    title: "OWASP: Regular Expression Denial of Service REDOS"
    url: https://owasp.org/www-community/attacks/Regular_expression_Denial_of_Service_-_ReDoS
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Матеріал спільноти OWASP з безпеки застосунків."
---

## Short answer

**`ZoneInfo` використовує базу даних IANA з повною історією переходів DST, тому автоматично коректує зсув під час арифметики datetime.**[^py314-library-collections] Фіксований `timezone(timedelta(hours=...))` ніколи не змінюється: якщо додати `timedelta(days=1)` через межу DST, «wall clock» покаже неправильний місцевий час. `ZoneInfo` також підтримує `fold` для неоднозначних моментів під час «відкату» годинника.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
