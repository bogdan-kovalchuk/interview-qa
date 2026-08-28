---
id: py-ctxmgr-0009
title: "Як `__aexit__` має завершити cleanup після `CancelledError`, не поглинувши cancellation завдання?"
description: "__aexit__ має виконати cleanup і потім або не перехоплювати CancelledError, або повторно її підняти, щоб cancellation дійшла до завдання."
track: python
section: context-managers
level: senior
type: practical
tags: [aexit, cancellederror]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel-with-statement-context-managers
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#with-statement-context-managers
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-contextlib
    title: "Python 3.14: Library/contextlib"
    url: https://docs.python.org/3.14/library/contextlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-asyncio-task-task-cancellation
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#task-cancellation
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`__aexit__` має виконати cleanup і потім або не перехоплювати `CancelledError`, або повторно її підняти, щоб cancellation дійшла до завдання.**[^py314-reference-datamodel-with-statement-context-managers] `CancelledError` успадковує від `BaseException`, тому звичайний `except Exception` її не зловить. <span class="warn">Якщо код навмисно подавляє `CancelledError`, він зобов'язаний викликати `Task.uncancel()`, інакше structured concurrency (TaskGroup, timeout) працюватиме некоректно.</span> Загальне правило: cleanup -> re-raise.

## Detailed explanation

`CancelledError` – це виняток, яким asyncio сигналізує coroutine про потребу зупинитися; він
приходить у `__aexit__` так само, як будь-яка інша помилка, через параметри `exc_type`, `exc_val`
і `exc_tb`.[^py314-reference-datamodel-with-statement-context-managers]

Головна пастка – `CancelledError` успадковує `BaseException`, а не
`Exception`.[^py314-library-asyncio-task-task-cancellation] Тому `except Exception` його не ловить,
і cleanup-код, написаний "як завжди", коректно пропускає скасування далі. Проблема виникає, коли
`__aexit__` явно ловить ширший виняток (`except BaseException` або голий `except:`) заради cleanup –
тоді він зобов'язаний виконати потрібні дії і одразу підняти виняток повторно (`raise`), інакше
cancellation завдання буде "проковтнуте", і задача продовжить виконання, ніби нічого не відбулося.

Безпечний патерн – виконати cleanup у `try`, а `CancelledError` не перехоплювати або підняти
повторно:

```python
async def __aexit__(self, exc_type, exc_val, exc_tb):
    try:
        await self.conn.close()
    except asyncio.CancelledError:
        # cleanup already ran above; re-raise so cancellation reaches the task
        raise
```

Якщо cleanup сам виконує await-виклики, вони теж можуть отримати `CancelledError` – огортання в
`try/finally` гарантує, що ресурс закриється навіть тоді, коли скасування прийшло саме під час
закриття.

Якщо код навмисно вирішує подавити скасування (наприклад, `__aexit__` повертає truthy значення),
він зобов'язаний викликати `task.uncancel()`, бо `asyncio.TaskGroup` і `asyncio.timeout()`
рахують кількість активних cancellation-запитів і без цього виклику вважатимуть задачу досі
скасованою.[^py314-library-asyncio-task-task-cancellation]

**Типові помилки з `__aexit__` і скасуванням:**
- ловити `CancelledError` через `except Exception`, вважаючи, що це звичайний виняток;
- перехопити `CancelledError` заради cleanup і забути `raise`, через що скасування губиться;
- подавити `CancelledError` (`return True`) без виклику `task.uncancel()`, ламаючи облік у
  `TaskGroup`.

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
