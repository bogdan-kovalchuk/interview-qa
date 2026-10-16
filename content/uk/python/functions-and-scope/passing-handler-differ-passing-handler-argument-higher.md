---
id: py-funcs-0020
title: "Чим відрізняється передавання `handler` від передавання `handler()` як аргументу функції вищого порядку?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-reference-datamodel-objects-values-and-types
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#objects-values-and-types
  - source_id: py314-reference-expressions-calls
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#calls
  - source_id: py314-reference-expressions-lambdas
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#lambdas
---

## Short answer

**`handler` передає сам function object (callable), який функція вищого порядку може викликати пізніше; `handler()` негайно викликає функцію й передає її результат.**[^py314-reference-datamodel-objects-values-and-types] Типова помилка: `register(handler())` реєструє значення, що повертає `handler`, а не саму функцію. Якщо `handler` повертає `None`, реєструється `None`.

## Detailed explanation

Різниця в тому, що саме стоїть у виразі: ім’я функції чи її виклик. Вираз `handler` дає сам function object, тобто посилання на об’єкт, який можна викликати будь-коли пізніше. Вираз `handler()` є викликом: Python спершу виконує функцію, і її результат стає значенням аргумента. Усі вирази аргументів обчислюються до того, як виклик узагалі починається.[^py314-reference-expressions-calls] Тому в `register(handler())` спочатку виконується `handler()`, і лише потім `register` отримує те, що той повернув.

Функція вищого порядку бачить лише готове значення аргумента. Вона очікує callable і викличе його у власний момент. Якщо замість callable прийшов результат, помилка проявиться не там, де її допущено, а пізніше, коли хтось спробує викликати збережене значення.

Приклад показує обидва варіанти. Виклик `register(on_start)` зберігає function object і нічого не друкує. Виклик `register(on_start())` виконує функцію одразу, тому `started` з’являється під час реєстрації, а в список потрапляє `None`:

```python
handlers = []

def register(callback):
    handlers.append(callback)

def on_start():
    print("started")

register(on_start)      # stores the function object, prints nothing
register(on_start())    # prints "started" now, stores None
print([type(h).__name__ for h in handlers])  # ['function', 'NoneType']

try:
    for h in handlers:
        h()             # the first call prints "started"; calling None fails
except TypeError as e:
    print("TypeError:", e)  # TypeError: 'NoneType' object is not callable
```

Помилка відкладена: цикл викликає збережені об’єкти, і `None` викликати не можна, тому виконання падає з `TypeError`, хоча неправильний виклик стояв раніше, в іншому місці коду.

Якщо handler потребує аргументів, `register(handler(42))` знову виконує функцію одразу. Щоб відкласти виклик з аргументом, передайте `lambda: handler(42)`. Lambda сама є function object, і вона викличе `handler` з аргументом лише тоді, коли її викличе функція вищого порядку.[^py314-reference-expressions-lambdas]

**Типові помилки:**
- писати `register(handler())` замість `register(handler)`: реєстрація проходить без винятку, тому помилку легко не помітити;
- вважати, що `handler()` лише передає функцію далі: насправді вона виконується тут і зараз;
- передавати `handler(42)` там, де потрібен відкладений виклик; замість цього використати `lambda: handler(42)`.
