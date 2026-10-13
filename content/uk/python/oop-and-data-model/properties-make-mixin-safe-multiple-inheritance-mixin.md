---
id: py-oop-0020
title: "Які властивості роблять mixin безпечним для множинного успадкування і чому mixin зазвичай не володіє основним state об’єкта?"
description: "Mixin зазвичай додає поведінку, а не володіє state: він не вимагає обов’язкових аргументів у __init__, передає керування через super() і покладається на атрибути, які дають інші класи."
track: python
section: oop-and-data-model
level: senior
type: practical
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
  - source_id: py314-builtins-functions-super
    title: "Python 3.14: Built-in Functions/super"
    url: https://docs.python.org/3.14/builtins/functions.html#super
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, розділ super: порядок пошуку після type за __mro__, zero-argument form (type і перший аргумент методу), застереження про вкладені функції, рекомендація однакової сигнатури в cooperative methods. Не описує object.__init__ і не дає правил проєктування mixin."
---

## Short answer

**Mixin додає поведінку, а не володіє основним state об’єкта: зазвичай він не має обов’язкових аргументів у `__init__` і працює з атрибутами, які надають інші класи.** Передає він керування через `super()` з тією самою сигнатурою, що й решта cooperative methods.[^py314-builtins-functions-super] <span class="warn">Два mixins, що записують в один атрибут, можуть мовчки перезаписати дані один одного.</span> Тому mixin варто документувати разом з атрибутами та методами, яких він очікує від інших класів.

## Detailed explanation

Mixin – це клас, який додає повторно використовувану поведінку іншим класам через множинне успадкування. Зазвичай його не створюють окремо: він стоїть у MRO разом з класом, який створює об’єкт і зберігає основний стан. Звідси правило: mixin додає методи, а дані залишає тому класу, що створює екземпляр. Це домовленість проєктування, а не обмеження, яке Python перевіряє.

Причина видна з моделі даних: екземпляр має простір імен у вигляді словника, і всі класи його MRO можуть писати в цей самий словник.[^py314-reference-datamodel] Два mixins, що використовують одне ім’я атрибута, конфліктують, навіть якщо кожен з них окремо правильний. Приклад:

```python
class LoggingMixin:
    def __init__(self, *args, **kwargs):
        self.items = []                       # the mixin writes its own state
        super().__init__(*args, **kwargs)

class CacheMixin:
    def __init__(self, *args, **kwargs):
        self.items = {}                       # same attribute name: silent clash
        super().__init__(*args, **kwargs)

class Service(LoggingMixin, CacheMixin):
    pass

s = Service()
print(type(s.items).__name__)                 # dict: CacheMixin replaced the list
```

`Service()` спершу виконує `LoggingMixin.__init__`, який створює список, а потім `CacheMixin.__init__`, який замінює його словником. Помилки немає, тож такий конфлікт легко пропустити.

Друга умова – сигнатура. Якщо `__init__` mixin вимагає позиційний аргумент, то кожен, хто створює клас із цим mixin, мусить його передати, тобто mixin змінює конструктор усього класу. Тому mixin приймає `*args, **kwargs` і передає їх далі, як і решта cooperative methods.[^py314-builtins-functions-super]

Третя умова – позиція. Mixin не має знати, який клас стоїть перед ним або після нього. Тому він викликає `super()`, а не `Base.method(self)`: `super()` шукає наступний клас у MRO фактичного типу, тож mixin не залежить від сусідніх класів, якщо його атрибути є в комбінації.[^py314-builtins-functions-super] Але порядок bases визначає, чий метод перекриває чий, тому mixin, що має перекривати метод, ставлять раніше за клас, який його визначає (той може не викликати `super()`).[^py314-howto-mro]

**Типові помилки:**
- вважати, що два mixins з однаковим іменем атрибута ізольовані, бо оголошені в різних класах;
- додати до mixin обов’язковий аргумент `__init__`, який інші класи в комбінації не передають;
- використовувати атрибут, який mixin сам не створює і не документує, і зламати комбінацію, де його немає.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
