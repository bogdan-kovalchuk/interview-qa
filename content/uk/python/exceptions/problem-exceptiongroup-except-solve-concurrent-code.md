---
id: py-excpt-0012
title: "Яку проблему вирішують `ExceptionGroup` та `except*` у concurrent code?"
description: "ExceptionGroup дозволяє підняти кілька незалежних exception одночасно, а except* – вибірково обробити потрібні типи, не втрачаючи решти."
track: python
section: exceptions
level: middle
type: mechanism
tags: [exceptiongroup]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-asyncio-task-taskgroup
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: TaskGroup збирає помилки задач в ExceptionGroup, а KeyboardInterrupt і SystemExit піднімаються без групи."
  - source_id: py314-library-asyncio-task-gather
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#asyncio.gather
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: при return_exceptions=False (за замовчуванням) першу помилку отримує той, хто чекає gather(); решта до нього не передається."
  - source_id: py314-reference-compound-stmts-except-star
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#except-star
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: семантика except*, розщеплення групи та передача необробленої частини далі."
  - source_id: pep-0654-exception-groups
    title: "PEP 654: Exception Groups and except*"
    url: https://peps.python.org/pep-0654/
    accessed: 2026-10-13
    kind: spec
    version: "3.11"
    applicability: "PEP 654: ExceptionGroup і except* запропоновано для Python 3.11 (Python-Version: 3.11)."
---

## Short answer

**`ExceptionGroup` дозволяє підняти кілька не пов’язаних exception одночасно, а `except*` – вибірково обробити потрібні типи, не втрачаючи решти.**[^py314-tutorial-errors] У concurrent code, наприклад у `asyncio.TaskGroup`, кілька задач можуть впасти з різними exception. Один `raise` передає лише один exception, тому група збирає їх в один об’єкт, а `except*` розщеплює її за типом і обробляє кожну підгрупу окремо.[^py314-library-asyncio-task-taskgroup]

## Detailed explanation

Звичайний `raise` передає обробнику один exception. Коли кілька паралельних задач падають одночасно, це типова ситуація для concurrency-фреймворків: у документації Python прямо сказано, що в такому випадку варто зібрати всі помилки, а не піднімати лише першу.[^py314-tutorial-errors] Наприклад, `asyncio.gather()` без `return_exceptions=True` передає викликачу першу помилку, а решта до нього не доходить.[^py314-library-asyncio-task-gather]

`ExceptionGroup(msg, excs)` (з Python 3.11) вирішує це як звичайний exception, що містить список інших.[^pep-0654-exception-groups] Вкладені exceptions доступні тільки для читання через поле `exceptions`.[^py314-library-exceptions] `ExceptionGroup` є підкласом `Exception`, тож `except Exception` його ловить, а `except ValueError` – ні, бо сама група не є `ValueError`.[^py314-library-exceptions] `asyncio.TaskGroup` використовує ту саму форму: коли всі задачі завершились і частина з них упала з виключенням, відмінним від `CancelledError`, він піднімає `ExceptionGroup` з цими помилками. `KeyboardInterrupt` і `SystemExit` він піднімає повторно як є, без групи.[^py314-library-asyncio-task-taskgroup]

Нижче три задачі: дві падають з `ValueError`, одна з `KeyError`. Кожен `except*` отримує свою підгрупу:

```python
import asyncio

async def fail(n):
    await asyncio.sleep(0)
    raise ValueError(f"task {n} failed")

async def bad_key():
    await asyncio.sleep(0)
    raise KeyError("missing")

async def main():
    try:
        async with asyncio.TaskGroup() as tg:
            tg.create_task(fail(1))
            tg.create_task(fail(2))
            tg.create_task(bad_key())
    except* ValueError as eg:
        print("ValueError group:", eg.exceptions)
    except* KeyError as eg:
        print("KeyError group:", eg.exceptions)

asyncio.run(main())

# ValueError group: (ValueError('task 1 failed'), ValueError('task 2 failed'))
# KeyError group: (KeyError('missing'),)
```

Групу варто застосовувати, коли кілька помилок є справжніми незалежними результатами і кожну треба обробити. Якщо помилка одна, звичайний exception простіший.

**Типові помилки:**
- очікувати, що `except ValueError` спіймає помилку всередині групи: групу обробляють через `except*` або через `except ExceptionGroup`;
- змішувати `except` і `except*` в одному `try` – це синтаксична помилка;[^py314-reference-compound-stmts-except-star]
- логувати групу через `str(eg)`: це показує повідомлення групи й кількість вкладених exception (наприклад, `there were problems (2 sub-exceptions)`), але не їхні типи й повідомлення.[^py314-tutorial-errors]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
