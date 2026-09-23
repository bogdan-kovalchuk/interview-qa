---
id: py-fileio-0011
title: "Як задати custom JSON encoding для непідтримуваного type, не втрачаючи явного wire schema?"
description: "Передати default-функцію (або підкласити json.JSONEncoder) для кодування, і object_hook – для декодування, використовуючи dict із маркерним ключем як wire-схему."
track: python
section: files-and-io
level: middle
type: practical
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-library-io
    title: "Python 3.14: Library/io"
    url: https://docs.python.org/3.14/library/io.html
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
  - source_id: py314-library-json
    title: "Python 3.14: Library/json"
    url: https://docs.python.org/3.14/library/json.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-pickle
    title: "Python 3.14: Library/pickle"
    url: https://docs.python.org/3.14/library/pickle.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-os-os-fsync
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.fsync
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-os-os-replace
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.replace
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-tempfile
    title: "Python 3.14: Library/tempfile"
    url: https://docs.python.org/3.14/library/tempfile.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Передати `default`-функцію (або підкласити `json.JSONEncoder`) для кодування, і `object_hook` – для декодування, використовуючи dict із маркерним ключем як wire-схему.**[^py314-library-io] Наприклад, `complex` можна зберігати як `{"__complex__": true, "real": …, "imag": …}`. Під час `json.loads` функція `object_hook` отримує кожен dict і за наявності маркера відновлює оригінальний type; інакше повертає dict без змін. Такий підхід дає self-describing формат, сумісний із будь-яким JSON-парсером.

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
