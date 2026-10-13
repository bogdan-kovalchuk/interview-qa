---
id: py-funcs-0013
title: "How do `global` and `nonlocal` differ in which scope they look for a binding to assign to?"
description: "global binds a name in the module's top-level namespace, while nonlocal binds it to the nearest enclosing function scope and never to the module."
track: python
section: functions-and-scope
level: middle
type: comparison
tags: [global, nonlocal]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-simple-stmts-the-global-statement
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#the-global-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-simple-stmts-the-nonlocal-statement
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#the-nonlocal-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Resolution of names section: a global statement makes uses of the names in the block refer to the top-level namespace; nonlocal refers to the nearest enclosing function scope. Python 3.14 documentation."
---

## Short answer

**`global` binds a name to the module's top-level namespace, and `nonlocal` binds it to the nearest enclosing function scope.**[^py314-reference-executionmodel-resolution-of-names] For `nonlocal`, a binding must exist in one of the enclosing functions and is not looked up in the module; if there is none, a `SyntaxError` is raised.[^py314-reference-simple-stmts-the-nonlocal-statement] `global`, by contrast, always refers to the module level, not to a name in an enclosing function.[^py314-reference-executionmodel-resolution-of-names]

## Detailed explanation

`global` and `nonlocal` answer the same question: where an assignment to a name in a function body goes. Without a declaration, an assignment makes the name local to the body, so it is impossible to assign to a module-level name from a function without `global`.[^py314-reference-simple-stmts-the-global-statement]

`global` applies to the whole current block (a module, a function body, or a class body): the listed names are interpreted as globals, so their uses in the block refer to the module's namespace.[^py314-reference-simple-stmts-the-global-statement] A nested function with `global x` does not change the `x` of the outer function, even if that function has its own `x`; it changes the module-level `x`. The example shows this:

```python
x = 'module'

def outer():
    x = 'outer'
    def use_global():
        global x
        x = 'global assigned'
    def use_nonlocal():
        nonlocal x
        x = 'nonlocal assigned'
    use_global()
    print(x)     # outer: the global assignment did not reach outer's x
    use_nonlocal()
    print(x)     # nonlocal assigned

outer()
print(x)         # global assigned: the global declaration reached the module
```

`nonlocal` works differently. It looks for a binding only in the local scopes of the enclosing functions, and the module does not take part in that search. So `nonlocal x` in a function nested directly in the module, with no `x` in the enclosing function, gives a `SyntaxError`, even when a module-level `x` exists.[^py314-reference-simple-stmts-the-nonlocal-statement]

The declarations have limits. A `global` statement must come before any use or assignment of the name in the same block; otherwise a `SyntaxError` is raised.[^py314-reference-simple-stmts-the-global-statement] Likewise, `nonlocal` at module level is a `SyntaxError`, because there are no enclosing functions.[^py314-reference-simple-stmts-the-nonlocal-statement]

**Common mistakes:**
- writing `nonlocal x` for a module-level `x`: for the module you need `global`;
- expecting `global x` in a nested function to change the `x` of the outer function;
- putting `global x` after a read or assignment of `x` in the same block: this is a `SyntaxError`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
