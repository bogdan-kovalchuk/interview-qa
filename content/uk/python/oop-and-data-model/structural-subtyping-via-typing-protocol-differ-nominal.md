---
id: py-oop-0026
title: "Чим structural subtyping через `typing.Protocol` відрізняється від nominal inheritance через ABC?"
track: python
section: oop-and-data-model
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
  - source_id: py314-howto-descriptor
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html
  - source_id: py314-howto-mro
    title: "Python 3.14: Howto/mro"
    url: https://docs.python.org/3.14/howto/mro.html
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
  - source_id: py314-library-typing-nominal-vs-structural-subtyping
    title: "Python 3.14: Library/typing (Nominal vs structural subtyping)"
    url: https://docs.python.org/3.14/library/typing.html#nominal-vs-structural-subtyping
  - source_id: py314-library-typing-protocol
    title: "Python 3.14: Library/typing (typing.Protocol)"
    url: https://docs.python.org/3.14/library/typing.html#typing.Protocol
  - source_id: py314-library-typing-runtime-checkable
    title: "Python 3.14: Library/typing (typing.runtime_checkable)"
    url: https://docs.python.org/3.14/library/typing.html#typing.runtime_checkable
  - source_id: py314-library-abc-abcmeta-register
    title: "Python 3.14: Library/abc (ABCMeta.register)"
    url: https://docs.python.org/3.14/library/abc.html#abc.ABCMeta.register
  - source_id: py314-library-abc-abcmeta-subclasshook
    title: "Python 3.14: Library/abc (ABCMeta.__subclasshook__)"
    url: https://docs.python.org/3.14/library/abc.html#abc.ABCMeta.__subclasshook__
---

## Short answer

**`Protocol` використовує structural subtyping: клас відповідає йому, якщо має методи з сумісними сигнатурами, без явного успадкування.**[^py314-library-typing-nominal-vs-structural-subtyping] `isinstance` приймає `Protocol` лише з `@runtime_checkable`[^py314-library-typing-protocol] і тоді перевіряє лише наявність атрибутів, а не їхні типи.[^py314-library-typing-runtime-checkable] ABC за замовчуванням nominal: належність задає сам ABC через явне успадкування або `register()`.[^py314-library-abc-abcmeta-register] Але ABC з `__subclasshook__`, наприклад `collections.abc.Iterable`, під час виконання перевіряють структуру.[^py314-library-abc-abcmeta-subclasshook]

## Detailed explanation

Різниця в тому, хто визначає належність класу до типу. Для ABC за замовчуванням належність оголошує сам ABC: клас має явно успадкувати його або бути зареєстрованим. Structural subtyping, на якому побудовано `Protocol`, не вимагає жодного зв’язку між класами: static type checker перевіряє, чи клас має методи з сумісними сигнатурами, і самому класу нічого оголошувати не треба.[^py314-library-typing-nominal-vs-structural-subtyping]

Під час виконання поведінка інша. `isinstance()` приймає `Protocol` лише тоді, коли його позначено `@runtime_checkable`; без декоратора така перевірка дає `TypeError`.[^py314-library-typing-protocol] Декоратор робить перевірку грубою: вона бачить лише наявність атрибутів і методів, а їхні сигнатури ігнорує.[^py314-library-typing-runtime-checkable] Наступний приклад показує, що клас з іншою сигнатурою `close` все одно проходить перевірку:

```python
from typing import Protocol, runtime_checkable


@runtime_checkable
class Closable(Protocol):
    def close(self) -> None: ...


class LogFile:  # no base class: only the method matters
    def close(self) -> None:
        pass


class Socket:
    def close(self, force: bool) -> None:  # different signature
        pass


print(isinstance(LogFile(), Closable))  # True
print(isinstance(Socket(), Closable))   # True: the runtime check ignores signatures
```

Реєстрація через `register()` працює інакше: клас записується як virtual subclass ABC, без перевірки структури. Після цього `isinstance()` і `issubclass()` вважають його підкласом, але ABC не з’являється в MRO цього класу, а його методи не викликаються навіть через `super()`.[^py314-library-abc-abcmeta-register] Метод `__subclasshook__` дає ще один спосіб: ABC сам вирішує, чи вважати клас підкласом, наприклад за наявністю методу в `__dict__` класу.[^py314-library-abc-abcmeta-subclasshook]

На практиці `Protocol` зручний, коли описуємо очікувану поведінку чужих об’єктів і достатньо статичної перевірки. ABC доречний, коли спільна реалізація живе в базовому класі або коли належність має бути явною, як у плагінах, що реєструються.

**Типові помилки:**
- вважати, що `isinstance()` з `@runtime_checkable` Protocol перевіряє сигнатури або типи, а не лише наявність атрибутів;
- вважати, що `register()` додає ABC до MRO або переносить його методи в клас;
- викликати `isinstance()` з `Protocol`, який не позначено `@runtime_checkable`: це `TypeError`.
