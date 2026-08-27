---
id: py-coll-0021
title: "Коли key function у `sorted()` краща за реалізацію rich comparison methods у domain class?"
description: "Key function краща, коли порядок сортування залежить від контексту або зовнішніх даних, а не від природного порядку самого класу."
track: python
section: collections
level: senior
type: comparison
tags: [sorted]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-sorting
    title: "Python 3.14: Howto/sorting"
    url: https://docs.python.org/3.14/howto/sorting.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Key function краща, коли порядок сортування залежить від контексту або зовнішніх даних, а не від природного порядку самого класу.**[^py314-library-stdtypes] Rich comparison methods (наприклад, `__lt__`) визначають єдиний канонічний порядок класу; key function дозволяє сортувати за будь-яким похідним ключем без зміни класу. Наприклад, `sorted(users, key=lambda u: scores[u.id])` сортує за зовнішнім словником, що неможливо виразити через `__lt__`.

## Detailed explanation

Rich comparison прив'язує порядок до самого класу: `__lt__` – це одна, канонічна відповідь на
питання "що менше". Якщо потрібно сортувати тих самих `User` то за `age`, то за `name`, то за
`score` із зовнішнього словника, довелося б або тримати кілька версій `__lt__` (неможливо – метод
один), або перемикати стан класу перед кожним сортуванням, що і крихко, і не thread-safe. Key
function знімає це обмеження: кожен виклик `sorted(data, key=...)` несе власну, локальну для цього
виклику логіку порядку, і клас узагалі не повинен знати про існування такого порядку.

Продуктивність теж на користь key function, коли обчислення ключа дороге: `sorted()` викликає
`key(x)` рівно один раз для кожного елемента (це відомо як decorate-sort-undecorate, або
Schwartzian transform), а потім порівнює вже готові ключі. Якби порядок задавався через `__lt__`,
та сама дорога логіка виконувалася б повторно при кожному парному порівнянні під час сортування –
O(n log n) разів замість O(n).[^py314-howto-sorting]

Key function – єдиний спосіб відсортувати дані, які не є екземплярами власного класу і не можуть
отримати `__lt__` (наприклад, `dict`, `tuple` із зовнішнього джерела, чи об'єкти сторонньої
бібліотеки): `sorted(records, key=lambda r: r["score"])` працює без жодної зміни типу `records`.

Rich comparison, натомість, виправданий, коли в домені дійсно існує один природний, стабільний
порядок, що є частиною сенсу самого типу – наприклад, `Decimal` чи `datetime`, де "менше" означає
одне й те саме в будь-якому контексті використання; тоді `__lt__` (разом із `functools.total_ordering`,
щоб не писати всі шість методів вручну) робить порядок частиною публічного API типу, а не
деталлю окремого виклику `sorted()`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
