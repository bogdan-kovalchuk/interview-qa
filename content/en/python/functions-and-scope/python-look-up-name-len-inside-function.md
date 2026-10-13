---
id: py-funcs-0014
title: "How will Python look up the name `len` inside a function if there is no local binding, but the module defines its own `len`?"
description: "Python looks up a name in local, enclosing, module-global and builtin scopes in that order, so a module-level len is found before the builtin len."
track: python
section: functions-and-scope
level: middle
type: mechanism
tags: [len]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-executionmodel-resolution-of-names
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html#resolution-of-names
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**Python looks up a name first in the local scope, then in the enclosing scope, then in the module's global namespace, and only after that in builtins; so a module-level `len` is found before the builtin `len`.**[^py314-reference-executionmodel-resolution-of-names] There is no local binding, and the enclosing scope (if the function is not nested) also does not contain `len`, so the search reaches the module, finds the `len` defined there, and never reaches builtins.

## Detailed explanation

A name such as `len` inside a function body is resolved when it is used, not during `def`. Python takes the nearest scope in which the name is bound: first the function's local namespace, then the enclosing function's (if it is nested), then the global namespace of the module that contains the code, and only after that builtins.[^py314-reference-executionmodel-resolution-of-names]

A module-level `len` shadows the builtin one for the code of that module. The example shows how the result of the same call to `count` changes:

```python
def count(items):
    return len(items)               # the name is looked up when this call runs

print(count([1, 2, 3]))             # 3: no module-level len yet, so builtins len is used

def len(obj):
    return 'module len'

print(count([1, 2, 3]))             # module len: the module-level name is found first

import builtins
print(builtins.len([1, 2, 3]))      # 3: the builtin is still reachable explicitly

del len
print(count([1, 2, 3]))             # 3: without the module-level name, lookup reaches builtins

def outer():
    def len(obj):
        return 'enclosing len'
    def inner():
        return len([1])
    return inner()

print(outer())                      # enclosing len: the enclosing scope is searched before the module
```

The lookup happens at call time, so the state of the namespace at that moment is what counts. `count` sees the module-level `len` even though it is defined after `def count`, because the name already exists when the call runs. The builtin `len` does not disappear: it can be reached as `builtins.len`, and `del len` brings the lookup back to it. Builtins are the namespace of the module `builtins`, searched last.[^py314-reference-executionmodel-resolution-of-names]

A nested function takes precedence over the module: if the enclosing function defines its own `len`, then `inner` finds that one and the search stops there. This is the same order, except that the enclosing scope sits between local and global.

**Common mistakes:**
- thinking that the name `len` is bound during `def`: the lookup happens during the call, against the namespace as it is at that time;
- ignoring the enclosing scope: a `len` in the outer function shadows both the module-level and the builtin one;
- thinking that `builtins.len` is unavailable once the module redefines `len`: it can still be called explicitly.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
