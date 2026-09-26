---
id: py-cpyint-0018
title: "Чим `sys.getsizeof()` відрізняється від recursive measurement повного object graph?"
description: "sys.getsizeof() повертає лише розмір самого об'єкта (через __sizeof__), не враховуючи пам'ять об'єктів, на які він посилається."
track: python
section: cpython-internals
level: middle
type: comparison
tags: [sys-getsizeof]
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

**`sys.getsizeof()` повертає лише розмір самого об'єкта (через `__sizeof__`), не враховуючи пам'ять об'єктів, на які він посилається.**[^py314-library-dis] Наприклад, `sys.getsizeof([1]*1000)` повідомить лише розмір list-об'єкта (масив pointer'ів), але не розмір 1000 int-об'єктів. Для повного вимірювання object graph потрібна рекурсивна функція, яка обходить усі вкладені об'єкти та враховує `id()` для уникнення дублікатів. `getsizeof()` також додає GC overhead для об'єктів під управлінням garbage collector.

## Detailed explanation

Функція `sys.getsizeof()` виконує виключно поверхневе (shallow) вимірювання пам'яті, викликаючи спеціальний метод об'єкта `__sizeof__()` та додаючи накладні витрати заголовка garbage collector (`PyGC_Head`), якщо об'єкт відстежується GC.[^py314-library-sys] Для складених контейнерів (списків, словників, кортежів або екземплярів класів) повернуте значення містить лише розмір власної C-структури контейнера та його внутрішнього масиву вказівників (`PyObject*`), але не пам'ять самих об'єктів, на які ці вказівники посилаються.

Через це виклик `sys.getsizeof()` для великих вкладених структур даних створює хибну ілюзію низького споживання пам'яті. Наприклад, список із мільйона однакових рядків чи словників поверне лише розмір буфера вказівників (кілька мегабайтів), тоді як реальний обсяг виділеної пам'яті під самі рядки чи словники в купі CPython може сягати сотень мегабайтів. Крім того, для звичайних екземплярів класів `sys.getsizeof(instance)` повертає лише розмір структури самого екземпляра, ігноруючи словник атрибутів `__dict__` або динамічно зв'язані ресурси.

Повне вимірювання графа об'єктів вимагає рекурсивного обходу всіх залежностей, наприклад за допомогою функції `gc.get_referents()` або власного обходу полів контейнерів.[^py314-library-gc] При такому обході критично важливо вести реєстр уже відвіданих адрес (`id(obj)`), щоб уникнути нескінченної рекурсії на циклічних посиланнях і не підраховувати двічі спільні об'єкти, такі як інтерновані рядки, кешовані малі цілі числа або синглтони на кшталт `None`.

Різниця між поверхневим вимірюванням та рекурсивним обходом графа об'єктів:

```python
import gc
import sys

def total_size(obj, seen=None):
    """Recursively calculate the full memory footprint of an object graph."""
    if seen is None:
        seen = set()
    obj_id = id(obj)
    if obj_id in seen:
        return 0
    seen.add(obj_id)
    size = sys.getsizeof(obj)
    for referent in gc.get_referents(obj):
        size += total_size(referent, seen)
    return size

nested_data = [[1, 2, 3] for _ in range(100)]

shallow = sys.getsizeof(nested_data)
deep = total_size(nested_data)

print(f"Shallow: {shallow} bytes")  # ~920 bytes (outer list container only)
print(f"Deep: {deep} bytes")        # ~9800+ bytes (includes nested lists and ints)
```

**Типові помилки та підводні камені:**
- Оцінювати використання пам'яті кешами, деревами чи JSON-документами за допомогою `sys.getsizeof()`, отримуючи значення, занижені в десятки або сотні разів.
- Реалізовувати рекурсивний підрахунок без множини `seen`, що спричиняє `RecursionError` на циклічних структурах або багаторазове дублювання спільних об'єктів.
- Не враховувати спільні підструктури (shared memory): якщо два контейнери посилаються на один масив, наївна сума їхніх розмірів подвоїть пам'ять спільних даних.
- Забувати про пам'ять C-розширень і буферів: `__sizeof__` не завжди відображає пам'ять, виділену бібліотеками на C поза стандартними механізмами CPython (для цього надійніше використовувати модуль `tracemalloc`).

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
