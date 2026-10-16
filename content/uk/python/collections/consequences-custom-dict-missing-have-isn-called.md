---
id: py-coll-0012
title: "Які наслідки має custom `dict.__missing__()` і чому він не викликається однаково всіма способами доступу до key?"
track: python
section: collections
sources:
  - source_id: py314-library-stdtypes
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
  - source_id: py314-howto-sorting
    title: "Python 3.14: Howto/sorting"
    url: https://docs.python.org/3.14/howto/sorting.html
---

## Short answer

**`__missing__(key)` викликається лише методом `__getitem__()`, коли key відсутній; `get()`, `pop()` та `setdefault()` його не викликають.**[^py314-library-stdtypes] Це означає, що `d[missing_key]` запустить `__missing__`, а `d.get(missing_key)` поверне `None` (або вказаний default) без виклику `__missing__`. Саме на цьому механізмі побудований `collections.defaultdict`: його `__missing__` викликає `default_factory` і записує результат у словник.

## Detailed explanation

Ключова відмінність – `__missing__` це hook, який викликає сам `dict.__getitem__()` на C-рівні, а
не окремий універсальний перехоплювач доступу до словника. Тому будь-який код, що йде в обхід
`__getitem__`, цей hook просто не побачить: `key in d` (тобто `__contains__`) перевіряє наявність
ключа напряму в таблиці й ніколи не викликає `__missing__`, так само як `pop(key, default)` і
`setdefault(key, default)` реалізовані через власну C-логіку, що не делегує в
`__missing__`.[^py314-library-stdtypes]

Наслідок – можлива неузгодженість: якщо `__missing__` створює запис (як у `defaultdict`), то
`key in d` поверне `False` до першого `d[key]`, але `True` одразу після нього, хоча жодного
explicit присвоєння в коді не було. Якщо ж `__missing__` не мутує словник, а лише обчислює й
повертає значення (як `collections.Counter`, де відсутній ключ трактується як `0` без запису в
таблицю), то `d[key]` і `key in d` залишаються узгодженими – словник не «росте» від самих лише
читань.

Базовий `dict` не визначає `__missing__` узагалі, тому `KeyError` при `d[missing_key]` для
звичайного словника – це стандартна поведінка `__getitem__` без делегування; hook застосовується
лише в підкласах, де його явно перевизначено.

Ще одна практична пастка – якщо `__missing__` сам звертається до `self[key]` для того самого
ключа без базового випадку, це призводить до нескінченної рекурсії, бо кожен промах знову
викликає `__missing__`.
