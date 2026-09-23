---
id: py-fileio-0001
title: "Яка межа між `str` та `bytes` в text I/O і де мають відбуватися encoding та decoding?"
description: "Text I/O працює з str, binary I/O – з bytes; кодування (encoding) відбувається при записі str -> bytes, а декодування (decoding) – при читанні bytes -> str."
track: python
section: files-and-io
level: middle
type: mechanism
tags: [str, bytes]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
applies_to:
  - product: "CPython"
    version: null
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

**Text I/O працює з `str`, binary I/O – з `bytes`; кодування (encoding) відбувається при записі `str` -> `bytes`, а декодування (decoding) – при читанні `bytes` -> `str`.**[^py314-library-io] У CPython шар `TextIOWrapper` розташований поверх буферизованого бінарного потоку: при `write()` він кодує текст у байти й передає їх нижче, при `read()` – декодує прочитані байти назад у `str`. Бінарний шар (`BufferedWriter`/`BufferedReader`) не виконує ні кодування, ні трансляції newlines.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
