---
id: py-funcs-0024
title: "How did the standard semantics of evaluating annotations change in Python 3.14, and why should `annotationlib` be used for inspecting them safely instead of relying only on reading `__annotations__` directly?"
description: "How did the standard semantics of evaluating annotations change in Python 3.14, and why should `annotationlib` be used for inspecting them safely instead of relying only on reading `__annotations__` directly?"
track: python
section: functions-and-scope
level: senior
type: mechanism
tags: [annotationlib, annotations]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-howto-annotations
    title: "Python 3.14: Howto/annotations"
    url: https://docs.python.org/3.14/howto/annotations.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-annotationlib
    title: "Python 3.14: Library/annotationlib"
    url: https://docs.python.org/3.14/library/annotationlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: pep-649
    title: "PEP 649"
    url: https://peps.python.org/pep-0649/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "PEP 649 specification."
  - source_id: py314-reference-compound-stmts-annotations
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#annotations
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: annotations are lazily evaluated by default; the future import of annotations."
---

## Short answer

**In Python 3.14, annotations are evaluated lazily by default (PEP 649): the compiler generates an `__annotate__` callable that runs only when the annotations are accessed, not when the definition executes.**[^pep-649] To inspect them safely, use `annotationlib.get_annotations()` rather than reading `__annotations__` directly.[^py314-howto-annotations] The `Format.FORWARDREF` format returns `ForwardRef` objects for unresolved names instead of raising `NameError`, which the default `Format.VALUE` can do.[^py314-library-annotationlib] PEP 563 (`from __future__ import annotations`) stores annotations as strings, and it is scheduled to be deprecated and removed.[^py314-reference-compound-stmts-annotations]

## Detailed explanation

Before Python 3.14, annotations were evaluated while `def` or `class` executed, so referring to a name that was not yet defined raised `NameError` immediately.[^py314-library-annotationlib] In 3.14, by default, the interpreter keeps only what is needed to evaluate an annotation later, and evaluates it when the annotations are accessed.[^py314-reference-compound-stmts-annotations] To do this, the compiler creates a separate `__annotate__` function that returns the annotations dict.[^pep-649]

The consequence is that an error in an annotation moves from definition time to access time. The example:

```python
# Python 3.14+
from annotationlib import Format, get_annotations

class Node:
    def link(self, other: Later) -> None:  # Later is not defined yet
        ...

try:
    get_annotations(Node.link)
except NameError as e:
    print("VALUE:", e)                     # VALUE: name 'Later' is not defined
print(get_annotations(Node.link, format=Format.FORWARDREF)["other"].__forward_arg__)  # Later
print(get_annotations(Node.link, format=Format.STRING))  # {'other': 'Later', 'return': 'None'}

class Later: ...
print(get_annotations(Node.link)["other"].__name__)  # Later

def outer():
    Item = int
    def inner(x: Item) -> Item:
        return x
    return inner

print(outer().__annotations__)  # {'x': <class 'int'>, 'return': <class 'int'>}
```

The default format, `Format.VALUE`, fails with `NameError` while `Later` does not exist, whereas `Format.FORWARDREF` and `Format.STRING` do not raise that error. `get_annotations()` returns a new dict on each call.[^py314-library-annotationlib]

Local variables also behave differently. If an annotation refers to a free variable of the function, the `__annotate__` function is a closure, so `x: Item` in `inner` sees the local `Item` and yields `int`.[^pep-649] Under PEP 563, the same `__annotations__` would contain the string `'Item'`.

Reading `__annotations__` directly without handling `NameError` is risky: accessing the attribute triggers evaluation, and the `NameError` surfaces right there.[^py314-library-annotationlib]

**Common mistakes:**
- expecting an error in an annotation to appear during `def`: in 3.14 it appears when the annotations are accessed;
- reading `__annotations__` directly in tooling without handling `NameError`; use `get_annotations()` with the appropriate format instead;
- adding `from __future__ import annotations` to new code as a way to handle forward references: this mode stores strings, it is scheduled for removal, and `get_annotations()` and `typing.get_type_hints()` resolve such annotations less reliably.[^py314-reference-compound-stmts-annotations]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
