---
id: py-decor-0012
title: "Що станеться з decorated name, якщо decorator поверне `None` замість callable?"
description: "Ім'я decorated функції буде зв'язане з None, і будь-який її виклик підніме TypeError: 'NoneType' object is not callable."
track: python
section: decorators
level: middle
type: pitfall
tags: []
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
    version: "3.14"
  flags: []
anki:
  export: true
sources:
  - source_id: py314-glossary-term-decorator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-decorator
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/decorators.md#L112-L120
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Ім'я decorated функції буде зв'язане з `None`, і будь-який її виклик підніме `TypeError: 'NoneType' object is not callable`.**[^py314-glossary-term-decorator] Синтаксис `@decorator` еквівалентний `func = decorator(func)`: що повернув декоратор, те й стане новим значенням імені. Якщо декоратор повертає `None` (явно або через відсутність `return`), початкова функція втрачається.

```python
def bad_decorator(func):
    return None

@bad_decorator
def foo():
    pass

print(type(foo), foo)  # <class 'NoneType'> None

foo()  # TypeError: 'NoneType' object is not callable
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
