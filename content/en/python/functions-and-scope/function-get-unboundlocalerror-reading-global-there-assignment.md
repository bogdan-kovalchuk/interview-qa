---
id: py-funcs-0012
title: "Why can a function get an `UnboundLocalError` when reading a global `x`, if there is an assignment `x = ...` further down in its body?"
description: "Python treats a name as local to a function if the body contains any binding of it, so every use of that name in the body refers to the local name."
track: python
section: functions-and-scope
level: middle
type: pitfall
tags: [unboundlocalerror]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython"
    version: null
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
  - source_id: py314-faq-programming-why-am-i-getting-an-unboundlocalerror
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-am-i-getting-an-unboundlocalerror-when-the-variable-has-a-value
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
---

## Short answer

**Python treats a name in a function body as local if the body contains any binding operation for it (assignment, `for`, `import`, and so on), so every reference to that name in the body refers to the local name.**[^py314-reference-executionmodel-resolution-of-names] If a read happens before the first assignment, the local variable has no value yet and an `UnboundLocalError` is raised.[^py314-faq-programming-why-am-i-getting-an-unboundlocalerror] To read a global `x` in such a function, declare `global x`; then all references to `x` in the body refer to the module-level name.[^py314-reference-executionmodel-resolution-of-names]

## Detailed explanation

Python determines local names from the text of the block, not from the order in which the lines run: the local variables of a code block are determined by scanning the entire text of the block for name binding operations.[^py314-reference-executionmodel-resolution-of-names] If a block contains a binding operation for a name, then all references to that name in the block refer to the local name, even those that stand before the assignment. Binding operations include not only assignments but also `for`, `import`, `with ... as`, `except ... as`, and the parameters of the function.

So a read of `x` before the assignment does not fall through to the global `x`. The local name already exists in the body but is not yet bound to a value, so Python raises `UnboundLocalError`, a subclass of `NameError`.[^py314-reference-executionmodel-resolution-of-names] In CPython 3.11 and later the message reads `cannot access local variable 'x' where it is not associated with a value`; the FAQ gives the same text.[^py314-faq-programming-why-am-i-getting-an-unboundlocalerror]

Three functions with one module-level `x` show the limits of the rule:

```python
x = 10

def read_then_assign():
    print(x)   # raises UnboundLocalError: the assignment below makes x local to the whole body
    x = 20

def read_only():
    print(x)   # 10: no binding in this body, so x is looked up as a global

def with_global():
    global x
    print(x)   # 10: the global declaration applies to the whole body
    x = 20     # rebinds the module-level x
```

To read the global `x` in a function that also assigns it, declare `global x`. The declaration must come before every use of the name in the block. After it, all references, including `x = 20`, refer to the module-level `x` rather than creating a local name.[^py314-reference-executionmodel-resolution-of-names]

**Common mistakes:**
- thinking that the order of lines matters: an assignment anywhere in the body is enough to make the name local for the whole body;
- thinking that there is no global `x`: it exists, but the function refers to a local name that has not been assigned yet;
- adding `global x` as a "fix" for a read: the declaration changes the assignments in the body too, not only the reads.

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
