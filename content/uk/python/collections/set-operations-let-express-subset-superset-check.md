---
id: py-coll-0015
title: "Як set operations дозволяють виразити перевірку subset/superset без ручних nested loops?"
description: "Оператори <= (issubset) і >= (issuperset) виконують перевірку включення всіх елементів за один виклик, без явних циклів."
track: python
section: collections
level: middle
type: practical
tags: []
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L36-L70
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Оператори `<=` (`issubset`) і `>=` (`issuperset`) виконують перевірку включення всіх елементів за один виклик, без явних циклів.**[^py314-library-stdtypes] `a <= b` повертає `True`, якщо кожен елемент `a` міститься в `b`. Оператор `<` – strict (proper) subset: `a < a` дає `False`, тоді як `a <= a` – `True`. Це працює за O(len(a)) у середньому, бо кожен `in` для set – O(1).

## Detailed explanation

Ключова відмінність між методами (`issubset`, `issuperset`) і операторами (`<=`, `>=`) – у типі
допустимого аргумента. `a.issubset(b)` приймає будь-який iterable для `b` (список, кортеж,
генератор) і сам перетворює його на set перед перевіркою, тоді як оператор `a <= b` вимагає, щоб
`b` теж був set (або frozenset) – для довільного iterable він підійме `TypeError`, бо `<=`
визначений через `__le__`/`__ge__` саме для типу set, а не для протоколу iterable.[^py314-library-stdtypes]

Реалізаційно перевірка `a <= b` (subset) ітерує саме по `a` і для кожного елемента виконує `in b` –
членство в set-і O(1) у середньому, тому загальна складність O(len(a)), незалежно від розміру `b`.
Це асиметрично: `a <= b` і `b >= a` еквівалентні за результатом, але обидва виконують ітерацію по
меншому за семантикою операнду (`a`), а не по більшому.

Практична перевага перед ручними вкладеними циклами не лише в стислості запису, а й у складності:
наївна перевірка "кожен елемент a є в b" через вкладений цикл по списках дає O(len(a) * len(b)),
тоді як set-based перевірка – O(len(a)) завдяки хеш-таблиці всередині `b`.

Строгі варіанти `<` і `>` (proper subset/superset) додають умову нерівності множин: `a < b` істинне,
якщо `a <= b` і `a != b`. На відміну від `issubset`/`issuperset`, для строгих операторів немає
окремого методу – `a < b` доступне лише як оператор, а еквівалент через методи потрібно писати
вручну: `a.issubset(b) and a != b`.[^py314-library-collections]

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
