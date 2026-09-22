---
id: py-objtypes-0018
title: "Коли `bytearray` доцільніший за `bytes` і який trade-off створює його mutability?"
description: "bytearray доцільний, коли потрібно модифікувати binary дані in-place (побайтове читання/запис буфера, accumulation даних з мережі) без створення нових об'єктів на кожну зміну."
track: python
section: objects-and-types
level: middle
type: comparison
tags: [bytearray, bytes]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/data_types.md#L498-L586
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`bytearray` доцільний, коли потрібно модифікувати binary дані in-place (побайтове читання/запис буфера, accumulation даних з мережі) без створення нових об'єктів на кожну зміну.**[^py314-reference-datamodel] На відміну від `bytes`, `bytearray` mutable, тому підтримує assignment і deletion за індексом. Trade-off: `bytearray` unhashable – його не можна використовувати як dict key або елемент `set`, а його mutability означає, що всі посилання на той самий об'єкт бачать зміни (aliasing).

## Detailed explanation

`bytearray` є мутабельною послідовністю цілих чисел у діапазоні 0–255, що надає можливість змінювати двійкові дані in-place на противагу незмінному типу `bytes`.[^py314-reference-datamodel]

Оскільки `bytes` незмінний, будь-яка модифікація – конкатенація пакетів із мережі, оновлення заголовків чи зрізи з перезаписом – вимагає створення нового об'єкта `bytes` і копіювання всіх наявних даних ($O(N)$ на кожну операцію). Послідовне накопичення фрагментів призводить до квадратичної складності $O(N^2)$ за часом та пам'яттю. Натомість `bytearray` спирається на неперервний буфер у C-пам'яті з надлишковим виділенням (аналогічно до `list`), що забезпечує амортизовану складність $O(1)$ для додавання елементів (`.extend()`, `+=`), мутації за індексом чи зрізом (`buf[0] = 0xFF`) та прямого читання через `socket.recv_into()` або `file.readinto()` без проміжних алокацій.[^py314-library-stdtypes]

Проте мутабельність створює відчутні архітектурні компроміси. По-перше, `bytearray` не реалізує метод `__hash__` (є unhashable), через що його неможливо використовувати як ключ у `dict` або елемент у `set`, тоді як `bytes` вільно хешується та кешується. По-друге, спільне використання мутабельного буфера різними функціями чи потоками створює ризик аліасингу (aliasing): неконтрольована зміна даних однією частиною системи стає видимою для всіх посилань. Тому перед передачею даних у зовнішні шари або невідомим споживачам часто створюють захисну копію або приводять буфер до незмінного `bytes(ba)`.

Порівняння конкатенації та мутації in-place між `bytes` та `bytearray`:

```python
# bytes is immutable: modifications create new objects
b = b"hello"
# b[0] = 0x48  # TypeError: 'bytes' object does not support item assignment
new_b = b + b" world"
print(b, new_b)  # b'hello' b'hello world'

# bytearray is mutable: supports in-place modifications
ba = bytearray(b"hello")
ba[0] = ord("H")  # in-place item assignment
ba.extend(b" world")  # in-place append without reallocating whole object
print(ba)  # bytearray(b'Hello world')

# Hashability trade-off
print(isinstance(hash(b), int))  # True
try:
    hash(ba)
except TypeError as err:
    print(type(err).__name__)  # TypeError
```

**Практичні рекомендації та типові підводні камені:**
- накопичення бінарних даних: для збирання потоку байтів (наприклад, із сокета) слід використовувати `bytearray` або список частин `list[bytes]` з фінальним `b''.join()`, уникаючи квадратичного `b += chunk`;
- захист від аліасингу (aliasing): якщо мутабельний `bytearray` передається іншим компонентам системи, безпечніше перетворити його на незмінний `bytes(ba)`;
- відсутність хешування: неможливість використовувати `bytearray` як ключ у `dict` або в кешах вимагає явної конвертації у `bytes`;
- прямий ввід-вивід: методи `sock.recv_into(ba)` та `f.readinto(ba)` дозволяють записувати байти безпосередньо в попередньо виділену пам'ять без створення проміжних об'єктів.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
