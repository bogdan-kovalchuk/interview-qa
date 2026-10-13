---
id: py-fileio-0008
title: "Як `seek()` і `tell()` використовуються для random access і чому offsets text streams не завжди можна трактувати як character positions?"
description: "У binary mode seek() і tell() працюють із байтовими зміщеннями; у text mode tell() повертає opaque number, а seek() приймає лише значення з tell() або нульові зміщення."
track: python
section: files-and-io
level: middle
type: mechanism
tags: [seek, tell]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
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
  - source_id: py314-library-io-iobase-seek
    title: "Python 3.14: Library/io (IOBase.seek)"
    url: https://docs.python.org/3.14/library/io.html#io.IOBase.seek
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: seek() встановлює позицію потоку за байтовим зміщенням відносно whence."
  - source_id: py314-library-io-textiobase-seek
    title: "Python 3.14: Library/io (TextIOBase.seek)"
    url: https://docs.python.org/3.14/library/io.html#io.TextIOBase.seek
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: у text mode зміщення має бути значенням з tell() або нулем, інші значення дають undefined behavior; підтримуються чотири форми виклику."
  - source_id: py314-library-io-textiobase-tell
    title: "Python 3.14: Library/io (TextIOBase.tell)"
    url: https://docs.python.org/3.14/library/io.html#io.TextIOBase.tell
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: tell() повертає opaque number, який зазвичай не є кількістю байтів у базовому сховищі."
  - source_id: ietf-rfc3629
    title: "RFC 3629: UTF-8, a transformation format of ISO 10646"
    url: https://www.rfc-editor.org/rfc/rfc3629#section-3
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "RFC 3629, розділ 3: UTF-8 кодує символи Unicode послідовностями від 1 до 4 октетів; не описує поведінку Python."
---

## Short answer

**У binary mode `seek()` і `tell()` працюють із байтовими зміщеннями; у text mode `tell()` повертає opaque number, який зазвичай не є кількістю байтів, а `seek()` приймає лише значення з `tell()` або нульові зміщення.**[^py314-library-io-iobase-seek][^py314-library-io-textiobase-tell][^py314-library-io-textiobase-seek] У text mode з UTF-8 один символ займає від 1 до 4 байтів, тому позиція в байтах не дорівнює позиції в символах.[^ietf-rfc3629] Довільне число в `seek()` є undefined behavior: у CPython зміщення всередині багатобайтового символу дає `UnicodeDecodeError`.

## Detailed explanation

Random access означає перехід до потрібного місця без читання всього попереднього вмісту. Для binary file позиція – це байтове зміщення. `seek(offset)` переміщує курсор, `tell()` повертає поточну позицію.[^py314-library-io-iobase-seek] Для записів фіксованого розміру запис із номером `i` починається з байта `i * record_size`. Приклад (`#` коментарі показують результат):

```python
import os
import tempfile

path = os.path.join(tempfile.mkdtemp(), 'records.bin')
with open(path, 'wb') as f:
    for i in range(5):
        f.write(i.to_bytes(4, 'little'))  # fixed-size records of 4 bytes

with open(path, 'rb') as f:
    f.seek(3 * 4)                               # jump to record 3 without reading 0..2
    print(int.from_bytes(f.read(4), 'little'))  # 3
    print(f.tell())                             # 16: a byte offset
```

У text mode позиції не можна трактувати як номери символів. Текстовий потік декодує байти в символи, а один символ в UTF-8 займає від 1 до 4 байтів.[^ietf-rfc3629] `tell()` повертає «opaque number»: за документацією, це зазвичай не кількість байтів, а значення, яке можна передати в `seek()` для відновлення позиції.[^py314-library-io-textiobase-tell] У прикладі нижче після читання трьох символів `tell()` дає 6, а не 3. Той самий код показує відновлення позиції і зміщення, яке не походить від `tell()`:

```python
import os
import tempfile

path = os.path.join(tempfile.mkdtemp(), 'text.txt')
with open(path, 'w', encoding='utf-8') as f:
    f.write('aж€😀bc\n')       # 7 characters, 13 bytes in UTF-8

with open(path, encoding='utf-8') as f:
    print(repr(f.read(3)))     # 'aж€'
    print(f.tell())            # 6, not 3: this is not a character index
    f.seek(0)
    f.read(2)                  # 'a', 'ж'
    pos = f.tell()             # 3
    print(f.read(1))           # €
    f.seek(pos)                # restores a value returned by tell()
    print(f.read(1))           # €
    try:
        f.seek(pos + 1)        # not a value from tell(): undefined behavior
        f.read(1)
    except UnicodeDecodeError:
        print('UnicodeDecodeError')  # byte 4 is inside '€' (bytes 3 to 5)
```

Межі `seek()` у text mode вузькі. `seek(0)`, `seek(0, SEEK_END)` і `seek(0, SEEK_CUR)` є допустимими, а `seek(cookie)` приймає лише значення з `tell()`.[^py314-library-io-textiobase-seek] Ненульові відносні зміщення CPython відхиляє з `io.UnsupportedOperation` (наприклад, `seek(1, SEEK_CUR)`, перевірено на 3.13 і 3.14). Номер символу тому не перетворюється на позицію для `seek()`: потрібно читати символи або працювати з байтами.

**Типові помилки:**
- обчислювати зміщення як номер символу, наприклад `seek(n)` для n-го символу UTF-8 тексту;
- вважати, що `tell()` у text mode – це кількість байтів або символів, і порівнювати його з довжиною рядка;
- передавати в `seek()` довільне число, наприклад індекс, знайдений регулярним виразом, замість значення з `tell()`: це undefined behavior.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
