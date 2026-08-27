---
id: py-async-0005
title: "Що робить asyncio Task або callback ready після I/O, timer чи suspension point і яких fairness та exact-order guarantees application code не має припускати?"
description: "Event loop виконує готові callback у порядку FIFO для call_soon, але порядок timer-callbackів з однаковим часом є невизначеним, а строгих fairness-гарантій між Tasks немає."
track: python
section: asyncio
level: middle
type: mechanism
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L204-L259
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Event loop виконує готові callback у порядку FIFO для `call_soon`, але порядок timer-callbackів з однаковим часом є невизначеним, а строгих fairness-гарантій між Tasks немає.**[^py314-library-asyncio-task] Коли I/O завершується або спливає timer, loop додає відповідний callback у ready-чергу. Callbacks, зареєстровані через `call_soon`, викликаються в порядку реєстрації. Проте для `call_later` / `call_at` з однаковим timestamp порядок не гарантовано. Task, яка не поступається керуванням через `await`, може відкладати інші Tasks на невизначений час.

## Detailed explanation

Усередині loop на кожній ітерації робить дві речі: опитує selector (`epoll`/`kqueue`/`select` –
залежно від ОС) із timeout до найближчого запланованого timer, і переносить у ready-чергу callbacks
для file descriptors, що стали готові, а також ті timers з внутрішньої heap, чий час уже
настав.[^py314-library-asyncio-eventloop] Тільки після цього loop послідовно виконує все, що
накопичилось у ready-черзі на цей момент.

Резюм Task після `await` теж проходить через цей самий механізм, а не якийсь окремий "task
scheduler". Коли Task призупиняється на Future, вона реєструє на цьому Future callback через
`add_done_callback`. Коли Future отримує результат (наприклад, I/O завершилось), викликається цей
callback, який просто ставить продовження Task у ready-чергу через `call_soon()`. Тобто "чекаюча"
Task – це просто callback, підвішений на подію, а не окрема сутність із власним пріоритетом.

Звідси й межі fairness. Ready-черга не знає, скільки часу Task уже чекала чи наскільки вона
"термінова" – єдиний критерій порядку виконання це FIFO-позиція в черзі callbacks на цю ітерацію.
Дві Tasks, розбуджені в одній ітерації, виконаються в порядку, в якому їхні `call_soon()`
відбулися, а не в порядку створення чи важливості. А для timers з однаковим `deadline` порядок
залежить від внутрішньої реалізації heap (порівняння за порядком вставки як tie-breaker не
гарантовано специфікацією).[^py314-library-asyncio-eventloop] Це означає, що код не має права
припускати ні "round-robin по Tasks", ні "перший запланований timer виконається першим при рівних
часах" – єдина тверда гарантія: callbacks, поставлені через `call_soon`, виконуються в порядку
виклику `call_soon`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
