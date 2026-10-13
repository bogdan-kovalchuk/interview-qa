---
id: py-excpt-0008
title: "Коли використовують bare `raise` усередині handler і чому `raise exc` може змінити traceback presentation?"
description: "Bare raise всередині except повторно кидає той самий exception object без зміни traceback; raise exc додає поточний frame до traceback."
track: python
section: exceptions
level: middle
type: mechanism
tags: [raise-exc]
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
  - source_id: py314-reference-simple-stmts-the-raise-statement
    title: "Python 3.14: Reference/simple Stmts"
    url: https://docs.python.org/3.14/reference/simple_stmts.html#the-raise-statement
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: оператор raise, bare raise як повторне піднімання активного exception і зміна поведінки з 3.11 для зміненого traceback."
---

## Short answer

**Bare `raise` всередині `except` повторно піднімає активний exception.**[^py314-reference-simple-stmts-the-raise-statement] У CPython bare `raise` не додає запису для свого рядка, тож traceback зберігає місце, де exception було піднято вперше. `raise exc`, навіть з тим самим об’єктом, додає запис для рядка `raise exc` перед початковим traceback, тому та сама функція з’являється у звіті двічі.

## Detailed explanation

Bare `raise` без аргументів повторно піднімає exception, який зараз обробляється (active exception). Так виглядає типовий шаблон «записати в лог або прибрати ресурси і передати далі»: обробник не створює новий об’єкт, а піднімає той самий.[^py314-reference-simple-stmts-the-raise-statement] Поза обробкою активного exception немає, і тоді bare `raise` сам піднімає `RuntimeError`.

Traceback – це ланцюжок записів, по одному на кожен frame, через який exception пройшов. У CPython bare `raise` не створює запис для свого рядка: exception продовжує шлях із наявним ланцюжком, тому звіт показує місце, де exception піднято вперше. Документація окремо фіксує зміну з 3.11: якщо traceback активного exception змінено в `except`, наступний `raise` піднімає exception зі зміненим traceback, а раніше використовувався traceback, що був на момент перехоплення.[^py314-reference-simple-stmts-the-raise-statement]

`raise exc` трактується як звичайне піднімання об’єкта, у якого вже є `__traceback__`. У CPython додається запис для поточного рядка, а старі записи лишаються за ним. Тому в звіті є і рядок `raise exc`, і рядок початкового виклику тієї самої функції, і здається, що помилка пройшла через обробник двічі, хоча сталася один раз. Тип і значення exception при цьому не змінюються; змінюється лише те, що бачить читач звіту.

Приклад: обидві функції викликають `inner()`, яка піднімає `ValueError`. Результат виведено через `traceback.extract_tb`, він однаковий на CPython 3.13 і 3.14.

```python
import traceback

def inner():
    raise ValueError("original")

def bare():
    try:
        inner()
    except ValueError:
        raise  # re-raises the active exception, adds no entry for this line

def same_object():
    try:
        inner()
    except ValueError as exc:
        raise exc  # adds an entry for this line in front of the original frames

for fn in (bare, same_object):
    try:
        fn()
    except ValueError as err:
        print(fn.__name__, [(f.name, f.lineno) for f in traceback.extract_tb(err.__traceback__)])
# bare [('<module>', 20), ('bare', 8), ('inner', 4)]
# same_object [('<module>', 20), ('same_object', 16), ('same_object', 14), ('inner', 4)]
```

**Типові помилки:**
- писати `raise err` замість `raise` в обробнику, який лише логує: з’являється зайвий запис у traceback;
- бачити одну функцію двічі у звіті й шукати другу помилку: помилка одна, а другий запис додав `raise exc`;
- викликати bare `raise` поза `except`: отримаєте `RuntimeError: No active exception to reraise`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
