---
id: py-modimp-0011
title: "Які завдання доречно виконувати в package `__init__.py`, а які створюють небажані import-time side effects?"
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
  - source_id: py314-reference-import-regular-packages
    title: "Python 3.14: Reference/import, Regular packages"
    url: https://docs.python.org/3.14/reference/import.html#regular-packages
  - source_id: py314-reference-import-loading
    title: "Python 3.14: Reference/import, Loading"
    url: https://docs.python.org/3.14/reference/import.html#loading
  - source_id: py314-reference-import-module-cache
    title: "Python 3.14: Reference/import, The module cache"
    url: https://docs.python.org/3.14/reference/import.html#the-module-cache
  - source_id: py314-tutorial-modules-importing-from-a-package
    title: "Python 3.14: Tutorial/modules, Importing * From a Package"
    url: https://docs.python.org/3.14/tutorial/modules.html#importing-from-a-package
---

## Short answer

**`__init__.py` виконується під час імпорту пакета, тому там доречна lightweight ініціалізація: convenience re-exports (`from .sub import Class`) та конфігурація, яка не вимагає I/O.**[^py314-reference-import-regular-packages] Змінна `__all__` задає, які імена бере `from package import *`, тож публічний API можна оголосити і там.[^py314-tutorial-modules-importing-from-a-package] Небажані import-time side effects – це важкі обчислення, мережеві виклики, запис у файли або зміна глобального стану: вони зазвичай виконуються один раз, при першому успішному `import`.[^py314-reference-import-module-cache] Вони уповільнюють запуск і створюють приховані залежності від порядку ініціалізації.

## Detailed explanation

`__init__.py` – це код, який Python виконує автоматично, коли імпортується regular package: об’єкти, визначені в ньому, стають атрибутами пакета.[^py314-reference-import-regular-packages] Це стосується і підмодулів. Оператор `import shop.models` спершу виконує `shop/__init__.py`, а потім `shop/models.py`.[^py314-reference-import-regular-packages] Тому все, що є в `__init__.py`, виконується для кожного, хто імпортує будь-який підмодуль, навіть якщо потрібен лише один клас.

Доречні завдання – дешеві, детерміновані дії, що не залежать від середовища: експорт публічного API (`from .models import Order` робить `Order` доступним як `shop.Order`), `__all__` і константи. Без `__all__` інструкція `from shop import *` лише імпортує пакет і бере імена, визначені в `__init__.py`.[^py314-tutorial-modules-importing-from-a-package]

Небажані side effects – це дії за межами модуля: читання і запис файлів, запити до мережі, відкриття з’єднань із базою даних, запуск потоків, зміна `sys.path` чи глобального логування. Користувач нічого не викликав явно, а `import` уже запустив цей код. Кеш `sys.modules` зазвичай не дає повторно виконати код: успішно імпортований пакет береться з кешу, поки запис там є.[^py314-reference-import-module-cache] Якщо import упав, запис видаляється, і наступний import виконує `__init__.py` знову.[^py314-reference-import-loading] Сам код може спрацювати в неочікуваний момент, наприклад під час тестів. Модуль додається до `sys.modules` ще до виконання коду, тож циклічний імпорт може побачити пакет лише частково заповненим.[^py314-reference-import-loading]

Приклад: `shop/__init__.py` з побічним ефектом. Файл `shop/models.py` містить лише `class Order: pass`.

```python
# shop/__init__.py
from .models import Order          # lightweight re-export: no I/O
__all__ = ["Order"]                # names bound by "from shop import *"

print("shop/__init__.py runs")     # import-time side effect: runs once per interpreter
```

Скрипт, який імпортує підмодулі цього пакета:

```python
# main.py  (output: "shop/__init__.py runs" once, then the class line)
import shop.models      # runs shop/__init__.py first, then shop/models.py
import shop             # already in sys.modules: __init__.py does not run again
from shop import *      # __all__ limits the names to Order
print(Order)            # <class 'shop.models.Order'>
```

**Типові помилки:**
- вважати, що `__init__.py` виконується лише тоді, коли імпортують сам пакет, а не його підмодуль;
- відкривати файли або мережеві з’єднання в `__init__.py`, а потім дивуватися, чому повільно стартують тести чи інструменти;
- вважати, що `__all__` обмежує все, що можна імпортувати: він впливає лише на `from package import *`.
