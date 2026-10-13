---
id: py-itergen-0011
title: "За якої умови перший виклик `generator.send(value)` допустимий і чому зазвичай спочатку надсилають `None`?"
description: "Перший виклик send() допускає лише None, бо на момент старту generator ще не дійшов до жодного yield, яким міг би прийняти значення."
track: python
section: iterators-and-generators
level: middle
type: pitfall
tags: [generator-send-value]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-generator-iterator-methods
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-iterator-methods
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: методи generator-iterator (__next__, send, throw, close) і їхня поведінка у призупиненому стані."
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

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
