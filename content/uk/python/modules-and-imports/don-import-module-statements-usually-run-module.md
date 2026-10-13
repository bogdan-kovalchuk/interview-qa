---
id: py-modimp-0003
title: "Чому два `import module` зазвичай не виконують top-level code модуля двічі, але можуть створити різні local bindings?"
description: "Top-level code виконується під час першого імпорту, поки модуль лишається в sys.modules; наступні import повертають той самий module object, але кожен import-statement зв’язує власні імена."
track: python
section: modules-and-imports
level: middle
type: comparison
tags: [import-module]
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
    applicability: "Розділ «The module cache» офіційної документації Python 3.14: після першого імпорту модуль лежить у sys.modules, і наступний import того самого імені повертає його з кешу; importlib.reload() повторно виконує код у тому самому object."
  - source_id: py314-reference-import-loading
    title: "Python 3.14: Reference/import, Loading"
    url: https://docs.python.org/3.14/reference/import.html#loading
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Розділ «Loading» офіційної документації Python 3.14: якщо завантаження модуля завершилося винятком, цей модуль видаляється з sys.modules, а вже завантажені модулі лишаються."
  - source_id: py314-reference-simple-stmts-import
    title: "Python 3.14: Reference/simple statements, The import statement"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#the-import-statement
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Розділ «The import statement» офіційної документації Python 3.14: import модуля зв’язує його ім’я (або ім’я після as) з module object; форма from ... import зв’язує посилання на значення атрибута."
---

## Short answer

**Top-level code виконується під час першого імпорту, поки модуль лишається в `sys.modules`; наступні `import` того самого імені повертають той самий module object.**[^py314-reference-import-module-cache] Кожен import-statement зв’язує власні імена в просторі імен імпортера: `import math` – ім’я `math` на module object, а `from math import pi` – ім’я `pi` на значення, яке було під час імпорту.[^py314-reference-simple-stmts-import] Тому зміна атрибута модуля пізніше не змінює ім’я, зв’язане через `from`.

## Detailed explanation

Перший `import` шукає модуль, створює module object і виконує його top-level код. Поки запис лишається в `sys.modules`, наступні `import` того самого імені знаходять його в кеші й нічого не виконують.[^py314-reference-import-module-cache] Тому неявний import виконує код один раз за дві умови: запис у кеші не видалено, і попередній імпорт не завершився винятком. Після винятку модуль видаляється з `sys.modules`, і наступний імпорт виконує файл знову.[^py314-reference-import-loading] Явний виклик `importlib.reload()` виконує код модуля знову, зберігаючи той самий module object; це не import statement.[^py314-reference-import-module-cache]

Друге питання – про прив’язку. Кожен import-statement зв’язує ім’я в локальному namespace імпортера, а форма визначає, яке саме:[^py314-reference-simple-stmts-import]

- `import m` зв’язує `m` з module object;
- `import m as x` зв’язує `x` з тим самим module object;
- `from m import name` зв’язує `name` зі значенням атрибута `m.name` на момент імпорту.

Приклад показує, що два імені вказують на один object, але прив’язка через `from` не стежить за атрибутом модуля:

```python
import sys
import tempfile
from pathlib import Path

# A throwaway module on disk, so the example can run as-is.
folder = Path(tempfile.mkdtemp())
(folder / 'settings_demo.py').write_text("print('executing settings_demo')\nvalue = 1\n")
sys.path.insert(0, str(folder))

import settings_demo as a        # prints: executing settings_demo
import settings_demo as b        # cache hit: nothing printed
from settings_demo import value  # binds the local name to the int 1

print(a is b)                    # True: one module object, two local names
print(a.value, value)            # 1 1
a.value = 2                      # rebind the attribute on the module object
print(a.value, value)            # 2 1: the from-import kept the old value
```

`a is b` дає `True`: модуль один, імен два. Зміна `a.value` змінює атрибут module object, але `value` лишається `1`, бо `from` зберіг посилання на значення, а не на атрибут.

Різні імена не означають різних об’єктів. Якщо `value` було б списком, `a.value.append(2)` був би видний і через `value`, бо це один і той самий list.

**Типові помилки:**
- очікувати, що повторний `import` знову виконає top-level код модуля;
- вважати, що `from m import name` стежить за змінами `m.name`;
- вважати, що `import m as a` і `import m as b` створюють дві копії модуля.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
