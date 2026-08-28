---
id: py-fund-0006
title: "Як відрізнити гарантію мови Python від особливості конкретної реалізації на прикладі memory management або bytecode?"
description: "Потрібно шукати правило в Python Language Reference і перевіряти, чи документація не позначає його як implementation detail."
track: python
section: fundamentals
level: middle
type: practical
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
    version: null
anki:
  export: true
sources:
  - source_id: py314-reference-executionmodel
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-faq-general
    title: "Python 3.14: Faq/general"
    url: https://docs.python.org/3.14/faq/general.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L3-L26
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Потрібно шукати правило в Python Language Reference і перевіряти, чи документація не позначає його як implementation detail.**[^py314-reference-executionmodel] Наприклад, наявність у кожного об’єкта identity, type і value є частиною data model, а адреса пам’яті як результат `id()` та формат bytecode прямо описані як деталі CPython. Код не повинен будувати переносиму логіку на таких деталях.

## Detailed explanation

Гарантія мови – це правило, записане в Python Language Reference: будь-яка реалізація мусить його
дотримуватися, інакше вона не Python. Деталь реалізації – це те, як конкретно CPython вирішив
виконати правило; інша реалізація має право зробити інакше.[^py314-reference-executionmodel]

Практичний спосіб перевірки – текстовий. Знайти твердження в Language Reference або в описі типу в
стандартній бібліотеці, і подивитися, чи не стоїть поруч застереження на кшталт «CPython
implementation detail». Такі місця позначені прямо, і саме вони – межа переносимості.

Корисно тримати в голові кілька контрастних пар. Гарантія: кожен об'єкт має identity, type і value, а
`id()` повертає стале унікальне число протягом життя об'єкта. Деталь: що це число – адреса в пам'яті,
і що малі цілі кешуються, тому `a is b` часто істинне.[^py314-reference-datamodel]

```python
x = 256
y = 256
x is y            # True in CPython - small-int cache, an implementation detail

x = 257
y = 257
x is y            # False in CPython - and either result is valid per the language

x == y            # True - this is the guarantee, and the only thing to rely on
```

Ще одна пара: гарантія – що `dict` зберігає порядок вставляння (з 3.7 це частина мови). Деталь – як
саме він це робить усередині та скільки пам'яті займає. І ще одна: гарантія – що `with` викличе
`__exit__` на виході з блоку; деталь – що в CPython об'єкт без посилань зникає негайно завдяки
reference counting.

**Практичні орієнтири, коли документація під рукою не допомагає:**
- поведінка описана в Language Reference або в PEP, який її вводив – це гарантія;
- поведінку видно лише через `dis`, `sys.getrefcount`, `id()` або розмір об'єкта – це деталь;
- модуль називається `_something` або документований як внутрішній – це деталь;
- поведінка змінювалася між мінорними версіями без запису в «Deprecations» – майже напевно
  деталь.[^py314-faq-general]

Найпростіша перевірка на здоровий глузд: чи має право PyPy зробити це інакше і лишитися Python? Якщо
так – ви спираєтеся на деталь реалізації.

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
