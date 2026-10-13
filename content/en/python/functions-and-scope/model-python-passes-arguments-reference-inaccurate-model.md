---
id: py-funcs-0010
title: "Why is the model \"Python passes arguments by reference\" inaccurate, and which model correctly explains both rebinding and mutation of a parameter?"
description: "The correct model is pass by assignment: the parameter receives a reference to the same object, but it is not an alias of the caller's variable."
track: python
section: functions-and-scope
level: middle
type: mechanism
tags: []
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
  - source_id: py314-faq-programming-why-did-changing-list-y-also-change-li
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-did-changing-list-y-also-change-list-x
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "FAQ section: `y = x` does not copy the list but gives a second name to the same object, so a mutation is visible through both names. Python 3.14 documentation."
  - source_id: py314-reference-simple-stmts-assignment-statements
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#assignment-statements
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Assignment statements section: a name that is not declared global or nonlocal is bound to the object in the current local namespace. Python 3.14 documentation."
  - source_id: py314-reference-simple-stmts-augmented-assignment
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#augmented-assignment-statements
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Augmented assignment section: where possible the operation is performed in place, so the old object is modified instead of a new one being created. Python 3.14 documentation."
---

## Short answer

**The correct model is `pass by assignment`: the parameter receives a reference to the same object, but it is not an alias of the caller's variable.**[^py314-faq-programming-how-do-i-write-a-function-with-output] Rebinding a parameter (`x = new_value`) only binds the local name to another object and does not affect the caller.[^py314-reference-simple-stmts-assignment-statements] Mutation (`x.append(v)`) changes the shared object, and both sides see the change.[^py314-faq-programming-why-did-changing-list-y-also-change-li] "Pass by reference" does not explain rebinding, and "pass by value" (copying) does not explain mutation; pass by assignment explains both.

## Detailed explanation

Pass by assignment means that during a call each parameter is bound to the same object that was passed as the argument, as if the statement `parameter = argument` had been executed. Python does not copy the object and does not create an alias for the caller's variable: the function gets a new name that refers to the same object.[^py314-faq-programming-how-do-i-write-a-function-with-output]

Rebinding is an ordinary assignment to a name. The statement `x = [99]` inside the function binds the local `x` to a new list, while the caller's name still refers to the old one. For a name that is not declared `global` or `nonlocal`, assignment binds it to the object in the current local namespace.[^py314-reference-simple-stmts-assignment-statements]

Mutation changes the object itself, not the name. `x.append(99)` adds an element to the list that the caller also refers to; because both names point to one list, the change is visible from both sides.[^py314-faq-programming-why-did-changing-list-y-also-change-li] This is why the model "pass by reference" does not work here: in it the parameter would be an alias of the caller's variable, and assigning to the parameter would change the variable itself, which does not happen in Python. The model "pass by value" in the sense of a copy does not explain why the caller sees the mutation.

The example shows both behaviours on one list:

```python
def rebind(x):
    x = [99]          # rebinding: only the local name x changes

def mutate(x):
    x.append(99)      # mutation: the list object the caller also holds changes

a = [1]
rebind(a)
print(a)              # [1]
mutate(a)
print(a)              # [1, 99]
```

The limit of the model is in what "the same object" means. Mutable objects (`list`, `dict`) can be changed through any name that refers to them. Immutable objects (`int`, `str`, `tuple`) cannot be changed, so "updating" them is always a rebinding. The `+=` operator is no exception: where possible it is performed in place, so for a list it changes the shared list, while for an int it only binds the local name to a new value.[^py314-reference-simple-stmts-augmented-assignment] So the same `x += ...` line can have different effects depending on the type.

**Common mistakes:**
- thinking that assigning to a parameter changes the caller's list: `x = []` inside the function does not touch it;
- thinking that `x += ...` is always only a rebinding;
- concluding from "Python passes by reference" that assigning to a parameter can replace the caller's object.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
