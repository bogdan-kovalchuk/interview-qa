---
id: py-excpt-0015
title: "Коли library має emit warning замість raise exception?"
track: python
section: exceptions
sources:
  - source_id: py314-tutorial-errors
    title: "Python 3.14: Tutorial/errors"
    url: https://docs.python.org/3.14/tutorial/errors.html
  - source_id: py314-library-exceptions
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html
  - source_id: py314-reference-compound-stmts-the-try-statement
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#the-try-statement
  - source_id: py314-library-warnings-module
    title: "Python 3.14: Library/warnings"
    url: https://docs.python.org/3.14/library/warnings.html#module-warnings
  - source_id: py314-library-warnings-categories
    title: "Python 3.14: Library/warnings"
    url: https://docs.python.org/3.14/library/warnings.html#warning-categories
  - source_id: py314-library-warnings-warn
    title: "Python 3.14: Library/warnings"
    url: https://docs.python.org/3.14/library/warnings.html#warnings.warn
  - source_id: py314-library-warnings-filter
    title: "Python 3.14: Library/warnings"
    url: https://docs.python.org/3.14/library/warnings.html#the-warnings-filter
---

## Short answer

**Library має emit warning, коли умова не є фатальною, але користувач має про неї знати.**[^py314-library-warnings-module] Типові випадки: застарілий API (`DeprecationWarning`) і сумнівна поведінка під час виконання (`RuntimeWarning`).[^py314-library-warnings-categories] `warnings.warn()` повідомляє і не перериває виконання, а користувач керує реакцією через фільтри, зокрема `error`, що перетворює warning на exception.[^py314-library-warnings-filter] Exception доречний, коли продовження дало б некоректний результат.

## Detailed explanation

Межа проста: exception означає, що виклик не можна коректно виконати, а warning – що виклик виконано, але викликач має знати про щось важливе. Документація модуля `warnings` формулює це так: попередження видають там, де умова, як правило, не виправдовує підняття exception і завершення програми.[^py314-library-warnings-module] Тому застарілий параметр, який ще працює, – це warning, а аргумент, з яким функція не може обчислити результат, – exception.

Категорія має значення, бо від неї залежить, чи побачить користувач попередження. `DeprecationWarning` призначена для інших розробників Python і за замовчуванням ігнорується, якщо її спричинив код поза `__main__`; `UserWarning` є категорією за замовчуванням для `warn()`; `RuntimeWarning` – для сумнівної поведінки під час виконання.[^py314-library-warnings-categories] Параметр `stacklevel=2` змушує `warn()` вказати на рядок викликача, а не на рядок усередині бібліотеки.[^py314-library-warnings-warn]

Нижче `connect()` приймає застарілий `legacy_port`, попереджає про це і працює далі. Порт поза діапазоном піднімає exception, бо продовжувати було б некоректно:

```python
import warnings

def connect(host, *, port=None, legacy_port=None):
    if legacy_port is not None:
        warnings.warn("legacy_port is deprecated; use port",
                      DeprecationWarning, stacklevel=2)  # point at the caller's line
        port = legacy_port
    if port is None:
        port = 443
    if not 0 < port < 65536:
        raise ValueError(f"port out of range: {port}")  # continuing would be wrong
    return f"{host}:{port}"

print(connect("example.org", legacy_port=8443))
# stderr: <file>:14: DeprecationWarning: legacy_port is deprecated; use port
# stderr:   print(connect("example.org", legacy_port=8443))
# example.org:8443

with warnings.catch_warnings():
    warnings.simplefilter("error", DeprecationWarning)  # the user turns the warning into an error
    try:
        connect("example.org", legacy_port=8443)
    except DeprecationWarning as exc:
        print("turned into exception:", exc)
# turned into exception: legacy_port is deprecated; use port

try:
    connect("example.org", port=0)
except ValueError as exc:
    print("raised:", exc)
# raised: port out of range: 0
```

Фільтр залишається у руках користувача: бібліотека вирішує, що попередити, а програма вирішує, що з цим робити, зокрема чи перетворювати warning на помилку.[^py314-library-warnings-filter]

**Типові помилки:**
- піднімати warning там, де далі виконання дасть некоректний результат: користувач побачить текст повідомлення, а дані будуть уже зіпсовані;
- не передавати `stacklevel=2` з бібліотечного `DeprecationWarning`: повідомлення вказуватиме на рядок у бібліотеці, а така категорія за замовчуванням не показується, тож користувач його не побачить;[^py314-library-warnings-categories]
- змінювати глобальні фільтри `warnings` у коді бібліотеки: це впливає на весь процес, а не лише на її виклики.
