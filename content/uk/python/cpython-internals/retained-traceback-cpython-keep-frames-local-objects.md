---
id: py-cpyint-0005
title: "Чому retained traceback у CPython може утримувати frames та їх local objects після завершення function?"
description: "Traceback object містить tb_frame, який посилається на frame object, а frame.f_locals може містити exception object – утворюючи цикл: frame -> locals -> exception -> __traceback__ -> traceback -> frame."
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
---

## Short answer

**Traceback object містить `tb_frame`, який посилається на frame object, а frame.f_locals може містити exception object – утворюючи цикл: frame -> locals -> exception -> __traceback__ -> traceback -> frame.**[^py314-library-dis] Цей цикл не дозволяє reference counting звільнити об'єкти, тож frames та їх локальні змінні залишаються в пам'яті навіть після повернення з функції. Цикл зрештою прибере cyclic GC, або його можна розірвати явно через `frame.clear()`.

## Detailed explanation

Traceback об'єкт містить `tb_frame` – посилання на frame, у якому сталося виключення, а сам frame
через `f_locals` тримає посилання на всі локальні змінні цього виклику, включно, можливо, з самим
exception об'єктом.

Якщо exception об'єкт десь збережено – наприклад, у списку логів, у змінній поза `except`-блоком, чи
просто через `sys.exc_info()` – а в нього самого є атрибут `__traceback__`, що вказує назад на
traceback, утворюється цикл: `frame -> f_locals -> exception -> __traceback__ -> traceback ->
tb_frame -> frame`.[^py314-reference-datamodel-traceback-objects]

Доки цей цикл не звільнить cyclic garbage collector, кожен frame у ланцюжку – не лише той, де
стався except, а й усі "батьківські" frames по стеку викликів – та всі їхні локальні змінні
лишаються живими, навіть якщо відповідні функції вже давно повернулися. На практиці це може
утримувати живими великі об'єкти (наприклад, дескриптор з'єднання чи великий буфер), просто тому
що вони були локальною змінною десь у стеку на момент виключення.

Саме тому CPython з Python 3.0 автоматично видаляє змінну з `except ... as e:` наприкінці
except-блоку – це розриває один з найчастіших джерел такого циклу, коли сам обробник тримає `e`
довше, ніж потрібно.

```python
try:
    raise ValueError("boom")
except ValueError as exc:
    saved = exc  # keeps exc.__traceback__ -> frame -> f_locals -> exc alive

# saved now holds a reference cycle through its own __traceback__
```

**Типові помилки:**
- зберігати виключення (`sys.exc_info()`, `logging.exception`, власний список помилок), не
  розуміючи, що це продовжує життя всього стеку frames;
- вважати `except Exception as e: ...` завжди безпечним, ігноруючи випадок, коли `e` явно
  копіюється у зовнішню змінну;
- дивуватися, чому пам'ять не звільняється одразу після обробленого виключення, замість перевірки
  на reference cycles через `gc`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
