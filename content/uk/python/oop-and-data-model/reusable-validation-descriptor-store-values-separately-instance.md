---
id: py-oop-0012
title: "Як reusable validation descriptor має зберігати значення окремо для кожного instance, не створюючи shared state між об’єктами?"
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
  - source_id: py314-reference-datamodel-object-set-name
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__set_name__
  - source_id: py314-howto-descriptor-managed-attributes
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#managed-attributes
  - source_id: py314-howto-descriptor-automatic-name-notification
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#automatic-name-notification
---

## Short answer

**Descriptor зберігає дані не в собі (бо він один на клас), а в `instance.__dict__` під службовим ключем, ім’я якого визначається через `__set_name__`.**[^py314-howto-descriptor-managed-attributes] `__set_name__` викликається під час створення класу й передає descriptor-у ім’я атрибута; descriptor обчислює private name (наприклад, `'_' + name`) і зберігає та читає значення через `setattr(obj, self.private_name, value)` і `getattr(obj, self.private_name)`.[^py314-reference-datamodel-object-set-name] Так один descriptor-об’єкт на клас обслуговує багато instance без shared mutable state.

## Detailed explanation

Головна пастка тут у тому, де живе descriptor. Він один на клас, бо лежить у `class.__dict__`. Якщо записати значення в `self.value` самого descriptor-а, усі instance ділитимуть одне значення. Тому descriptor тримає правила (ім’я, межі, перевірку), а значення зберігає в кожному instance.

Ім’я для ключа дає `__set_name__`. Під час створення класу `type.__new__` знаходить descriptor-и з цим методом і викликає його з класом-власником та ім’ям атрибута.[^py314-reference-datamodel-object-set-name] Далі descriptor будує службовий ключ (тут `_price`) і зберігає значення в `obj.__dict__` через `setattr`. Публічний атрибут лежить у класі як descriptor, а фактичні дані в instance dictionary.[^py314-howto-descriptor-managed-attributes] Ключ `_price` є лише домовленістю: `a._price` доступний будь-кому, бо Python приватності не забезпечує.

Приклад: descriptor перевіряє додатність і зберігає значення окремо для кожного instance. Коментарі показують результат запуску (CPython 3.14):

```python
class Positive:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = "_" + name       # key used in the instance __dict__

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self                      # accessed on the class
        return getattr(obj, self.private_name)

    def __set__(self, obj, value):
        if value <= 0:
            raise ValueError(f"{self.public_name} must be positive")
        setattr(obj, self.private_name, value)

class Item:
    price = Positive()
    qty = Positive()

a = Item()
b = Item()
a.price = 10
b.price = 20
print(a.price, b.price)              # 10 20: each instance keeps its own value
print(a.__dict__)                    # {'_price': 10}: the data lives on the instance
try:
    b.qty                            # no value has been stored yet
except AttributeError:
    print("qty is not set")          # qty is not set
```

Межі. `__set_name__` спрацьовує лише при створенні класу: descriptor, доданий пізніше через `setattr`, не отримає імені, доки ви не викличете `__set_name__` вручну.[^py314-howto-descriptor-automatic-name-notification] Той самий descriptor-об’єкт у двох класах отримає два виклики `__set_name__`, і останній перезапише `public_name` і `private_name`, тож на кожен атрибут потрібен окремий descriptor. Також `getattr` для ще не заданого значення піднімає `AttributeError`, тому `__get__` має або повертати значення за замовчуванням, або явно повідомляти про відсутність.

**Типові помилки:**
- писати значення в `self.value` descriptor-а: одне значення на весь клас;
- використовувати один і той самий descriptor-об’єкт для кількох атрибутів чи класів;
- вважати `_name` приватним: до нього можна звернутися напряму, а така назва може збігтися з іншим атрибутом.
