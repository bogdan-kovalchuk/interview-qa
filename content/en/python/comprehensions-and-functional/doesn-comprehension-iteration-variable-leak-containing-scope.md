---
id: py-compfn-0003
title: "Why doesn't a comprehension's iteration variable leak into the containing scope, while a walrus assignment expression inside a comprehension can bind in the containing scope?"
description: "Why doesn't a comprehension's iteration variable leak into the containing scope, while a walrus assignment expression inside a comprehension can bind in the containing scope?"
track: python
section: comprehensions-and-functional
level: senior
type: pitfall
tags: []
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-howto-functional
    title: "Python 3.14: Howto/functional"
    url: https://docs.python.org/3.14/howto/functional.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-expressions-displays-for-lists-sets-and-dict
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**A comprehension creates a separate implicit scope for its iteration variable, whereas `:=` (the assignment expression) explicitly binds its target in the containing scope, bypassing this isolation.**[^py314-howto-functional] For instance, after `[y := x for x in data]`, the name `y` remains accessible in the outer scope, whereas `x` does not. <span class="warn">If the containing scope declares `nonlocal` or `global` for that name, `:=` respects that declaration.</span>

## Detailed explanation

The isolation of comprehension iteration variables contrasted with the outer-binding behavior of `:=` reflects the deliberate evolution of Python's scoping architecture.[^py314-howto-functional]

In Python 2, list comprehension loop variables routinely leaked into the surrounding function or module scope, silently overwriting existing variables. In Python 3, every comprehension (list, set, dict, and generator expressions) is compiled into an isolated, implicit nested code object, ensuring iteration variables remain strictly local to that nested frame and disappear once evaluation finishes.[^py314-reference-expressions-displays-for-lists-sets-and-dict]

When PEP 572 introduced assignment expressions (`:=`), Python's designers deliberately engineered an exception to this isolation: a walrus assignment inside a comprehension binds directly into the nearest *enclosing* scope (the enclosing function or module), bypassing the comprehension's implicit frame.[^py314-reference-expressions-displays-for-lists-sets-and-dict] This pragmatic decision enables capturing expensive intermediate computations for both filtering and element generation without recalculating them. However, to prevent ambiguity and conflicting scopes, Python strictly forbids using the comprehension's iteration variable as the target of `:=` (for example, `[i := i + 1 for i in range(5)]` raises `SyntaxError`).

Differences between iteration variable isolation and walrus target binding:

```python
data = [1, 2, 3, 4]

# 1. Iteration variable 'item' is isolated within the comprehension scope:
squares = [item * item for item in data]
print("item" in locals())  # False: iteration variable does not leak

# 2. Walrus operator ':=' deliberately binds in the enclosing scope:
filtered = [last := x * 10 for x in data if x > 2]
print(filtered)            # [30, 40]
print("last" in locals())  # True: target leaks into containing scope
print(last)                # 40 (holds the value from the last matching iteration)

# 3. Reusing the comprehension variable as a walrus target is a SyntaxError:
# [x := x + 1 for x in data] -> SyntaxError: assignment expression cannot rebind comprehension iteration variable
```

**Subtle pitfalls and architectural constraints:**
- unintentional shadowing or overwriting of existing variables in the outer function due to `:=` inside a comprehension;
- attempting to rebind the comprehension's iteration variable using `:=`, triggering a compile-time `SyntaxError`;
- using `:=` within a comprehension defined directly at class level, which is disallowed by class scoping rules and raises `SyntaxError`;
- relying on the walrus variable after a comprehension where no elements matched the `if` filter, leaving the variable unbound or pointing to a previous stale value.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
