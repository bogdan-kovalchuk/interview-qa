---
id: py-oop-0031
title: "Чому `frozen=True` у `@dataclass` забороняє reassignment полів, але не робить вкладений mutable object незмінним?"
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
---

## Short answer

**`frozen=True` генерує `__setattr__` і `__delattr__`, які raise `FrozenInstanceError` при спробі переприв’язати поле.**[^py314-library-dataclasses] Але це не робить вкладені об’єкти незмінними: `__setattr__` стосується лише присвоєння самому полю, тому `obj.mutable_list.append(1)` проходить без помилки, і зміна списку видна через усі посилання на нього.[^py314-reference-datamodel] Документація dataclasses прямо зазначає: «It is not possible to create truly immutable Python objects».[^py314-library-dataclasses]

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Config:
    items: list[int]

c = Config([1, 2])
c.items = [3]        # raises FrozenInstanceError
c.items.append(3)    # OK - c.items == [1, 2, 3]
```

## Detailed explanation

`@dataclass(frozen=True)` не робить об’єкт незмінним у повному сенсі. Він додає до класу `__setattr__` і `__delattr__`, які викидають `FrozenInstanceError` на присвоєння полів.[^py314-library-dataclasses] У CPython так само падає спроба додати новий атрибут до екземпляра цього класу: `c.y = 5` теж дає `FrozenInstanceError` (спостережено на CPython 3.12–3.14). Захист, отже, стосується атрибутів самого екземпляра, а не того, на що ці атрибути посилаються.

Блокування реалізоване звичайними методами класу, тож це домовленість про використання, а не строгий захист. `__init__` теж мусить записувати поля через `object.__setattr__()`, бо документація прямо каже, що просте присвоєння в `__init__()` тут не працює.[^py314-library-dataclasses] Той самий виклик доступний і зовнішньому коду: `object.__setattr__(c, 'items', [3])` обійде перевірку.

Поле `items` зберігає посилання на об’єкт `list`. Frozen-клас забороняє замінити саме посилання `c.items`, але сам список лишається змінним. Документація описує це як різницю між незмінністю посилань і незмінністю значення: якщо незмінний контейнер містить змінний об’єкт, значення контейнера змінюється разом із ним.[^py314-reference-datamodel] Приклад показує присвоєння, яке блокується, і мутацію, яка проходить, а також хешування, яке падає:

```python
from dataclasses import dataclass, FrozenInstanceError

@dataclass(frozen=True)
class Config:
    items: list[int]

c = Config([1, 2])
try:
    c.items = [3]
except FrozenInstanceError:
    print("reassignment blocked")
c.items.append(3)        # OK: the list object itself is still mutable
print(c.items)           # [1, 2, 3]
try:
    hash(c)              # frozen + eq generate __hash__, which hashes the list
except TypeError as e:
    print(e)             # unhashable type: 'list'
```

За замовчуванням `eq=True` і `frozen=True` разом змушують `@dataclass` згенерувати `__hash__()`.[^py314-library-dataclasses] У CPython цей хеш рахується за полями, тож `list` у полі робить `hash(c)` неможливим. Frozen-екземпляр зі списком не можна класти в `set` або використовувати як ключ `dict`. Для значень, які справді мають бути незмінними, поля роблять hashable: `tuple` замість `list`, `frozenset` замість `set`. Але й `tuple` фіксує лише свої безпосередні елементи; якщо там лежить змінний об’єкт, його можна змінити.[^py314-reference-datamodel]

**Типові помилки:**
- вважати, що `frozen=True` робить увесь стан незмінним, зокрема вкладені `list` і `dict`;
- передати той самий `list` в інше місце й змінювати його там: зміна буде видна в `c.items`;
- зробити frozen-клас зі списком у полі ключем `dict` або елементом `set` і отримати `TypeError` під час `hash()`.
