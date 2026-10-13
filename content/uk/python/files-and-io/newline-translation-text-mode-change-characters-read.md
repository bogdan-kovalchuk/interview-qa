---
id: py-fileio-0003
title: "Як newline translation в text mode може змінити прочитані або записані characters на різних platforms?"
description: "У text mode з newline=None (типово) при читанні всі варіанти \\r\\n, \\r та \\n трансляються в \\n, а при записі \\n замінюється на os.linesep – на Windows це \\r\\n."
track: python
section: files-and-io
level: senior
type: pitfall
tags: []
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
  - source_id: py314-library-os-os-linesep
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.linesep
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: значення os.linesep на платформах і застереження щодо text mode."
  - source_id: py314-library-csv
    title: "Python 3.14: Library/csv"
    url: https://docs.python.org/3.14/library/csv.html#csv.writer
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: модуль csv просить відкривати файлові об’єкти з newline=''."
---

## Short answer

**У text mode з `newline=None` (типово) при читанні всі варіанти `\r\n`, `\r` та `\n` трансляються в `\n`, а при записі `\n` замінюється на `os.linesep` – на Windows це `\r\n`.**[^py314-library-io][^py314-library-os-os-linesep] <span class="warn">Це означає, що розмір файлу в байтах після round trip може відрізнятися від початкового, а хеші (наприклад, SHA-256) можуть не збігатися між платформами.</span>[^py314-library-io] Щоб уникнути трансляції, відкривайте файл із `newline=""` або працюйте в binary mode.[^py314-library-io]

## Detailed explanation

`newline` керує тим, як текстовий шар перекладає кінці рядків. Значення `None` (типове) вмикає universal newlines mode: при читанні `\n`, `\r` та `\r\n` перетворюються на `\n`, а при записі кожен `\n` замінюється на `os.linesep`.[^py314-library-io] Переклад відбувається в текстовому шарі, тому `str` у програмі й байти на диску можуть відрізнятися.

Нижче один файл із CRLF-рядком і голим `\r` наприкінці. Читання з типовими параметрами повертає `\n`, а з `newline=""` кінці рядків лишаються такими, як у файлі. Далі той самий текст записується з типовим `newline` і з `newline="\r\n"`. Вивід у коментарях отримано на CPython 3.13 і 3.14 у Linux, де `os.linesep` дорівнює `\n`:

```python
with open("lines.txt", "wb") as f:
    f.write(b"a\r\nb\r")                    # CRLF line, then a lone CR at the end

with open("lines.txt", encoding="utf-8") as f:           # newline=None (default)
    print(f.read().splitlines(True))                      # ['a\n', 'b\n']

with open("lines.txt", encoding="utf-8", newline="") as f:
    print(f.read().splitlines(True))                      # ['a\r\n', 'b\r']

with open("lines.txt", "w", encoding="utf-8") as f:       # newline=None on write
    f.write("a\nb\n")
print(open("lines.txt", "rb").read())                     # b'a\nb\n' on Linux, b'a\r\nb\r\n' on Windows

with open("lines.txt", "w", encoding="utf-8", newline="\r\n") as f:
    f.write("a\nb\n")
print(open("lines.txt", "rb").read())                     # b'a\r\nb\r\n' on every platform
```

На Windows `os.linesep` дорівнює `\r\n`,[^py314-library-os-os-linesep] тому той самий текстовий запис дає інші байти. Явний `newline="\r\n"` дає результат, як на Windows, на будь-якій платформі; `newline=""` і `newline="\n"` не перекладають нічого.[^py314-library-io] Документація os прямо радить не використовувати `os.linesep` як термінатор рядків у файлух, відкритих у text mode, а писати один `\n` на всіх платформах.[^py314-library-os-os-linesep]

Пастка проявляється там, де важать байти: хеш або розмір файлу, порівняння результатів між ОС, формати з фіксованими кінцями рядків. Модуль `csv` просить відкривати файлові об’єкти з `newline=""`: без цього рядки в полях у лапках можуть розбиратися неправильно, а на платформах із `\r\n` при записі з’являється зайвий `\r`.[^py314-library-csv] Якщо потрібні точні байти, відкривайте файл у binary mode і кодуйте або декодуйте текст явно.

**Типові помилки:**
- порівнювати хеші або розміри текстових файлів, записаних на різних ОС;
- читати файл із типовим `newline`, коли треба зберегти кінці рядків як є;
- відкривати CSV без `newline=""`: зайвий `\r` при записі на платформах із `\r\n` і неправильний розбір полів із переносами рядків.

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
