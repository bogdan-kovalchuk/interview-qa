---
id: py-decor-0011
title: "Як decorator для `async def` має зберегти awaitability та коректне поширення exceptions?"
description: "Wrapper має бути оголошений через async def і використовувати await для виклику оригінальної корутини – це зберігає awaitability та природне поширення exceptions."
track: python
section: decorators
level: senior
type: mechanism
tags: [async-def]
status: published
updated: 2026-09-13
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-glossary-term-decorator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-decorator
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/decorators.md#L279-L322
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Wrapper має бути оголошений через `async def` і викликати оригінальну корутину через `await` – це зберігає awaitability та природне поширення exceptions.**[^py314-glossary-term-decorator] Якщо wrapper написати як звичайну `def`, виклик decorated функції поверне не-awaited coroutine object замість реального результату, а `inspect.iscoroutinefunction()` для такої функції покаже `False`. Щоб один декоратор підтримував синхронні й асинхронні функції, тип перевіряють через `inspect.iscoroutinefunction()` і диспатчать на `async def wrapper` або `def wrapper`, застосовуючи `@functools.wraps(func)` для збереження метаданих. Exceptions поширюються через `await` природно: caller отримає той самий тип exception.
## Detailed explanation

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
