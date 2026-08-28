---
id: py-syntax-0003
title: "Why can the construct `value = user_input or default` incorrectly replace a valid value of `0` or an empty string?"
description: "Why can the construct `value = user_input or default` incorrectly replace a valid value of `0` or an empty string?"
track: python
section: syntax-and-control-flow
level: middle
type: pitfall
tags: [value-user-input-or-default]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/coding.md#L3-L20
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`or` returns the first truthy operand, so any falsy value (`0`, `""`, `[]`, `None`) gets replaced by `default`.**[^py314-reference-expressions] If `0` or `""` are valid inputs, the construct cannot tell "no value given" from "a correct falsy value". For an exact check, compare with `None` explicitly: `value = default if user_input is None else user_input`.

## Detailed explanation

`or` does not check "was a value provided" - it checks truthiness. The operator evaluates the left
operand, asks it for `__bool__` (or `__len__`), and returns the left operand if it is truthy,
otherwise the right one.[^py314-reference-expressions]

The problem is that falsy in Python does not mean "empty" or "unset". Falsy is `None`, `False`, `0`,
`0.0`, `''`, `[]`, `{}`, `set()` and any object whose `__len__` returned zero. Half of that is
perfectly correct user data.

```python
def make_port(user_input, default=8080):
    return user_input or default

make_port(0)        # 8080 - but 0 was a deliberate value, not "unset"
make_port('')       # 8080 - an empty string can be a valid name
make_port(None)     # 8080 - this is the only case that was actually meant
```

The correct check compares against whatever actually denotes absence. If absence is denoted by
`None`, then `is None` is what to check - an identity comparison against a single sentinel object,
independent of truthiness.

```python
def make_port(user_input, default=8080):
    return default if user_input is None else user_input
```

When `None` is itself a valid value, a sentinel of your own is needed - a unique object nobody
outside can pass in.

```python
MISSING = object()

def make_port(user_input=MISSING, default=8080):
    return default if user_input is MISSING else user_input
```

**Where this mistake shows up most often:**
- defaults for numeric parameters where `0` is legitimate input (timeout, offset, retries);
- string parameters where an empty string means "explicitly empty" rather than "not specified";
- collections: `items = items or []` quietly swaps the passed empty list for a new one, and a caller
  that expected to mutate the original stops working;
- reading configuration, where `False` is a valid flag value and `or True` turns it into `True`.

`or` stays appropriate where truthiness is the criterion: `name = user_name or 'anonymous'`, when an
empty string really should be treated as no name at all.[^py314-reference-simple-stmts]

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
