---
id: py-async-0004
title: "Чому для fire-and-forget Task потрібно зберігати strong reference та явно обробляти outcome?"
description: "Event loop зберігає лише weak references на Tasks, тому Task без зовнішнього посилання може бути знищена GC до завершення."
track: python
section: asyncio
level: senior
type: pitfall
tags: []
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L665-L745
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Event loop зберігає лише weak references на Tasks, тому Task без зовнішнього посилання може бути знищена GC до завершення.**[^py314-library-asyncio-task] Якщо Task завершується з exception і ніхто не читає результат, Python видасть <span class="warn">«Task exception was never retrieved»</span>. Стандартний патерн – зберігати Tasks у `set` і прибирати посилання через `add_done_callback`, або використовувати `TaskGroup`, який автоматично тримає strong references.

## Detailed explanation

Це свідомий вибір дизайну, а не недогляд: якби loop сам тримав strong reference на кожну створену
Task, довгоживучий процес, що постійно робить `create_task()` для fire-and-forget роботи, ніколи б
не звільняв пам'ять цих Tasks, навіть після їхнього завершення.[^py314-library-asyncio-eventloop]
Тому відповідальність за lifetime Task свідомо покладена на код, який її створив.

Момент, коли GC знищує Task, має значення для того, яке саме попередження побачить розробник. Якщо
Task знищується, ще не завершившись (немає жодного strong reference, а вона все ще pending), Python
видає інше попередження – «Task was destroyed but it is pending!» – і робота, яку вона мала
зробити, просто обривається на середині. Якщо ж Task встигла завершитися з exception до знищення,
спрацьовує саме `__del__` Task, який перевіряє, чи exception був прочитаний через `.result()` або
`.exception()`, і якщо ні – друкує «Task exception was never retrieved» у обробник exception
loop.[^py314-library-asyncio-task]

Ідіоматичний патерн, рекомендований документацією, – тримати всі fire-and-forget Tasks у
module-level `set` і видаляти посилання лише після завершення:

```python
background_tasks: set[asyncio.Task] = set()
task = asyncio.create_task(worker())
background_tasks.add(task)
task.add_done_callback(background_tasks.discard)
```

`add_done_callback` тут не для обробки результату, а лише для очищення набору – сам callback
викликається loop-ом уже після завершення Task, коли зберігати посилання більше не потрібно.

`TaskGroup` вирішує цю саму проблему структурно: він сам тримає strong references на всі свої
children, поки `async with` блок не завершиться, і саме тому там неможливо випадково "загубити"
Task – lifetime Task жорстко прив'язаний до lifetime блоку.

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
