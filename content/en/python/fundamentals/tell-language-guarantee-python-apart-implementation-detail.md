---
id: py-fund-0006
title: "How do you tell a language guarantee of Python apart from an implementation detail, using memory management or bytecode as an example?"
description: "How do you tell a language guarantee of Python apart from an implementation detail, using memory management or bytecode as an example?"
track: python
section: fundamentals
level: middle
type: practical
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython"
    version: null
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/interpreter.md#L3-L26
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Look the rule up in the Python Language Reference and check whether the documentation marks it as an implementation detail.**[^py314-reference-executionmodel] For example, every object having an identity, a type and a value is part of the data model, while the memory address returned by `id()` and the bytecode format are described outright as CPython details. Code must not build portable logic on such details.

## Detailed explanation

A language guarantee is a rule written down in the Python Language Reference: every implementation
must honour it, or it is not Python. An implementation detail is how CPython specifically chose to
carry that rule out; another implementation is entitled to do it
differently.[^py314-reference-executionmodel]

The practical check is textual. Find the statement in the Language Reference or in the type's
description in the standard library, and see whether a caveat such as "CPython implementation
detail" sits next to it. Those places are marked explicitly, and they are exactly where portability
ends.

It helps to keep a few contrasting pairs in mind. Guarantee: every object has an identity, a type
and a value, and `id()` returns a constant unique number for the lifetime of the object. Detail:
that this number is a memory address, and that small integers are cached, which is why `a is b` is
often true.[^py314-reference-datamodel]

```python
x = 256
y = 256
x is y            # True in CPython - small-int cache, an implementation detail

x = 257
y = 257
x is y            # False in CPython - and either result is valid per the language

x == y            # True - this is the guarantee, and the only thing to rely on
```

Another pair: the guarantee is that a `dict` preserves insertion order (since 3.7 that is part of
the language). The detail is how it does so internally and how much memory it takes. And one more:
the guarantee is that `with` calls `__exit__` on leaving the block; the detail is that in CPython an
object with no references disappears immediately thanks to reference counting.

**Practical heuristics when the documentation is not at hand:**
- the behaviour is described in the Language Reference or in the PEP that introduced it - a
  guarantee;
- the behaviour is visible only through `dis`, `sys.getrefcount`, `id()` or an object's size - a
  detail;
- the module is named `_something` or documented as internal - a detail;
- the behaviour changed between minor versions with no entry under "Deprecations" - almost certainly
  a detail.[^py314-faq-general]

The simplest sanity check: is PyPy entitled to do this differently and still be Python? If so, you
are leaning on an implementation detail.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
