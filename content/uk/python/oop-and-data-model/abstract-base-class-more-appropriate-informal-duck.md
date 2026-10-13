---
id: py-oop-0025
title: "Коли abstract base class доречніша за неформальну duck typing перевірку?"
description: "ABC доречні, коли потрібен контракт, що перевіряється при створенні instance, або явна реєстрація virtual subclass через register(); для простих сценаріїв достатньо duck typing."
track: python
section: oop-and-data-model
level: middle
type: comparison
tags: []
status: published
updated: 2026-10-13
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
  - source_id: py314-howto-descriptor
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-mro
    title: "Python 3.14: Howto/mro"
    url: https://docs.python.org/3.14/howto/mro.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-abc-abstractmethod
    title: "Python 3.14: Library/abc"
    url: https://docs.python.org/3.14/library/abc.html#abc.abstractmethod
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: abc.abstractmethod, вимога метакласу ABCMeta і неможливість створити клас з нереалізованими абстрактними методами."
  - source_id: py314-library-abc-abcmeta-register
    title: "Python 3.14: Library/abc"
    url: https://docs.python.org/3.14/library/abc.html#abc.ABCMeta.register
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: ABCMeta.register і віртуальні підкласи, для яких issubclass() і isinstance() дають True."
  - source_id: py314-library-abc-abcmeta-subclasshook
    title: "Python 3.14: Library/abc"
    url: https://docs.python.org/3.14/library/abc.html#abc.ABCMeta.__subclasshook__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: ABCMeta.__subclasshook__ і його значення True, False або NotImplemented, з прикладом перевірки наявності __iter__."
  - source_id: py314-library-typing-runtime-checkable
    title: "Python 3.14: Library/typing"
    url: https://docs.python.org/3.14/library/typing.html#typing.runtime_checkable
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: runtime_checkable, який перевіряє лише наявність методів або атрибутів, а не їхні сигнатури й типи."
---

## Short answer

**ABC доречніший, коли потрібен контракт, що перевіряється раніше: клас, який наслідує `ABC` (метаклас `ABCMeta`) і не реалізує всі `abstractmethod`, створити не можна.**[^py314-library-abc-abstractmethod] Метод `register()` оголошує клас віртуальним підкласом без успадкування, але перевірки наявних методів не робить (у CPython).[^py314-library-abc-abcmeta-register] Для простих сценаріїв, де важлива лише поведінка об’єкта, duck typing достатній і гнучкіший.

## Detailed explanation

Duck typing перевіряє поведінку в момент використання: якщо об’єкт має потрібний метод, код працює; якщо ні, помилка з’являється глибоко в коді, часто як `AttributeError`. ABC переносить перевірку на момент створення екземпляра: клас з нереалізованими абстрактними методами неможливо створити.[^py314-library-abc-abstractmethod] Приклад:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): ...

    @abstractmethod
    def perimeter(self): ...

class Half(Shape):
    def area(self):
        return 2

try:
    Half()
except TypeError as error:
    print(error)   # 3.12+: Can't instantiate abstract class Half without an implementation for abstract method 'perimeter'

class Registered:              # no base class, no methods
    pass

Shape.register(Registered)
print(isinstance(Registered(), Shape))  # True: register() does not check methods
```

Умова важлива: декоратор `abstractmethod` вимагає, щоб метаклас класу був `ABCMeta` або похідним від нього.[^py314-library-abc-abstractmethod] Без `ABC` або `metaclass=ABCMeta` він нічого не забороняє: у CPython клас з `@abstractmethod` без `ABCMeta` створюється без помилки.

`isinstance()` і `issubclass()` можна розширити двома способами. `register()` робить клас віртуальним підкласом, тому перевірка дає `True` навіть без успадкування.[^py314-library-abc-abcmeta-register] Наявність методів при цьому не перевіряється (у CPython). Це явна заява автора, а не перевірка структури. Метод `__subclasshook__` дає власну логіку: він повертає `True`, `False` або `NotImplemented`, і його можна написати так, щоб перевіряти наявність потрібних методів; документація показує приклад з `__iter__`.[^py314-library-abc-abcmeta-subclasshook]

Для структурної перевірки без успадкування є `typing.Protocol`. Декоратор `@runtime_checkable` дозволяє `isinstance()` з протоколом, але така перевірка бачить лише наявність методів або атрибутів, а не їхні сигнатури чи типи.[^py314-library-typing-runtime-checkable]

**Типові помилки:**
- вважати, що `@abstractmethod` без `ABC` або `ABCMeta` щось забороняє;
- вважати, що `register()` перевіряє методи класу (у CPython не перевіряє);
- вважати, що `isinstance()` з `@runtime_checkable` Protocol перевіряє сигнатури методів.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
