---
id: py-async-0022
title: "Як вибрати між `asyncio.Lock`, `Event`, `Condition` та `Semaphore` для coordination protocol?"
description: "Lock – взаємне виключення; Event – сигнал «щось сталося» багатьом Task; Condition – очікування зміни стану під захистом lock; Semaphore – обмеження кількості одночасних доступів."
track: python
section: asyncio
level: senior
type: comparison
tags: [asyncio-lock, event, condition, semaphore]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L1141-L1186
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`Lock` – взаємне виключення; `Event` – сигнал «щось сталося» багатьом Task; `Condition` – очікування зміни стану під захистом lock; `Semaphore` – обмеження кількості одночасних доступів.**[^py314-library-asyncio-task] `Lock` підходить, коли одна Task наразі модифікує спільний ресурс. `Event` – коли одна Task має повідомити іншим про готовність (наприклад, ініціалізацію), а `set()` залишається до `clear()`. `Condition` потрібен, якщо Task має чекати певної умови над ресурсом і одразу після пробудження отримати ексклюзивний доступ – типовий producer/consumer. `Semaphore(N)` обмежує N одночасних користувачів ресурсу (connection pool, throttle API-запитів).

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
