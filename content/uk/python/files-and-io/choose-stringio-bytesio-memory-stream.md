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
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
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
  - source_id: py314-library-io-stringio
    title: "Python 3.14: Library/io (StringIO)"
    url: https://docs.python.org/3.14/library/io.html#io.StringIO
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: StringIO – текстовий потік у пам’яті, наслідує TextIOBase, має параметр newline."
  - source_id: py314-library-io-bytesio
    title: "Python 3.14: Library/io (BytesIO)"
    url: https://docs.python.org/3.14/library/io.html#io.BytesIO
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: BytesIO – бінарний потік у пам’яті, наслідує BufferedIOBase."
  - source_id: py314-library-io-binary-io
    title: "Python 3.14: Library/io (Binary I/O)"
    url: https://docs.python.org/3.14/library/io.html#binary-io
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: бінарні потоки приймають bytes-like об’єкти і не виконують кодування, декодування чи трансляцію кінців рядків."
  - source_id: py314-library-io-bytesio-getbuffer
    title: "Python 3.14: Library/io (BytesIO.getbuffer)"
    url: https://docs.python.org/3.14/library/io.html#io.BytesIO.getbuffer
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: getbuffer() повертає view без копіювання; поки view існує, BytesIO не можна змінити за розміром або закрити."
  - source_id: py314-library-io-textiowrapper
    title: "Python 3.14: Library/io (TextIOWrapper)"
    url: https://docs.python.org/3.14/library/io.html#io.TextIOWrapper
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: TextIOWrapper – буферизований текстовий потік над бінарним буфером із параметрами encoding і write_through."
---

## Short answer

**Беріть `StringIO` для тексту (`str`) і `BytesIO` для бінарних даних (`bytes` або `bytearray`).** `StringIO` наслідує `io.TextIOBase` і приймає параметр `newline`, який керує трансляцією кінців рядків.[^py314-library-io-stringio] `BytesIO` наслідує `io.BufferedIOBase` і не виконує кодування чи декодування.[^py314-library-io-bytesio][^py314-library-io-binary-io] `getbuffer()` повертає view на буфер без копіювання, і зміни через нього одразу видно в `BytesIO`.[^py314-library-io-bytesio-getbuffer] Якщо API очікує текстовий stream, беріть `StringIO`; якщо бінарний (зображення, серіалізовані дані, мережеві пакети), беріть `BytesIO`.

## Detailed explanation

`StringIO` – це текстовий потік у пам’яті, а `BytesIO` – бінарний потік у пам’яті.[^py314-library-io-stringio][^py314-library-io-bytesio] Різниця в одиницях даних: `write()` у `StringIO` приймає лише `str`, а в `BytesIO` – лише bytes-like об’єкти, і `getvalue()` повертає відповідний тип. Тому вибір визначається тим, з чим працює код, який читає або пише в потік: з текстом чи з байтами.

Приклад показує типи даних, помилки при змішуванні та запис тексту в бінарний буфер через явне кодування.

```python
import io

text = io.StringIO()
text.write("hello")
print(text.getvalue())                 # hello

raw = io.BytesIO()
raw.write(b"\x89PNG")
print(raw.getvalue())                  # b'\x89PNG'

try:
    raw.write("hello")                 # str is not bytes-like
except TypeError as error:
    print(error)                       # a bytes-like object is required, not 'str'

try:
    text.write(b"x")                   # bytes is not str
except TypeError as error:
    print(error)                       # string argument expected, got 'bytes'

buf = io.BytesIO()
wrapper = io.TextIOWrapper(buf, encoding="utf-8", write_through=True)
wrapper.write("héllo")
print(buf.getvalue())                  # b'h\xc3\xa9llo'
```

Якщо текст потрібно записати в бінарний буфер, обгорніть `BytesIO` у `io.TextIOWrapper` з явним `encoding`: кодування тоді видно в місці створення, а не в ручному `.encode()` десь у коді.[^py314-library-io-textiowrapper] Параметр `write_through=True`, як у прикладі, передає дані в буфер одразу, без очікування `flush()`.[^py314-library-io-textiowrapper]

`getbuffer()` повертає view без копіювання даних; у CPython це `memoryview`. Поки view існує, `BytesIO` не можна змінити за розміром або закрити, тому view варто звільняти після використання.[^py314-library-io-bytesio-getbuffer]

**Типові помилки:**
- записувати `str` у `BytesIO` або bytes у `StringIO`: обидва варіанти викликають `TypeError`;
- вибирати `StringIO` для бінарного формату (зображення, пакети): він не приймає bytes, тож доведеться вигадувати кодування, якого формат не визначає;
- кодувати текст через `.encode()` в одному місці, а декодувати з іншим кодуванням в іншому.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
