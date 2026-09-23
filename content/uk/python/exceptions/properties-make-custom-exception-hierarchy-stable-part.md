---
id: py-excpt-0010
title: "Які властивості роблять custom exception hierarchy стабільною частиною library API?"
description: "Базовий клас, що успадковується від Exception, з ієрархією підкласів для різних категорій помилок, і достатньо специфічні імена для точного catching."
track: python
section: exceptions
level: middle
type: practical
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
anki:
  export: true
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Базовий клас, що успадковується від `Exception`, з ієрархією підкласів для різних категорій помилок, і достатньо специфічні імена для точного catching.**[^py314-tutorial-errors] Стабільна ієрархія дозволяє споживачам перехоплювати на потрібному рівні абстракції: загальний базовий клас для всієї бібліотеки, проміжні класи для категорій (наприклад, `ConnectionError`, `ValidationError`), і конкретні класи для окремих умов. Кожен клас має нести достатньо контексту в атрибутах для діагностики без парсингу message.

## Detailed explanation

TODO

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
