---
id: py-framew-0001
title: "Чим runtime validation у Pydantic відрізняється від static type checking?"
description: "Static type checkers аналізують анотації без виконання програми; Pydantic інтерпретує анотації під час виконання, щоб перевірити або перетворити input на model."
track: python
section: frameworks
level: middle
type: comparison
tags: []
frameworks: [pydantic]
status: published
updated: 2026-09-08
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-typing
    title: "Python 3.14: typing - Support for type hints"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-08
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python про статичне призначення та runtime behavior анотацій."
  - source_id: pydantic-models
    title: "Pydantic documentation: Models"
    url: https://pydantic.dev/docs/validation/latest/concepts/models/
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Офіційна документація Pydantic про validation, conversion, models і ValidationError."
---

## Short answer

**Static type checker аналізує анотації без виконання програми та повідомляє про несумісний із ними код; Python не забезпечує runtime enforcement звичайних анотацій.**[^py314-library-typing] Pydantic читає анотації під час validation input і повертає model, поля якої відповідають оголошеним типам, або викидає `ValidationError`.[^pydantic-models] За замовчуванням він може перетворювати сумісні input values, а strict mode може відхиляти таку coercion. Static checking потрібен для узгодженості коду під час розробки, а Pydantic для runtime trust boundaries; вони не замінюють один одного.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
