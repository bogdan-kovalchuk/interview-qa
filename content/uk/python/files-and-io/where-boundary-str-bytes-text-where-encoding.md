---
id: py-fileio-0001
title: "Яка межа між `str` та `bytes` в text I/O і де мають відбуватися encoding та decoding?"
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

**Text I/O працює з `str`, binary I/O – з `bytes`; кодування (encoding) відбувається при записі `str` -> `bytes`, а декодування (decoding) – при читанні `bytes` -> `str`.**[^py314-library-io] У CPython шар `TextIOWrapper` розташований поверх буферизованого бінарного потоку: при `write()` він кодує текст у байти й передає їх нижче, при `read()` – декодує прочитані байти назад у `str`. Бінарний шар (`BufferedWriter`/`BufferedReader`) не виконує ні кодування, ні трансляції newlines.

## Detailed explanation

Межа проходить між текстовим і бінарним шарами стека `io`. Text I/O приймає й повертає `str`, а binary I/O працює з bytes-подібними об’єктами та повертає `bytes`.[^py314-library-io] Кодування й декодування робить текстовий шар: `open()` у текстовому режимі повертає `TextIOWrapper`, який при записі перетворює `str` на байти вибраним кодуванням, а при читанні – байти назад на `str`. Саме тому бінарний потік не приймає `str`, а текстовий не віддає `bytes`.

Нижче та сама межа в коді: рядок явно переводиться в байти і назад, після чого два стандартні модулі показують, який тип очікує кожен шар.

```python
import json
import pickle

data = "Привіт".encode("utf-8")
print(data)                          # b'\xd0\x9f\xd1\x80...' (12 bytes for 6 characters)
print(data.decode("utf-8"))          # Привіт
print(len("Привіт"), len(data))      # 6 12

with open("data.json", "w", encoding="utf-8") as f:
    json.dump({"name": "Привіт"}, f, ensure_ascii=False)   # json writes str: text file

with open("data.pkl", "wb") as f:
    pickle.dump({"name": "Привіт"}, f)                     # pickle writes bytes: binary file
```

`json.dump()` потребує текстового файлу, бо модуль завжди створює `str`, тож `fp.write()` має приймати `str`.[^py314-library-json] `pickle.dump()` навпаки пише в бінарний файл, тобто в потік байтів.[^py314-library-pickle] `Path.write_text()` приймає `encoding` і `newline` (`newline` з Python 3.10), як і `open()`; `Path.read_text()` приймає `encoding` і `errors`, а параметр `newline` з’явився лише в 3.13, тож у 3.12 і раніше для нього треба `open()`.[^py314-library-pathlib] Правило для `encoding` одне для всіх трьох випадків.

Помилка тут тиха. Текст, декодований не тим кодуванням, не викликає винятку, якщо байти для цього кодування допустимі, а просто стає іншим текстом: UTF-8 байти від `"Привіт"`, декодовані як `cp1251`, дають рядок з іншими літерами. Кодування треба знати з контракту файлу, а не вгадувати за байтами.

**Типові помилки:**
- порівнювати результат `read()` з файлу, відкритого в binary mode, зі `str` (`b'...' != '...'`);
- очікувати, що текстовий `open()` повертає `bytes`, і декодувати вже прочитаний `str`;
- вгадувати кодування файлу замість того, щоб задати його явно.
