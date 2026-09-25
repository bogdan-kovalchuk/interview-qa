---
id: py-objtypes-0021
title: "Коли `isinstance()` є доречним runtime check, а коли protocol або duck typing робить код менш зв’язаним із concrete classes?"
description: "isinstance() доречний на межі API для швидких guards, у dispatch-логіці (наприклад серіалізація) та з ABC для virtual subclasses."
track: python
section: objects-and-types
level: middle
type: comparison
tags: [isinstance]
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-copy
    title: "Python 3.14: Library/copy"
    url: https://docs.python.org/3.14/library/copy.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-typing
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`isinstance()` доречний на межі API для швидких guards, у dispatch-логіці (наприклад серіалізація) та з ABC для virtual subclasses.**[^py314-reference-datamodel] Проте перевірка щодо конкретного класу tightly couple до ієрархії успадкування. `typing.Protocol` з `@runtime_checkable` та duck typing перевіряють поведінку (наявність методів/атрибутів) без вимоги конкретних класів. Duck typing ловить `AttributeError` під час виконання, а `@runtime_checkable` Protocol перевіряє лише наявність атрибутів, не сигнатури методів.

## Detailed explanation

Функція `isinstance()` призначена для номінальної перевірки типів та ієрархій успадкування, тоді як duck typing та `typing.Protocol` фокусуються на структурній сумісності об'єктів – наявності необхідних методів та атрибутів замість їхнього походження.[^py314-reference-datamodel]

Пряма перевірка `isinstance(obj, ConcreteClass)` є виправданою на межах системи, де потрібно захиститися від неочікуваних типів (наприклад, розрізнити рядок `str` та довільну послідовність `list` чи `Iterable`), а також у механізмах dispatch (як-от `functools.singledispatch` або серіалізатори даних). Крім того, Abstract Base Classes (ABC) дозволяють реалізувати механізм `__instancecheck__` та віртуальні підкласи за допомогою методу `register()`, уникаючи прямого успадкування, але зберігаючи перевірку через `isinstance()`.[^py314-reference-datamodel] Проте жорстка прив'язка до конкретних реалізацій порушує принцип підстановки Лісков та заважає тестуванню (mocking).

Duck typing реалізує ідіому EAFP (*Easier to Ask for Forgiveness than Permission*): замість попередніх інспекцій код одразу виконує потрібну операцію й перехоплює `AttributeError` чи `TypeError`. Декоратор `@runtime_checkable` для `typing.Protocol` надає зручний міст між статичною типізацією та runtime-перевірками, дозволяючи використовувати `isinstance(obj, MyProtocol)`.[^py314-library-typing] Проте у runtime `@runtime_checkable` перевіряє виключно наявність атрибутів (`hasattr`), повністю ігноруючи типи аргументів, їхню кількість та тип значення, що повертається.

Різниця між номінальною перевіркою, `@runtime_checkable` та duck typing:

```python
from typing import Protocol, runtime_checkable

@runtime_checkable
class Closable(Protocol):
    def close(self) -> None:
        ...

class Resource:
    def close(self) -> None:
        pass

class FaultyResource:
    close: int = 1  # attribute exists, but it is not callable

res = Resource()
faulty = FaultyResource()

# Protocol with @runtime_checkable inspects structural attributes via isinstance:
print(isinstance(res, Closable))     # True
print(isinstance(faulty, Closable))  # True: only checks hasattr(obj, 'close')!

# Duck typing (EAFP) verifies actual invocation at runtime:
def safe_close(obj: object) -> None:
    try:
        obj.close()  # type: ignore[attr-defined]
    except (AttributeError, TypeError):
        pass  # Object does not provide a callable close() method
```

**Типові помилки та практичні обмеження:**
- використання `isinstance(obj, list)` замість перевірки протоколу або ABC (`collections.abc.Sequence`), що ламає роботу з генераторами та кастомними колекціями;
- хибне очікування, що `@runtime_checkable` перевіряє сигнатури функцій або типи параметрів під час виконання;
- надмірне використання `isinstance()` всередині бізнес-логіки, що створює розгалужені ланцюжки `if/elif` замість поліморфізму;
- перехоплення занадто широкого винятку `Exception` замість точкового `(AttributeError, TypeError)` при використанні duck typing.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
