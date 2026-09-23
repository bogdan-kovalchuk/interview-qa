---
id: py-stdlib-0008
title: "Який boilerplate усуває `functools.total_ordering` і які performance та traceback trade-offs варто врахувати?"
description: "@total_ordering автоматично генерує відсутні методи порівняння (__lt__, __le__, __gt__, __ge__) на основі одного визначеного плюс __eq__."
track: python
section: standard-library
level: senior
type: practical
tags: [functools-total-ordering]
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

**`@total_ordering` автоматично генерує відсутні методи порівняння (`__lt__`, `__le__`, `__gt__`, `__ge__`) на основі одного визначеного плюс `__eq__`.**[^py314-library-collections] Trade-off: декоратор сповільнює виклик порівняння через додатковий рівень інкапсуляції та ускладнює traceback. Для hot path, де порівняння викликаються мільйони разів, краще реалізувати всі методи явно.

## Detailed explanation

TODO

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
