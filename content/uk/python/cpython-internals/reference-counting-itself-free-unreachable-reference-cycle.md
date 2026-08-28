---
id: py-cpyint-0009
title: "Чому reference counting сам не може звільнити unreachable reference cycle?"
description: "Тому що кожен об'єкт у циклі має reference count ≥ 1 від іншого об'єкта того ж циклу, і жоден refcount ніколи не досягає нуля – хоча весь цикл більше недоступний ззовні."
track: python
section: cpython-internals
level: middle
type: mechanism
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L102-L197
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Тому що кожен об'єкт у циклі має reference count ≥ 1 від іншого об'єкта того ж циклу, і жоден refcount ніколи не досягає нуля – хоча весь цикл більше недоступний ззовні.**[^py314-library-dis] Наприклад, якщо `a` посилається на `b`, а `b` посилається на `a`, і зовнішніх посилань немає, обидва refcount дорівнюють 1. Reference counting не може відрізнити такий «мертвий» цикл від живих посилань. Для цього потрібен cyclic garbage collector.

## Detailed explanation

Reference counting звільняє об'єкт лише тоді, коли його refcount падає рівно до нуля. У циклі
кожен елемент тримає посилання на інший, тому навіть якщо ззовні на весь цикл ніхто більше не
посилається, кожен окремий refcount лишається ≥ 1 і природним чином ніколи не досягне
нуля.[^py314-library-gc]

Наприклад: `a = []`, `b = []`, `a.append(b)`, `b.append(a)`, потім `del a` і `del b`. Після цього
обидва refcount дорівнюють 1 (кожен елемент тримає інший), хоча жодна змінна більше не називає ні
`a`, ні `b`.

Reference counting – суто локальний механізм: він знає лише "скільки разів на мене посилаються", а
не "чи існує шлях до мене від коренів" (стек викликів, глобальні змінні, модулі). Для циклу ці дві
речі розходяться, і без глобального аналізу графа об'єктів цю розбіжність не виправити.

Cyclic GC (модуль `gc`) вирішує це trial-deletion алгоритмом: для кожного container-об'єкта в
generation він рахує, скільки посилань на нього приходить від інших container-об'єктів тієї ж
generation, і віднімає це число від справжнього refcount. Якщо результат дорівнює нулю, об'єкт (і
решта циклу) недосяжний ззовні generation і вважається сміттям.[^py314-library-gc]

```python
import gc

class Node:
    def __init__(self):
        self.other = None

a, b = Node(), Node()
a.other, b.other = b, a  # reference cycle
del a, b                  # refcount of each node is still 1
gc.collect()               # only the cyclic collector can free them
```

**Типові помилки:**
- вважати `del` еквівалентом гарантованого звільнення пам'яті;
- забувати, що cyclic collector відстежує лише container-типи (list, dict, об'єкти з `__dict__`
  тощо) – прості non-container об'єкти в циклах не бувають;
- вимикати `gc` і одночасно створювати цикли без ручного `gc.collect()`, отримуючи memory leak.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
