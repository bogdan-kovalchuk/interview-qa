---
id: py-modimp-0009
title: "The modules `orders` and `payments` import each other for the sake of a shared protocol: which dependency-direction refactoring removes the cycle better than a local import?"
description: "Move the shared protocol (or abstract base class) into a third module, such as interfaces.py, so that orders and payments depend on it instead of on each other."
track: python
section: modules-and-imports
level: senior
type: practical
tags: [orders, payments]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  uk: 2
anki:
  export: true
sources:
  - source_id: py314-reference-import
    title: "Python 3.14: Reference/import"
    url: https://docs.python.org/3.14/reference/import.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py314-library-importlib
    title: "Python 3.14: Library/importlib"
    url: https://docs.python.org/3.14/library/importlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Official Python 3.14 documentation."
  - source_id: py-packaging-guide
    title: "Python Packaging User Guide"
    url: https://packaging.python.org/en/latest/tutorials/packaging-projects/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Official Python Packaging User Guide."
  - source_id: py314-library-typing-nominal-vs-structural-subtyping
    title: "Python 3.14: Library/typing (Nominal vs structural subtyping)"
    url: https://docs.python.org/3.14/library/typing.html#nominal-vs-structural-subtyping
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Structural compatibility of protocols: a class matches a protocol without explicit inheritance, and a static type checker verifies it."
---

## Short answer

**Move the shared protocol (or abstract base class) into a third module, such as `interfaces.py`, so that `orders` and `payments` depend on it rather than on each other.** A protocol defines a structure that a static type checker verifies, and a class matches it without explicit inheritance, so `payments` does not need to import the interface module.[^py314-library-typing-nominal-vs-structural-subtyping] The `interfaces` module then depends on neither side, and the cycle becomes a hierarchy. A local import inside a function only postpones the import; the dependency between the modules remains.

## Detailed explanation

A cycle between `orders` and `payments` means that each module, at module level, imports a name from the other. It fails when a `from` import, run while a module is loading, asks for a name that is not bound yet. The result depends on the entry point: if `Order` is defined above the import line in `orders.py`, entering through `orders` works, while entering through `payments` fails. So moving the import statement is not enough: the direction of the dependencies has to change, meaning what each module depends on. There are three options:

- **A local import** inside a function removes the cycle from load time, but the dependency remains, merely hidden.
- **Shared data** moves to a third module when both sides need the same fields, for example a dataclass `Order`.
- **Shared behaviour** is described by a protocol in `interfaces.py`, and the concrete payment object is passed in as an argument: `orders` depends on `interfaces`, `payments` depends on nothing, and `main.py` does the wiring.

An illustrative version after the refactoring (output checked on 3.12, 3.13 and 3.14):

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

The protocol is checked by a static type checker.[^py314-library-typing-nominal-vs-structural-subtyping] At run time Python itself does not verify the method signatures. Without the refactoring the cycle fails on `import orders` when `Order` is defined below the `from payments import ...` line in `orders.py`: `payments.py` does `from orders import Order` at module level, and `Order` is not defined yet (checked on 3.12, 3.13 and 3.14).

**Common mistakes:**
- assuming that a local import "fixes" the architecture: it only postpones the import, and the dependency remains;
- putting the concrete `orders` or `payments` classes into `interfaces.py`: then the third module imports both again, and the cycle returns;
- choosing an ABC over a protocol without a reason: an ABC usually requires explicit subclassing, so the implementation must import `interfaces`.

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
