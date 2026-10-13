---
id: py-fileio-0004
title: "Чим `flush()` Python stream відрізняється від `os.fsync()` і чому жоден із них не слід описувати як універсальну hardware-durability guarantee?"
description: "flush() виштовхує дані з внутрішнього буфера Python до ОС, а os.fsync(fd) просить ОС записати дані файлу на диск; що відбувається нижче за ОС, Python не контролює."
track: python
section: files-and-io
level: middle
type: comparison
tags: [flush, os-fsync]
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
  - source_id: linux-man-fsync
    title: "Linux man-pages: fsync(2)"
    url: https://man7.org/linux/man-pages/man2/fsync.2.html
    accessed: 2026-10-13
    kind: official
    version: null
    applicability: "Сторінка fsync(2) Linux man-pages: fsync() над файлом не гарантує запис каталогу з цим файлом; потрібен fsync() на дескрипторі каталогу. Специфічно для Linux, не POSIX-стандарт і не Windows."
---

## Short answer

**`flush()` передає буферизовані байти в raw stream, тобто до ОС, а `os.fsync(fd)` просить ОС записати дані файлу на диск.**[^py314-library-io][^py314-library-os-os-fsync] Ні те, ні інше не є універсальною hardware-durability гарантією: що відбувається нижче за ОС, наприклад у кеші пристрою, Python не контролює, і документація Python цього не обіцяє.[^py314-library-os-os-fsync] Документована послідовність для файлового об’єкта: `f.flush()`, а потім `os.fsync(f.fileno())`.[^py314-library-os-os-fsync]

## Detailed explanation

У CPython текстовий файл має кілька шарів буферизації. `TextIOWrapper` може тримати закодовані байти у власній черзі й передавати їх `BufferedWriter`-у пізніше. `BufferedWriter.flush()` примусово переносить байти з буфера в raw stream,[^py314-library-io] тобто передає їх ОС. Тому `flush()` потрібен, але він лише доводить дані до ОС; для запису на диск є окремий виклик.

`os.fsync()` документовано як примусовий запис даних файлу на диск: на Unix викликається native `fsync()`, на Windows – `_commit()`. Для файлового об’єкта документація показує послідовність `f.flush()`, а потім `os.fsync(f.fileno())`, щоб усі внутрішні буфери файлу були записані на диск.[^py314-library-os-os-fsync] Приклад:

```python
import os

with open("journal.log", "a", encoding="utf-8") as f:
    f.write("record 1\n")
    f.flush()              # Python buffer -> OS
    os.fsync(f.fileno())   # request that the OS writes the file's data to disk
```

Межа гарантії в тому, що `os.fsync()` описаний як запит до ОС. Документація Python не описує поведінку кеша пристрою, контролера чи файлової системи, а це шари, які Python не контролює. Тому після успішного виклику можна сказати, що Python попросив ОС записати дані на диск. Фраза «дані гарантовано збережені» без уточнення апаратури і файлової системи неправильна.

Для заміни файлу часто комбінують запис у тимчасовий файл, `flush()`, `os.fsync()` і `os.replace()`. Документація називає `os.replace()` атомарним на POSIX, якщо операція вдалася; вона може не вдатися, коли джерело і призначення на різних файлових системах.[^py314-library-os-os-replace] Атомарність заміни означає, що читач бачить старий або новий вміст файлу, але сама по собі не робить запис довговічним. На Linux `fsync()` над файлом не гарантує, що запис каталогу з цим файлом дійшов до диска, тож для довговічної заміни потрібен ще `fsync()` на дескрипторі каталогу.[^linux-man-fsync]

**Типові помилки:**
- вважати, що `flush()` записує дані на диск;
- викликати `os.fsync(f.fileno())` без попереднього `f.flush()`: дані, що лишилися в буфері Python, fsync не гарантує записати;
- називати `os.fsync()` гарантією збереження «навіть після збою живлення» без уточнення платформи й апаратури.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
