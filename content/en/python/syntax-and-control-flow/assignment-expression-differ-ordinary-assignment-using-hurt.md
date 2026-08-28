---
id: py-syntax-0005
title: "How does the assignment expression `:=` differ from an ordinary assignment, and when does using it hurt readability?"
description: "How does the assignment expression `:=` differ from an ordinary assignment, and when does using it hurt readability?"
track: python
section: syntax-and-control-flow
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/syntax.md#L229-L251
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Community source used to discover the topic; the answer text is independently written and does not copy this source."
---

## Short answer

**`:=` is an expression: it assigns a value and returns it, whereas `=` is a statement and has no value.**[^py314-reference-expressions] `:=` is useful when the computed value is needed both in the condition and in the body of the block (`while (chunk := f.read(8192)):`, for instance). <span class="warn">Overusing it in complex conditions or nested expressions hurts readability</span>, because it mixes the side effect of assignment into the logic of the expression. Added in Python 3.8 (PEP 572).

## Detailed explanation

The difference between `=` and `:=` is the difference between a statement and an expression. A
statement executes and has no value; an expression evaluates and does have one. That is exactly why
`=` cannot go inside a condition and `:=` can.[^py314-reference-simple-stmts]

The practical benefit is a single one: the value is needed twice - in the condition itself and in
the body of the block - and without `:=` you must either duplicate the call or write a `while True`
loop with a `break` in the middle.

```python
# without :=  - the read is duplicated, once before the loop and once inside it
chunk = f.read(8192)
while chunk:
    process(chunk)
    chunk = f.read(8192)

# with :=  - one call, in one place
while chunk := f.read(8192):
    process(chunk)
```

The same gain appears in a comprehension, where without `:=` an expensive computation would have to
run twice: once in the filter condition, once in the result expression.

```python
results = [y for x in data if (y := transform(x)) is not None]
```

`:=` has the lowest precedence of the operators, so parentheses are needed almost whenever the
expression is not a whole operand. `if (n := len(items)) > 10:` without parentheses would mean
`n := (len(items) > 10)` - an entirely different assignment.[^py314-reference-expressions]

**When `:=` hurts readability:**
- in a compound condition with `and`/`or`, where the reader has to track which operands were
  evaluated at all because of short-circuiting;
- when the assigned name is used far below in the code - the variable appeared "somewhere inside
  parentheses", and its birthplace is hard to find;
- in nested expressions, where several `:=` on one line turn the expression into a sequence of side
  effects;
- where an ordinary line with `=` before the `if` reads just as well - there `:=` saves a line and
  spends attention.

A limitation that occasionally surprises: `:=` cannot be used as a standalone top-level statement.
`x := 5` is a syntax error, because it is an expression rather than an assignment; ordinary
assignment is what `=` is for. Likewise `:=` does not work with attributes or indices: only plain
names can be targets.[^py314-reference-expressions]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
