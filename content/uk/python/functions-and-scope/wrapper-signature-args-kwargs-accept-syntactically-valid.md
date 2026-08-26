---
id: py-funcs-0005
title: "Чому wrapper із сигнатурою `(*args, **kwargs)` може прийняти синтаксично коректний виклик, який потім відхилить обгорнута функція, і на якому етапі виникає `TypeError`?"
description: "Wrapper (*args,"
track: python
section: functions-and-scope
level: senior
type: mechanism
tags: [args-kwargs, typeerror]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-reference-expressions-calls
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#calls
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-inspect-inspect-signature
    title: "Python 3.14: Library/inspect"
    url: https://docs.python.org/3.14/library/inspect.html#inspect.signature
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functions.md#L35-L93
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Wrapper `(*args, **kwargs)` приймає будь-яку комбінацію аргументів, тому перевірка сигнатури відбувається лише на етапі виклику обгорнутої функції.**[^py314-reference-expressions-calls] Наприклад, якщо внутрішня функція має сигнатуру `def inner(a, b)`, а wrapper викликають `wrapper(1, 2, 3)`, wrapper успішно зв'яже `args = (1, 2, 3)`, але розпакування `inner(*args)` дасть `TypeError: inner() takes 2 positional arguments but 3 were given`. Помилка виникає всередині wrapper, у момент виклику inner, а не на вході wrapper.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
