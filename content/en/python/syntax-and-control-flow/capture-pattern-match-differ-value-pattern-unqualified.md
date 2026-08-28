---
id: py-syntax-0009
title: "How does a capture pattern in `match` differ from a value pattern, and why can an unqualified name unexpectedly bind a new variable?"
description: "How does a capture pattern in `match` differ from a value pattern, and why can an unqualified name unexpectedly bind a new variable?"
track: python
section: syntax-and-control-flow
level: middle
type: comparison
tags: [match]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  uk: 2
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

**A capture pattern (a bare name, e.g. `case x:`) always succeeds and binds the subject to a new name; a value pattern (a qualified name, e.g. `case Color.RED:`) compares the subject with a known value using `==`.**[^py314-reference-expressions] If you expected `case status:` to compare against an existing `status` variable, a new `status` variable is created instead, shadowing the previous one. To compare with a known value, use a dotted name (`case MyEnum.status:`) or a literal.

## Detailed explanation

In a `match`, a bare name never means "compare with what is in this variable". The grammar decides
by the shape of the name: an unqualified name is a capture pattern, a dotted name is a value
pattern.[^py314-reference-compound-stmts]

A capture pattern always succeeds. It compares nothing and simply binds the subject to that name -
which is why any `case x:` matches anything and shadows every case after it.

A value pattern compares. It evaluates the qualified name (`Color.RED`, `settings.MODE`) and checks
the subject against it with `==`.

```python
status = 404

match code:
    case status:          # capture pattern: matches ANY code and rebinds `status`
        print('matched')  # runs always; `status` is now equal to `code`

match code:
    case HTTPStatus.NOT_FOUND:   # value pattern: compares with ==
        print('not found')
```

The reason for that decision is readability in the typical case. Most patterns take a structure
apart and give names to parts of the subject, so the dot-free form is reserved for exactly that;
comparing against a stored value is the rarer case, and for it you have to write something
different.

**How to compare with an existing value:**
- move the constant into a class or an enum and use a dotted name: `case Status.ACTIVE:`;
- collect the constants in a module and write `case codes.NOT_FOUND:`;
- use the literal directly when the value is known: `case 404:`;
- as a last resort, a capture with a guard: `case value if value == status:` - though that is just
  an ordinary comparison, only wordier.

The mistake is easy to miss because the code does not fail: the branch simply always fires, and the
variable is quietly overwritten. Static analysers mostly warn about the unreachable cases that
follow - and that is the most reliable signal that a capture was written where a comparison was
meant.[^py314-reference-expressions]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
