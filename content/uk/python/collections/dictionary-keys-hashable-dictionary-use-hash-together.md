---
id: py-coll-0007
title: "Чому keys словника мають бути hashable і як dictionary використовує hash разом з equality?"
description: "Ключ має бути hashable – мати __hash__() та __eq__() – тому що dict використовує hash для визначення bucket, а equality для розв'язання колізій."
track: python
section: collections
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-sorting
    title: "Python 3.14: Howto/sorting"
    url: https://docs.python.org/3.14/howto/sorting.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L206-L242
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Ключ має бути hashable – мати `__hash__()` та `__eq__()` – тому що dict використовує hash для визначення bucket, а equality для розв'язання колізій.**[^py314-library-stdtypes] Спочатку обчислюється `hash(key)` для пошуку позиції; якщо в bucket вже є елементи, викликається `__eq__()` для порівняння з кожним. <span class="warn">Об'єкти, що порівнюються як рівні, повинні мати однаковий hash – інакше ключ «загубиться».</span>

## Detailed explanation

CPython `dict` – це не list ланцюжків (chaining) для кожного bucket, а open addressing: значення
`hash(key)` після маскування під розмір таблиці дає стартовий слот, і якщо він зайнятий іншим
ключем, використовується детермінована послідовність проб (perturbation), що бере додаткові біти
того самого hash, поки не знайдеться порожній слот або слот з рівним ключем.[^py314-library-stdtypes]
Тому «bucket» тут – не контейнер із кількома елементами, а один слот масиву, і швидкість lookup
залежить від того, наскільки рідко трапляються колізії hash.

Контракт hashable-типу – якщо `a == b`, то обов'язково `hash(a) == hash(b)` – критичний саме через
цю схему: пошук спочатку звужує простір до слотів з однаковим hash, і лише потім `__eq__`
підтверджує остаточний збіг. Якщо цей контракт порушено (рівні обʼєкти з різним hash), пошук за
ключем може взагалі не дійти до слоту, де лежить «рівний» ключ, і `d[a]` не знайде запис, зроблений
як `d[b] = ...`.

Мутабельні built-in типи (`list`, `dict`, `set`) навмисно unhashable, бо якщо обчислити `hash` для
обʼєкта в момент вставки, а потім змінити цей обʼєкт, його майбутній hash при пошуку вже не
збігатиметься зі збереженим слотом – ключ стає «загубленим»: він фізично лишається в таблиці,
видимий при ітерації, але недосяжний через `d[key]`, бо hash більше не веде до правильного слота.

Ще один наслідок – визначення `__eq__` у класі без явного `__hash__` автоматично робить екземпляри
unhashable (Python встановлює `__hash__ = None`), бо інтерпретатор не може гарантувати
узгодженість hash і equality без явної реалізації обох. `tuple` і `frozenset` hashable лише тоді,
коли hashable кожен їхній елемент – рекурсивно.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
