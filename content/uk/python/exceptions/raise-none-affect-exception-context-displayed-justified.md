---
id: py-excpt-0009
title: "Як `raise ... from None` впливає на відображення exception context і коли це виправдано?"
description: "raise NewError(...) from None встановлює __cause__ = None і __suppress_context__ = True, тому traceback приховує implicit __context__."
track: python
section: exceptions
level: senior
type: practical
tags: [raise-from-none]
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

**`raise NewError(...) from None` встановлює `__cause__ = None` і `__suppress_context__ = True`, тому traceback не показує implicit `__context__`.**[^py314-library-exceptions] Оригінальний exception лишається в `__context__` для діагностики, але стандартний traceback його не виводить. Це доречно, коли внутрішній exception є деталлю реалізації, наприклад при перекладі `KeyError` на `AttributeError` у API бібліотеки, і користувачеві він нічого не дає.

## Detailed explanation

Коли `raise` стоїть усередині обробки іншого exception, Python за замовчуванням записує оброблений exception у `__context__` нового, і стандартний traceback показує обидва. Явний `from` замінює цю поведінку: `raise NewError(...) from exc` показує `exc` як причину. `from None` – крайній варіант: він задає `__cause__ = None` і ставить `__suppress_context__ = True`, тож показ `__context__` вимикається.[^py314-library-exceptions] Документація називає це заміною старого exception новим для показу, а старий лишається в `__context__` для налагодження.[^py314-library-exceptions]

Приклад: `get_field` перекладає `KeyError` на власний `NotFound`. Якщо виняток не перехоплено, traceback показує лише `NotFound`; атрибути видно, коли виняток перехоплено:

```python
class NotFound(Exception):
    pass

def get_field(record, name):
    try:
        return record[name]
    except KeyError:
        raise NotFound(f"no field {name!r}") from None  # hides the KeyError in the traceback

try:
    get_field({}, "name")
except NotFound as err:
    print(repr(err.__cause__))       # None
    print(err.__suppress_context__)  # True
    print(repr(err.__context__))     # KeyError('name'), still available
```

Ціна така: з traceback зникає первинна причина – ключ, якого не знайшли, і рядок, де це сталося. Якщо `KeyError` є помилкою в коді, а не очікуваною деталлю, `from None` ускладнює діагностику, бо `__context__` доводиться діставати вручну. Доречний він у вузькому випадку: внутрішній exception є деталлю реалізації, його тип не допоможе викликачу виправити виклик, а новий exception повністю описує помилку. Якщо первинну причину треба показати, краще `from exc`: тоді traceback містить обидва exception.[^py314-library-exceptions]

**Типові помилки:**
- ставити `from None` за замовчуванням, щоб traceback виглядав чистішим, і втрачати причину багу;
- вважати, що `from None` видаляє `__context__`: атрибут лишається, змінюється лише показ;
- обирати `from None`, коли викликачу потрібна причина для діагностики: `from exc` показує обидва exception.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
