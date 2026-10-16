---
id: py-funcs-0008
title: "Коли власний sentinel object кращий за `None` як default argument у публічному API?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
  - source_id: py314-reference-expressions-calls
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#calls
  - source_id: py314-reference-expressions-is-not
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#is-not
---

## Short answer

**Sentinel варто використовувати, коли `None` є допустимим значенням параметра і його треба відрізняти від «аргумент не передано».** Коли аргумент пропущено, Python підставляє default у той самий параметр, тож функція бачить лише значення.[^py314-reference-expressions-calls] Наприклад, у `def get(key, default=_MISSING)` виклик `get(key, None)` повертає `None`, якщо ключа немає, а `get(key)` викликає `KeyError`. Sentinel – це приватний `object()`, який порівнюють через `is`, тож звичайний аргумент з ним не збігається.[^py314-reference-expressions-is-not] Якщо `None` не має окремого змісту, простіший звичайний `default=None`.

## Detailed explanation

Значення за замовчуванням – це звичайне значення, яке Python підставляє в параметр, коли аргумент не передано.[^py314-reference-expressions-calls] Всередині функції є лише об’єкт у параметрі, без відомостей про те, передали його чи ні. Тому якщо `None` сам має зміст (наприклад, `ttl=None` означає «ніколи не спливає»), то `default=None` не відрізнить «користувач нічого не передав» від «користувач явно передав `None`».

Sentinel розділяє ці випадки. Це унікальний об’єкт, якого звичайний виклик не має; значення за замовчуванням обчислюється один раз під час `def`, тож усі виклики бачать той самий об’єкт.[^py314-reference-compound-stmts-function-definitions] Функція перевіряє його за ідентичністю:

```python
_MISSING = object()   # private sentinel: callers do not have it by accident

def get(key, default=_MISSING):
    values = {'host': 'localhost'}
    if key in values:
        return values[key]
    if default is _MISSING:
        raise KeyError(key)
    return default

print(get('host'))          # localhost
print(get('port', None))    # None: explicit None is a valid answer
print(get('port', 8080))    # 8080
try:
    get('port')
except KeyError as error:
    print('KeyError', error)  # KeyError 'port'
```

У прикладі `get('port', None)` повертає `None`, бо явне `None` є відповіддю, а `get('port')` кидає `KeyError`, бо сентинел показує, що `default` не задано. Перевірка через `is` потрібна тому, що `x is y` істинне тоді і лише тоді, коли обидва імені посилаються на той самий об’єкт.[^py314-reference-expressions-is-not] Порівняння через `==` ненадійне: об’єкт з власним `__eq__` може вважатися рівним sentinel, і функція піде не тією гілкою.

У публічному API є ціна. `inspect.signature` показує звичайний `object()` як `<object object at 0x…>`, а це мало що каже в документації. Невеликий клас із читабельним `__repr__` вирішує цю проблему. Сентинел також додає ім’я, яке користувач має знати. Тому його варто брати тоді, коли `None` має власний зміст, а не як стилістичний вибір.

**Типові помилки:**
- брати sentinel там, де `None` не має окремого значення, і ускладнювати API без потреби;
- перевіряти sentinel через `==` замість `is`;
- лишати в публічній сигнатурі sentinel без читабельного `repr`, через що в документації видно адресу пам’яті.
