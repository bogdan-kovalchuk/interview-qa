---
id: py-excpt-0013
title: "Why can a single `except*` handle only a subgroup of exceptions, while the rest of the group continues to propagate?"
description: "Why can a single `except*` handle only a subgroup of exceptions, while the rest of the group continues to propagate?"
track: python
section: exceptions
level: senior
type: mechanism
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-reference-compound-stmts-except-star
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#except-star
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation: except* semantics, splitting the group, passing the unmatched part on, and the rule that except and except* cannot be mixed in one try."
  - source_id: pep-0654-exception-groups
    title: "PEP 654: Exception Groups and except*"
    url: https://peps.python.org/pep-0654/
    accessed: 2026-10-13
    kind: spec
    version: "3.11"
    applicability: "PEP 654: ExceptionGroup and except* were proposed for Python 3.11 (Python-Version: 3.11)."
---

## Short answer

**Each `except*` splits the group with `split()` into a matching part and a remainder: the handler receives only the match, and the remainder moves on to the next `except*` clauses.**[^py314-reference-compound-stmts-except-star] After all clauses run, the unhandled part is merged with exceptions raised in the handlers and propagates onward. This lets different levels of the call stack handle different types from one group.

## Detailed explanation

`except*` (since Python 3.11) filters a group; it does not catch a single exception.[^pep-0654-exception-groups] When an `ExceptionGroup` is raised in the `try` block, each `except*` clause splits it into a subgroup of matches and a subgroup of non-matches. If the match is not empty, it becomes the handled exception, is assigned to the clause's target, and the clause body runs. The remainder goes to the next `except*` clause.[^py314-reference-compound-stmts-except-star]

The splitting is done by `split()`, which returns a pair `(match, rest)`: `match` is `subgroup(condition)`, and `rest` is the remaining non-matching part; an empty part is `None`. The nesting structure of the group is preserved, and the `message`, `__cause__` and `__context__` values carry over to the result.[^py314-library-exceptions]

Below, `process()` handles only `ValueError`. The `OSError` subgroup does not match there, so it propagates to the outer `try`. The match always arrives as a group, even when it holds one exception:

```python
def load_all():
    raise ExceptionGroup("load failed",
                         [ValueError("bad value"), OSError("disk gone")])

def process():
    try:
        load_all()
    except* ValueError as eg:
        print("handled in process:", eg.exceptions)
    # the OSError part does not match here, so it propagates

try:
    process()
except* OSError as eg:
    print("handled at top level:", eg.exceptions)

# handled in process: (ValueError('bad value'),)
# handled at top level: (OSError('disk gone'),)
```

Handling does not swallow the group. If a handler raises a new exception, it is merged with the remainder into one group.[^py314-reference-compound-stmts-except-star] So an `except*` either handles its match or passes the remainder on, and the outer levels decide what to do with the remainder.

**Common mistakes:**
- assuming that `eg` in `except*` is a single exception: it is always an `ExceptionGroup`, and the individual exceptions are in `eg.exceptions`;
- mixing `except` and `except*` in one `try`, which is a syntax error;[^py314-reference-compound-stmts-except-star]
- expecting the unhandled part to disappear: if no level handles it, it propagates as a group and ends the program with a traceback.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
