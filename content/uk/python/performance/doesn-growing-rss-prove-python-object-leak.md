---
id: py-perf-0020
title: "Чому зростання RSS не доводить Python object leak і які додаткові вимірювання потрібні?"
description: "Зростання RSS саме по собі не доводить leak: RSS включає pymalloc arenas, фрагментацію та пам’ять C-розширень."
track: python
section: performance
level: senior
type: pitfall
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-library-tracemalloc
    title: "Python 3.14: Library/tracemalloc"
    url: https://docs.python.org/3.14/library/tracemalloc.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, модуль tracemalloc: відстежує більшість блоків, виділених Python (не всю пам’ять процесу); порівняння двох знімків для пошуку leak."
  - source_id: py314-c-api-memory
    title: "Python 3.14: C Api/memory"
    url: https://docs.python.org/3.14/c-api/memory.html#the-pymalloc-allocator
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, розділ pymalloc: дрібні об’єкти до 512 байт, арени фіксованого розміру (1 MiB на 64-bit); більші алокації йдуть до PyMem_RawMalloc. Не описує, коли арени повертаються ОС."
  - source_id: cpython-obmalloc-arena-release
    title: "CPython Objects/obmalloc.c: arena release"
    url: https://github.com/python/cpython/blob/v3.14.6/Objects/obmalloc.c#L2431
    accessed: 2026-10-13
    kind: official
    version: "3.14.6"
    applicability: "Вихідний код CPython 3.14.6, Objects/obmalloc.c, рядок 2431 (if (nf == ao->ntotalpools && ao->nextarena != NULL)): арена звільняється системі, коли всі її pools вільні і вона не остання в списку. Деталь реалізації CPython, а не гарантія мови."
  - source_id: py314-library-gc
    title: "Python 3.14: Library/gc"
    url: https://docs.python.org/3.14/library/gc.html#gc.is_tracked
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, gc.get_objects і gc.is_tracked: повертаються лише об’єкти, які відстежує збирач; атомарні типи як правило не відстежуються. Не описує пам’ять процесу."
  - source_id: py314-library-sys
    title: "Python 3.14: Library/sys"
    url: https://docs.python.org/3.14/library/sys.html#sys.getallocatedblocks
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, sys.getallocatedblocks: кількість блоків, виділених інтерпретатором; значення може змінюватися між викликами через внутрішні кеші, тому може знадобитися gc.collect() і _clear_internal_caches(). Не є мірою RSS."
---

## Short answer

**Зростання RSS саме по собі не доводить Python object leak: RSS показує всю фізичну пам’ять процесу, а не лише живі об’єкти Python.** Дрібні об’єкти до 512 байт живуть в arenas pymalloc,[^py314-c-api-memory] а в CPython арена повертається ОС лише тоді, коли всі її pools вільні,[^cpython-obmalloc-arena-release] тому RSS може не впасти після звільнення. Щоб відрізнити leak, порівнюють знімки `tracemalloc`, рахують `gc.get_objects()` і дивляться на `sys.getallocatedblocks()` після `gc.collect()` (а за потреби й `sys._clear_internal_caches()`) при повторюваному навантаженні.[^py314-library-sys]

## Detailed explanation

RSS (Resident Set Size) – це обсяг фізичної пам’яті процесу, яка зараз знаходиться в RAM. Цей показник не розрізняє, що саме її займає: живі Python-об’єкти, блоки, які Python уже звільнив, але ще не повернув ОС, фрагментацію, пам’ять C-розширень чи файли, відображені в пам’ять. Тому зростання RSS – це симптом, який треба пояснити, а не доказ leak.

CPython виділяє дрібні об’єкти через pymalloc. Об’єкти до 512 байт беруться з arenas фіксованого розміру, а більші алокації йдуть до `PyMem_RawMalloc()`.[^py314-c-api-memory] Звільнений дрібний об’єкт лише звільняє свій блок усередині pool. Арена повертається ОС тільки тоді, коли всі її pools вільні,[^cpython-obmalloc-arena-release] тож одна жива структура в арені не дає віддати весь її обсяг. Тому RSS після `del` може лишатися високим, навіть якщо посилань на об’єкти вже немає.

Python-level leak означає, що кількість об’єктів зростає за сталого навантаження, зазвичай тому, що їх ще тримає якесь посилання: глобальний список, кеш без ліміту, замикання або реєстр callback-ів. Обмежений кеш зростає лише до свого ліміту й далі стабілізується, тому сигналом є тренд від ітерації до ітерації, а не одне значення. Саме зростання RSS без такого тренду лишається лише підозрою.

Для Python-рівневого росту використовують такі вимірювання:

- **tracemalloc.** Модуль відстежує більшість блоків, виділених Python, і зберігає traceback місця виділення. Порівняння двох знімків його документація прямо називає способом знайти leak.[^py314-library-tracemalloc]
- **gc.get_objects().** Повертає об’єкти, які відстежує збирач сміття. Атомарні типи як правило не відстежуються: у CPython `gc.is_tracked("abc")` дає `False`, тож рядки не з’являються в цьому списку.[^py314-library-gc]
- **sys.getallocatedblocks().** Повертає кількість блоків, які інтерпретатор тримає зараз. Значення може відрізнятися між викликами через внутрішні кеші, тому може знадобитися `gc.collect()`, а за потреби `sys._clear_internal_caches()`, і порівняння трендів.[^py314-library-sys]

Приклад: цикл зберігає 10 000 об’єктів `bytes` по 1000 байт у словнику, а найбільша різниця двох знімків `tracemalloc` припадає на рядок, який тримає їх живими.

```python
import tracemalloc

tracemalloc.start()
cache = {}
before = tracemalloc.take_snapshot()

for i in range(10_000):
    cache[i] = bytes(1000)

after = tracemalloc.take_snapshot()
top = after.compare_to(before, "lineno")[0]
print(top.traceback[0].lineno)  # 8: the cache[i] = ... line keeps the blocks alive
```

Це не означає, що tracemalloc бачить усе. У CPython пам’ять, яку C-код отримує напряму через `malloc()`, не потрапляє у знімки tracemalloc, тому відсутність росту в tracemalloc не доводить відсутності витоку в C-коді.

**Типові помилки:**
- вважати зростання RSS доказом leak без знімків і без повторення навантаження;
- читати одне значення `sys.getallocatedblocks()` без `gc.collect()` і без порівняння з попередніми вимірюваннями;
- шукати leak рядків або байтів через `gc.get_objects()`, де вони як правило не з’являються.

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
