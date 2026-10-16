---
id: py-modimp-0004
title: "Як порушення import protocol або ручне редагування `sys.modules` може призвести до двох module objects для одного source file?"
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
---

## Short answer

**Той самий файл можна імпортувати під різними повними іменами, і тоді `sys.modules` містить два різні module objects для одного source file.**[^py314-reference-import-module-cache] <span class="warn">Це небезпечно, коли модуль зберігає стан (singleton, кеш, реєстр) або визначає класи, за якими перевіряють тип: копія має власний стан, а `isinstance`- і `except`-перевірки з класами різних копій не спрацьовують.</span> Ключем у `sys.modules` є повне ім’я, а не шлях до файлу, тому `pkg.registry` і `registry` для Python – різні модулі.[^py314-reference-import-module-cache]

## Detailed explanation

Ключ у `sys.modules` – повне ім’я модуля, а не шлях до файлу.[^py314-reference-import-module-cache] Тому один source file, імпортований під двома іменами, дає два module objects: кожне ім’я має власний запис у кеші, і кожне завантаження виконує файл окремо. Однакові записи в `sys.path` самі по собі дубля не створюють, бо повторний import того самого імені знаходить запис у кеші.

Приклад створює пакет `pkg` з модулем `registry`, який має стан. Папку пакета додано до `sys.path` поруч із батьківською, тож той самий файл доступний і як `pkg.registry`, і як `registry`:

```python
import sys
import tempfile
from pathlib import Path

# A throwaway package on disk: pkg/registry.py holds state and a class.
root = Path(tempfile.mkdtemp())
(root / 'pkg').mkdir()
(root / 'pkg' / '__init__.py').write_text('')
(root / 'pkg' / 'registry.py').write_text("class Plugin: pass\nREGISTRY = []\n")
sys.path.insert(0, str(root))
sys.path.insert(0, str(root / 'pkg'))  # the same folder is now also a top-level path

import pkg.registry as via_package   # cached as 'pkg.registry'
import registry as via_flat          # same source file, different name

print(via_package is via_flat)                          # False: two module objects
print(via_package.__file__ == via_flat.__file__)        # True: same source file
print(isinstance(via_flat.Plugin(), via_package.Plugin))  # False: two class objects

# Manually dropping a cache entry and importing again also gives a second object.
first = via_package
del sys.modules['pkg.registry']
import pkg.registry as second
print(first is second)                                  # False
print(first.REGISTRY is second.REGISTRY)                # False: state is not shared
```

У виводі `via_package is via_flat` дає `False`, а `__file__` збігаються. Клас `Plugin` з однієї копії не є екземпляром `Plugin` з іншої: `class` виконується двічі і створює два класи. Стан теж подвоюється, бо `REGISTRY` у кожної копії свій.

Ручний шлях дає той самий результат: після `del sys.modules[...]` старе посилання вказує на інший object зі своїм станом. Документація прямо каже, що два такі objects не будуть однаковими.[^py314-reference-import-module-cache]

Дубль шкідливий, коли модуль має стан, визначає класи, за якими перевіряють тип (`isinstance`, `except`), або має побічні ефекти при імпорті. Навіть без стану класи з різних копій не збігаються. Запобіжники: один повний імпорт на файл, жодної папки пакета в `sys.path`, жодного ручного редагування `sys.modules`.

**Типові помилки:**
- вважати, що однаковий `__file__` означає один module object (ключ кешу – ім’я);
- додати папку пакета до `sys.path`, щоб «спростити» імпорт, і отримати другу копію модуля зі своїм станом;
- видалити запис із `sys.modules`, щоб скинути стан, і не помітити, що старі посилання тримають попередній стан.
