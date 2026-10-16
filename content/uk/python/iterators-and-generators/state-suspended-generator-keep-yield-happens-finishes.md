---
id: py-itergen-0006
title: "Який state зберігає suspended generator між двома `yield` і що відбувається після його завершення?"
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

**Suspended generator зберігає локальні змінні, instruction pointer, evaluation stack та стан exception handling.**[^py314-reference-expressions-yield-expressions] Коли тіло завершується через `return` або вихід без `yield`, `next()` піднімає `StopIteration`.[^py314-reference-expressions-generator-iterator-methods] Далі кожен наступний `next()` знову піднімає `StopIteration`.[^py314-library-stdtypes-iterator-types] Щоб пройти послідовність знову, треба викликати generator function заново, і це створить новий generator.[^py314-reference-expressions-yield-expressions]

## Detailed explanation

Suspended generator – це не просто функція, що «чекає». Коли виконання доходить до `yield`, зберігається весь стан: прив’язки локальних змінних, instruction pointer, внутрішній evaluation stack і стан exception handling. Коли споживач знову викликає метод generator, тіло продовжує так, ніби `yield` був звичайним викликом.[^py314-reference-expressions-yield-expressions]

У прикладі локальна змінна `x` живе між викликами, а після останнього `yield` generator завершується:

```python
def gen():
    x = 10                          # local variable kept while suspended
    yield x                         # suspended here
    yield x + 1                     # resumed here by the next call

g = gen()
print(next(g))                      # 10
print(next(g))                      # 11
try:
    next(g)                         # the body ends: StopIteration
except StopIteration:
    print("finished")
try:
    next(g)                         # a finished generator keeps raising StopIteration
except StopIteration:
    print("still finished")
```

Вивід: `10`, `11`, потім `finished` і `still finished`. Коли тіло доходить до кінця або виконує `return`, generator виходить без нового `yield`, і `next()` піднімає `StopIteration`.[^py314-reference-expressions-generator-iterator-methods] Якщо ж виняток не перехоплено всередині тіла, він поширюється до виклику `next()`.[^py314-reference-expressions-generator-iterator-methods] Після цього generator уже завершений, і у CPython наступний `next()` піднімає `StopIteration`; це спостереження з запусків на CPython 3.12–3.14, а не окреме правило документації.

Пройти ту саму послідовність через той самий generator object ще раз неможливо: після `StopIteration` він більше нічого не віддає, а кожен наступний `next()` знову піднімає `StopIteration`. Реалізація iterator, яка цього не робить, вважається зламаною.[^py314-library-stdtypes-iterator-types] Щоб отримати нову послідовність, треба викликати generator function заново, і тоді створюється новий generator з власним станом.[^py314-reference-expressions-yield-expressions]

**Типові помилки:**
- вважати, що generator «перезапускається», якщо викликати `next()` після `StopIteration`;
- очікувати, що локальні змінні скидаються між викликами: призупинений generator зберігає їх;
- після винятку, що вилетів із тіла, очікувати, що можна продовжити з того самого місця.
