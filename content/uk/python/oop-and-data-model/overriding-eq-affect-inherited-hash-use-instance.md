---
id: py-oop-0024
title: "Як перевизначення `__eq__` впливає на успадкований `__hash__` і використання instance у set або dict?"
description: "Якщо клас перевизначає __eq__ без визначення __hash__, то __hash__ неявно встановлюється в None, і instances стають unhashable – використання в set або dict викличе TypeError."
track: python
section: oop-and-data-model
level: senior
type: mechanism
tags: [eq, hash]
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
  - source_id: py314-reference-datamodel-object-hash
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__hash__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: object.__hash__, вимога до hash для рівних об’єктів, неявний __hash__ = None і явне повернення hash батька."
  - source_id: py314-library-dataclasses-dataclass
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: правила створення __hash__ для dataclass залежно від параметрів eq і frozen."
---

## Short answer

**Клас, що перевизначає `__eq__` без `__hash__`, отримує `__hash__ = None`: його екземпляри стають unhashable, тож використання в `set` або як ключа `dict` викликає `TypeError`.**[^py314-reference-datamodel-object-hash] Рівні об’єкти мають мати однаковий hash, і новий `__eq__` без узгодженого `__hash__` цього не гарантує.[^py314-reference-datamodel-object-hash] Батьківський `__hash__` не успадковується автоматично; його можна повернути явно через `__hash__ = Base.__hash__`, але тоді відповідальність за узгодженість лежить на авторі.[^py314-reference-datamodel-object-hash]

## Detailed explanation

Хешовані колекції (`set`, `frozenset`, `dict`) використовують hash, щоб обрати bucket, і `__eq__`, щоб порівняти елементи всередині нього. Тому головна вимога до `__hash__` така: об’єкти, що порівнюються як рівні, мають мати однаковий hash.[^py314-reference-datamodel-object-hash] Для змінюваних класів із `__eq__` документація радить не реалізовувати `__hash__`: якщо hash змінюється після додавання ключа, елемент опиняється не в своєму bucket.[^py314-reference-datamodel-object-hash]

Python ставить `__hash__ = None` у класі, який перевизначає `__eq__` і не визначає `__hash__`.[^py314-reference-datamodel-object-hash] Тому підклас, що перевизначає `__eq__`, втрачає hash навіть тоді, коли батьківський клас його має. Приклад:

```python
class Base:
    def __hash__(self):
        return 1

class Child(Base):
    def __eq__(self, other):
        return True

print(Child.__hash__)                 # None: Base.__hash__ is not inherited
try:
    hash(Child())
except TypeError as error:
    print(error)                      # unhashable type: 'Child'

class Id:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        return isinstance(other, Id) and self.name == other.name

    __hash__ = object.__hash__        # id-based hash kept by hand: wrong for this __eq__

a, b = Id("x"), Id("x")
print(a == b, hash(a) == hash(b))     # True False: equal objects, different hashes
print(len({a, b}))                    # 2: both stay in the set
```

Щоб повернути hash батька, треба явно написати `__hash__ = Base.__hash__`. Але цей hash має відповідати новій рівності. У прикладі `Id` hash із `object` ґрунтується на ідентичності, тоді як `__eq__` порівнює `name`, тому рівні об’єкти мають різні hash. У CPython `set` порівнює елементи на рівність лише тоді, коли їхні hash збігаються, тож обидва об’єкти лишаються в множині.

Той самий механізм діє для dataclass: якщо клас сам не визначає `__hash__`, то при `eq=True` і `frozen=False` (типові значення) він встановлюється в `None`, а з `frozen=True` dataclass генерує hash за полями.[^py314-library-dataclasses-dataclass]

**Типові помилки:**
- перевизначити `__eq__` у підкласі й очікувати, що hash батька працює без явного рішення;
- скопіювати `__hash__ = Base.__hash__` до класу з іншою рівністю, що порушує правило з прикладу;
- хешувати змінюваний об’єкт за полями, які змінюються після додавання в `set` або `dict`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
