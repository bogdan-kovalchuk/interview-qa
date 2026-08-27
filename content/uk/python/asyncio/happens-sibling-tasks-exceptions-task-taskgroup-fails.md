---
id: py-async-0010
title: "Що відбувається з sibling Tasks та exceptions, коли одна Task у `TaskGroup` падає?"
description: "Якщо будь-яка Task у TaskGroup завершується з exception (окрім CancelledError), усі sibling Tasks скасовуються, а всі exception агрегуються в ExceptionGroup, який піднімається при виході з context manager."
track: python
section: asyncio
level: middle
type: mechanism
tags: [taskgroup]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-asyncio-task
    title: "Python 3.14: Library/asyncio Task"
    url: https://docs.python.org/3.14/library/asyncio-task.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-asyncio-eventloop
    title: "Python 3.14: Library/asyncio Eventloop"
    url: https://docs.python.org/3.14/library/asyncio-eventloop.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-asyncio-dev
    title: "Python 3.14: Library/asyncio Dev"
    url: https://docs.python.org/3.14/library/asyncio-dev.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L746-L791
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Якщо будь-яка Task у `TaskGroup` завершується з exception (окрім `CancelledError`), усі sibling Tasks скасовуються, а всі exception агрегуються в `ExceptionGroup`, який піднімається при виході з context manager.**[^py314-library-asyncio-task] Нові Tasks після першого збою додати не можна. `KeyboardInterrupt` і `SystemExit` піднімаються одразу без агрегації. Якщо тіло `async with` саме кидає exception, воно теж включається до фінального `ExceptionGroup`.

## Detailed explanation

Послідовність подій усередині `TaskGroup` фіксована. Щойно перша child Task падає з "справжнім"
exception (не `CancelledError`), group переходить у стан "aborting" і одразу викликає `.cancel()`
на кожній ще не завершеній sibling Task.[^py314-library-asyncio-task] Після цього `__aexit__`
чекає, поки геть усі children фактично завершаться – і скасовані, і та, що впала першою, – перш ніж
вирішувати, що піднімати далі.

Важливо, що скасування siblings не гарантує "тихого" завершення: Task, яку скасували, може
перехопити `CancelledError` у `try/except` і замість повторного `raise` кинути щось інше під час
cleanup. Таке "друге" exception теж потрапляє до фінального `ExceptionGroup`, тому набір зібраних
exception може бути більшим за один. А ось сам `CancelledError`, який виникає в sibling саме
внаслідок скасування з боку group, до `ExceptionGroup` не додається – це очікуваний, а не
аварійний результат.

`TaskGroup` навмисно піднімає `ExceptionGroup` (PEP 654), а не просто перше exception, як робить
`gather()` за замовчуванням: якщо впало кілька Tasks одночасно (наприклад, дві з них звертались до
одного недоступного сервісу), розробник бачить усі причини одразу, а не лише ту, що встигла
першою. Обробляти такий результат треба через `except*`, а не звичайний `except`, бо `ExceptionGroup`
не є прямим instance жодного окремого типу exception усередині нього.

Стан "aborting" також блокує подальше `create_task()` на цій самій group – спроба додати нову Task
після початку скасування піднімає `RuntimeError`, бо group більше не гарантує, що встигне дочекатися
й скасувати щось, додане після старту завершення.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
