---
id: py-modimp-0002
title: "Яку роль відіграє `sys.modules` під час повторного імпорту того самого module name?"
description: "sys.modules – це кеш, який зберігає вже завантажені module objects; повторний import того самого імені повертає кешований об’єкт без пошуку та виконання коду."
track: python
section: modules-and-imports
level: middle
type: mechanism
tags: [sys-modules]
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
  - source_id: py314-reference-import-module-cache
    title: "Python 3.14: Reference/import, The module cache"
    url: https://docs.python.org/3.14/reference/import.html#the-module-cache
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Розділ «The module cache» офіційної документації Python 3.14: sys.modules перевіряється першим; значення None дає ModuleNotFoundError; видалений ключ викликає новий пошук; importlib.reload() повторно виконує код у тому самому object; старий і новий objects після повторного імпорту не є однаковими, якщо на старий є посилання."
  - source_id: py314-reference-import-loading
    title: "Python 3.14: Reference/import, Loading"
    url: https://docs.python.org/3.14/reference/import.html#loading
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Розділ «Loading» офіційної документації Python 3.14: якщо завантаження модуля завершилося винятком, цей модуль видаляється з sys.modules."
---

## Short answer

**`sys.modules` – це кеш, який зберігає вже завантажені module objects; повторний `import` того самого імені повертає кешований об’єкт без пошуку та виконання коду.**[^py314-reference-import-module-cache] Якщо `sys.modules[name]` містить module object, import негайно повертає його. Якщо значення дорівнює `None`, виникає `ModuleNotFoundError`.[^py314-reference-import-module-cache] Видалення ключа з `sys.modules` змушує наступний імпорт шукати та виконувати модуль заново, створюючи новий module object.[^py314-reference-import-module-cache]

## Detailed explanation

`sys.modules` – перше місце, яке перевіряє import. Ключ у ньому – повне ім’я модуля, значення – module object. Якщо ключ є і значення не `None`, Python повертає цей object без пошуку через finders і без виконання коду.[^py314-reference-import-module-cache] Сам `import` при цьому знову зв’язує ім’я в локальному namespace, але модуль не перевиконується.

Приклад створює тимчасовий модуль і показує три випадки: попадання в кеш, ручне видалення ключа і значення `None`.

```python
import sys
import tempfile
from pathlib import Path

# A throwaway module on disk, so the example can run as-is.
folder = Path(tempfile.mkdtemp())
(folder / 'counter_mod.py').write_text("print('executing counter_mod')\n")
sys.path.insert(0, str(folder))

import counter_mod   # not cached yet: the file is found and executed
import counter_mod   # sys.modules hit: nothing is printed
first = counter_mod

del sys.modules['counter_mod']   # manually drop the cache entry
import counter_mod   # cache miss: the file is searched and executed again
print(counter_mod is first)      # False: a new module object

sys.modules['blocked_mod'] = None  # None in the cache forces a failure
try:
    import blocked_mod
except ModuleNotFoundError:
    print('ModuleNotFoundError')
# Output: executing counter_mod, executing counter_mod, False, ModuleNotFoundError
```

Перший `import` знаходить файл і виконує його, другий нічого не друкує, бо береться з кешу. Після `del sys.modules[...]` наступний `import` знову шукає файл, виконує його і створює новий module object, тому `is` дає `False`. Старий object не знищується, доки на нього є посилання: змінна `first` тримає його живим.[^py314-reference-import-module-cache]

Значення `None` працює інакше: Python не шукає модуль, а одразу піднімає `ModuleNotFoundError`, навіть якщо файл існує.[^py314-reference-import-module-cache] Щоб перевиконати код у вже існуючому object, використовують `importlib.reload()`.[^py314-reference-import-module-cache] Якщо ж завантаження завершилося винятком, модуль видаляється з `sys.modules`, і наступний імпорт спробує знову.[^py314-reference-import-loading]

**Типові помилки:**
- вважати, що кожен повторний `import` знову виконує код модуля (це так, лише коли запису в кеші немає або попередній імпорт упав);
- видаляти ключ із `sys.modules`, щоб «перезавантажити» модуль, і потім порівнювати старі посилання з новими;
- очікувати від `importlib.reload()` нового module object (reload повторно використовує той самий object).

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
