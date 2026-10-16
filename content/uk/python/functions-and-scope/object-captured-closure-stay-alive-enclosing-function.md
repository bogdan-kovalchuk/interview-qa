---
id: py-funcs-0019
title: "Чому об’єкт, захоплений closure, може залишатися живим після завершення зовнішньої функції, і як це впливає на утримання пам’яті?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#user-defined-functions
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
  - source_id: py314-reference-executionmodel-dynamic-features
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#dynamic-features
  - source_id: py314-reference-datamodel-object-del
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__del__
---

## Short answer

**Closure зберігає посилання на захоплені змінні через атрибут `__closure__` (кортеж cell-об’єктів), тому ці об’єкти залишаються досяжними й не звільняються, доки жива сама closure.**[^py314-reference-datamodel] Це може призвести до неочікуваного утримання великих об’єктів у пам’яті: якщо closure захопила посилання на великий список і зберігається довго (наприклад, у callback), список теж залишається живим. Рішення – захоплювати лише потрібне значення (наприклад, `n = len(big)`), а не великий об’єкт; `del` у зовнішній функції не допоможе, якщо closure ще читає змінну.

## Detailed explanation

Коли вкладена функція посилається на змінну зовнішньої функції, ця змінна живе в cell-об’єкті, а не лише у frame зовнішньої функції. Функція зберігає свої cell-об’єкти в `__closure__`, і саме це утримує захоплені об’єкти після завершення зовнішньої функції.[^py314-reference-datamodel] Коли зовнішня функція повертається, її frame зникає, але cell лишається, поки існує closure.

Приклад: функція вже повернулася, а великий список лишився в пам’яті, бо `handler` його читає.

```python
def make_handler():
    big = list(range(1_000_000))   # a large list
    def handler():
        return len(big)            # the closure references big, so its cell keeps the list alive
    return handler

h = make_handler()                 # make_handler() has returned
print(len(h.__closure__[0].cell_contents))  # 1000000: the list is still reachable
```

Closure захоплює саму змінну, а не значення на момент створення: якщо зовнішня функція пізніше переприв’яже `big`, closure побачить нове значення.[^py314-reference-executionmodel-dynamic-features] У CPython об’єкт звільняється, щойно його reference count стає нулем, якщо циклічні посилання не заважають.[^py314-reference-datamodel-object-del] Тому `del h` у CPython звільняє список одразу, без очікування збирача сміття.

Пастка – спроба звільнити пам’ять через `del big` у зовнішній функції. Якщо closure ще читає `big`, cell стає порожньою, і `h()` дає `NameError: cannot access free variable 'big' ...`. Надійніший спосіб – зберегти в closure лише потрібне: `n = len(big)`, потім `del big` до створення closure. Тоді список звільняється одразу, а closure читає `n`.

**Типові помилки:**
- вважати, що closure фіксує значення змінної на момент створення, а не саму змінну;
- використати `del` у зовнішній функції, коли closure ще читає змінну: замість звільнення пам’яті виходить `NameError`;
- очікувати, що GC звільнить захоплений об’єкт, поки closure жива: доки на нього є посилання через cell, він не звільняється.
