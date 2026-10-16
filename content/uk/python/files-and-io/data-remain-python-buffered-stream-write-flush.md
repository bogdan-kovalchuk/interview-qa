---
id: py-fileio-0005
title: "Які дані можуть залишатися в Python buffered stream після `write()` і що змінює `flush()`?"
track: python
section: files-and-io
sources:
  - source_id: py314-library-io
    title: "Python 3.14: Library/io"
    url: https://docs.python.org/3.14/library/io.html
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
  - source_id: py314-library-json
    title: "Python 3.14: Library/json"
    url: https://docs.python.org/3.14/library/json.html
  - source_id: py314-library-pickle
    title: "Python 3.14: Library/pickle"
    url: https://docs.python.org/3.14/library/pickle.html
  - source_id: py314-library-os-os-fsync
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.fsync
  - source_id: py314-library-os-os-replace
    title: "Python 3.14: Library/os"
    url: https://docs.python.org/3.14/library/os.html#os.replace
  - source_id: py314-library-tempfile
    title: "Python 3.14: Library/tempfile"
    url: https://docs.python.org/3.14/library/tempfile.html
---

## Short answer

**Після `write()` дані можуть залишатися у внутрішніх буферах Python: у текстовому шарі `TextIOWrapper` або в `BufferedWriter` – і ще не бути передані в raw-потік ОС.**[^py314-library-io] `flush()` примусово записує буфер у raw stream, і інші дескриптори того самого файлу бачать дані (спостережено на Linux). Для запису на диск є `os.fsync()`.[^py314-library-os-os-fsync] Буфер також скидається при `close()`.[^py314-library-io]

## Detailed explanation

Запис іде через кілька місць. `TextIOWrapper` кодує `str` у байти й може тримати їх у власній черзі. `BufferedWriter` накопичує байти у буфері й передає їх raw-потоку, тобто ОС, коли буфер треба записати, або за викликом `flush()`.[^py314-library-io] Тому після `write()` дані можуть ще не потрапити до ОС, і файл на диску їх не містить.

Розмір файлу показує, де лежать дані. Обидва `print` виконуються всередині `with`, тобто до закриття файлу:

```python
import os

with open("events.txt", "w", encoding="utf-8") as f:
    f.write("started\n")
    print(os.path.getsize("events.txt"))  # 0: the text is still in Python's buffers
    f.flush()
    print(os.path.getsize("events.txt"))  # 8: flush() passed the bytes to the OS
```

Крім `flush()`, буфер скидається при `close()`: документація описує його як «flush and close this stream».[^py314-library-io] У CPython скидання спостерігається також при `seek()` і при заповненні буфера, але документація не задає для заповнення фіксованого порогу. Розмір буфера залежить від версії: `print(io.DEFAULT_BUFFER_SIZE)` дає 8192 на 3.12 і 3.13 та 131072 на 3.14 (спостережено; документація значення не задає), а `open()` бере розмір блоку з `os.stat()`, якщо це можливо.[^py314-library-io] Логіку на конкретному розмірі буфера будувати не можна.

Після `flush()` дані вже в ОС: другий дескриптор того самого файлу в тому самому процесі прочитав записане без `fsync` (спостережено на Linux). Це видимість у межах ОС, а не запис на диск, для якого потрібен `os.fsync()`.[^py314-library-os-os-fsync] Щоб прибрати буферизацію Python, можна відкрити файл у binary mode з `buffering=0`: документація називає це способом створити raw stream, і тоді `write()` звертається до ОС без проміжного буфера.[^py314-library-io]

**Типові помилки:**
- перевіряти файл одразу після `write()` і робити висновок, що запис не вдався;
- вважати, що `flush()` записує дані на диск, а не лише передає їх ОС;
- покладатися на конкретний розмір буфера: він різний між версіями Python і залежить від файлу.
