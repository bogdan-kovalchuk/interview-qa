---
id: py-modimp-0008
title: "Що означає partially initialized module під час circular import і чому не всі його names уже доступні?"
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
  - source_id: py314-reference-import-loading
    title: "Python 3.14: Reference/import (Loading)"
    url: https://docs.python.org/3.14/reference/import.html#loading
---

## Short answer

**Partially initialized module – це module object, який уже є в `sys.modules`, а його код ще виконується, тому доступні лише ті names, що були визначені до точки циклічного імпорту.**[^py314-reference-import-loading] Import machinery додає модуль до `sys.modules` до виконання коду, щоб цикл не породжував нескінченної рекурсії.[^py314-reference-import-loading] Якщо модуль A імпортує B, а B знову імпортує A, другий імпорт A повертає незавершений об’єкт. Звернення до ще не визначених names дає `AttributeError` (`a.name`) або `ImportError` (`from a import name`).

## Detailed explanation

Спочатку import system створює модуль і реєструє його в `sys.modules`, і лише потім loader виконує код модуля. Документація вимагає, щоб модуль уже був у `sys.modules` до виконання коду: інакше код, який імпортує сам себе прямо чи опосередковано, рекурсував би без кінця.[^py314-reference-import-loading] Тому повторний `import left` не запускає модуль знову, а повертає об’єкт, виконання якого ще не дійшло до кінця.

Які names доступні з такого об’єкта, визначає порядок виконання: ім’я з’являється тоді, коли відпрацювала інструкція, що його прив’язує. Нижче `left.py` визначає `LIMIT` до рядка `import right`, а `compute` – після нього. Запуск через `python main.py` (ілюстративний приклад, вивід перевірено на 3.12, 3.13 і 3.14):

```python
# left.py
LIMIT = 10              # bound before the cycle point
import right            # right.py runs now, while left is only partly initialized

def compute():          # not bound yet during the cycle
    return LIMIT * 2


# right.py
import left

print(left.LIMIT)                # 10: bound before the import line in left.py
print(hasattr(left, "compute"))  # False: def compute has not run yet
# from left import compute       # ImportError at this point: compute is not bound yet

def use():
    return left.compute()        # looked up when use() runs, after both modules load


# main.py
import left
import right

print(right.use())               # prints 10 and False from right.py, then 20
```

`main.py` імпортує `left` першим, тож `right` бачить незавершений `left`: `LIMIT` уже є, `compute` ще ні. Виклик `left.compute()` усередині `use()` працює, бо атрибут шукається в момент виклику, коли обидва модулі вже завантажені. Порядок входу має значення: якщо почати з `right`, то `left` виконається повністю до `hasattr`, і `hasattr(left, "compute")` дасть `True`.

Рядок `from left import compute` на тому самому етапі дає `ImportError`, бо `compute` ще не прив’язано. Тип винятку однаковий у 3.12, 3.13 і 3.14, але текст різниться. У 3.12: `cannot import name 'compute' from partially initialized module 'left' (most likely due to a circular import)`. У 3.13 і 3.14, коли `left.py` лежить у каталозі скрипта: `cannot import name 'compute' from 'left' (consider renaming ... if it has the same name as a library you intended to import)`; тут від 3.13 повідомлення вже не називає циклічний імпорт. Якщо ж `left` знаходиться через `PYTHONPATH`, усі три версії пишуть «partially initialized module» і «most likely due to a circular import».

**Типові помилки:**
- вважати, що `import left` у `right.py` дає повний модуль; він дає незавершений об’єкт, і names, визначені нижче точки циклу, відсутні;
- писати `from left import compute` на верхньому рівні модуля, що входить у цикл: це `ImportError` під час завантаження, а не `AttributeError` пізніше;
- «лікувати» цикл перестановкою рядків імпорту, не перевіривши, які names потрібні вже під час імпорту.
