---
id: py-stdlib-0006
title: "Чому `itertools.groupby()` групує лише consecutive equal keys і коли input потрібно попередньо відсортувати?"
description: "groupby() створює нову групу щоразу, коли змінюється значення ключа – як Unix uniq, а не SQL GROUP BY."
track: python
section: standard-library
level: senior
type: pitfall
tags: [itertools-groupby]
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

**`groupby()` створює нову групу щоразу, коли змінюється значення ключа – як Unix `uniq`, а не SQL `GROUP BY`.**[^py314-library-collections] Щоб усі елементи з однаковим ключем потрапили в одну групу, input потрібно відсортувати за тим самим key function. Група є ітератором, що розділяє underlying iterable з `groupby`; якщо дані потрібні пізніше, їх треба одразу зберегти в `list`.

## Detailed explanation

TODO

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
