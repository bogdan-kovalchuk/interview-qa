---
id: py-itergen-0011
title: "За якої умови перший виклик `generator.send(value)` допустимий і чому зазвичай спочатку надсилають `None`?"
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
  - source_id: py314-reference-expressions-generator-iterator-methods
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-iterator-methods
---

## Short answer

**Для щойно створеного generator перший `send()` допускає лише `None`, бо до першого `yield` немає виразу, який міг би прийняти значення.**[^py314-reference-expressions-generator-iterator-methods] У CPython будь-яке інше значення викликає `TypeError`. Тому generator зазвичай запускають через `next(gen)`, який передає `None` і зупиняє generator на першому `yield`.[^py314-reference-expressions-generator-iterator-methods]

## Detailed explanation

Вираз `send(value)` робить `value` результатом поточного виразу `yield` і повертає наступне значення, яке generator віддає. Тому `send()` може передати значення лише тоді, коли generator уже призупинений на `yield`. Щойно створений generator такого місця ще не має, бо його тіло не виконувалось. Документація прямо вимагає, щоб виклик, який запускає generator, передавав `None`, бо немає виразу `yield`, який міг би прийняти значення.[^py314-reference-expressions-generator-iterator-methods]

Приклад показує обидві ситуації: невдалий перший `send()` і запуск через `None`. Коментарі показують вивід, перевірений на CPython 3.13 і 3.14:

```python
def echo():
    received = yield 'ready'        # the value sent later arrives here
    print('got', received)
    yield 'next'

g = echo()
try:
    g.send('hello')                 # first call with a non-None value
except TypeError as error:
    print('TypeError:', error)      # can't send non-None value to a just-started generator
print(g.send(None))                 # ready: runs the body up to the first yield
print(g.send('hello'))              # got hello, then next
```

У CPython невдалий перший `send('hello')` не запускає generator, тому наступний `send(None)` починає його з початку і зупиняється на першому `yield`. Значення `'hello'` потрапляє в `received` лише тоді, коли generator уже призупинений на `yield`. Є й друге уточнення: `send()` повертає наступне значення, яке generator віддав через `yield`, а не значення, яке було надіслано. Коли generator відновлюють через `__next__`, поточний вираз `yield` завжди дорівнює `None`.[^py314-reference-expressions-generator-iterator-methods]

Отже, умова така: для щойно створеного generator перше значення через `send()` має бути `None`. Після того як generator призупинився на `yield`, `send(value)` з будь-яким значенням працює. Тому на практиці його спершу «прогрівають» одним `next(gen)`, який зупиняє generator на першому `yield`, а далі значення передають через `send()`.[^py314-reference-expressions-generator-iterator-methods]

**Типові помилки:**
- починати роботу з generator через `send(value)` зі значенням, відмінним від `None`; у CPython це `TypeError`;
- вважати, що `send(value)` повертає надіслане значення; воно повертає наступне значення, яке generator віддав через `yield`;
- плутати `next(gen)` і `send(value)`: обидва відновлюють generator, але лише `send()` передає значення в поточний `yield`.
