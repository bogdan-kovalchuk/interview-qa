---
id: py-async-0021
title: "Чому конкурентні coroutines можуть мати race condition на shared state навіть у одному OS thread?"
description: "Тому що await є точкою добровільної поступки: event loop може перемкнути виконання на іншу Task, і та побачить проміжний стан shared resource."
track: python
section: asyncio
level: middle
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/async.md#L1141-L1186
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Тому що `await` є точкою добровільної поступки: event loop може перемкнути виконання на іншу Task, і та побачить проміжний стан shared resource.**[^py314-library-asyncio-task] У CPython event loop kooperативно планує задачі: поки Task не виконає `await`, жодна інша Task у тому самому thread не працює. Але як тільки coroutine робить `await` (наприклад, на I/O чи `asyncio.sleep`), loop передає керування іншій Task, яка може змінити спільний словник, лічильник чи список до того, як перша Task продовжить роботу. Рішення – використовувати `asyncio.Lock` навколо критичних секцій або проектувати код так, щоб між `await`-точками стан залишався консистентним.

## Detailed explanation

Ключова відмінність від race condition між OS threads: тут перемикання може статися лише в точці
`await`, а не в довільному місці, тому пряма лінія коду без жодного `await` завжди виконується
атомарно відносно інших Task. Це звужує поверхню проблеми, але не усуває її: класичний приклад –
«перевір, потім дій» (check-then-act) над спільним ресурсом, коли перевірка та дія розділені
`await`:

```python
if balance >= amount:
    await ledger.write(amount)   # інша Task встигає списати тут
    balance -= amount
```

Якщо між перевіркою `balance >= amount` і фактичним списанням є `await ledger.write(...)`, інша
Task може встигнути виконати той самий блок і теж пройти перевірку зі старим значенням `balance`,
після чого обидві спишуть кошти, хоча сумарно їх могло не вистачати.[^py314-library-asyncio-dev]

На відміну від race condition між потоками, тут порядок перемикань не є довільним у сенсі
апаратних гонок – він детермінований відносно того, які callbacks стали ready і в якому порядку.
Але для викликача це однаково виглядає як недетермінізм, бо порядок готовності залежить від
зовнішніх факторів (наприклад, коли саме прийшла відповідь мережі), а не від порядку рядків коду.

Найнадійніший спосіб уникнути проблеми – тримати критичну секцію, що містить і перевірку, і зміну
стану, без жодного `await` усередині; якщо `await` неминучий (наприклад, потрібен I/O для запису),
секцію треба огорнути в `asyncio.Lock`, щоб інші Task чекали звільнення, а не проходили паралельно
той самий блок.

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
