---
id: py-fund-0012
title: "How does the executable nature of `def` and `class` statements affect conditional definition, redefinition, and import-time side effects?"
description: "How does the executable nature of `def` and `class` statements affect conditional definition, redefinition, and import-time side effects?"
track: python
section: fundamentals
level: senior
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-executionmodel
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-faq-general
    title: "Python 3.14: Faq/general"
    url: https://docs.python.org/3.14/faq/general.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**`def` and `class` are executable statements: they create the function or class object and bind the name at run time, not at compile time.**[^py314-reference-executionmodel] They can therefore be placed inside `if`/`else`, loops and nested scopes - only the branch that actually runs defines anything. A repeated `def` or `class` with the same name in the same scope simply rebinds the name to a new object. And because a module body executes top to bottom on import, any module-level code (I/O, network calls, print) becomes an import-time side effect, which complicates testing and reuse.

## Detailed explanation

`def` and `class` declare nothing at compile time - they are statements that execute when control
reaches them. `def` creates a function object and binds a name; `class` executes the class body in a
separate namespace, creates a class object and binds a
name.[^py314-reference-executionmodel]

The first consequence: both statements can go anywhere a statement can go - inside an `if`, a loop,
another function. Only the branch control reached runs, so a definition is conditional not
"formally" but literally.

```python
if sys.platform == 'win32':
    def newline():
        return '\r\n'
else:
    def newline():
        return '\n'

# only one of the two objects was ever created; the other `def` never ran
```

The second consequence: a repeated `def` with the same name in the same scope redefines nothing in
the sense of overloading - it merely rebinds the name to a new object, and the previous one becomes
unreachable. Python therefore has no overloading by signature: the last `def` wins.

```python
def handle(x):
    return 'first'

def handle(x, y):      # not an overload - it replaces the name binding
    return 'second'

handle(1)              # TypeError: handle() missing 1 required positional argument: 'y'
```

The third consequence concerns import. A module body is a sequence of statements too, executed top
to bottom on the first import. Everything written at module level runs exactly then: `def` and
`class` create objects, and anything else performs its side
effect.[^py314-reference-executionmodel]

**What follows in practice:**
- a decorator is applied when the `def` executes, not when the function is called - so the decorator
  sees the function once, at definition time;
- default argument values are evaluated when the `def` executes, once, not on every call;
- module-level code that reads a file, goes to the network or prints becomes an import-time side
  effect: it cannot be skipped once the module is imported;
- that is precisely why an entry point is hidden behind `if __name__ == '__main__':` - so that
  importing the module does not run the program.

The practical benefit of conditional definition is real: platform- or version-specific variants of a
function are written without a dispatching wrapper, and no condition check is left on the hot
path.[^py314-faq-general]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
