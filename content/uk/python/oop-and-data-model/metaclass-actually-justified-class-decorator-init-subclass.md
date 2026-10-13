---
id: py-oop-0030
title: "Коли metaclass справді виправданий, а коли class decorator або `__init_subclass__` дає простіше рішення?"
description: "Metaclass потрібен, щоб втручатися в створення класу, наприклад у namespace через `__prepare__`; для реєстрації й перевірки підкласів простіші `__init_subclass__` або class decorator."
track: python
section: oop-and-data-model
level: senior
type: comparison
tags: [init-subclass]
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
  - source_id: py314-reference-datamodel-preparing-the-class-namespace
    title: "Python 3.14: Reference/datamodel (Preparing the class namespace)"
    url: https://docs.python.org/3.14/reference/datamodel.html#preparing-the-class-namespace
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: метод __prepare__ створює namespace, який отримує тіло класу і передається в __new__ metaclass."
  - source_id: py314-reference-datamodel-creating-the-class-object
    title: "Python 3.14: Reference/datamodel (Creating the class object)"
    url: https://docs.python.org/3.14/reference/datamodel.html#creating-the-class-object
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: class object створюється після виконання тіла класу; type.__new__ викликає __set_name__ і __init_subclass__ батька, потім застосовуються class decorators."
  - source_id: py314-reference-datamodel-customizing-class-creation
    title: "Python 3.14: Reference/datamodel (Customizing class creation)"
    url: https://docs.python.org/3.14/reference/datamodel.html#customizing-class-creation
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: __init_subclass__ викликається для майбутніх підкласів, а не для класу, де визначений; class decorator діє лише на клас, до якого застосований."
  - source_id: py314-reference-datamodel-determining-the-appropriate-metaclass
    title: "Python 3.14: Reference/datamodel (Determining the appropriate metaclass)"
    url: https://docs.python.org/3.14/reference/datamodel.html#determining-the-appropriate-metaclass
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: вибір metaclass за bases; якщо жоден кандидат не є підтипом усіх інших, визначення класу завершується TypeError."
  - source_id: py314-reference-datamodel-special-method-lookup
    title: "Python 3.14: Reference/datamodel (Special method lookup)"
    url: https://docs.python.org/3.14/reference/datamodel.html#special-method-lookup
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: неявні виклики спеціальних методів шукаються в type(obj), а не в екземплярі; для класу це type(cls)."
  - source_id: py314-reference-datamodel-customizing-instance-and-subclass-checks
    title: "Python 3.14: Reference/datamodel (Customizing instance and subclass checks)"
    url: https://docs.python.org/3.14/reference/datamodel.html#customizing-instance-and-subclass-checks
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: __instancecheck__ і __subclasscheck__ у metaclass; abc.ABCMeta реалізує їх для ABC."
---

## Short answer

**Metaclass виправданий, коли треба втрутитися в саме створення класу, наприклад змінити namespace через `__prepare__` або відхилити визначення ще до створення class object.**[^py314-reference-datamodel-preparing-the-class-namespace][^py314-reference-datamodel-creating-the-class-object] `__init_subclass__` викликається для кожного нового підкласу і підходить для реєстрації чи перевірки підкласів без metaclass.[^py314-reference-datamodel-customizing-class-creation] Class decorator діє лише на клас, до якого його застосовано, тож він простіший для одноразової зміни одного класу.[^py314-reference-datamodel-customizing-class-creation]

## Detailed explanation

Metaclass втручається раніше за інші: `__prepare__` створює namespace, у якому виконується тіло класу.[^py314-reference-datamodel-preparing-the-class-namespace] `__init_subclass__` викликається всередині `type.__new__` після створення class object, а class decorator застосовується ще після цього.[^py314-reference-datamodel-creating-the-class-object]

Реєстрація через `__init_subclass__` охоплює всі підкласи, а декоратор діє лише на клас, до якого його явно застосовано:

```python
REGISTRY = []


class Plugin:
    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)
        REGISTRY.append(cls.__name__)


class CsvPlugin(Plugin):
    pass


class JsonPlugin(Plugin):
    pass


print(REGISTRY)  # ['CsvPlugin', 'JsonPlugin']: every subclass is registered


DECORATED = []


def register(cls):
    DECORATED.append(cls.__name__)
    return cls


@register
class XmlPlugin:
    pass


class SubXmlPlugin(XmlPlugin):  # not decorated, so register() never runs for it
    pass


print(DECORATED)  # ['XmlPlugin']
```

`__init_subclass__` не викликається для класу, де його оголошено, а лише для майбутніх підкласів.[^py314-reference-datamodel-customizing-class-creation] А metaclass може відхилити дубль ще в тілі класу, чого `__init_subclass__` не вміє, бо бачить уже перезаписаний атрибут:

```python
class NoDuplicates(dict):
    def __setitem__(self, key, value):
        if key in self and not key.startswith("__"):
            raise TypeError(f"duplicate definition of {key!r}")
        super().__setitem__(key, value)


class StrictMeta(type):
    @classmethod
    def __prepare__(mcls, name, bases, **kwargs):
        return NoDuplicates()


try:
    class Strict(metaclass=StrictMeta):
        def run(self):
            return 1

        def run(self):
            return 2
except TypeError as error:
    print(error)  # duplicate definition of 'run'
```

Metaclass також потрібен, коли треба задати поведінку самого класу. Неявні виклики `__call__`, `__iter__`, `__getitem__` чи `__instancecheck__` шукаються в `type(cls)`, а не на самому класі: присвоєння `C.__iter__` не змінює `for x in C`. Так працюють `ABCMeta` (`__instancecheck__`) і `Enum` (`__iter__`, `__getitem__`).[^py314-reference-datamodel-special-method-lookup][^py314-reference-datamodel-customizing-instance-and-subclass-checks] Decorator і `__init_subclass__` цього не вміють, бо не змінюють `type(cls)`.

На практиці спочатку варто розглянути декоратор або `__init_subclass__`. Metaclass ускладнює композицію: якщо bases мають несумісні metaclass, визначення класу завершується `TypeError`.[^py314-reference-datamodel-determining-the-appropriate-metaclass]

**Типові помилки:**
- брати metaclass для реєстрації, для якої вистачає `__init_subclass__`;
- очікувати, що `__init_subclass__` або декоратор перехопить тіло класу чи замінить metaclass;
- вважати, що class decorator діє на підкласи, або що `__init_subclass__` викликається для класу, де його визначено.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
