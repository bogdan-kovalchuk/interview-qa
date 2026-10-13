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
updated: 2026-10-13
content_revision: 3
reconciled_with:
  uk: 3
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
  - source_id: pep-563
    title: "PEP 563: Postponed Evaluation of Annotations"
    url: https://peps.python.org/pep-0563/
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "PEP that postponed evaluation of function and variable annotations (available since Python 3.7). It does not describe which types may be written there."
---

## Short answer

**`typing.List[str]` is a legacy typing alias, while `list[str]` is the built-in generic syntax introduced in Python 3.9 and preferred for code targeting 3.9 or newer.**[^py314-library-typing][^pep585] Static type checkers normally interpret both as a list of strings. They are not identical runtime objects, however, and neither annotation validates a list's elements at runtime. Code executed on Python 3.8 cannot evaluate `list[str]`; use `typing.List[str]` there, or postpone annotation evaluation when the surrounding tooling supports that design.

## Detailed explanation

For a type checker, `List[str]` from `typing` and `list[str]` mean the same type: a list of strings. They differ as runtime objects. `typing.List` is a deprecated alias for the built-in `list`, which the `typing` module keeps for compatibility.[^py314-library-typing] The built-in `list` now parameterizes itself through `__class_getitem__()`, so `list[str]` creates its own generic alias object.[^pep585] In CPython, `List[str]` is a `typing._GenericAlias` and `list[str]` is a `types.GenericAlias`. Both have `__origin__` (`list`) and `__args__` (`(str,)`), but `List[str] == list[str]` evaluates to `False`.

Before Python 3.9, `typing.List` was the only way to parameterize a collection at runtime, because the built-in `list` did not accept `[]`. PEP 585 added that ability in Python 3.9, and since then the documentation has marked the older aliases as deprecated. The interpreter issues no warnings for them, and they may eventually be removed from `typing`.[^pep585]

Annotations are not checked at runtime. A function with `items: list[str]` accepts `[42]` and returns `42`; only a type checker can report that mistake. `list[str]` is also not usable for a runtime type test: `isinstance(x, list[str])` raises `TypeError` (in CPython 3.12 to 3.14), so write `isinstance(x, list)` instead. Example:

```python
from typing import List

print(List[str] == list[str])                              # False: two different runtime objects
print(type(List[str]).__name__, type(list[str]).__name__)  # _GenericAlias GenericAlias

def first(items: list[str]) -> str:
    return items[0]

print(first([42]))                                         # 42: the annotation is not checked at runtime
```

Evaluating `list[str]` at runtime requires Python 3.9 or newer: PEP 585 ties the built-in generic syntax to 3.9 and notes that type aliases and casting need the type outside an annotation, in a runtime context.[^pep585] For code that must run on 3.8, use `typing.List[str]` in runtime expressions. For annotations alone, `from __future__ import annotations` (available since 3.7) keeps `list[str]` from being evaluated,[^pep-563] but this works only where the surrounding tooling understands that form.[^pep585]

**Common mistakes:**
- assuming that `list[str]` checks the list's elements at runtime (see the example above);
- comparing `List[str]` and `list[str]` with `==` or `isinstance` and expecting identical behaviour;
- writing `list[str]` in runtime code (aliases, casts, `isinstance` calls) that must run on 3.8, and getting a `TypeError` only on the older version.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
