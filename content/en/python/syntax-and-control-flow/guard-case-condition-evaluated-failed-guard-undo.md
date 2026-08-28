---
id: py-syntax-0010
title: "When is the guard in `case ... if condition` evaluated, and does a failed guard undo the bindings the pattern itself created?"
description: "When is the guard in `case ... if condition` evaluated, and does a failed guard undo the bindings the pattern itself created?"
track: python
section: syntax-and-control-flow
level: senior
type: mechanism
tags: [case-if-condition]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
applies_to:
  - product: "CPython"
    version: "3.14"
anki:
  export: true
sources:
  - source_id: py314-reference-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-simple-stmts
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-compound-stmts
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/syntax.md#L164-L228
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**A guard is evaluated only after the pattern succeeds; if the guard is false the case is not chosen, but the bindings made by the pattern are NOT guaranteed to be undone.**[^py314-reference-expressions] The Language Reference warns explicitly: "Do not rely on bindings being made for a failed match. Conversely, do not rely on variables remaining unchanged after a failed match." In CPython 3.14 the bindings persist (after `case (y,) if y > 100:`, for instance, `y` stays bound even when the guard fails), but that is an implementation detail.

## Detailed explanation

A `case` with a guard is checked in two steps. The pattern is matched first; only if it succeeds is
the condition after `if` evaluated. That order exists because a guard almost always refers to names
the pattern bound - without a successful match they would simply not
exist.[^py314-reference-compound-stmts]

The surprising consequence: for the guard to look at `y`, `y` must already be bound. So by the time
the condition is checked the bindings are **already made**, and if the guard turns out false they do
not go anywhere.

```python
y = 'original'

match (500,):
    case (y,) if y > 100:      # pattern matches, y is bound to 500
        print('big')           # guard is False, so this branch is skipped
    case _:
        print('fallback')

y    # 500 in CPython 3.14 - the binding from the failed case survived
```

The Language Reference does not describe this as a guarantee but warns in both directions: do not
rely on bindings being made after a failed match, and do not rely on variables remaining
unchanged.[^py314-reference-expressions] The current CPython behaviour is therefore an
implementation detail, and code must not lean on it either way.

**What to do about it in practice:**
- do not use names inside a `match` that mean something after the construct - patterns overwrite
  them freely;
- if a value is needed after the `match`, assign it explicitly inside the branch that actually ran;
- do not rely on the "old" variable right after a `match`, even when no branch fired;
- remember that this applies to wildcard-like names too: `case value if ...:` binds `value` whenever
  the pattern succeeds.

The practical rule is simple: `match` is a construct that **binds**, not merely one that checks.
Treat its names as local to the branch, even though the language does not technically make them so.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
