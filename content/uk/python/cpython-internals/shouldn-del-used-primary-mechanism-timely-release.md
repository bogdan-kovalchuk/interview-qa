---
id: py-cpyint-0014
title: "Чому `__del__` не слід використовувати як основний механізм timely release зовнішніх resources?"
description: "__del__ не гарантує ні своєчасного виклику, ні виклику взагалі: він може бути відкладений cyclic GC, пропущений при shutdown інтерпретатора, а винятки всередині нього ігноруються."
track: python
section: cpython-internals
level: senior
type: pitfall
tags: [del]
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

**`__del__` не гарантує ні своєчасного виклику, ні виклику взагалі: він може бути відкладений cyclic GC, пропущений при shutdown інтерпретатора, а винятки всередині нього ігноруються.**[^py314-library-dis] Конкретні ризики: (1) якщо об'єкт потрапляє в reference cycle, `__del__` викликається лише коли cyclic GC його виявить; (2) при shutdown інтерпретатора глобальні змінні можуть вже дорівнювати `None`; (3) `__del__` може викликатися з довільного потоку, що створює ризик deadlock при захопленні lock. Для timely release використовуйте context manager (`with`) або `weakref.finalize`.

## Detailed explanation

Метод `__del__` у Python є асинхронним фіналізатором об'єкта, а не детермінованим деструктором (на відміну від RAII у C++), тому його виклик не гарантує своєчасного (timely) звільнення дефіцитних зовнішніх ресурсів, таких як дескриптори файлів, сокети чи з'єднання з базою даних.[^py314-library-gc] В основі керування пам'яттю CPython лежить підрахунок посилань (reference counting): фіналізатор викликається негайно лише тоді, коли лічильник посилань об'єкта падає до нуля. Проте якщо об'єкт стає частиною циклічного посилання (reference cycle) – навіть ненавмисно через замикання або зворотні посилання, – його лічильник ніколи не досягає нуля при виході зі скоупу. Звільнення такого об'єкта відкладається до наступного запуску cyclic GC (`gc.collect()`), що загрожує вичерпанням лімітів операційної системи задовго до збирання пам'яті.

Критичною небезпекою є також поведінка під час shutdown інтерпретатора (`sys.exit()`, завершення процесу або аварійна зупинка). Під час фіналізації середовища глобальні змінні модулів послідовно очищаються та зв'язуються з `None`, тому звернення до імпортованих модулів або допоміжних функцій усередині `__del__` часто аварійно завершується з помилкою `AttributeError` чи `TypeError`.[^py314-library-sys] Крім того, винятки, підняті всередині `__del__`, не перехоплюються блоками `try...except`: CPython просто друкує попередження у `sys.stderr` і продовжує роботу, що маскує збої очищення.

Для детермінованого контролю життєвого циклу зовнішніх ресурсів у Python використовують контекстні менеджери (`with` або `async with`) із явно визначеним методом `close()`. Якщо ж необхідний резервний механізм очищення на випадок, коли розробник забув закрити ресурс, надійним інструментом є `weakref.finalize`, який реєструє функцію очищення через слабке посилання, не блокуючи роботу cyclic GC і коректно функціонуючи під час shutdown інтерпретатора.

Демонстрація затримки виклику `__del__` у разі виникнення циклічного посилання:

```python
import gc

class BadResource:
    def __init__(self, name: str):
        self.name = name
        self.other = None

    def __del__(self):
        print(f"__del__ executed for {self.name}")

def create_cycle():
    a = BadResource("A")
    b = BadResource("B")
    a.other = b
    b.other = a
    # a and b go out of scope here, but refcounts remain 1 due to the cycle
    print("Scope exited, but finalizers have not run yet.")

create_cycle()
# Both resources are leaked until explicit or threshold cyclic GC runs
print("Triggering manual GC collection:")
gc.collect()

# Output:
# Scope exited, but finalizers have not run yet.
# Triggering manual GC collection:
# __del__ executed for A
# __del__ executed for B
```

**Архітектурні ризики та типові помилки використання `__del__`:**
- використання `__del__` замість контекстного менеджера: ресурси операційної системи (файлові дескриптори, мережеві сокети) вичерпуються раніше, ніж спрацьовує збирач сміття;
- блокування та deadlocks у багатопотокових додатках: `__del__` може бути викликаний довільним потоком у непередбачуваній точці виконання програми;
- воскресіння об'єкта (object resurrection): збереження посилання на `self` під час роботи `__del__` повертає об'єкт до життя у нестабільному стані.

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
