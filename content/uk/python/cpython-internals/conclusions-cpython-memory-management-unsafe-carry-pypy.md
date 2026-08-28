---
id: py-cpyint-0020
title: "Які висновки про memory management CPython небезпечно переносити на PyPy або іншу Python implementation?"
description: "Reference counting, миттєва деаллокація при refcount=0, конкретний bytecode, sys.getrefcount() та id() як адреса в пам'яті – усі це деталі CPython, які не гарантовані іншими implementations."
track: python
section: cpython-internals
level: senior
type: comparison
tags: []
status: published
updated: 2026-09-05
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L27-L46
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Reference counting, миттєва деаллокація при refcount=0, конкретний bytecode, `sys.getrefcount()` та `id()` як адреса в пам'яті – усі це деталі CPython, які не гарантовані іншими implementations.**[^py314-library-dis] PyPy використовує tracing GC замість reference counting: `__del__` може бути викликаний значно пізніше або в іншому порядку; `sys.getrefcount()` повертає невизначене значення; `id()` не відповідає фізичній адресі; bytecode взагалі відсутній (JIT компілює в machine code). Тому будь-який код, що покладається на timing фіналізації або на specific memory layout, є непереносимим.

## Detailed explanation

CPython – лише одна з реалізацій Python, і частина спостережуваної поведінки, яка здається частиною
мови, насправді є деталлю саме CPython allocator і reference counting.[^py314-c-api-memory]
Перенесення такого висновку на PyPy, MicroPython чи Jython може дати цілком інший результат.

Найважливіший приклад – момент виклику `__del__`. У CPython об'єкт звільняється синхронно, щойно
refcount падає до нуля, тому фіналізатор спрацьовує детерміновано в момент останнього `del` або
виходу зі scope. PyPy натомість використовує tracing (generational) GC без reference counting:
`__del__` викликається під час чергового циклу збору, який може статися значно пізніше або взагалі
не встигнути до завершення процесу.[^py314-library-gc]

`sys.getrefcount()` та `id()` – ще два інструменти, чия семантика прив'язана до CPython.
`sys.getrefcount()` читає поле `ob_refcnt`, якого немає в реалізаціях без reference counting, тому
виклик або відсутній, або повертає значення без сенсу. `id()` у CPython – це фізична адреса об'єкта
в пам'яті, а в PyPy – довільний ідентифікатор, не пов'язаний з розташуванням об'єкта.[^py314-library-sys]

Bytecode CPython (`dis`-вивід) – ще одна деталь, якої взагалі немає в PyPy: там методи компілюються
JIT-трасувальником у machine code, минаючи стабільний набір опкодів CPython.

**Що небезпечно переносити з CPython на іншу реалізацію:**
- очікування, що ресурс (файл, socket, lock) звільниться одразу після того, як об'єкт вийшов зі
  scope, без явного `with` чи `close()`;
- порівняння продуктивності чи allocation count через `sys.getrefcount()`;
- використання `id()` як стабільного, порівнюваного значення адреси;
- припущення про порядок або момент виконання `__del__` у циклах з посиланнями.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
