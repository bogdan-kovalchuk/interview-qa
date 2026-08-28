---
id: py-fund-0010
title: "When can monkey patching be justified, and what risks does it create for the locality of changes, tests, and dependency upgrades?"
description: "When can monkey patching be justified, and what risks does it create for the locality of changes, tests, and dependency upgrades?"
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/general.md#L300-L331
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**Monkey patching is justified mostly as a short-lived, controlled substitution in a test, or as a narrow compatibility workaround when dependency injection is unavailable.**[^py314-reference-executionmodel] It hides dependencies, mutates shared state, can make tests order-dependent and can break after a dependency update. In tests it is better to apply a scoped `unittest.mock.patch()` in the right namespace, so that the substitution is guaranteed to be undone.

## Detailed explanation

Monkey patching is the replacement of an attribute of an already existing module, class or object at
run time. Since a class in Python is an object with a mutable `__dict__` too, assigning
`SomeClass.method = other` always works and immediately affects the whole
process.[^py314-reference-datamodel]

The cost is exactly in that "whole process". A patch has no scope: it is not confined to the module
that made it, it does not undo itself, and it is invisible in the code whose behaviour it changes. A
reader of a function calling `requests.get` gets no hint that somewhere in a conftest it was
replaced.

The class is what must be patched, not the instance - and that is the most common mistake. A
function assigned to an instance attribute does not become a bound method: the descriptor protocol
applies only to class attributes, so `self` is not passed.[^py314-reference-datamodel]

```python
class Service:
    def fetch(self):
        return 'real'

def fake(self):
    return 'patched'

Service.fetch = fake          # correct: descriptor protocol binds `self`
Service().fetch()             # 'patched'

obj = Service()
obj.fetch = fake              # wrong: an instance attribute, not a bound method
obj.fetch()                   # TypeError: fake() missing 1 required positional argument
```

In tests the right tool is `unittest.mock.patch()`, because it undoes the substitution on exit from
the context manager or decorator. Patch where the name **is looked up**, not where it is defined: if
a module did `from x import get`, what needs patching is `mymodule.get`, not `x.get`.

**When monkey patching is justified:**
- in a test, through a scoped `patch()`, with a guaranteed rollback;
- as a narrow workaround for an incompatibility in a third-party library until a fix ships - with a
  comment, a link to the issue and a plan to remove it;
- for instrumentation (a profiler, tracing) that deliberately intervenes in someone else's code.

**Why it is a bad architectural decision:**
- the dependency becomes invisible: it appears in no signature and no import;
- tests become order-dependent if the patch is not undone - the result depends on run order;
- a library update can silently break the patch, because it leans on a private detail;
- two patches of the same attribute conflict silently, and the last one wins.

Where there is a choice, dependency injection gives the same result explicitly: the dependency is
passed as an argument, visible in the signature and replaceable without global
state.[^py314-reference-executionmodel]

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
