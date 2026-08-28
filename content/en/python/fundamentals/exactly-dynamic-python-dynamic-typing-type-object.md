---
id: py-fund-0004
title: "What exactly is dynamic about Python's dynamic typing: the type of an object, or the binding of a name to an object?"
description: "What exactly is dynamic about Python's dynamic typing: the type of an object, or the binding of a name to an object?"
track: python
section: fundamentals
level: middle
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
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/general.md#L104-L137
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**What is dynamic is the binding of a name to an object, not the type of an object that already exists.**[^py314-reference-executionmodel] Every object has its own immutable type, but assignment can rebind the same name to a different object, including one of another type. "Changing the type of a variable" therefore means, in practice, a new binding of the name.

## Detailed explanation

In Python a name and an object are different things. An object has identity, type and value, and its
type is fixed from creation to destruction. A name is an entry in a namespace pointing at an object,
and it is that entry which can be rebound.[^py314-reference-datamodel]

The phrase "the variable changed its type" therefore does not describe what happened. What happened
is something else: assignment wrote into the same namespace a reference to a **different** object,
which has a type of its own. The old object was neither changed nor converted - it simply stopped
being reachable under that name.

`id()`, which shows an object's identity, makes this visible: after rebinding the identity differs,
so this is a different object, not the same one in a new guise.

```python
x = 1
print(type(x), id(x))    # <class 'int'>  140234...

x = "one"
print(type(x), id(x))    # <class 'str'>  140235...  - a different object entirely
```

A consequence that matters in practice: every name that pointed at the old object keeps pointing at
it. Rebinding one name does not change the others.

```python
a = [1, 2]
b = a
a = "gone"     # rebinds only `a`
print(b)       # [1, 2] - `b` still refers to the original list
```

This also explains why mutation and rebinding are different operations: `a.append(3)` changes the
**object** every name sees, while `a = [...]` changes only the **name**.

**What exactly is dynamic, and what is not:**
- dynamic: the binding of a name to an object, and it can be changed any number of times;
- dynamic: attribute lookup and operator selection, because they are decided by the object's type at
  the moment of execution;[^py314-reference-executionmodel]
- **not** dynamic: the type of an object that already exists - it is fixed and does not change;
- **not** dynamic: which operations are available - that is decided by the type of the current
  object, not by what the code would like.

This is why the annotation `x: int` forbids nothing at run time: it states an intent for an external
analyser, while the binding machinery stays exactly the same.[^py314-faq-general]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
