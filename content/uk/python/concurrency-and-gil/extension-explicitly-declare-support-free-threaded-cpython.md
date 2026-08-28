---
id: py-gil-0011
title: "Як C extension явно позначає підтримку free-threaded CPython 3.14 і що може статися під час import несумісного extension?"
description: "C extension позначає підтримку free-threaded build через слот Py_mod_gil зі значенням Py_MOD_GIL_NOT_USED (multi-phase init) або виклик PyUnstable_Module_SetGIL(module, Py_MOD_GIL_NOT_USED) (single-phase init)."
track: python
section: concurrency-and-gil
level: senior
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython free-threaded build"
    version: "3.14"
anki:
  export: true
sources:
  - source_id: py314-library-threading
    title: "Python 3.14: Library/threading"
    url: https://docs.python.org/3.14/library/threading.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-multiprocessing
    title: "Python 3.14: Library/multiprocessing"
    url: https://docs.python.org/3.14/library/multiprocessing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-concurrent-futures
    title: "Python 3.14: Library/concurrent.futures"
    url: https://docs.python.org/3.14/library/concurrent.futures.html
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
  - source_id: py314-howto-free-threading-extensions
    title: "Python 3.14: Howto/free Threading Extensions"
    url: https://docs.python.org/3.14/howto/free-threading-extensions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**C extension позначає підтримку free-threaded build через слот `Py_mod_gil` зі значенням `Py_MOD_GIL_NOT_USED` (multi-phase init) або виклик `PyUnstable_Module_SetGIL(module, Py_MOD_GIL_NOT_USED)` (single-phase init).**[^py314-library-threading] <span class="warn">Якщо extension не декларує підтримку:</span> при import видається warning і GIL автоматично вмикається назад, зводячи нанівець переваги free-threaded build. Для умовної компіляції використовується макрос `Py_GIL_DISABLED`.

## Detailed explanation

Free-threaded build CPython вимагає, щоб кожен C extension явно підтвердив, що він safe для роботи
без GIL; без такого підтвердження extension вважається несумісним і за замовчуванням змушує CPython
повернути GIL.[^py314-howto-free-threading-extensions]

Спосіб декларації залежить від стилю ініціалізації extension. Для multi-phase init (PEP 489,
`Py_mod_exec` слоти) додається окремий слот `Py_mod_gil` зі значенням `Py_MOD_GIL_NOT_USED` у масиві
`PyModuleDef_Slot`. Для старішого single-phase init, де модуль створюється напряму через
`PyModule_Create`, той самий ефект дає виклик `PyUnstable_Module_SetGIL(module, Py_MOD_GIL_NOT_USED)`
у функції `PyInit_*` одразу після створення об'єкта module.

Приклад декларації підтримки free-threaded build у multi-phase init:

```c
static PyModuleDef_Slot module_slots[] = {
    {Py_mod_exec, module_exec},
    {Py_mod_gil, Py_MOD_GIL_NOT_USED},
    {0, NULL},
};
```

Якщо extension не містить жодної з цих декларацій, import на free-threaded build видає
`RuntimeWarning` і автоматично вмикає GIL для всього процесу – навіть якщо extension фактично
thread-safe. Це консервативна поведінка "за замовчуванням небезпечно": CPython не намагається
вгадати безпеку extension, а покладається на explicit opt-in автора.[^py314-howto-free-threading-python]

Для умовного коду під free-threaded build використовується макрос `Py_GIL_DISABLED`, визначений
лише в такому build. Він дозволяє огортати ділянки, що потребують додаткової синхронізації (critical
sections, atomic operations), у `#ifdef Py_GIL_DISABLED`, не дублюючи весь файл для обох
конфігурацій.

**Типові помилки:**
- декларувати `Py_MOD_GIL_NOT_USED`, не перевіривши реальну thread-safety внутрішніх C-структур та
  кешів;
- забувати, що декларація – це обіцянка автора extension, а не автоматична перевірка з боку CPython;
- плутати `Py_mod_gil` (per-module slot) із загальним прапорцем компіляції `Py_GIL_DISABLED`
  (per-build macro).

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
