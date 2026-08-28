---
id: py-fund-0009
title: "How does reflection differ from ordinary access to an object's attribute that is already known in advance?"
description: "How does reflection differ from ordinary access to an object's attribute that is already known in advance?"
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/general.md#L394-L407
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**With ordinary access the attribute name is fixed in the code, whereas reflection determines or examines the structure of an object at run time.**[^py314-reference-executionmodel] For example, `obj.run` reaches a known attribute, while `getattr(obj, name)` chooses it by a runtime string, and `inspect` can examine live objects. Reflection uses the ordinary attribute protocol rather than bypassing it.

## Detailed explanation

The difference is not in the mechanism but in where the attribute name comes from. `obj.run` and
`getattr(obj, 'run')` are literally the same operation: the compiler turns the dot into the same
lookup through `__getattribute__`.[^py314-reference-datamodel] Reflection bypasses nothing and
violates nothing.

The difference is that with ordinary access the name is fixed in the code at writing time, while
with reflection it becomes a **value**: a string that can be read from configuration, assembled from
parts, or obtained from another object.

The second half of reflection is not access but **examination**: finding out what an object has at
all, what parameters a method takes, where it came from. That is what `dir()`, `type()`, `vars()`
and the `inspect` module are for.

```python
handler = obj.run                  # the name is fixed at write time
handler = getattr(obj, name)       # the name is a value, decided at run time

dir(obj)                           # what attributes exist at all
inspect.signature(obj.run)         # (self, timeout: int = 30) - introspection, not access
```

The practical price of reflection is the loss of static guarantees. The compiler and the analysers
do not know which name will be computed, so they will not warn about a typo, will not rename the
attribute during a refactor, and will not show that the method is called at all. The error surfaces
at run time, at the moment of access itself.[^py314-reference-executionmodel]

**Where reflection is appropriate:**
- serialization and ORMs: the code must work with fields it does not know at writing time;
- a plugin API with a fixed set of hook names declared in the contract;
- tooling - debuggers, profilers, test frameworks - which by definition examine someone else's code;
- factories, where the "configuration string to implementation" mapping is checked against an
  allowlist.

**Where it is more of a smell:**
- `getattr` with a name glued together from strings, instead of a dict;
- walking `dir()` looking for methods "by prefix" instead of an explicit interface;
- reflection in internal code where the set of types is known and closed.

In short: ordinary access says "I know what I need"; reflection says "I will find out at run time
what is here". Both use the same protocol, and the second pays for its flexibility with
invisibility.[^py314-faq-general]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
