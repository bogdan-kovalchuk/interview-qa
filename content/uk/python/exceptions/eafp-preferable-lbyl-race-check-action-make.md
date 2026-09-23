---
id: py-excpt-0014
title: "Коли EAFP доречніший за LBYL і як race між check та action може зробити LBYL некоректним?"
description: "EAFP доречніший, коли перевірка стану не гарантує його незмінність до моменту дії – класичний race TOCTOU (time-of-check to time-of-use)."
track: python
section: exceptions
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-04
content_revision: 1
reconciled_with:
  en: 1
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
---

## Short answer

**EAFP доречніший, коли перевірка стану не гарантує його незмінність до моменту дії – класичний race TOCTOU (time-of-check to time-of-use).**[^py314-tutorial-errors] LBYL спочатку перевіряє умову, потім виконує дію; між цими кроками стан може змінитися (інший потік, мережевий запит, файл видалено). EAFP одразу виконує дію й ловить exception, уникаючи вікна race. Наприклад, замість `if os.path.exists(p): open(p)` надійніше `try: open(p) except OSError`.

## Detailed explanation

TODO

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
