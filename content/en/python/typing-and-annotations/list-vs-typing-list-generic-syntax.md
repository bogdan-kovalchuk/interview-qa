---
id: py-typing-0001
title: "What is the difference between List[str] from typing and list[str] built-in in Python 3.9+?"
description: "typing.List[str] is a legacy typing alias; list[str] is the built-in generic syntax added in Python 3.9 and is preferred when Python 3.9 or newer is the target."
track: python
section: typing-and-annotations
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-08
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-08
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: pep585
    title: "PEP 585: Type Hinting Generics In Standard Collections"
    url: https://peps.python.org/pep-0585/
    accessed: 2026-09-08
    kind: official
    version: null
    applicability: "PEP that introduced built-in generic syntax."
---

## Short answer

**`typing.List[str]` is a legacy typing alias, while `list[str]` is the built-in generic syntax introduced in Python 3.9 and preferred for code targeting 3.9 or newer.**[^py314-library-typing][^pep585] Static type checkers normally interpret both as a list of strings. They are not identical runtime objects, however, and neither annotation validates a list's elements at runtime. Code executed on Python 3.8 cannot evaluate `list[str]`; use `typing.List[str]` there, or postpone annotation evaluation when the surrounding tooling supports that design.

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
