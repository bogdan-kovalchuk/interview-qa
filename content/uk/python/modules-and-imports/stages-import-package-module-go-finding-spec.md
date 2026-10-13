---
id: py-modimp-0001
title: "Які етапи проходить `import package.module` від пошуку специфікації до виконання module code?"
description: "Кожне ім’я в import package.module проходить чотири етапи: перевірку sys.modules, пошук ModuleSpec через finders, створення module object і виконання коду модуля."
track: python
section: modules-and-imports
level: middle
type: mechanism
tags: [import-package-module]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
    version: null
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
  - source_id: py314-reference-import-searching
    title: "Python 3.14: Reference/import, Searching"
    url: https://docs.python.org/3.14/reference/import.html#searching
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Розділ «Searching» офіційної документації Python 3.14: для import foo.bar.baz спочатку виконується імпорт верхнього рівня foo, потім foo.bar і foo.bar.baz."
  - source_id: py314-reference-import-module-cache
    title: "Python 3.14: Reference/import, The module cache"
    url: https://docs.python.org/3.14/reference/import.html#the-module-cache
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Розділ «The module cache» офіційної документації Python 3.14: sys.modules перевіряється першим; якщо ім’я там є, повертається кешований object."
  - source_id: py314-reference-import-meta-path
    title: "Python 3.14: Reference/import, The meta path"
    url: https://docs.python.org/3.14/reference/import.html#the-meta-path
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Розділ «The meta path» офіційної документації Python 3.14: find_spec() і його аргумент path (для підмодуля це __path__ батька); повернений spec або None передає пошук далі."
  - source_id: py314-reference-import-loading
    title: "Python 3.14: Reference/import, Loading"
    url: https://docs.python.org/3.14/reference/import.html#loading
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Розділ «Loading» офіційної документації Python 3.14: модуль записується в sys.modules до виконання коду; module object створює loader; exec_module() виконує код модуля."
  - source_id: py314-reference-import-submodules
    title: "Python 3.14: Reference/import, Submodules"
    url: https://docs.python.org/3.14/reference/import.html#submodules
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Розділ «Submodules» офіційної документації Python 3.14: після завантаження підмодуль є атрибутом батьківського пакета."
  - source_id: py314-reference-import-regular-packages
    title: "Python 3.14: Reference/import, Regular packages"
    url: https://docs.python.org/3.14/reference/import.html#regular-packages
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Розділ «Regular packages» офіційної документації Python 3.14: __init__.py звичайного пакета виконується під час імпорту пакета."
  - source_id: py314-reference-simple-stmts-import
    title: "Python 3.14: Reference/simple statements, The import statement"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#the-import-statement
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Розділ «The import statement» офіційної документації Python 3.14: import для модуля верхнього рівня зв’язує його ім’я, для вкладеного модуля зв’язує ім’я верхнього пакета."
---

## Short answer

**`import package.module` імпортує спочатку `package`, потім `module`, і для кожного імені виконує той самий ланцюжок: перевірку `sys.modules`, пошук через `sys.meta_path`, створення module object і виконання коду.**[^py314-reference-import-searching] Пошук `module` іде в `package.__path__`, а не в `sys.path`.[^py314-reference-import-meta-path] Модуль додається в `sys.modules` до виконання свого коду.[^py314-reference-import-loading] Сам `import` зв’язує в локальному namespace лише ім’я `package`.[^py314-reference-simple-stmts-import]

## Detailed explanation

`import package.module` – це два імпорти, а не один. Спочатку імпортується `package`.[^py314-reference-import-searching] Якщо `package` – звичайний пакет з `__init__.py`, Python імпортує його так само, як звичайний `import package`: знаходить його і виконує `__init__.py`; namespace package такого файлу не має.[^py314-reference-import-regular-packages] Лише після цього шукається `module`, і шлях пошуку береться з `package.__path__`.[^py314-reference-import-meta-path]

Для кожного з двох імен етапи однакові:

- `sys.modules`: якщо ім’я там є, повертається кешований object, і далі нічого не виконується.[^py314-reference-import-module-cache]
- `sys.meta_path`: finders викликають `find_spec()`; перший, що повертає spec, визначає результат.[^py314-reference-import-meta-path]
- створення: loader створює module object (через `create_module()` або стандартним `ModuleType`), і module уже є в `sys.modules` до виконання коду.[^py314-reference-import-loading]
- виконання: `exec_module()` виконує код модуля в його namespace.[^py314-reference-import-loading]

Приклад замінює файли пам’яттю і логує кожен виклик `find_spec()`:

```python
import sys
import importlib.abc
import importlib.machinery

# Fake package "demo" with submodule "demo.mod", served from memory.
SOURCES = {
    'demo': "print('demo/__init__ runs')\n",
    'demo.mod': "print('demo.mod module code runs')\nVALUE = 42\n",
}


class MemoryFinder(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def find_spec(self, fullname, path, target=None):
        where = 'None' if path is None else 'parent __path__'
        print(f'find_spec({fullname!r}, {where})')
        if fullname not in SOURCES:
            return None  # let the next meta path finder try
        return importlib.machinery.ModuleSpec(
            fullname, self, is_package=(fullname == 'demo'))

    def exec_module(self, module):
        code = SOURCES[module.__name__]
        exec(compile(code, module.__name__, 'exec'), module.__dict__)


sys.meta_path.insert(0, MemoryFinder())

# Output: find_spec('demo', None), demo/__init__ runs,
#         find_spec('demo.mod', parent __path__), demo.mod module code runs
import demo.mod
print(demo.mod.VALUE)  # 42
```

Для `demo.mod` finder отримує `__path__` батька, тож підмодуль шукається в пакеті, а не в `sys.path`. Після завантаження підмодуль є атрибутом пакета.[^py314-reference-import-submodules] Ім’я `demo` прив’язує import statement, а не import machinery.[^py314-reference-simple-stmts-import]

**Типові помилки:**
- вважати, що `import package.module` зв’язує в локальному namespace ім’я `module` (зв’язується `package`);
- шукати підмодуль у `sys.path`, хоча пошук іде в `__path__` батьківського пакета;
- плутати `find_spec()`, який лише шукає spec, із `exec_module()`, який виконує код модуля.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
