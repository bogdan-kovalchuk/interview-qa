---
id: py-funcs-0006
title: "What do two consecutive calls `append(1)` and `append(2)` return for `def append(x, items=[]): items.append(x); return items`, and why?"
description: "What do two consecutive calls `append(1)` and `append(2)` return for `def append(x, items=[]): items.append(x); return items`, and why?"
track: python
section: functions-and-scope
level: middle
type: pitfall
tags: [append-1, append-2, def-append-x-items-items-append-x-return-items]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-faq-programming-why-are-default-values-shared-between
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-are-default-values-shared-between-objects
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**`append(1)` returns `[1]`, `append(2)` returns `[1, 2]`: both calls work with the same list.**[^py314-faq-programming-why-are-default-values-shared-between] The default object `[]` is created once, when `def` runs, not on every call.[^py314-reference-compound-stmts-function-definitions] The parameter `items` refers to that single object, so `.append()` accumulates elements across calls. <span class="warn">This is a classic mutable default trap.</span> The correct pattern is to use `items=None` and create a new list inside the function.[^py314-faq-programming-why-are-default-values-shared-between]

## Detailed explanation

Default values are evaluated from left to right when the `def` statement runs, not on every call to the function. The expression `[]` in the signature is evaluated once: the resulting list is stored with the function and used by every call where `items` is not passed.[^py314-reference-compound-stmts-function-definitions] So two calls without `items` work with the same list, not with two empty ones.

The next example shows what is shared. The first two results are the same object, which the function changes on every call:

```python
def append(x, items=[]):
    items.append(x)
    return items

print(append(1))              # [1]
print(append(2))              # [1, 2]: the same list object, not a new one
print(append.__defaults__)    # ([1, 2],): the default object itself was changed

first = append(3)
second = append(4)
print(first is second)        # True: both names refer to one list
print(first)                  # [1, 2, 3, 4]: the earlier result changed too
```

The returned value is not a snapshot of the state but a reference to the shared list. If you keep the result of the first call, it shows `[1, 2, 3, 4]` after the later calls. The fix is `items=None` and creating the list inside the function when `items is None`: then each call without an argument gets a new object.[^py314-faq-programming-why-are-default-values-shared-between]

The trap applies only to mutable default values. Numbers, strings and `None` cannot be changed in place, so sharing them is safe.[^py314-faq-programming-why-are-default-values-shared-between]

**Common mistakes:**
- assuming that each call without `items` gets a new empty list;
- keeping the result of the first call and expecting it to stay unchanged after the second call;
- writing `items=[]` or `items={}` in a function that changes that argument.

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
