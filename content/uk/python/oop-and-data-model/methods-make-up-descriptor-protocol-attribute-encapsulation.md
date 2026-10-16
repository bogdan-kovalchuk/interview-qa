---
id: py-oop-0010
title: "Які методи утворюють descriptor protocol і яку проблему інкапсуляції атрибутів він вирішує?"
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
  - source_id: py314-reference-datamodel-invoking-descriptors
    title: "Python 3.14: Reference/datamodel, Invoking Descriptors"
    url: https://docs.python.org/3.14/reference/datamodel.html#invoking-descriptors
  - source_id: py314-reference-datamodel-implementing-descriptors
    title: "Python 3.14: Reference/datamodel, Implementing Descriptors"
    url: https://docs.python.org/3.14/reference/datamodel.html#implementing-descriptors
  - source_id: py314-reference-datamodel-object-set-name
    title: "Python 3.14: Reference/datamodel, object.__set_name__"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__set_name__
  - source_id: py314-howto-descriptor-validator-class
    title: "Python 3.14: Howto/descriptor, Validator class"
    url: https://docs.python.org/3.14/howto/descriptor.html#validator-class
  - source_id: py314-tutorial-classes-private-variables
    title: "Python 3.14: Tutorial/classes, Private Variables"
    url: https://docs.python.org/3.14/tutorial/classes.html#private-variables
---

## Short answer

**Descriptor protocol складається з методів `__get__`, `__set__` та `__delete__`; клас, що визначає хоча б один із них, є descriptor і дає змогу винести логіку доступу до атрибута (валідацію, обчислення, логування) в окремий об’єкт, зберігаючи звичайний dot-синтаксис.**[^py314-reference-datamodel-invoking-descriptors] Замість того щоб вимагати від користувача викликати `get_x()` / `set_x()`, descriptor перехоплює `obj.x`, коли він знайдений у класі. Так можна змінити внутрішнє зберігання без зміни публічного інтерфейсу, але сам descriptor не робить атрибут приватним.[^py314-tutorial-classes-private-variables]

## Detailed explanation

Descriptor protocol – це три методи: `__get__` для читання, `__set__` для присвоєння і `__delete__` для `del`. Будь-який об’єкт, що визначає хоча б один із них, є descriptor. Python застосовує його тоді, коли знаходить такий об’єкт як атрибут класу під час `obj.x`.[^py314-reference-datamodel-invoking-descriptors] Descriptor має бути в словнику класу або його базового класу, тому descriptor, записаний як атрибут екземпляра, не викликається.[^py314-reference-datamodel-implementing-descriptors]

Проблему, яку він вирішує, видно з альтернатив. Звичайний атрибут не дає місця для контролю: якщо пізніше знадобиться валідація, доведеться змінити всі місця присвоєння. Методи `get_x()` і `set_x()` дають місце для контролю, але змінюють API: кожен виклик треба переписати. Descriptor дає і контроль, і звичайний синтаксис: клас оголошує його один раз, а користувачі пишуть `obj.x = value`. Саме так descriptor керує доступом до атрибута і перевіряє значення перед збереженням.[^py314-howto-descriptor-validator-class]

Приклад: descriptor `Positive` перевіряє значення перед збереженням, а `Box` використовує звичайний синтаксис присвоєння:

```python
class Positive:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name   # where the value is stored on the instance

    def __get__(self, obj, objtype=None):
        if obj is None:                  # accessed on the class, e.g. Box.width
            return self
        return obj.__dict__[self.private_name]

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f'{self.private_name[1:]} must be positive')
        obj.__dict__[self.private_name] = value

    def __delete__(self, obj):
        del obj.__dict__[self.private_name]

class Box:
    width = Positive()
    height = Positive()

    def __init__(self, width, height):
        self.width = width    # calls Positive.__set__
        self.height = height

b = Box(3, 4)
print(b.width * b.height)   # 12: call sites keep plain attribute syntax
print(b.__dict__)           # {'_width': 3, '_height': 4}: the storage is still reachable
try:
    b.width = -1
except ValueError as e:
    print(e)                # width must be positive
```

`__set_name__` викликається під час створення класу і передає descriptor ім’я атрибута, яким його присвоєно. Тому `Positive` знає, що зберігати під `_width`.[^py314-reference-datamodel-object-set-name] Descriptor не робить дані приватними: значення лежить у `b.__dict__` під іменем `_width` і доступне напряму. У Python немає справжніх приватних змінних екземпляра, тож інкапсуляція тут означає контрольований доступ через ім’я атрибута, а не приховування сховища.[^py314-tutorial-classes-private-variables]

**Типові помилки:**
- ставити descriptor у `__init__` як атрибут екземпляра (`self.width = Positive()`): його `__get__` і `__set__` не викликаються;
- не перевіряти `obj is None` у `__get__`: доступ через клас (`Box.width`) тоді падає з `AttributeError`;
- вважати, що descriptor робить дані приватними: `b._width` і `b.__dict__` доступні.
