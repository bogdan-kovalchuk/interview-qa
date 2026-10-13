---
id: py-excpt-0003
title: "Коли перехоплення `BaseException` може зламати graceful shutdown або cancellation semantics?"
description: "except BaseException перехоплює SystemExit, KeyboardInterrupt, GeneratorExit і asyncio.CancelledError: без raise процес не завершиться через sys.exit() чи Ctrl-C, а скасування task-и проковтується."
track: python
section: exceptions
level: senior
type: pitfall
tags: [baseexception]
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
  - source_id: py314-library-asyncio-task-task-cancellation
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#task-cancellation
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: CancelledError напряму наслідує BaseException; TaskGroup і asyncio.timeout() можуть працювати некоректно, якщо coroutine проковтує CancelledError; CancelledError зазвичай піднімають знову після cleanup."
  - source_id: py314-library-asyncio-task-cancel-method
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task.cancel
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: Task.cancel() не гарантує скасування, якщо coroutine придушує виняток; придушення активно не рекомендується і потребує виклику Task.uncancel()."
  - source_id: py314-reference-expressions-generator-iterator-methods
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#generator-iterator-methods
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: generator.close() піднімає GeneratorExit у точці паузи; якщо генератор не перехоплює його, close() повертається без помилки; якщо генератор yield-ить значення, close() піднімає RuntimeError."
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: якщо генератор фіналізується без відновлення, викликається close(), що дозволяє виконатися відкладеним finally-блокам."
---

## Short answer

**`except BaseException` перехоплює `SystemExit`, `KeyboardInterrupt` і `GeneratorExit`; якщо handler не re-raise-ить виняток, процес не завершиться через `sys.exit()` або Ctrl-C.**[^py314-library-exceptions] `asyncio.CancelledError` теж наслідує `BaseException`, тож handler без `raise` мовчки проковтує скасування task-и.[^py314-library-asyncio-task-task-cancellation] <span class="warn">Якщо перехоплений `GeneratorExit` змусити yield-ити значення, `.close()` генератора завершиться помилкою `RuntimeError`.</span>[^py314-reference-expressions-generator-iterator-methods] Такий handler доречний тоді, коли після cleanup виняток піднімається знову, наприклад на верхньому рівні програми.

## Detailed explanation

`Exception` є підкласом `BaseException`, але `SystemExit` і `KeyboardInterrupt` наслідують `BaseException` напряму, щоб код, який ловить `Exception`, не перехоплював запит на завершення; `GeneratorExit` – бо технічно це не помилка. Тому `sys.exit()` і Ctrl-C піднімаються до interpreter-а й завершують процес.[^py314-library-exceptions]

Якщо `except BaseException` не піднімає виняток знову, `sys.exit()` перестає завершувати програму, а Ctrl-C ніби не спрацьовує. Для `GeneratorExit` є своя пастка. `generator.close()` піднімає його в точці паузи. Якщо генератор його не перехоплює, `close()` тихо повертається, а `finally`-блоки виконуються.[^py314-reference-expressions-yield-expressions][^py314-reference-expressions-generator-iterator-methods] Якщо ж handler yield-ить значення, `close()` піднімає `RuntimeError`:

```python
def reader():
    try:
        yield "line 1"
    except BaseException:       # catches the GeneratorExit raised by close()
        yield "cleanup"         # yielding here makes close() fail

gen = reader()
next(gen)
try:
    gen.close()
except RuntimeError as error:
    print(error)                # generator ignored GeneratorExit
```

`asyncio.CancelledError` теж наслідує `BaseException` напряму, тому `except BaseException` без `raise` мовчки проковтує скасування task-и.[^py314-library-asyncio-task-task-cancellation] Документація `Task.cancel()` попереджає, що скасування не гарантоване, якщо coroutine придушує виняток.[^py314-library-asyncio-task-cancel-method] `TaskGroup` і `asyncio.timeout()` покладаються на cancellation і можуть працювати некоректно, якщо її проковтнути.[^py314-library-asyncio-task-task-cancellation] Приклад:

```python
import asyncio

async def worker():
    try:
        await asyncio.sleep(10)
    except BaseException:       # swallows CancelledError
        return "finished"

async def main():
    task = asyncio.create_task(worker())
    await asyncio.sleep(0)      # let the task reach sleep()
    task.cancel()
    print(await task)           # finished
    print(task.cancelled())     # False: the cancellation was swallowed

asyncio.run(main())
```

Якщо cancellation придушують свідомо, потрібно ще викликати `Task.uncancel()`; придушення прямо не рекомендується.[^py314-library-asyncio-task-cancel-method] Правильний шаблон – cleanup, а потім `raise`.[^py314-library-asyncio-task-task-cancellation]

**Типові помилки:**
- писати `except BaseException` замість `except Exception`, хоча потрібен лише `Exception`;
- ловити `BaseException` без `raise` у coroutine, яку мають скасувати `TaskGroup` або `asyncio.timeout()`;
- yield-ити значення з handler-а `GeneratorExit` і очікувати, що `close()` пройде без помилки.

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
