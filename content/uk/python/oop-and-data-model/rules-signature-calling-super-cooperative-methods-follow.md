---
id: py-oop-0019
title: "Яких правил сигнатури та виклику `super()` мають дотримуватися cooperative methods у multiple-inheritance hierarchy?"
description: "Cooperative methods за рекомендацією документації мають мати однакову сигнатуру в усій hierarchy; кожен клас забирає свої аргументи, решту передає через super(**kwargs), а корінь ланцюжка нічого не передає далі."
track: python
section: oop-and-data-model
level: senior
type: practical
tags: [super]
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

**За рекомендацією документації, cooperative methods мають мати одну сигнатуру, бо порядок викликів визначається під час виконання.**[^py314-builtins-functions-super] Кожен клас забирає з `kwargs` свої аргументи і передає решту через `super().method(*args, **kwargs)`. Корінь ланцюжка нічого не передає далі: `object.__init__` у CPython відхиляє зайві аргументи, якщо тип перевизначає `__init__` або не перевизначає `__new__`. Метод без `super()` обриває ланцюжок.

## Detailed explanation

Документація пояснює, навіщо потрібна однакова сигнатура: порядок викликів у кооперативній ієрархії визначається під час виконання, він змінюється разом з ієрархією і може включати класи-сусіди, невідомі заздалегідь. Тому метод не знає, який клас стоїть наступним, і має приймати те, що передає попередній клас.[^py314-builtins-functions-super]

Практична форма – `*args, **kwargs` у кожному методі. Клас забирає свій ключ через `pop`, а решту передає далі. Корінь ланцюжка, тут `Root`, перевіряє, що не лишилось нерозібраних аргументів. `Named` і `Colored` не знають одне про одного: `Item(Colored, Named)` визначає порядок під час виконання, тож `Colored` забирає свій ключ першим, а `Named` бачить лише залишок. Приклад:

```python
class Root:
    # Last class before object: it forwards nothing, because object takes no arguments.
    def __init__(self, *args, **kwargs):
        if args or kwargs:
            raise TypeError(f'unused arguments: {args}, {kwargs}')

class Named(Root):
    def __init__(self, *args, **kwargs):
        self.name = kwargs.pop('name')        # takes its own argument
        super().__init__(*args, **kwargs)     # passes the rest on

class Colored(Root):
    def __init__(self, *args, **kwargs):
        self.color = kwargs.pop('color', 'none')
        super().__init__(*args, **kwargs)

class Item(Colored, Named):
    pass

item = Item(name='box', color='red')
print(item.name, item.color)                  # box red
print([k.__name__ for k in Item.__mro__])     # ['Item', 'Colored', 'Named', 'Root', 'object']
# Named does not know that Colored ran first: it receives only what is left.
try:
    Named(name='box', color='red')
except TypeError as e:
    print('TypeError:', e)                    # Root receives the unconsumed color
```

Якщо корінь викличе `super().__init__(**kwargs)` із непорожнім `kwargs`, у CPython виклик падає з `TypeError`: `object.__init__()` приймає лише `self`. Тому `super().__init__()` без аргументів безпечний, а з аргументами – ні.

Метод без `super()` обриває ланцюжок: класи після нього в MRO не виконуються. Тоді клас мусить сам зробити всю роботу, яку мали б зробити наступні класи.

**Типові помилки:**
- передавати в `object` або в корінь ланцюжка аргументи, які ніхто не забрав: у CPython це `TypeError`;
- додати обов’язковий позиційний аргумент до `__init__` одного класу, не змінивши виклики в решті ланцюжка;
- пропустити `super()` у класі, бо «я тут останній»: за ним у MRO можуть бути інші класи.

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
