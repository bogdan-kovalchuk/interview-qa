---
id: py-oop-0027
title: "Як параметри `eq`, `frozen` і `unsafe_hash` впливають на генерацію `__eq__` і `__hash__` для `@dataclass`?"
description: "eq=True генерує __eq__; eq=True з frozen=False робить клас unhashable, а frozen=True з eq=True генерує __hash__; unsafe_hash=True примушує генерувати __hash__."
track: python
section: oop-and-data-model
level: middle
type: mechanism
tags: [eq, frozen, unsafe-hash, hash, dataclass]
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
    title: "Python 3.14: Reference/datamodel (object.__hash__)"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__hash__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: контракт __hash__ і __eq__, зокрема що змінні об’єкти з власним __eq__ не мають реалізовувати __hash__."
  - source_id: py314-library-dataclasses-dataclass
    title: "Python 3.14: Library/dataclasses (dataclasses.dataclass)"
    url: https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: правила генерації __eq__ і __hash__ за параметрами eq, frozen, unsafe_hash; конфлікт unsafe_hash з явним __hash__ і з __setattr__ при frozen=True."
  - source_id: py314-library-dataclasses-frozeninstanceerror
    title: "Python 3.14: Library/dataclasses (FrozenInstanceError)"
    url: https://docs.python.org/3.14/library/dataclasses.html#dataclasses.FrozenInstanceError
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: FrozenInstanceError піднімається згенерованими __setattr__ і __delattr__ для frozen-dataclass; є підкласом AttributeError."
---

## Short answer

**`eq=True` (типово) генерує `__eq__`; якщо клас не визначає `__hash__` явно, з `frozen=True` генерується `__hash__`, а з `frozen=False` ставиться `__hash__ = None`, тобто клас unhashable; `eq=False` не чіпає `__hash__`, тож він успадковується від superclass.**[^py314-library-dataclasses-dataclass] `frozen=True` робить присвоєння полів помилкою `FrozenInstanceError`.[^py314-library-dataclasses-frozeninstanceerror] `unsafe_hash=True` примушує генерувати `__hash__`, хоча документація називає це небажаним, спеціальним випадком.[^py314-library-dataclasses-dataclass]

## Detailed explanation

Усі правила зводяться до контракту `__hash__`. Об’єкти, що порівнюються як рівні, мають мати однаковий hash, а для змінного об’єкта hash не може змінюватися, поки об’єкт є ключем словника чи елементом множини. Тому документація Python радить не реалізовувати `__hash__` у класі, який має змінні об’єкти і власний `__eq__`.[^py314-reference-datamodel-object-hash] Dataclass застосовує це сам: якщо клас не визначає `__hash__` явно, при `eq=True` і `frozen=False` він ставить `__hash__ = None`, тобто клас не може бути елементом множини чи ключем словника.[^py314-library-dataclasses-dataclass]

Згенерований `__hash__` має відповідати тому самому контракту, тож рівні екземпляри frozen-класу мають однаковий hash:

```python
from dataclasses import dataclass


@dataclass
class Mutable:  # eq=True, frozen=False
    x: int


@dataclass(frozen=True)
class Frozen:  # eq=True, frozen=True
    x: int


print(Mutable.__hash__)                    # None: the class is unhashable
print(hash(Frozen(1)) == hash(Frozen(1)))  # True: equal fields give equal hashes
```

`eq=False` працює інакше: dataclass не створює `__eq__`, тож порівняння успадковується від superclass (для `object` це порівняння за ідентичністю), а `__hash__` не змінюється. Якщо клас сам визначає `__eq__`, параметр `eq` ігнорується.[^py314-library-dataclasses-dataclass]

`frozen=True` додає `__setattr__` і `__delattr__`, які піднімають `FrozenInstanceError`, тож поля не можна присвоїти після створення. Якщо клас сам визначає `__setattr__` або `__delattr__`, поєднання з `frozen=True` дає `TypeError` уже під час декорування.[^py314-library-dataclasses-frozeninstanceerror][^py314-library-dataclasses-dataclass]

`unsafe_hash=True` змушує згенерувати `__hash__` і для змінного класу, але тоді зміна поля після додавання об’єкта в множину ламає пошук:

```python
from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Point:
    x: int


p = Point(1)
seen = {p}        # the hash is computed from x == 1
p.x = 2           # the hash changes while p is stored in the set
print(p in seen)  # False: the lookup computes the new hash and misses
```

Поєднання `unsafe_hash=True` з явно визначеним `__hash__` у тому самому класі дає `TypeError`.[^py314-library-dataclasses-dataclass]

**Типові помилки:**
- вважати, що `eq=True` сам по собі дає `__hash__`: для змінного класу він дає `None`;
- очікувати, що `eq=False` зробить клас unhashable: `__hash__` лишається від superclass, для `object` це hash за ідентичністю;
- ставити `unsafe_hash=True` на змінний клас, який зберігається в множинах або ключах словника.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
