---
id: py-oop-0007
title: "Чому property зазвичай не можна затінити однойменним значенням в `instance.__dict__`?"
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
  - source_id: py314-howto-descriptor-properties
    title: "Python 3.14: Howto/descriptor, Properties"
    url: https://docs.python.org/3.14/howto/descriptor.html#properties
---

## Short answer

**`property` реалізований як data descriptor (визначає `__get__`, `__set__`, `__delete__`), тому за правилами attribute lookup він має пріоритет над instance `__dict__`.**[^py314-reference-datamodel-invoking-descriptors] Навіть якщо вручну записати `obj.__dict__['x'] = value`, звернення `obj.x` викличе getter property, а не поверне значення зі словника. <span class="warn">Словник досі доступний напряму через `obj.__dict__['x']`, але `obj.x` його не повертає; змінити поведінку `obj.x` можна лише на рівні класу, наприклад замінивши сам property.</span>

## Detailed explanation

Attribute lookup для `obj.x` спершу знаходить `x` у класі. Якщо знайдений об’єкт визначає `__get__` і `__set__` (та/або `__delete__`), це data descriptor, який перекриває словник екземпляра: Python викликає його `__get__` і не читає словник.[^py314-reference-datamodel-invoking-descriptors] `property()` будує саме такий descriptor, який викликає функцію під час доступу до атрибута.[^py314-howto-descriptor-properties] Тому навіть `property` без setter є data descriptor: присвоєння `obj.x = ...` до нього піднімає `AttributeError` і не записує значення в словник.

Приклад: клас з property і значення з тим самим іменем, записане в словник напряму:

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

t = Temperature(20)
t.__dict__['celsius'] = 99     # the dict now holds a value under the same name
print(t.celsius)               # 20: the property wins, the dict entry is ignored
print(t.__dict__['celsius'])   # 99: the value is there, but attribute access never returns it
try:
    t.celsius = 5
except AttributeError as e:
    print(e)                   # property 'celsius' of 'Temperature' object has no setter
```

Слово «зазвичай» у питанні має значення. Пріоритет над словником має лише data descriptor; non-data descriptor, наприклад звичайний метод, словник екземпляра перекриває.[^py314-reference-datamodel-invoking-descriptors] Це і робить property надійним для контролю: логіка getter і setter виконується під час кожного доступу через `obj.x`, тож екземпляр не може обійти її, записавши значення у власний словник.[^py314-reference-datamodel-invoking-descriptors] Тому значення, яке зберігає property, зазвичай лежить в іншому атрибуті (тут `_celsius`), а не під іменем самого property.

**Типові помилки:**
- вважати, що запис у `obj.__dict__['x']` змінить результат `obj.x`, якщо для `x` є property;
- очікувати, що присвоєння до property без setter створить значення в словнику: воно піднімає `AttributeError`.
