---
id: py-modimp-0013
title: "Чому `importlib.reload(module)` не оновлює автоматично всі раніше створені instances та names, імпортовані через `from ... import ...`?"
description: "importlib.reload() перезапускає код модуля в тому самому module object, але не оновлює назв, скопійованих через from ... import ... в інші модулі, і не змінює класи вже створених instance’ів."
track: python
section: modules-and-imports
level: senior
type: pitfall
tags: [importlib-reload-module, from-import]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-import
    title: "Python 3.14: Reference/import"
    url: https://docs.python.org/3.14/reference/import.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-importlib
    title: "Python 3.14: Library/importlib"
    url: https://docs.python.org/3.14/library/importlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py-packaging-guide
    title: "Python Packaging User Guide"
    url: https://packaging.python.org/en/latest/tutorials/packaging-projects/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційний посібник із packaging для Python."
  - source_id: py314-library-importlib-reload
    title: "Python 3.14: Library/importlib, importlib.reload()"
    url: https://docs.python.org/3.14/library/importlib.html#importlib.reload
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: reload повторно виконує код модуля в його словнику; імена з from-імпортів в інших модулях і класи, створені раніше, не оновлюються; reload не потокобезпечний."
  - source_id: py314-reference-simple-stmts-import
    title: "Python 3.14: Reference/simple statements, The import statement"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#the-import-statement
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: from-імпорт зберігає посилання на значення в поточному namespace."
---

## Short answer

**`importlib.reload()` зазвичай перезапускає код модуля в тому самому module object, але не оновлює імен, скопійованих через `from ... import ...` в інших модулях, і не змінює класи вже створених instance’ів.**[^py314-library-importlib-reload] Причина: `from ... import ...` зберігає посилання на значення в namespace імпортера, тому reload не змінює чужі namespace.[^py314-reference-simple-stmts-import] Клас, визначений заново, стає новим class object, а наявні instance’и продовжують використовувати старий клас.[^py314-library-importlib-reload] Імена, яких нова версія модуля не визначає, лишаються зі старими значеннями.

## Detailed explanation

`importlib.reload(module)` зазвичай не створює новий module object: він повторно компілює файл і виконує module-level код у вже імпортованому модулі, а нові об’єкти прив’язуються до імен у тому самому словнику. Імена, яких нова версія не визначає, лишаються зі старими значеннями.[^py314-library-importlib-reload]

Найчастіше здивування викликає `from ... import ...`. Цей оператор бере значення в момент імпорту і зберігає на нього посилання в namespace імпортера, а не створює зв’язку з модулем.[^py314-reference-simple-stmts-import] Тому після reload `MODE` у `main.py` лишається `"v1"`, а `config.MODE` стає `"v2"`.

Модуль `config.py` спочатку містить `MODE = "v1"` і клас `Service`:

```python
# config.py (first version)
MODE = "v1"

class Service:
    def run(self):
        return "v1 run"
```

Скрипт `main.py` імпортує модуль двома способами, змінює файл на диску і викликає reload. Коментарі показують результат:

```python
# main.py
import importlib
import config
from config import MODE, Service

svc = Service()                      # instance of the original class

# Edit config.py on disk here: MODE = "v2", and run() returns "version 2 run".
with open("config.py", "w") as f:
    f.write('MODE = "v2"\n\nclass Service:\n    def run(self):\n        return "version 2 run"\n')

importlib.reload(config)
print(MODE)                          # v1: the name copied by from-import is not rebound
print(config.MODE)                   # v2: attribute lookup sees the new value
print(svc.run())                     # v1 run: the instance keeps the old class
print(Service is config.Service)     # False: reload created a new class object
print(isinstance(svc, config.Service))  # False: the old instance is not an instance of the new class
```

`reload` виконує оператор `class` заново, тож `config.Service` – це новий class object, а старий `svc` лишається екземпляром старого класу. Документація описує це так: екземпляри, створені раніше, продовжують використовувати старе визначення класу.[^py314-library-importlib-reload]

Щоб уникнути пастки, звертайтеся до атрибутів модуля (`config.MODE`, `config.Service`) або повторно виконуйте `from`-інструкцію: документація називає обидва способи.[^py314-library-importlib-reload] Сам reload не потокобезпечний, тому під час виклику з кількох потоків потрібна синхронізація.[^py314-library-importlib-reload]

**Типові помилки:**
- очікувати, що reload оновить усі посилання: імена з `from`-імпортів в інших модулях, уже створені екземпляри класів;
- перевантажувати модуль, у якому визначено клас, і перевіряти `isinstance` зі старими екземплярами;
- робити reload модулів `sys`, `__main__` або `builtins`: документація прямо не рекомендує це, а модулі-розширення можуть впасти.[^py314-library-importlib-reload]

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
