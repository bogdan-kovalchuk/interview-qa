---
id: py-fund-0005
title: "Why are dynamic typing and strong typing not opposite characteristics of a language?"
description: "Why are dynamic typing and strong typing not opposite characteristics of a language?"
track: python
section: fundamentals
level: middle
type: comparison
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

**Dynamic typing describes when a type is determined and checked, while strong typing informally describes how strict the rules are for interaction between incompatible types.**[^py314-reference-executionmodel] In Python a name can be rebound to objects of different types, but the operations available are still decided by the type of the current object. The two characteristics therefore answer different questions and can coexist.

## Detailed explanation

Dynamic typing and strong typing are answers to two different questions, so they do not lie on one
axis and cannot be opposites. The first question is **when** the type is known. The second is **how
strictly** the language treats operations between incompatible types.

Dynamic typing means the type belongs to the object rather than to the name, and is checked at the
moment the operation runs. A name in Python is just a reference, and assignment can rebind it to an
object of another type without breaking anything.[^py314-reference-executionmodel]

Strong typing is an informal term, which is exactly why it gets confused. It means the language does
not perform implicit conversions between incompatible types just to make something work: `1 + "1"`
in Python is a `TypeError`, not `2` and not `"11"`.[^py314-reference-datamodel] In a weakly typed
language the same expression would silently produce a result.

An example showing both characteristics in one fragment:

```python
x = 1
x = "one"        # dynamic: the name is rebound to an object of another type, no error

1 + "1"          # strong: TypeError, no implicit coercion between int and str
int("1") + 1     # 2 - conversion happens only when it is asked for explicitly
```

The first line works precisely because of dynamic typing; the second fails precisely because of
strong typing. Both are Python, and neither contradicts the other.

**The usual confusions around these terms:**
- "dynamic means weak" - no: Python is dynamic and strong, C is static and relatively weak (implicit
  conversions between numeric types and pointers);
- "the variable changed its type" - the binding of the name changed, while the type of the object
  itself is fixed from creation to destruction;
- "type hints make Python statically typed" - annotations are not checked at run time, they exist
  for external analysers, and the runtime semantics stay dynamic;
- "strong typing is a formal term" - it is not, there is no formal definition, so in an argument it
  helps to talk about concrete behaviour rather than about the label.

The practical consequence of the "dynamic plus strong" pair is this: a type mismatch in Python is
found late (only once the line runs) but is found loudly - as an exception at the operation, not as
a quietly wrong value that surfaces three layers of calls later.[^py314-faq-general]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
