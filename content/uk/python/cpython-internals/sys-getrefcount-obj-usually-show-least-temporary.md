---
id: py-cpyint-0007
title: "Чому `sys.getrefcount(obj)` зазвичай показує щонайменше одне temporary reference понад очікуване?"
description: "Тому що сам виклик sys.getrefcount(obj) створює тимчасове посилання на obj, яке передається як аргумент функції і враховується в refcount на момент вимірювання."
track: python
section: cpython-internals
level: senior
type: pitfall
tags: [sys-getrefcount-obj]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-library-dis
    title: "Python 3.14: Library/dis"
    url: https://docs.python.org/3.14/library/dis.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-gc
    title: "Python 3.14: Library/gc"
    url: https://docs.python.org/3.14/library/gc.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-c-api-memory
    title: "Python 3.14: C Api/memory"
    url: https://docs.python.org/3.14/c-api/memory.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-sys
    title: "Python 3.14: Library/sys"
    url: https://docs.python.org/3.14/library/sys.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-free-threading-python
    title: "Python 3.14: Howto/free Threading Python"
    url: https://docs.python.org/3.14/howto/free-threading-python.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-traceback-objects
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#traceback-objects
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Тому що сам виклик `sys.getrefcount(obj)` створює тимчасове посилання на `obj`, яке передається як аргумент функції і враховується в refcount на момент вимірювання.**[^py314-library-dis] Це тимчасове посилання існує лише під час виклику і зникає після повернення. Документація `sys` прямо зазначає, що значення зазвичай на одиницю більше очікуваного. Для immortal objects (наприклад, інтерновані рядки) значення може бути дуже великим і не відображає реальну кількість посилань.

## Detailed explanation

Функція `sys.getrefcount(obj)` повертає значення лічильника посилань `ob_refcnt` з C-структури `PyObject`, яке під час виконання виклику завжди збільшене щонайменше на одиницю через передачу об'єкта як аргументу в саму функцію.[^py314-library-sys] Коли в Python обчислюється вираз `sys.getrefcount(obj)`, віртуальна машина кладе посилання на `obj` на стек оцінювання (evaluation stack) для передачі в тіло функції. У C-рівні функція `sys_getrefcount_impl` зчитує макрос `Py_REFCNT(op)` у момент, коли цей стек-фрейм виклику є повністю сформованим і активним, тому його локальне посилання неминуче враховується в загальний підсумок.

Після завершення виклику та виходу з функції стек-фрейм знищується і тимчасове посилання негайно вивільняється, проте повернуте ціле число вже зафіксувало стан на момент виконання. Якщо ж об'єкт передається як частина складнішого виразу (наприклад, усередині тимчасового списку, кортежу чи генератора), кількість тимчасових посилань може зрости ще більше. Крім того, інструменти інспекції, налагоджувачі та об'єкти `traceback` (доступні через `sys.exc_info()`) нерідко утримують додаткові неявні посилання у власних стек-фреймах.

У сучасних версіях CPython (починаючи з Python 3.12 і PEP 683) ситуацію ускладнює наявність immortal objects: такі глобальні синглтони, як малі числа, інтерновані рядки, `True`, `False` та `None`, мають лічильник посилань, зафіксований на спеціальному константному значенні у мільярди одиниць.[^py314-c-api-memory] Це зроблено для оптимізації багатопотоковості та уникнення деградації кеш-ліній процесора. Для таких об'єктів `sys.getrefcount()` завжди повертає величезне число, яке взагалі не відображає кількість реальних змінних у програмі.

Демонстрація базового збільшення лічильника та поведінки для immortal-об'єктів:

```python
import sys

class Item:
    pass

item = Item()
# Baseline: 1 variable reference in local scope + 1 inside getrefcount argument
print(f"Direct: {sys.getrefcount(item)}")

container = [item, item]
# Now: 1 in item + 2 in container + 1 in getrefcount argument
print(f"In list: {sys.getrefcount(item)}")

# Immortal objects (PEP 683) do not reflect real references
print(f"Immortal: {sys.getrefcount(None)}")

# Output:
# Direct: 2
# In list: 4
# Immortal: 4294967295
```

**Типові помилки та підводні камені під час налагодження:**
- забувати про +1 під час аналізу витоків пам'яті: якщо локальна змінна одна, `getrefcount` повертає 2, що є абсолютно нормальним станом;
- намагатися аналізувати immortal-об'єкти: лічильники для `0`, `""` або `None` є штучними константами і не змінюються при додаванні посилань;
- ігнорувати замикання (closures) і стек-фрейми: глобальні змінні або змінні у `sys.exc_info()` та `traceback` утримують об'єкти в пам'яті довше, ніж очікує розробник.

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
