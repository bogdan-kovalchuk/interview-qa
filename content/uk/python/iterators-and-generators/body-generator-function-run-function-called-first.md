---
id: py-itergen-0005
title: "Коли виконується тіло generator function: під час виклику функції чи першого `next()`?"
track: python
section: iterators-and-generators
sources:
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
  - source_id: py314-reference-expressions-generator-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-expressions
---

## Short answer

**Тіло generator function не виконується під час виклику – воно запускається лише при першому `next()`.**[^py314-reference-expressions-yield-expressions] Виклик generator function миттєво повертає generator object без виконання жодного рядка тіла. Перший `next()` (або `for`) запускає виконання з початку до першого `yield`. Тому помилки в тілі виникають лише під час ітерації, а не при створенні generator.

## Detailed explanation

Тіло generator function не виконується під час виклику самої функції. Виклик функції з `yield` повертає generator – ітератор, який зберігає стан виконання й керує тілом. Тіло починається тоді, коли викликано один із методів generator, найчастіше `next()` через `for` або вбудовану функцію `next()`. Виконання йде до першого `yield`, призупиняється і віддає його значення.[^py314-reference-expressions-yield-expressions]

Далі кожен наступний `next()` продовжує з місця призупинення. Помилка всередині тіла, наприклад `int("x")`, з’явиться лише тоді, коли виконання дійде до цього рядка. Прив’язка аргументів – окреме питання: у CPython неправильна кількість аргументів дає `TypeError` уже під час виклику, ще до будь-якого `next()`. Приклад нижче показує обидва моменти; повідомлення в тілі друкується лише з першим `next()`:

```python
def parse(values):
    print("body started")           # runs on the first next(), not on the call
    for value in values:
        yield int(value)

gen = parse(["1", "x"])             # prints nothing: the body has not started
print("generator created")
print(next(gen))                    # prints "body started", then 1
try:
    next(gen)                       # int("x") raises inside the body
except ValueError:
    print("ValueError on the second next()")
```

Вивід починається з `generator created`, далі йде `body started` і `1`, а другий `next()` піднімає `ValueError`, який тут перехоплено.

Генераторний вираз `(x for x in items)` має одну відмінність: найлівіший iterable обчислюється одразу, тож помилка в ньому з’являється під час створення виразу, а не при `next()`.[^py314-reference-expressions-generator-expressions]

**Типові помилки:**
- очікувати, що `gen = parse(...)` виконує код до першого `yield`, наприклад друк або відкриття файлу;
- вважати, що помилка в тілі з’явиться вже під час створення generator;
- плутати створення generator зі споживанням: без `next()` або `for` тіло не виконується ніколи.
