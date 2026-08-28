---
id: py-syntax-0007
title: "When does the `else` block of a `for` or `while` loop run, and how does `break` change that behaviour?"
description: "When does the `else` block of a `for` or `while` loop run, and how does `break` change that behaviour?"
track: python
section: syntax-and-control-flow
level: middle
type: mechanism
tags: [break]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/loops.md#L3-L34
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`else` runs when the loop finishes naturally (the iterable is exhausted or the condition became false), and is skipped if a `break` fired.**[^py314-reference-expressions] For `for`: `else` runs after the iterator is exhausted. For `while`: `else` runs when the condition becomes false. `continue` does not prevent `else` from running, as long as the loop later ends normally.

## Detailed explanation

A loop `else` does not mean "otherwise" but "if the loop reached the end on its own". It runs
exactly when the loop ended naturally: the iterable was exhausted in a `for`, or the condition
became false in a `while`.[^py314-reference-compound-stmts]

The only thing that cancels it is `break`. Neither `continue`, nor an exception, nor `return` has
anything to do with it: the first does not stop the loop from reaching its end, and the last two
take control out of the construct entirely, so `else` never comes up.

The most useful case is a search, where "found it" has to be told apart from "went through
everything and did not find it". Without `else` a flag is introduced for that.

```python
for item in items:
    if item.matches(query):
        found = item
        break
else:
    raise LookupError('nothing matched')   # runs only if the loop was not broken
```

The same code with a flag is longer and carries an extra variable whose state has to be tracked:

```python
found = None
for item in items:
    if item.matches(query):
        found = item
        break
if found is None:
    raise LookupError('nothing matched')
```

The name really is unfortunate - the language's own author admitted as much. Read `for ... else` as
"nothing interrupted the loop", not as a counterpart to `if`.

**What to remember about the behaviour:**
- an empty iterable is also a natural completion, so `else` runs even though the loop body never
  did;
- a `while` whose condition is false immediately behaves the same way: the body did not run, the
  `else` did;
- `continue` changes nothing: the loop can still end naturally and run the `else`;
- an exception inside the loop skips `else`, because control leaves the construct other than by
  normal completion.[^py314-reference-simple-stmts]

Because the semantics of `for ... else` are unknown to most readers, it is worth either adding a
short comment or reserving it for cases where the flag alternative really is noticeably
worse.[^py314-reference-expressions]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
