---
id: py-excpt-0005
title: "У Python 3.14 що станеться з pending `return` з `try`, якщо `finally` теж виконає `return`, і чому compiler тепер видає `SyntaxWarning` для такого control flow?"
description: "return з finally завжди переважає: функція повертає значення з finally, а pending return з try губиться."
track: python
section: exceptions
level: middle
type: pitfall
tags: [syntaxwarning]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
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
  - source_id: pep-0765-finally-control-flow
    title: "PEP 765: Disallow return/break/continue that exit a finally block"
    url: https://peps.python.org/pep-0765/
    accessed: 2026-10-13
    kind: spec
    version: null
    applicability: "Специфікація PEP 765: мова дозволяє SyntaxWarning або SyntaxError для return, break і continue, що виходять із finally; попередження очікується під час компіляції, а не для вже скомпільованого коду."
---

## Short answer

**`return` з `finally` завжди переважає: функція повертає значення з `finally`, а pending `return` з `try` губиться.**[^py314-tutorial-errors] Це останній `return`, який виконується, тому interpreter використовує саме його. У Python 3.14 compiler видає `SyntaxWarning` для `return` у `finally`, бо такий pattern приховує exceptions і заплутує control flow.[^py314-tutorial-errors]

```python
def foo():
    try:
        return 'try'
    finally:
        return 'finally'

foo()  # returns 'finally'; CPython 3.14 warns at compile time
```

## Detailed explanation

Коли `try` доходить до `return`, значення вже обчислене, але функція ще не повернулася: спершу виконується `finally`, і результат визначає останній виконаний `return`. Якщо `finally` містить `return`, його значення стає результатом функції, а значення з `try` відкидається. Так само `return`, `break` або `continue` у `finally` відкидає виняток, що летів із `try`: він не піднімається далі.[^py314-reference-compound-stmts-the-try-statement]

```python
def bar():
    try:
        1 / 0                     # raises ZeroDivisionError
    finally:
        return 42                 # the exception is discarded, not re-raised

print(bar())                      # 42
```

У CPython 3.14 компілятор видає `SyntaxWarning` для `return`, `break` або `continue`, які виходять із `finally`. До цього, зокрема в CPython 3.13, такого попередження немає.[^py314-reference-compound-stmts-the-try-statement][^py314-tutorial-errors] Мотивація в тому, що проковтнутий виняток небезпечніший за неправильне значення: він рідше помічається в тестах.[^pep-0765-finally-control-flow]

Мовна специфікація дозволяє `SyntaxWarning` або `SyntaxError`, а PEP 765 очікує, що попередження з’явиться під час компіляції, але не під час виконання вже скомпільованого коду.[^pep-0765-finally-control-flow] На CPython 3.14 воно з’являється при `compile()`, при імпорті без актуального `.pyc` і в `py_compile`, але не при `ast.parse()` і не при імпорті з готовим `.pyc`. Тому інструмент, який лише розбирає код через `ast.parse()`, його не побачить. У CPython 3.14 `return` у вкладеній функції, визначеній у `finally`, попередження не викликає: це вихід із іншої функції, а не з `finally`.

**Типові помилки:**
- вважати, що `return` у `try` спрацює, якщо `finally` теж містить `return`;
- очікувати, що виняток із `try` буде піднятий після `finally` з `return`, `break` або `continue`;
- ігнорувати `SyntaxWarning`, бо код уже працює: попередження видно під час компіляції, а не під час виконання скомпільованого коду.

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
