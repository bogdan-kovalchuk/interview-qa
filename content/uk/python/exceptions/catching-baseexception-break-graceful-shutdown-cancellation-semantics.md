---
id: py-excpt-0003
title: "Коли перехоплення `BaseException` може зламати graceful shutdown або cancellation semantics?"
description: "except BaseException перехоплює SystemExit, KeyboardInterrupt і GeneratorExit, що блокує штатне завершення процесу, зупинку через Ctrl-C та закриття генераторів."
track: python
section: exceptions
level: senior
type: pitfall
tags: [baseexception]
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

**`except BaseException` перехоплює `SystemExit`, `KeyboardInterrupt` і `GeneratorExit`, що блокує штатне завершення процесу, зупинку через Ctrl-C та закриття генераторів.**[^py314-tutorial-errors] <span class="warn">Якщо такий handler не re-raise-ить виняток, інтерпретатор не вийде через `sys.exit()`, а генератор не зможе звільнити ресурси при `.close()`.</span> Виправдано лише на найвищому рівні application loop з явним re-raise або логуванням перед виходом.

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
