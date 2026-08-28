---
id: py-syntax-0011
title: "Why does the order of `case` clauses in structural pattern matching affect the reachability of the patterns that follow?"
description: "Why does the order of `case` clauses in structural pattern matching affect the reachability of the patterns that follow?"
track: python
section: syntax-and-control-flow
level: middle
type: pitfall
tags: [case]
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

**The case blocks in a `match/case` are checked top to bottom, and after the first successful match its block runs while the rest are ignored.**[^py314-reference-expressions] A broader pattern (a capture variable or the `_` wildcard, for instance) placed before a narrower one therefore makes the latter unreachable - control never arrives there. An irrefutable case block (`case _:`) has to come last, or the case blocks after it will never fire.

## Detailed explanation

`match` is not a jump table and not a search for the best match. It is a sequential check from top
to bottom: the first pattern that matches (and whose guard is true) runs its block, and the rest are
never considered.[^py314-reference-compound-stmts]

The order of the cases is therefore logic, not formatting. A broader pattern placed earlier makes
every narrower one below it unreachable: control simply does not get there.

```python
match command:
    case [action, *rest]:        # matches ANY non-empty sequence
        generic(action, rest)
    case ['quit']:               # unreachable - the case above already matched
        do_quit()
```

This is sharpest with an irrefutable pattern - one that cannot fail to match: a bare name
(`case value:`) or the wildcard (`case _:`). For those the compiler does not even wait for run time:
if such a case is not last, it is a `SyntaxError`.[^py314-reference-expressions]

```python
match value:
    case _:          # SyntaxError: wildcard makes remaining patterns unreachable
        default()
    case 42:
        answer()
```

A guard changes the picture but not the rule. `case x if x > 100:` is not irrefutable, because the
guard may be false, so such a case is allowed before others - and that is exactly how ranges are
written, from narrower to broader.

**How to keep the order right:**
- specific literals and exact structures at the top, general shapes below;
- `case _:` always last, like a `default` in a switch;
- order the guarded variants from the narrowest condition to the broadest, because they too are
  checked in turn;
- if a branch looks dead, it almost always means a too-broad pattern sits above it - in particular a
  capture with a bare name, which matches anything.

Unlike `switch` in C there is no fallthrough here: once a block has run the `match` ends, and no
`break` is needed.[^py314-reference-simple-stmts]

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
