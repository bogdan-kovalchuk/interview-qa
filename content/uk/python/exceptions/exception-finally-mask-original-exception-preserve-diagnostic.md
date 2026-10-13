---
id: py-excpt-0006
title: "Як exception у `finally` може замаскувати original exception і як зберегти діагностичний контекст?"
description: "Якщо finally кидає новий exception, він замінює оригінальний у поширенні, а оригінальний зберігається лише як __context__."
track: python
section: exceptions
level: senior
type: pitfall
tags: []
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
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

**Якщо `finally` піднімає новий exception, він замінює оригінальний у поширенні, а оригінальний лишається лише як `__context__`.**[^py314-reference-compound-stmts-the-try-statement] <span class="warn">Якщо логувати лише новий exception, оригінальна причина зникає з логу.</span> Щоб зберегти контекст, обгорніть cleanup у внутрішній `try/except` усередині `finally` і залогуйте помилку cleanup; збережений оригінальний exception тоді піднімається знову в кінці `finally`.[^py314-reference-compound-stmts-the-try-statement]

## Detailed explanation

Якщо `finally` піднімає новий виняток, поки інший ще поширюється, оригінальний виняток не зникає: він стає `__context__` нового. Документація описує це так: коли виняток піднімається під час обробки іншого, його `__context__` встановлюється автоматично, і обробка може відбуватися й у `finally`.[^py314-library-exceptions] Новий виняток заміщає старий у поширенні, тож `except` далі за стеком бачить лише його.[^py314-reference-compound-stmts-the-try-statement]

```python
def work():
    try:
        raise ValueError("original failure")
    finally:
        raise RuntimeError("cleanup failed")  # replaces the original in flight

try:
    work()
except RuntimeError as e:
    print(e)                          # cleanup failed
    print(repr(e.__context__))        # ValueError('original failure')
```

У CPython стандартний traceback друкує обидва винятки, розділені рядком «During handling of the above exception, another exception occurred». Проблема в коді, який бачить лише новий виняток: він логує тільки його текст або ловить тип оригінального винятку, який до нього вже не доходить.

Безпечніший варіант – обробити помилку cleanup всередині `finally`. Внутрішній `except` її поглинає, тому новий виняток не виникає, і збережений оригінальний виняток піднімається знову в кінці `finally`.[^py314-reference-compound-stmts-the-try-statement]

```python
def work():
    try:
        raise ValueError("original failure")
    finally:
        try:
            raise RuntimeError("cleanup failed")  # stands in for a failing close()
        except RuntimeError as cleanup_error:
            print("cleanup error logged:", cleanup_error)

try:
    work()
except ValueError as e:
    print("original propagated:", e)  # original propagated: original failure
```

У реальному коді замість `print` використовуйте `logging`. Явний ланцюжок через `raise ... from` (`__cause__`) доречний тоді, коли новий виняток справді є наслідком старого, а не незалежною помилкою cleanup.[^py314-library-exceptions]

**Типові помилки:**
- логувати лише `str(e)` нового винятку і втрачати першопричину;
- ловити тип оригінального винятку ззовні, не враховуючи, що піднявся інший тип;
- вважати, що `__context__` завжди видно: код, який друкує лише повідомлення винятку, його не покаже.

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
