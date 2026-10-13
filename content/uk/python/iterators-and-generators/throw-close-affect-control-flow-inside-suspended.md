---
id: py-itergen-0012
title: "Як `throw()` і `close()` впливають на control flow усередині suspended generator?"
description: "throw() піднімає задану exception, а close() – GeneratorExit, саме в тій точці yield, де generator був призупинений."
track: python
section: iterators-and-generators
level: senior
type: mechanism
tags: [throw, close]
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

**`throw()` піднімає переданий exception у точці призупиненого `yield`, а `close()` піднімає там `GeneratorExit`.**[^py314-reference-expressions-generator-iterator-methods] Якщо generator перехоплює виняток у `try/except` навколо `yield`, він може продовжити роботу і віддати наступне значення, яке повертає `throw()`. Якщо виняток, переданий через `throw()`, не оброблено, він поширюється до виклику. <span class="warn">Якщо після `GeneratorExit` generator знову виконує `yield`, `close()` піднімає `RuntimeError`.</span>[^py314-reference-expressions-generator-iterator-methods]

## Detailed explanation

Призупинений generator стоїть на `yield`. `next()` і `send()` відновлюють його звичайним способом і передають значення в цей вираз. `throw()` і `close()` відновлюють його інакше: вони піднімають exception у точці `yield`, тож `try`, `except` і `finally` навколо цього `yield` спрацьовують так, ніби саме цей вираз викинув виняток.[^py314-reference-expressions-generator-iterator-methods]

Приклад з `throw()`: generator перехоплює виняток, віддає нове значення, і це значення повертає `throw()`. Коментарі показують вивід на CPython 3.13 і 3.14:

```python
def catcher():
    try:
        yield 1                     # suspended here
    except ValueError as error:
        print('caught', repr(error))
        yield 'after catch'         # throw() returns this value
    yield 'end'

g = catcher()
print(next(g))                      # 1
print(g.throw(ValueError('boom')))  # caught ValueError('boom'), then after catch
print(next(g))                      # end
```

Якщо exception не перехоплено, `throw()` його не ковтає: виняток поширюється до виклику, а після цього generator завершений. Для `close()` правило інше: він піднімає `GeneratorExit`, який generator може не перехоплювати. `finally` навколо `yield` виконується і при `close()`, і при непійманому `throw()`.[^py314-reference-expressions-generator-iterator-methods]

Приклад з `close()` показує `finally`. У CPython, якщо generator ще не запускався, `close()` не виконує його тіло:

```python
def resource():
    print('open')
    try:
        yield 1
    finally:
        print('cleanup')            # runs when the paused generator is closed

g = resource()
next(g)                             # open
g.close()                           # cleanup
g2 = resource()
g2.close()                          # prints nothing: the body never started
```

Якщо generator у відповідь на `GeneratorExit` повертає значення через `return`, то з Python 3.13 `close()` повертає його. Якщо ж після `GeneratorExit` він знову виконує `yield`, `close()` піднімає `RuntimeError`.[^py314-reference-expressions-generator-iterator-methods]

**Типові помилки:**
- думати, що `close()` лише «закриває» generator: він піднімає `GeneratorExit` у точці призупинення, тож `finally` виконується;
- після `GeneratorExit` знову віддавати значення через `yield`: тоді `close()` піднімає `RuntimeError`;
- очікувати, що `throw()` завжди повертає значення: якщо generator не перехопив виняток або завершився без наступного `yield`, виняток поширюється або піднімається `StopIteration`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
