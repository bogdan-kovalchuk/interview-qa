---
id: py-modimp-0009
title: "Модулі `orders` і `payments` імпортують один одного заради спільного protocol: який dependency-direction refactoring усуне cycle краще за local import?"
description: "Винести спільний protocol (або abstract base class) у третій модуль – наприклад, interfaces.py – щоб orders і payments залежали від нього, а не один від одного."
track: python
section: modules-and-imports
level: senior
type: practical
tags: [orders, payments]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-import
    title: "Python 3.14: Reference/import"
    url: https://docs.python.org/3.14/reference/import.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-importlib
    title: "Python 3.14: Library/importlib"
    url: https://docs.python.org/3.14/library/importlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py-packaging-guide
    title: "Python Packaging User Guide"
    url: https://packaging.python.org/en/latest/tutorials/packaging-projects/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційний посібник із packaging для Python."
  - source_id: py314-library-typing-nominal-vs-structural-subtyping
    title: "Python 3.14: Library/typing (Nominal vs structural subtyping)"
    url: https://docs.python.org/3.14/library/typing.html#nominal-vs-structural-subtyping
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Структурна сумісність протоколів: клас відповідає протоколу без явного успадкування, а перевіряє це статичний type checker."
---

## Short answer

**Винести спільний protocol (або abstract base class) у третій модуль – наприклад, `interfaces.py` – щоб `orders` і `payments` залежали від нього, а не один від одного.** Protocol задає структуру, яку перевіряє статичний type checker, і клас відповідає їй без явного успадкування, тому `payments` не мусить імпортувати модуль з інтерфейсом.[^py314-library-typing-nominal-vs-structural-subtyping] Тоді `interfaces` ні від кого не залежить, і цикл стає ієрархією. Відкладений імпорт усередині функції лише переносить момент імпорту, а залежність між модулями лишається.

## Detailed explanation

Цикл між `orders` і `payments` означає, що кожен модуль на рівні модуля імпортує ім’я з іншого. Він падає тоді, коли `from`-імпорт під час завантаження просить ім’я, яке ще не прив’язане. Результат залежить від того, з якого модуля почали: якщо `Order` визначено вище за рядок імпорту в `orders.py`, вхід через `orders` працює, а вхід через `payments` падає. Тому замінити місце імпорту недостатньо: треба змінити напрям залежностей. Є три варіанти:

- **Відкладений (local) import** усередині функції прибирає цикл із часу завантаження, але залежність лишається, тільки прихованою.
- **Спільні дані** переносять у третій модуль, якщо обидві сторони потребують тих самих полів, наприклад dataclass `Order`.
- **Спільна поведінка** описується protocol у `interfaces.py`, а конкретний платіж передається аргументом: `orders` залежить від `interfaces`, `payments` не залежить ні від кого, а зв’язування робить `main.py`.

Ілюстративний варіант після рефакторингу (вивід перевірено на 3.12, 3.13 і 3.14):

```python
# interfaces.py: imports nothing from orders or payments
from typing import Protocol

class PaymentGateway(Protocol):
    def charge(self, order_id: int, amount: int) -> bool: ...


# orders.py: depends on the protocol, not on payments
from interfaces import PaymentGateway

class OrderService:
    def __init__(self, gateway: PaymentGateway) -> None:
        self._gateway = gateway

    def place(self, order_id: int, amount: int) -> bool:
        return self._gateway.charge(order_id, amount)


# payments.py: satisfies the protocol structurally, imports nothing from orders
class CardPayments:
    def charge(self, order_id: int, amount: int) -> bool:
        print(f"charge order {order_id}: {amount}")
        return True


# main.py: the only module that knows both sides
from orders import OrderService
from payments import CardPayments

service = OrderService(CardPayments())
print(service.place(7, 100))
# charge order 7: 100
# True
```

Протокол перевіряє статичний type checker.[^py314-library-typing-nominal-vs-structural-subtyping] Під час виконання Python сам по собі не звіряє сигнатури методів. Без рефакторингу цикл падає на `import orders`, якщо `Order` визначено нижче за рядок `from payments import ...` у `orders.py`: `payments.py` робить `from orders import Order` на рівні модуля, а `Order` ще не визначено (перевірено на 3.12, 3.13 і 3.14).

**Типові помилки:**
- вважати, що local import «виправляє» архітектуру: він лише відкладає імпорт, а залежність лишається;
- додати в `interfaces.py` конкретні класи `orders` або `payments`: тоді третій модуль знову імпортує обидва, і цикл повертається;
- брати ABC замість protocol без причини: ABC зазвичай вимагає явного успадкування, тож реалізація мусить імпортувати `interfaces`.

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
