---
id: py-excpt-0005
title: "У Python 3.14 що станеться з pending `return` з `try`, якщо `finally` теж виконає `return`, і чому compiler тепер emits `SyntaxWarning` для такого control flow?"
description: "return з finally завжди переважає: функція повертає значення з finally, а pending return з try губиться."
track: python
section: exceptions
level: middle
type: pitfall
tags: [syntaxwarning]
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
execution:
  language: python
  standard: null
  toolchain:
    name: cpython
    version: "3.14.7"
  flags: []
anki:
  export: true
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/exceptions.md#L155-L199
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`return` з `finally` завжди переважає: функція повертає значення з `finally`, а pending `return` з `try` губиться.**[^py314-tutorial-errors] Це останній `return`, який виконується, тому interpreter використовує саме його. У Python 3.14 compiler видає `SyntaxWarning` для `return` у `finally` (PEP 765), бо такий pattern приховує exceptions і ламає очікуваний control flow.

```python
def foo():
    try:
        return 'try'
    finally:
        return 'finally'

foo()  # SyntaxWarning; повертає 'finally'
```

## Detailed explanation

TODO

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
