---
id: py-modimp-0010
title: "Чим regular package з `__init__.py` відрізняється від namespace package?"
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
  - source_id: pep-0420
    title: "PEP 420: Implicit Namespace Packages"
    url: https://peps.python.org/pep-0420/
  - source_id: py314-reference-import-regular-packages
    title: "Python 3.14: Reference/import (Regular packages)"
    url: https://docs.python.org/3.14/reference/import.html#regular-packages
  - source_id: py314-reference-import-namespace-packages
    title: "Python 3.14: Reference/import (Namespace packages)"
    url: https://docs.python.org/3.14/reference/import.html#namespace-packages
  - source_id: py314-library-importlib-modulespec-origin
    title: "Python 3.14: Library/importlib (ModuleSpec.origin)"
    url: https://docs.python.org/3.14/library/importlib.html#importlib.machinery.ModuleSpec.origin
---

## Short answer

**Regular package – це каталог із файлом `__init__.py`, що лежить в одному каталозі; namespace package такого файлу не має й може складатися з порцій у різних каталогах.**[^pep-0420] Файл `__init__.py` regular package виконується при імпорті.[^py314-reference-import-regular-packages] Regular package з тим самим ім’ям має пріоритет, навіть якщо знайдений пізніше в `sys.path`, ніж порції namespace package.[^pep-0420] `__path__` namespace package – спеціальний ітерабельний тип, а не звичайний список: при наступному імпорті всередині пакета він знову шукає порції, якщо змінився шлях батьківського пакета або `sys.path`.[^py314-reference-import-namespace-packages] `ModuleSpec.origin` такого пакета дорівнює `None`.[^py314-library-importlib-modulespec-origin]

## Detailed explanation

Regular package і namespace package – два способи створити пакет, і import system розрізняє їх під час пошуку в `sys.path`. Для кожного каталогу `foo` перевіряється наявність `foo/__init__.py`. Якщо файл є, повертається regular package одразу. Якщо ні, але є каталог `foo` без `__init__.py`, він записується як порція, і пошук триває. Якщо regular package не знайдено, з усіх записаних порцій створюється namespace package.[^pep-0420]

Звідси дві практичні відмінності. По-перше, regular package має один каталог, тож його підмодулі шукаються лише в ньому. По-друге, namespace package збирає підмодулі з усіх порцій, які знайшлися на шляху, навіть якщо вони лежать у різних місцях файлової системи, в zip-архівах чи інших джерелах.[^py314-reference-import-namespace-packages]

Ілюстративний приклад: два каталоги дають один namespace package `shop` (вивід перевірено на 3.12, 3.13 і 3.14):

```python
# Layout: site-a/shop/plugins/cart.py and site-b/shop/plugins/search.py; no shop/__init__.py
import sys
sys.path[:0] = ["site-a", "site-b"]
import shop.plugins.cart
import shop.plugins.search
print(shop.__spec__.origin)           # None
print(type(shop.__path__).__name__)   # _NamespacePath
```

`origin` дорівнює `None`, бо в namespace package немає одного файлу, з якого його завантажено.[^py314-library-importlib-modulespec-origin] Ім’я класу `_NamespacePath` – деталь CPython, тож на нього в коді не варто спиратися. Якщо додати `site-a/shop/__init__.py`, то `shop` стає regular package з одним `__path__` (`site-a/shop`), і `import shop.plugins.search` падає з `ModuleNotFoundError`. PEP 420 описує namespace package без атрибута `__file__`.[^pep-0420] У CPython 3.12–3.14 атрибут усе ж є, зі значенням `None`.

**Типові помилки:**
- додати порожній `__init__.py` в одну з порцій і несподівано втратити підпакети з інших каталогів;
- вважати, що `__file__` namespace package вказує на каталог: у CPython це `None`;
- вважати `__path__` namespace package звичайним списком, який не змінюється після імпорту: при наступному імпорті всередині пакета його порції перераховуються, якщо змінився шлях батьківського пакета або `sys.path`.
