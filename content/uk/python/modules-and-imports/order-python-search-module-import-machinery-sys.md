---
id: py-modimp-0005
title: "У якому порядку Python шукає module через import machinery та `sys.path`?"
track: python
section: modules-and-imports
sources:
  - source_id: py314-reference-import
    title: "Python 3.14: Reference/import"
    url: https://docs.python.org/3.14/reference/import.html
  - source_id: py314-library-importlib
    title: "Python 3.14: Library/importlib"
    url: https://docs.python.org/3.14/library/importlib.html
  - source_id: py-packaging-guide
    title: "Python Packaging User Guide"
    url: https://packaging.python.org/en/latest/tutorials/packaging-projects/
  - source_id: py314-reference-import-module-cache
    title: "Python 3.14: Reference/import, The module cache"
    url: https://docs.python.org/3.14/reference/import.html#the-module-cache
  - source_id: py314-reference-import-meta-path
    title: "Python 3.14: Reference/import, The meta path"
    url: https://docs.python.org/3.14/reference/import.html#the-meta-path
  - source_id: py314-reference-import-finders-and-loaders
    title: "Python 3.14: Reference/import, Finders and loaders"
    url: https://docs.python.org/3.14/reference/import.html#finders-and-loaders
  - source_id: py314-reference-import-path-based-finder
    title: "Python 3.14: Reference/import, The Path Based Finder"
    url: https://docs.python.org/3.14/reference/import.html#the-path-based-finder
  - source_id: py314-library-sys-path
    title: "Python 3.14: Library/sys, sys.path"
    url: https://docs.python.org/3.14/library/sys.html#sys.path
---

## Short answer

**Python спочатку перевіряє `sys.modules`, потім проходить `sys.meta_path`, де за замовчуванням built-in, frozen і path-based finder.**[^py314-reference-import-finders-and-loaders] Path-based finder послідовно обходить записи `sys.path` для top-level модуля і `__path__` батьківського пакета для підмодуля.[^py314-reference-import-path-based-finder] Finder для кожного запису береться з `sys.path_importer_cache`, а якщо його там немає, створюється через `sys.path_hooks` і кешується.[^py314-reference-import-path-based-finder]

## Detailed explanation

Пошук іде у фіксованому порядку, який можна відтворити вручну:

- `sys.modules`: якщо ім’я там є, пошук завершено.[^py314-reference-import-module-cache]
- `sys.meta_path` по черзі; стандартні finders за документацією – built-in, frozen і path-based.[^py314-reference-import-finders-and-loaders] У CPython їхні класи BuiltinImporter, FrozenImporter і PathFinder (спостережено на 3.13 і 3.14).
- `PathFinder` перебирає записи `sys.path` для top-level модуля або `__path__` батьківського пакета для підмодуля.[^py314-reference-import-path-based-finder]
- для кожного запису береться finder із `sys.path_importer_cache`. Якщо його немає, `sys.path_hooks` створює finder; якщо жоден hook не підійшов, у кеш лягає `None`.[^py314-reference-import-path-based-finder]
- перший знайдений spec перемагає. Якщо нічого не знайдено, піднімається `ModuleNotFoundError`.[^py314-reference-import-meta-path]

Порядок `sys.meta_path` має наслідок: built-in модуль знаходиться раніше за `sys.path`, тож файл `itertools.py` на початку `sys.path` його не перекриває. Це спостереження в CPython 3.13 і 3.14 (`itertools.__spec__.origin` дає `'built-in'`), а не цитата з документації.

Серед записів `sys.path` перемагає перший, що містить файл:

```python
import sys
import tempfile
from pathlib import Path

first_dir = Path(tempfile.mkdtemp())
second_dir = Path(tempfile.mkdtemp())
(first_dir / 'finder_demo.py').write_text("WHERE = 'first_dir'\n")
(second_dir / 'finder_demo.py').write_text("WHERE = 'second_dir'\n")

sys.path[:0] = [str(first_dir), str(second_dir)]  # first_dir is searched first
import finder_demo
print(finder_demo.WHERE)  # first_dir: the first match wins
print(type(sys.path_importer_cache[str(first_dir)]).__name__)  # FileFinder: cached per entry
```

Початковий `sys.path` береться з `PYTHONPATH` і встановлених за замовчуванням місць. За замовчуванням (якщо не задано `-P` або `PYTHONSAFEPATH`) перед ними додається директорія скрипта, поточна директорія для `-m` або порожній рядок для `-c` і REPL.[^py314-library-sys-path]

Список `sys.meta_path` не завжди містить лише стандартні finders. У системному CPython 3.13 першим стоїть finder із `_distutils_hack` (спостережено), тож три стандартні finders не є повним переліком.

**Типові помилки:**
- вважати, що `sys.path_importer_cache` кешує знайдений модуль (він кешує finder для запису `sys.path`);
- очікувати, що файл на початку `sys.path` перекриє built-in модуль;
- шукати підмодуль у `sys.path`, а не в `__path__` батьківського пакета.
