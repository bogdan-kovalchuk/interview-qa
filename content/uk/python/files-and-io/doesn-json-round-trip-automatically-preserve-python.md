---
id: py-fileio-0012
title: "Чому JSON round trip не зберігає автоматично всі Python types та object identities?"
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
  - source_id: py314-library-json-encoder-table
    title: "Python 3.14: Library/json (JSONEncoder)"
    url: https://docs.python.org/3.14/library/json.html#json.JSONEncoder
  - source_id: py314-library-json-encoder-default
    title: "Python 3.14: Library/json (Encoders and Decoders)"
    url: https://docs.python.org/3.14/library/json.html#py-to-json-table
  - source_id: py314-library-json-decoder-table
    title: "Python 3.14: Library/json (JSONDecoder)"
    url: https://docs.python.org/3.14/library/json.html#json.JSONDecoder
  - source_id: py314-library-json-dump
    title: "Python 3.14: Library/json (dump)"
    url: https://docs.python.org/3.14/library/json.html#json.dump
---

## Short answer

**JSON має обмежений набір типів, тому round trip через `json.dumps` і `json.loads` не відтворює Python-типи та object identity.**[^py314-library-json-encoder-table] Tuple повертається як list.[^py314-library-json-decoder-table] Ключі `int`, `float`, `bool` і `None` стають рядками JSON-форми: число 1 стає `"1"`, `True` – `"true"`, `None` – `"null"`.[^py314-library-json-dump] `set` і custom класи без `default` викликають `TypeError`.[^py314-library-json-encoder-default] У CPython спільні посилання стають окремими копіями, а циклічні структури `json.dumps` відхиляє з `ValueError`.

## Detailed explanation

Модуль `json` відображає Python-значення в JSON за фіксованою таблицею: `dict` стає object, `list` і `tuple` стають array, `str` – string, `int` і `float` – number, а `True`, `False` і `None` – true, false і null.[^py314-library-json-encoder-table] Значення поза цією таблицею не мають подання: без `default` енкодер викликає `TypeError`.[^py314-library-json-encoder-default] Тому `json.loads(json.dumps(x))` повертає найближче JSON-подання `x`, а не сам `x`.

Перетворення не симетричне. Tuple записується як array, а читається назад як `list`, тому `(1, 2) == [1, 2]` дає `False`, і після round trip рівність порушена.[^py314-library-json-decoder-table] Ключі dict можуть бути `str`, `int`, `float`, `bool` або `None`, але в JSON усі ключі є рядками, тому `{1: "x"}` повертається як `{'1': 'x'}`, а `{True: 1, None: 2}` як `{'true': 1, 'null': 2}`.[^py314-library-json-dump] Ключ-tuple відхиляється вже під час кодування з `TypeError`, бо такого типу ключа в JSON немає.[^py314-library-json-encoder-table]

Object identity теж не переноситься. Серіалізатор записує спільний список у кожному місці, де він є, а декодер створює окремий `list` для кожного входження. У CPython `restored["a"] is restored["b"]` після round trip дає `False`, а в початковому словнику той самий вираз дає `True`. Циклічні структури відхиляються: при типовому `check_circular=True` кодер перевіряє контейнери на цикли, щоб уникнути нескінченної рекурсії, а з `check_circular=False` очікується `RecursionError`.[^py314-library-json-encoder-default]

Приклад показує ці розбіжності; вивід однаковий на CPython 3.13 і 3.14.

```python
import json

print(json.loads(json.dumps((1, 2))))  # [1, 2], tuple comes back as list
print(json.loads(json.dumps({1: "x"})))  # {'1': 'x'}, int key becomes str

shared = [1, 2]
restored = json.loads(json.dumps({"a": shared, "b": shared}))
print(restored["a"] is restored["b"])  # False, one shared list became two

try:
    json.dumps({(2, 3): "tuple key"})
except TypeError as error:
    print(error)  # keys must be str, int, float, bool or None, not tuple

cyclic = []
cyclic.append(cyclic)
try:
    json.dumps(cyclic)
except ValueError as error:
    print(error)  # Circular reference detected
```

**Типові помилки:**
- очікувати, що `json.loads(json.dumps(x)) == x` для будь-якого `x`: tuple стає list, і рівність порушується;
- використовувати `default=str` для всіх невідомих типів: значення повернеться рядком, і початковий тип уже не відновиться;
- покладатися на identity спільних об’єктів після декодування: кожне входження стає окремим об’єктом.
