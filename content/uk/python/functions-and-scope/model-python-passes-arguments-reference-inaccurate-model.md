---
id: py-funcs-0010
title: "Чому модель «Python передає аргументи за посиланням» неточна, і яка модель коректно пояснює одночасно rebinding та mutation параметра?"
description: "Коректна модель – pass by assignment (pass by object reference): параметр отримує посилання на той самий об'єкт, але не є alias змінної викликача."
track: python
section: functions-and-scope
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-faq-programming-how-do-i-write-a-function-with-output
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functions.md#L373-L421
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Коректна модель – `pass by assignment` (pass by object reference): параметр отримує посилання на той самий об'єкт, але не є alias змінної викликача.**[^py314-faq-programming-how-do-i-write-a-function-with-output] Rebinding параметра (`x = new_value`) змінює лише локальне зв'язування й не впливає на викликача. Mutation (`x.append(v)`) змінює спільний об'єкт, що видно обом сторонам. Модель «pass by reference» не пояснює rebinding, а «pass by value» не пояснює mutation – pass by assignment пояснює обидва випадки.

## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
