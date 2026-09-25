---
id: py-compfn-0008
title: "Функція `retry(operation)` має прийняти behavior ззовні: як first-class function дозволяє передати operation без її негайного виклику?"
description: "У Python функції є об'єктами першого класу: можна передати посилання на функцію (без дужок ()), і retry викличе її всередині, коли потрібно."
track: python
section: comprehensions-and-functional
level: middle
type: practical
tags: [retry-operation]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-howto-functional
    title: "Python 3.14: Howto/functional"
    url: https://docs.python.org/3.14/howto/functional.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-displays-for-lists-sets-and-dict
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**У Python функції є об'єктами першого класу: можна передати посилання на функцію (без дужок `()`), і `retry` викличе її всередині, коли потрібно.**[^py314-howto-functional] Наприклад, `retry(fetch_data)` передає callable, а `retry(fetch_data())` передала б уже виконаний результат. `retry` може приймати `operation: Callable[[], T]` та викликати `operation()` у циклі спроб.

## Detailed explanation

У Python функції є об'єктами першого класу (first-class citizens), тобто їх можна присвоювати змінним, зберігати у структурах даних, повертати з інших функцій і передавати як звичайні аргументи.[^py314-howto-functional] Коли ми передаємо функцію за її іменем без круглих дужок `()`, передається посилання на сам об'єкт функції (callable), а не результат її обчислення. Це дозволяє відкласти виконання коду до потрібного моменту (lazy or deferred execution) і делегувати контроль за викликом зовнішній підпрограмі, такій як `retry`.

Якщо ж випадково викликати функцію в місці передачі аргументу – `retry(operation())`, – інтерпретатор виконає її негайно ще до передачі керування в `retry`. У такому разі `retry` отримає вже повернуте значення або не зможе перехопити виняток, якщо перша ж спроба завершиться помилкою, що повністю руйнує логіку повторних спроб. Передаючи саме callable, функція `retry` отримує змогу викликати `operation()` усередині блоку `try...except`, регулювати паузи між спробами, рахувати лічильник повторень і реагувати лише на очікувані класи винятків.

Коли операція вимагає власних аргументів, властивість first-class function дозволяє елегантно комбінувати її із замиканнями (closures), `functools.partial` або `lambda`-виразами, наприклад `retry(lambda: fetch_user(user_id))` або через передачу `*args` та `**kwargs` безпосередньо в сигнатуру `retry`.

Реалізація патерну `retry` за допомогою передачі callable-об'єкта:

```python
import time
from typing import Callable, TypeVar

T = TypeVar("T")


def retry(operation: Callable[[], T], max_attempts: int = 3, delay: float = 0.1) -> T:
    for attempt in range(1, max_attempts + 1):
        try:
            return operation()  # Called only when retry decides
        except Exception as exc:
            if attempt == max_attempts:
                raise
            time.sleep(delay)
    raise RuntimeError("Unreachable")


# Passing the function reference without parentheses
call_count = 0


def unstable_network_call() -> str:
    global call_count
    call_count += 1
    if call_count < 3:
        raise ConnectionError("Temporary glitch")
    return "success"


result = retry(unstable_network_call)
print(result)
# Output: success
```

**Типові помилки та практичні рекомендації:**
- випадковий виклик функції під час передачі: `retry(fetch())` замість `retry(fetch)`;
- втрата аргументів операції: якщо операція потребує параметрів, передавати `functools.partial(fetch, url)` або `lambda: fetch(url)`, а не викликати функцію заздалегідь;
- поглинання системних винятків: обробляти лише очікувані винятки (наприклад, мережеві чи операційні помилки) замість `except BaseException:`, який перехоплює `KeyboardInterrupt` та `SystemExit`.

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
