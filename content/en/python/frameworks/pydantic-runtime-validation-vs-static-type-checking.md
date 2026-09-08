---
id: py-framew-0001
title: "How does Pydantic runtime validation differ from static type checking?"
description: "Static type checkers analyze annotations without executing the program; Pydantic interprets annotations at runtime to validate or convert input into a model."
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
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-typing
    title: "Python 3.14: typing - Support for type hints"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-08
    kind: official
    version: "3.14"
    applicability: "Official Python documentation on the static purpose and runtime behavior of annotations."
  - source_id: pydantic-models
    title: "Pydantic documentation: Models"
    url: https://pydantic.dev/docs/validation/latest/concepts/models/
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "Official Pydantic documentation on validation, conversion, models, and ValidationError."
---

## Short answer

**A static type checker analyzes annotations without executing the program and reports code that is inconsistent with them; Python does not enforce ordinary annotations at runtime.**[^py314-library-typing] Pydantic reads annotations when it validates input, then returns a model whose fields conform to the declared types or raises `ValidationError`.[^pydantic-models] It may convert compatible input by default, while strict mode can reject such coercion. Use static checking for developer-time consistency and Pydantic at runtime trust boundaries; neither replaces the other.

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
