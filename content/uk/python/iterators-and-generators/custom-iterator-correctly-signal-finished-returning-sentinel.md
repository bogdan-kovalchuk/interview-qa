---
id: py-itergen-0003
title: "Як правильно сигналізувати завершення custom iterator і чому повернення sentinel value з `__next__` не є еквівалентом?"
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
  - source_id: py314-reference-compound-stmts-for
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-for-statement
  - source_id: py314-library-functions-iter
    title: "Python 3.14: Library/functions"
    url: https://docs.python.org/3.14/library/functions.html#iter
  - source_id: pep-479
    title: "PEP 479: Change StopIteration handling inside generators"
    url: https://peps.python.org/pep-0479/
---

## Short answer

**Коректний спосіб – підняти `StopIteration` з `__next__()`, коли елементів більше немає.**[^py314-library-stdtypes-iterator-types] Цикл `for` завершується, коли iterator вичерпано.[^py314-reference-compound-stmts-for] Повернений sentinel value цикл не зупиняє: споживач отримує його як черговий елемент і продовжує ітерацію, тож без `StopIteration` цикл сам не зупиниться.

## Detailed explanation

Протокол iterator визначає кінець через виняток `StopIteration`. Цикл `for` виконує suite для кожного елемента, який віддає iterator, і завершується, коли iterator вичерпано.[^py314-reference-compound-stmts-for] Значення, яке повертає `__next__()`, цикл завжди сприймає як елемент, тому жодне значення саме собою кінця не позначає. Після того як `__next__()` підніме `StopIteration`, кожен наступний його виклик має знову піднімати цей виняток.[^py314-library-stdtypes-iterator-types]

Ось клас, який повертає `None` замість `StopIteration`. Його `__next__()` ніколи не завершує ітерацію, тому `islice()` потрібен, щоб зупинити вивід:

```python
from itertools import islice

class Source:
    def __init__(self, items):
        self._items = list(items)
        self._pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._pos >= len(self._items):
            return None                  # wrong: None reaches the loop as an item
        item = self._items[self._pos]
        self._pos += 1
        return item

print(list(islice(Source([1, 2]), 5)))   # [1, 2, None, None, None]: no end on its own
```

Правильна версія піднімає `StopIteration`, і цикл завершується сам:

```python
class Source:
    def __init__(self, items):
        self._items = list(items)
        self._pos = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._pos >= len(self._items):
            raise StopIteration          # the end signal defined by the protocol
        item = self._items[self._pos]
        self._pos += 1
        return item

print(list(Source([1, 2])))              # [1, 2]
```

Є два обмеження. По-перше, у generator function `StopIteration` піднімати вручну не можна: PEP 479 замінює його на `RuntimeError`, а завершити генератор можна через `return`.[^pep-479] Наприклад, генератор з `yield 1` і наступним `raise StopIteration` при обході дає `RuntimeError: generator raised StopIteration`.

По-друге, сентинел має сенс у двоаргументній формі `iter(callable, sentinel)`. Там `iter()` сам порівнює значення, яке повертає `callable()`, із `sentinel` і піднімає `StopIteration`.[^py314-library-functions-iter] Той самий `None`, який у класі вище був звичайним елементом, тут зупиняє цикл:

```python
values = iter([1, 2, None, 3])
for x in iter(lambda: next(values), None):
    print(x)                             # 1, then 2; the loop stops at None
```

**Типові помилки:**
- повертати `None` або порожній рядок з `__next__()` як ознаку кінця: цикл не зупиняється;
- піднімати `StopIteration` всередині generator function замість `return`: виходить `RuntimeError`;
- вважати, що після першого `StopIteration` можна знову викликати `__next__()` і отримати елементи: виняток повторюється.
