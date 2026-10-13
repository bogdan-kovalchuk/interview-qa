---
id: py-excpt-0007
title: "Чим implicit exception chaining відрізняється від явного `raise NewError(...) from original`?"
description: "Implicit chaining автоматично встановлює __context__, коли новий exception виникає під час обробки іншого; явний from встановлює __cause__ і позначає прямий причинний зв’язок."
track: python
section: exceptions
level: middle
type: comparison
tags: [raise-newerror-from-original]
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

**Implicit chaining автоматично встановлює `__context__`, коли новий exception піднімається, поки інший обробляється (зазвичай у `except`-блоці); явний `from` встановлює `__cause__`.**[^py314-library-exceptions] Implicit показується в traceback як «During handling of the above exception, another exception occurred», а явний – як «The above exception was the direct cause of the following exception».[^py314-tutorial-errors] Встановлення `__cause__` також ставить `__suppress_context__ = True`, тому traceback показує `__cause__`, а не `__context__`.[^py314-library-exceptions]

## Detailed explanation

Обидва механізми записують причинний зв’язок в сам об’єкт exception, а не лише в текст traceback. Implicit chaining спрацьовує без окремого рішення автора: якщо новий exception піднімається, поки інший уже обробляється, Python записує оброблений exception у `__context__` нового.[^py314-library-exceptions] Тож зв’язок є побічним ефектом того, де стоїть `raise`, а не окремою дією.

Явний `from` є рішенням автора: `raise NewError(...) from original` записує `original` у `__cause__` і одразу ставить `__suppress_context__ = True`. Стандартний traceback після цього показує ланцюжок за `__cause__` і не показує `__context__`. Сам `__context__` при цьому не стирається: він лишається доступним для налагодження.[^py314-library-exceptions]

Приклад: в обох функціях `NewError` піднімається всередині `except`-блоку, але лише в другій є `from`. Значення нижче перевірено на CPython 3.13 і 3.14, вони однакові.

```python
class NewError(Exception):
    pass

def implicit():
    try:
        {}["key"]
    except KeyError:
        raise NewError("lookup failed")  # __context__ is set automatically

def explicit():
    try:
        {}["key"]
    except KeyError as original:
        raise NewError("lookup failed") from original  # __cause__ is set

try:
    implicit()
except NewError as err:
    print(type(err.__context__).__name__)  # KeyError
    print(err.__cause__)                   # None
    print(err.__suppress_context__)        # False

try:
    explicit()
except NewError as err:
    print(type(err.__context__).__name__)  # KeyError, still set
    print(type(err.__cause__).__name__)    # KeyError
    print(err.__suppress_context__)        # True
```

Стандартний обробник traceback позначає ці випадки різними фразами: для implicit – «During handling of the above exception, another exception occurred», для explicit – «The above exception was the direct cause of the following exception».[^py314-tutorial-errors]

На практиці `from` доречний, коли функція перекладає низькорівневу помилку на рівень свого API і причину треба зберегти. `from None` задає `__cause__ = None` і приховує `__context__` від показу, але не видаляє його.[^py314-library-exceptions]

**Типові помилки:**
- вважати, що implicit chaining треба вмикати: він спрацьовує сам, якщо `raise` виконується під час обробки іншого exception;
- вважати, що `from` стирає `__context__`: атрибут лишається, змінюється лише показ у traceback;
- вважати, що `from` ловить exception: він лише називає причину нового exception, а ловить `except`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
