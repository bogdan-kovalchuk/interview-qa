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
  - source_id: py314-library-json-encoder-table
    title: "Python 3.14: Library/json (JSONEncoder)"
    url: https://docs.python.org/3.14/library/json.html#json.JSONEncoder
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: перелік типів, які JSONEncoder серіалізує за замовчуванням."
  - source_id: py314-library-json-encoder-default
    title: "Python 3.14: Library/json (Encoders and Decoders)"
    url: https://docs.python.org/3.14/library/json.html#py-to-json-table
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: параметр default для непідтримуваних типів, TypeError без нього і підклас із методом default()."
  - source_id: py314-library-json-decoder-object-hook
    title: "Python 3.14: Library/json (JSON-to-Python conversion table)"
    url: https://docs.python.org/3.14/library/json.html#json-to-py-table
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: object_hook викликається з результатом кожного декодованого JSON object, і його значення замінює dict."
  - source_id: py314-library-json-dump
    title: "Python 3.14: Library/json (dump)"
    url: https://docs.python.org/3.14/library/json.html#json.dump
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: параметр cls для підкласу JSONEncoder з перевизначеним методом default()."
---

## Short answer

**Для кодування передайте `default`-функцію, а для декодування – `object_hook`.** `default` викликається лише для об’єктів, які `json` не вміє серіалізувати, і має повернути JSON-сумісне подання або викликати `TypeError`.[^py314-library-json-encoder-default] `object_hook` викликається для кожного декодованого JSON object, і його результат замінює dict.[^py314-library-json-decoder-object-hook] Тип записується як dict із маркерним ключем, наприклад `{"__complex__": true, "real": …, "imag": …}`, тож wire-схема лишається явною.

## Detailed explanation

Стандартний енкодер `json` за замовчуванням серіалізує лише `dict`, `list`, `tuple`, `str`, `int`, `float`, `True`, `False` і `None`.[^py314-library-json-encoder-table] Усе інше, наприклад `complex` або `set`, без додаткового правила викликає `TypeError`.[^py314-library-json-encoder-default] Тому custom type потрібні дві сторони: кодер, який перетворює значення на JSON-сумісне подання, і декодер, який розпізнає це подання та відновлює об’єкт.

`default` викликається лише для значень, які енкодер не може серіалізувати звичайним способом. Функція має або повернути JSON-сумісне подання, або викликати `TypeError` для невідомого типу. Повернення `None` чи `str(obj)` тихо міняє дані: значення стає іншим JSON-типом, і декодер уже не відновить початковий тип. Той самий механізм доступний через підклас `json.JSONEncoder` з перевизначеним методом `default()`, який передають через `cls=`.[^py314-library-json-encoder-default][^py314-library-json-dump] На боці декодування `object_hook` викликається для кожного JSON object після його розбору.[^py314-library-json-decoder-object-hook] У CPython вкладені об’єкти передаються в hook раніше за зовнішні.

Маркерний ключ робить wire-формат явним: той, хто читає JSON, бачить, що значення описує `complex`. Межа підходу в тому, що `object_hook` бачить усі JSON object. Звичайний dict із `"__complex__": 1` лишається dict, бо перевірка `is True` його відсікає, але dict із `"__complex__": true` у будь-яких даних буде відновлено як `complex`. Тому маркер має бути рідкісним іменем або версійованим префіксом, а декодер має перевіряти й набір очікуваних полів.

Приклад кодує `complex` і відновлює його під час декодування; інші значення проходять без змін.

```python
import json

def encode_special(obj):
    if isinstance(obj, complex):
        return {"__complex__": True, "real": obj.real, "imag": obj.imag}
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

def decode_special(d):
    if d.get("__complex__") is True:
        return complex(d["real"], d["imag"])
    return d

text = json.dumps({"z": 1 + 2j, "n": 3}, default=encode_special)
print(text)  # {"z": {"__complex__": true, "real": 1.0, "imag": 2.0}, "n": 3}
restored = json.loads(text, object_hook=decode_special)
print(restored)  # {'z': (1+2j), 'n': 3}
```

**Типові помилки:**
- плутати аргументи: `default` передають у `json.dumps`, а `object_hook` – у `json.loads`;
- повертати `None` або `str(obj)` для невідомого типу замість `TypeError`, через що дані тихо змінюють тип;
- брати надто загальний маркер на кшталт `"type"`, який може збігтися з реальними даними.

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
