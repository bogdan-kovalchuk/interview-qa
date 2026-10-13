---
id: py-oop-0006
title: "Що реально робить name mangling для атрибута `__value` і чому це не є security-механізмом приватності?"
description: "Name mangling автоматично перейменовує __value у _ClassName__value, щоб уникнути випадкових колізій імен у підкласах."
track: python
section: oop-and-data-model
level: middle
type: mechanism
tags: [value]
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
  - source_id: py314-reference-expressions-private-name-mangling
    title: "Python 3.14: Reference/expressions, Private name mangling"
    url: https://docs.python.org/3.14/reference/expressions.html#private-name-mangling
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: правило, за яким приватний ідентифікатор (два або більше початкових `_`, без кінцевих `__`) перетворюється на форму з іменем класу до генерації коду. Не описує mangling як механізм безпеки."
  - source_id: py314-tutorial-classes-private-variables
    title: "Python 3.14: Tutorial/classes, Private Variables"
    url: https://docs.python.org/3.14/tutorial/classes.html#private-variables
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: мета mangling (уникнути колізій імен, визначених у підкласах); правила розроблені переважно для уникнення випадкових помилок, доступ і зміна залишаються можливими; один початковий `_` як домовленість. Не описує descriptor."
---

## Short answer

**Name mangling автоматично перейменовує `__value` у `_ClassName__value`, щоб уникнути колізій із іменами, визначеними в підкласах.**[^py314-tutorial-classes-private-variables] Трансформація відбувається до генерації коду: ідентифікатор `__name` (два або більше початкових `_`, без кінцевих `__`) у визначенні класу `Foo` стає `_Foo__name`.[^py314-reference-expressions-private-name-mangling] Це не блокує доступ: до мангленого імені можна звернутися напряму, тож механізм захищає від випадкових колізій, а не від навмисного доступу.[^py314-tutorial-classes-private-variables]

## Detailed explanation

Name mangling – це перетворення імені під час компіляції, а не механізм, що працює під час виконання. Ідентифікатор, який починається з двох або більше `_` і не закінчується двома `_`, вважається private name свого класу. Перед генерацією коду Python замінює його на довшу форму: ім’я класу без початкових підкреслень, один `_` попереду і далі саме ім’я.[^py314-reference-expressions-private-name-mangling] Тому `__value` у класі `Base` стає `_Base__value`, а в класі `_Base` також `_Base__value`.

Мета правила – уникнути колізій із іменами, які визначає підклас. Якщо і `Base`, і `Child` записують `self.__value`, у `__dict__` екземпляра з’являються два різні ключі, і підклас не перезаписує значення базового класу.[^py314-tutorial-classes-private-variables] Перевіримо це:

```python
class Base:
    def __init__(self):
        self.__value = 'base'      # stored as _Base__value

class Child(Base):
    def __init__(self):
        super().__init__()
        self.__value = 'child'     # stored as _Child__value, no clash

c = Child()
print(vars(c))  # {'_Base__value': 'base', '_Child__value': 'child'}
```

Отже, `__value` не є способом приховати дані: це лише зміна імені, під яким атрибут лежить у `__dict__`. Мангльований атрибут – звичайний атрибут, і його можна прочитати з будь-якого місця програми:

```python
class Account:
    def __init__(self, balance):
        self.__balance = balance   # stored as _Account__balance

acc = Account(100)
print(acc._Account__balance)      # 100: the mangled name is an ordinary attribute
print(hasattr(acc, '__balance'))  # False: the string '__balance' is not mangled
print(vars(acc))                  # {'_Account__balance': 100}
```

Рядок, переданий у `hasattr`, `getattr` чи `setattr`, не перетворюється, бо правило стосується ідентифікаторів у тексті класу.[^py314-reference-expressions-private-name-mangling] Документація Python пояснює, що правила mangling розроблені переважно для уникнення випадкових помилок, а не для захисту: доступ і зміна залишаються можливими, навіть коли атрибут задуманий як приватний.[^py314-tutorial-classes-private-variables] Для атрибута, який не призначений для використання ззовні, у Python зазвичай ставлять один `_` як домовленість.[^py314-tutorial-classes-private-variables]

**Типові помилки:**
- вважати, що `__value` недоступний ззовні класу: його можна прочитати як `obj._ClassName__value`;
- очікувати, що підклас перевизначить `self.__value` базового класу: з mangling це два різні атрибути;
- шукати мангльований атрибут через `getattr(obj, '__value')`: рядок не перетворюється.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
