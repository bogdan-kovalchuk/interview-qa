---
id: py-oop-0029
title: "Чому class є instance метакласу `type` і які основні етапи проходить class statement до створення class object?"
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
  - source_id: py314-reference-datamodel-metaclasses
    title: "Python 3.14: Reference/datamodel (Metaclasses)"
    url: https://docs.python.org/3.14/reference/datamodel.html#metaclasses
  - source_id: py314-reference-datamodel-creating-the-class-object
    title: "Python 3.14: Reference/datamodel (Creating the class object)"
    url: https://docs.python.org/3.14/reference/datamodel.html#creating-the-class-object
  - source_id: py314-reference-datamodel-object-new
    title: "Python 3.14: Reference/datamodel (object.__new__)"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__new__
  - source_id: py314-reference-datamodel-resolving-mro-entries
    title: "Python 3.14: Reference/datamodel (Resolving MRO entries)"
    url: https://docs.python.org/3.14/reference/datamodel.html#resolving-mro-entries
---

## Short answer

**Клас є instance свого metaclass; якщо metaclass не вказано, ним є `type`, тож `type(MyClass)` дає `type`.**[^py314-reference-datamodel-metaclasses] Етапи: розв’язання MRO entries для bases, визначення metaclass, `__prepare__` для namespace, виконання тіла класу і, нарешті, виклик `metaclass(name, bases, namespace)`.[^py314-reference-datamodel-metaclasses] Цей виклик створює class object; `__init__` виконується після `__new__`, якщо той повернув instance цього metaclass.[^py314-reference-datamodel-creating-the-class-object][^py314-reference-datamodel-object-new]

## Detailed explanation

Клас теж є об’єктом, тож у нього є тип, і цей тип задає metaclass. Коли metaclass не вказано і bases не мають іншого, Python використовує `type`: тіло класу виконується в новому namespace, а ім’я прив’язується до результату `type(name, bases, namespace)`.[^py314-reference-datamodel-metaclasses] Тому `class C` є instance `type`, і `isinstance(C, type)` дає `True`. Базовий клас `Base` при цьому визначає поведінку екземплярів `C`, а не самого класу.

Порядок етапів видно в трасі. Metaclass друкує повідомлення в `__prepare__`, `__new__` і `__init__`, а базовий клас має `__init_subclass__`:

```python
class Meta(type):
    @classmethod
    def __prepare__(mcls, name, bases, **kwargs):
        print("prepare")  # printed 1st
        return {}

    def __new__(mcls, name, bases, namespace, **kwargs):
        print("new")  # printed 3rd
        return super().__new__(mcls, name, bases, namespace)

    def __init__(cls, name, bases, namespace, **kwargs):
        print("init")  # printed 5th
        super().__init__(name, bases, namespace)


class Base:
    def __init_subclass__(cls, **kwargs):
        print("init_subclass")  # printed 4th, inside type.__new__
        super().__init_subclass__(**kwargs)


class Demo(Base, metaclass=Meta):
    print("body")  # printed 2nd, after __prepare__ and before __new__
```

Перед тілом класу Python розв’язує bases, які не є класами: якщо база має `__mro_entries__`, її замінює результат цього методу. Так працюють не-класові бази, наприклад `list[int]`, яку замінює `list`.[^py314-reference-datamodel-resolving-mro-entries] Після створення class object `type.__new__` викликає `__set_name__` для дескрипторів у namespace, потім `__init_subclass__` найближчого батька в MRO. Class decorators застосовуються останніми, уже до готового class object.[^py314-reference-datamodel-creating-the-class-object] Тому декоратор не бачить тіло класу як namespace, він отримує лише результат створення.

**Типові помилки:**
- плутати bases і metaclass: `Base` визначає поведінку екземплярів `Demo`, а `Meta` визначає поведінку самого класу `Demo`;
- вважати, що class decorator бачить namespace тіла класу, а не створений class object;
- очікувати, що `__init__` metaclass’у виконається раніше за `__init_subclass__`: у трасі він іде після.
