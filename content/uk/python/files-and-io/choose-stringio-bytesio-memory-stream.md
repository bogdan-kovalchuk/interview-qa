---
id: py-fileio-0014
title: "Коли обрати `StringIO`, а коли `BytesIO` для in-memory stream?"
description: "StringIO – коли дані типу str (текст), BytesIO – коли bytes або bytearray (бінарні дані)."
track: python
section: files-and-io
level: middle
type: comparison
tags: [stringio, bytesio]
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

**`StringIO` – коли дані типу `str` (текст), `BytesIO` – коли `bytes` або `bytearray` (бінарні дані).**[^py314-library-io] `StringIO` наслідує `io.TextIOBase` і підтримує newline-translation через параметр `newline`. `BytesIO` наслідує `io.BufferedIOBase`, не виконує жодного кодування/декодування та надає `getbuffer()` для zero-copy доступу до буфера. Якщо API очікує текстовий stream – `StringIO`, якщо бінарний (зображення, серіалізовані дані, мережеві пакети) – `BytesIO`.

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
