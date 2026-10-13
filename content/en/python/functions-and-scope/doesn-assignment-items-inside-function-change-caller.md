---
id: py-funcs-0009
title: "Why doesn't the assignment `items = []` inside a function change the caller's list, while `items.append(value)` can change it?"
description: "Why doesn't the assignment `items = []` inside a function change the caller's list, while `items.append(value)` can change it?"
track: python
section: functions-and-scope
level: middle
type: comparison
tags: [items, items-append-value]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-faq-programming-how-do-i-write-a-function-with-output
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#how-do-i-write-a-function-with-output-parameters-call-by-reference
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-faq-programming-why-did-changing-list-y-also-change-list-x
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-did-changing-list-y-also-change-list-x
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: a change to a mutable object is visible through all names that refer to it; assigning to a name only rebinds that name."
  - source_id: py314-reference-simple-stmts-augmented-assignment
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#augmented-assignment-statements
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: augmented assignment (+=) is performed in place when possible, modifying the old object instead of creating a new one."
---

## Short answer

**`items = []` creates a new local binding of the name, whereas `items.append(value)` changes the same object that both the parameter and the caller's variable refer to.**[^py314-faq-programming-how-do-i-write-a-function-with-output] Assignment only rebinds the local name `items` to a new object and does not affect the original. The method `.append()` changes the object itself, not the name; because the caller and the function refer to one list, the change is visible to both.

## Detailed explanation

Python passes arguments by assignment: the parameter is bound to the same object that the caller passed. The parameter name, however, is not an alias of the caller's name. The two bindings are independent, and rebinding one does not change the other. The FAQ describes this as passing arguments by assignment, with no call-by-reference.[^py314-faq-programming-how-do-i-write-a-function-with-output]

The following example shows both situations:

```python
def rebind(items):
    items = ['new']            # the local name now refers to another list
    return items

def mutate(items):
    items.append('new')        # changes the list that the caller also refers to

data = ['old']
rebind(data)
print(data)                    # ['old']: the caller's name still refers to the original list
mutate(data)
print(data)                    # ['old', 'new']: the same list object was changed
```

The rule is simple: rebinding a name (`items = ...`) changes only the local variable, while changing the object itself (`items.append(...)`, `items[0] = ...`) is visible through every name that refers to it.[^py314-faq-programming-why-did-changing-list-y-also-change-list-x]

Be careful with `+=`. For a list, `items += [value]` is done in place: the object changes, and the caller sees the change. `items = items + [value]` builds a new list and leaves the caller's list unchanged. The documentation describes augmented assignment this way: when possible, the operation is performed in place, and the old object is modified instead of a new one being created.[^py314-reference-simple-stmts-augmented-assignment]

**Common mistakes:**
- expecting that assigning `items = ...` inside the function changes the caller's list;
- writing `items += [value]` without noticing that for a list it is an in-place change that the caller sees;
- modifying an argument without saying so in the function name or documentation, so the caller does not expect the side effect.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
