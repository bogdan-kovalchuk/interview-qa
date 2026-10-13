---
id: py-oop-0018
title: "Як Python розв’язує успадкування типу diamond і чому прямі виклики конкретних parent methods можуть виконати одну ланку двічі?"
description: "C3 MRO містить кожен клас діаманта рівно один раз, а super() іде по цьому порядку; прямі виклики Parent.method(self) обходять MRO фактичного типу і можуть викликати спільного предка двічі."
track: python
section: oop-and-data-model
level: middle
type: pitfall
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

**C3 MRO містить кожен клас діаманта рівно один раз, а `super()` іде по цьому порядку; прямі виклики `Parent.method(self)` шукають метод у самому `Parent` і його предках, тобто обходять MRO фактичного типу.**[^py314-howto-mro][^py314-reference-datamodel] <span class="warn">Якщо `Left.method` і `Right.method` викликають `Base.method(self)` напряму, то `Bottom.method`, що викликає їх обох, виконає `Base.method` двічі.</span> Розв’язок – cooperative pattern: кожен клас викликає `super().method()`, і ланцюжок проходить кожен клас з MRO один раз.[^py314-builtins-functions-super]

## Detailed explanation

Діамант – це `Bottom(Left, Right)`, де `Left(Base)` і `Right(Base)`. Для такої ієрархії C3 будує `Bottom.__mro__ = Bottom, Left, Right, Base, object`. Алгоритм злиття додає клас у результат і видаляє його з усіх списків, тож спільний предок `Base` з’являється в MRO лише раз.[^py314-howto-mro] Пошук атрибутів у базових класах використовує той самий C3 MRO і коректно працює з діамантами.[^py314-reference-datamodel]

Спочатку прямі виклики, потім cooperative версія з `super()` у тому самому прикладі:

```python
class Base:
    def method(self):
        print('Base.method')

class Left(Base):
    def method(self):
        print('Left.method')
        Base.method(self)      # direct call: bypasses the MRO

class Right(Base):
    def method(self):
        print('Right.method')
        Base.method(self)

class Bottom(Left, Right):
    def method(self):
        print('Bottom.method')
        Left.method(self)
        Right.method(self)

Bottom().method()
# Bottom.method
# Left.method
# Base.method
# Right.method
# Base.method   <- the shared base runs twice

class CoBase:
    def method(self):
        print('CoBase.method')

class CoLeft(CoBase):
    def method(self):
        print('CoLeft.method')
        super().method()

class CoRight(CoBase):
    def method(self):
        print('CoRight.method')
        super().method()

class CoBottom(CoLeft, CoRight):
    def method(self):
        print('CoBottom.method')
        super().method()

CoBottom().method()
# CoBottom.method
# CoLeft.method
# CoRight.method
# CoBase.method   <- each class runs once, in MRO order
```

У прямій версії `Base.method(self)` називає клас явно. Пошук іде від `Base` і його предків, а не від MRO `Bottom`, тож `Left` і `Right` обидва доходять до `Base.method`, і він виконується двічі.[^py314-reference-datamodel]

У cooperative версії кожен клас викликає `super().method()`. `CoBottom` через `super()` переходить до `CoLeft`, `CoLeft` – до `CoRight`, бо наступним за `CoLeft` у MRO `CoBottom` є `CoRight`, а `CoRight` – до `CoBase`. Кожен клас виконується один раз і в порядку MRO.[^py314-builtins-functions-super]

Клас, який не викликає `super()`, обриває ланцюжок: класи після нього в MRO не виконуються. Тому схема працює лише тоді, коли кожен клас ланцюжка викликає `super()`.

**Типові помилки:**
- писати `Parent.method(self)` у класі з кількома батьками замість `super().method()`;
- вважати, що спільний предок у діаманті виконається один раз, якщо два батьки викликають його напряму;
- не викликати `super()` в одному з класів ланцюжка, через що класи після нього в MRO мовчки не виконуються.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
