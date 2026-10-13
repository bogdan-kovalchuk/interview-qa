---
id: py-excpt-0013
title: "Чому один `except*` може обробити лише підгрупу exceptions, а решта group продовжить propagation?"
description: "Кожен except* розщеплює групу через split() на збіг і решту; handler отримує лише збіг, а решта переходить до наступних except* і далі вгору."
track: python
section: exceptions
level: senior
type: mechanism
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
  - source_id: py314-reference-compound-stmts-except-star
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#except-star
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: семантика except*, розщеплення групи, передача необробленої частини далі та заборона змішувати except і except* в одному try."
  - source_id: pep-0654-exception-groups
    title: "PEP 654: Exception Groups and except*"
    url: https://peps.python.org/pep-0654/
    accessed: 2026-10-13
    kind: spec
    version: "3.11"
    applicability: "PEP 654: ExceptionGroup і except* запропоновано для Python 3.11 (Python-Version: 3.11)."
---

## Short answer

**Кожен `except*` розщеплює групу через `split()` на збіг і решту: handler отримує лише збіг, а решта переходить до наступних `except*`.**[^py314-reference-compound-stmts-except-star] Після всіх clauses необроблена частина об’єднується з exception, піднятими в handlers, і поширюється далі. Так різні рівні call stack можуть обробляти різні типи з однієї групи.

## Detailed explanation

`except*` (з Python 3.11) фільтрує групу, а не ловить один exception.[^pep-0654-exception-groups] Коли в `try` піднято `ExceptionGroup`, кожен `except*` розщеплює її на підгрупу збігів і підгрупу решти. Якщо збіг не порожній, він стає обробленим exception, потрапляє до змінної clause, і виконується тіло. Решта переходить до наступного `except*`.[^py314-reference-compound-stmts-except-star]

Розщеплення робить `split()`. Він повертає пару `(match, rest)`, де `match` – це `subgroup(condition)`, а `rest` – решта; порожня частина дорівнює `None`. Структура вкладених груп зберігається, а `message`, `__cause__` і `__context__` переходять до обох частин.[^py314-library-exceptions]

Нижче `process()` обробляє лише `ValueError`. Підгрупа з `OSError` не збігається, тому піднімається далі до зовнішнього `try`. Збіг завжди приходить як група, навіть з одним exception:

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

Обробка не «з’їдає» групу. Якщо handler піднімає новий exception, він об’єднується з рештою в одну групу.[^py314-reference-compound-stmts-except-star] Тож `except*` або обробляє збіг, або передає решту далі, а рішення щодо решти ухвалюють зовнішні рівні.

**Типові помилки:**
- вважати, що `eg` у `except*` – це один exception: він завжди `ExceptionGroup`, а самі exceptions лежать у `eg.exceptions`;
- змішувати `except` і `except*` в одному `try`: це синтаксична помилка;[^py314-reference-compound-stmts-except-star]
- очікувати, що необроблена частина зникне: якщо її не обробить жоден рівень, вона піднімається як група й завершує програму з трасуванням.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
