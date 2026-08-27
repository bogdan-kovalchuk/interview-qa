---
id: py-coll-0008
title: "Чим `d[key]`, `d.get(key)` і `setdefault()` відрізняються за поведінкою при відсутньому key та можливими side effects?"
description: "d[key] викликає KeyError; d.get(key) повертає None (або переданий default) без побічних ефектів; d.setdefault(key, default) вставляє default у словник, якщо ключ відсутній, і повертає його."
track: python
section: collections
level: middle
type: comparison
tags: [d-key, d-get-key, setdefault]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L118-L138
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`d[key]` викликає `KeyError`; `d.get(key)` повертає `None` (або переданий default) без побічних ефектів; `d.setdefault(key, default)` вставляє `default` у словник, якщо ключ відсутній, і повертає його.**[^py314-library-stdtypes] Метод <span class="warn">`setdefault()` завжди обчислює аргумент `default`, навіть коли ключ існує – це може бути небажаним side effect, якщо створення default дороге.</span>

## Detailed explanation

`d[key]` реалізовано через `__getitem__`, який при відсутньому ключі викликає гачок `__missing__`
замість того, щоб одразу кидати `KeyError` напряму.[^py314-library-stdtypes] Базовий `dict` визначає
`__missing__` так, що він просто кидає `KeyError`, але саме цей гачок і робить можливим
`collections.defaultdict`: він перевизначає `__missing__` так, щоб той викликав `default_factory()`,
вставляв результат у словник під цим ключем і повертав його. Тобто `d[key]` для `defaultdict` – це
не інша операція, а той самий протокол з іншою реалізацією гачка.

`d.get(key, default)` не використовує `__missing__` узагалі: це метод, який сам перевіряє
наявність ключа і повертає готове значення `default` без запису в словник і без жодної мутації –
найбезпечніший варіант для read-only доступу, коли відсутність ключа – нормальний, очікуваний
випадок.

`d.setdefault(key, default)` поєднує читання й потенційний запис, але з важливою пасткою: вираз
`default` обчислюється при кожному виклику, ще до перевірки наявності ключа. У поширеному
патерні групування `d.setdefault(key, []).append(x)` це означає, що новий порожній список
створюється на кожному виклику, навіть коли ключ уже є і цей список одразу викидається як
непотрібний. Для дешевого `default` (число, `None`) це неважливо, але для дорогого – це зайва
робота на кожен виклик, а не лише на перший.

Саме тому для патерну "groupby в dict" `collections.defaultdict(list)` зазвичай кращий за
`setdefault`: `default_factory()` викликається лише всередині `__missing__`, тобто рівно тоді,
коли ключа справді немає, а не на кожному зверненні. Синтаксично обидва підходи виглядають
однаково компактно, але семантично `defaultdict` уникає зайвого створення об'єкта на "гарячому"
шляху, коли ключ уже існує.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
