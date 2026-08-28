---
id: py-cpyint-0015
title: "У free-threaded CPython 3.14 `sys.getrefcount()` для object повертає несподівано велике значення: як immortalization це пояснює і чому це значення не слід тлумачити як точну кількість references?"
description: "У free-threaded build певні об'єкти (code constants, interned strings) стають immortal – їх refcount ніколи не змінюється і встановлений у дуже велике sentinel-значення, тому sys.getrefcount() повертає саме його, а не..."
track: python
section: cpython-internals
level: middle
type: practical
tags: [sys-getrefcount]
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

**У free-threaded build певні об'єкти (code constants, interned strings) стають immortal – їх refcount ніколи не змінюється і встановлений у дуже велике sentinel-значення, тому `sys.getrefcount()` повертає саме його, а не реальну кількість посилань.**[^py314-library-dis] Immortalization усуває atomic refcount contention між потоками: оскільки об'єкт ніколи не буде deallocated, немає потреби оновлювати лічильник. Документація явно зазначає, що для immortal об'єктів повернене значення не відображає фактичну кількість references і його не слід використовувати ні для чого, окрім перевірки на 0 або 1.

## Detailed explanation

Immortalization – це механізм CPython, який позначає окремі об'єкти як такі, що ніколи не будуть
deallocated: замість звичайного reference counting їхнє поле `ob_refcnt` встановлюється у фіксоване
sentinel-значення (дуже велике число, підібране так, щоб подальші inc/dec ніколи не переповнили й не
занулили його), і подальші incref/decref над таким об'єктом стають no-op.[^py314-howto-free-threading-python]

Ідея з'явилася для free-threaded build (PEP 703): без GIL кожен incref/decref мав би бути
atomic-операцією, а найгарячіші об'єкти – `None`, `True`, `False`, малі кешовані int, interned
strings, code constants – читаються й "утримуються" мільйонами місць одночасно. Зробивши їх
immortal, інтерпретатор прибирає ці atomic-операції з hot path замість того, щоб намагатися їх
оптимізувати.[^py314-c-api-memory]

`sys.getrefcount(obj)` не має спеціального case для immortal об'єктів: вона просто читає те саме
поле `ob_refcnt` і додає 1 за тимчасове посилання на `obj` під час самого виклику.[^py314-library-sys]
Для immortal об'єкта це поле – не лічильник, а sentinel-константа, тому повернене число не має
жодного стосунку до кількості реальних посилань і виглядає невиправдано великим.

Приклад, який показує різницю між звичайним і immortal об'єктом:

```python
import sys

class Plain:
    pass

obj = Plain()
print(sys.getrefcount(obj))     # small, real number of references

print(sys.getrefcount(None))    # huge sentinel value, not a real count
```

**Типові помилки:**
- читати повернене значення як точну кількість `del`, потрібних для деструкції об'єкта;
- дивуватися, чому число не зменшується після видалення локальних змінних, що посилалися на
  immortal об'єкт;
- використовувати `sys.getrefcount()` для діагностики memory leaks замість `tracemalloc` чи
  `gc.get_referrers()`;
- забувати, що з Python 3.12+ immortal стали не лише `None`/`True`/`False`, а й малі кешовані int та
  деякі рядки, тож поведінка відрізняється від старіших версій.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
