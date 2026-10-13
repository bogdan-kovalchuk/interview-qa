---
id: py-modimp-0012
title: "Що саме захищає `if __name__ == \"__main__\"` і чого він не змінює в import semantics?"
description: "if __name__ == \"__main__\" захищає код від виконання під час імпорту: коли модуль запускають як скрипт, __name__ дорівнює \"__main__\", а при звичайному import – своїй dotted name."
track: python
section: modules-and-imports
level: middle
type: mechanism
tags: [if-name-main]
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
  - source_id: py314-library-main
    title: "Python 3.14: Library/__main__, Top-level code environment"
    url: https://docs.python.org/3.14/library/__main__.html#name-main
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: __name__ дорівнює '__main__' у верхньому рівні програми та імені модуля при імпорті; код під if __name__ == '__main__' не виконується при імпорті."
  - source_id: py314-reference-import-loading
    title: "Python 3.14: Reference/import, Loading"
    url: https://docs.python.org/3.14/reference/import.html#loading
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: модуль додається в sys.modules до виконання його коду, а повторний import повертає вже створений модуль."
  - source_id: py314-reference-import-special-considerations-for-main
    title: "Python 3.14: Reference/import, Special considerations for __main__"
    url: https://docs.python.org/3.14/reference/import.html#special-considerations-for-main
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: файл, запущений як скрипт, і той самий файл, імпортований під своїм іменем, є різними модулями."
---

## Short answer

**`if __name__ == "__main__"` захищає лише свій блок: він виконується, коли модуль є верхнім рівнем програми (наприклад, `python3 file.py`), а при `import` блок пропускається, бо `__name__` дорівнює dotted name модуля.**[^py314-library-main] Guard не змінює import semantics: решта коду модуля виконується при `import` як звичайно, а сам модуль кешується в `sys.modules`.[^py314-reference-import-loading] Якщо той самий файл запустити як скрипт і потім імпортувати, Python розглядає це як два різні module objects.[^py314-reference-import-special-considerations-for-main]

## Detailed explanation

Guard спирається на одне правило. Модуль, який Python виконує як верхній рівень програми, отримує `__name__ == "__main__"`, а будь-який імпортований модуль – своє ім’я, наприклад `calc` або `pkg.calc`, якщо файл лежить у пакеті.[^py314-library-main] Тому `if __name__ == "__main__":` захищає саме блок під собою: розбір аргументів командного рядка, демонстрацію, виклик `main()`. Цей блок не виконується при імпорті, і завдяки цьому з того самого файлу можна імпортувати функції та класи без побічних дій.

Файл `calc.py` містить код, який виконується завжди, і код, який виконується лише як скрипт:

```python
# calc.py
print("calc: top-level code runs on import too")  # not guarded

def square(x):
    return x * x

if __name__ == "__main__":
    print("calc: guarded block, only when run as a script")
    print(square(3))
```

`python3 calc.py` друкує обидва рядки та `9`. Якщо ж виконати `import calc`, друкується лише перший рядок: функція `square` доступна, а guarded block – ні.

Guard не означає «не виконувати модуль при імпорті»: Python усе одно створює module object, реєструє його в `sys.modules` і виконує весь код верхнього рівня, включно з рядками поза блоком. Пропускається лише сам блок. Повторний `import` того самого імені повертає об’єкт із кешу без повторного виконання.[^py314-reference-import-loading]

Пастка виникає, коли файл запускають як скрипт і він же імпортується під своїм іменем. У `sys.modules` з’являється запис `__main__`, а `import dup` шукає запис `dup`, якого ще немає, тож файл виконується вдруге як окремий module object. Документація прямо називає такі модулі різними.[^py314-reference-import-special-considerations-for-main]

Файл `dup.py` демонструє цю пастку: його запускають як скрипт, а він імпортує себе під своїм іменем.

```python
# dup.py, run as: python3 dup.py
import sys

print("dup executed as", __name__)
if __name__ == "__main__":
    import dup                       # the same file, loaded again under the name "dup"
    print("same module object:", dup is sys.modules["__main__"])
```

Результат запуску:

```text
dup executed as __main__
dup executed as dup
same module object: False
```

Наслідки: код поза guard виконується двічі, а класи, визначені в обох копіях, є різними класами.

**Типові помилки:**
- вважати, що guard робить модуль безпечним для імпорту: код поза блоком виконується завжди;
- тримати функції та класи, потрібні іншим модулям, усередині `if __name__ == "__main__":`: імпортер їх не побачить;
- імпортувати файл, запущений як скрипт, і очікувати, що його код виконається один раз.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
