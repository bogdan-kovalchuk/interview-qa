---
id: py-perf-0011
title: "Чому arguments для function з `lru_cache` мають бути hashable і що станеться, якщо передати `list` чи `dict`?"
description: "lru_cache зберігає результати в dict, тому всі positional і keyword arguments мають бути hashable; list і dict відхиляються з TypeError."
track: python
section: performance
level: middle
type: pitfall
tags: [lru-cache, list, dict]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-functools-functools-lru-cache
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.lru_cache
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: результати зберігаються в dict, тому аргументи мають бути hashable; maxsize=None вимикає LRU."
  - source_id: py314-library-functools-functools-cache
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.cache
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: functools.cache() еквівалентний lru_cache(maxsize=None), тобто без обмеження розміру."
  - source_id: py314-glossary-term-hashable
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-hashable
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: визначення hashable; кортеж hashable лише тоді, коли hashable всі його елементи; екземпляри власних класів hashable за замовчуванням, а їхній hash береться з id()."
  - source_id: py314-reference-datamodel-object-hash
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__hash__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: якщо __hash__ дорівнює None, отримання hash дає TypeError; клас, що визначає __eq__ без __hash__, не може бути елементом hashable-колекцій."
---

## Short answer

**`lru_cache` зберігає результати у внутрішньому dict, тому всі positional і keyword arguments мають бути hashable.**[^py314-library-functools-functools-lru-cache] Передача `list` або `dict` дає `TypeError: unhashable type`, і в CPython тіло функції при цьому не виконується. Обхідний шлях: перетворити аргумент на `tuple` або `frozenset` з hashable елементами, якщо функція приймає такий тип. Hashable не означає immutable: екземпляри власних класів hashable за замовчуванням, а їхній hash береться з `id()`[^py314-glossary-term-hashable], тож зміна атрибутів залишає застарілий результат у cache.

## Detailed explanation

`lru_cache` зберігає результати в dict. Кожен виклик спочатку будує ключ з позиційних і іменованих аргументів, а потім шукає його в dict, тому документація вимагає, щоб усі ці аргументи були hashable.[^py314-library-functools-functools-lru-cache] Hashable означає, що об’єкт має hash-значення, яке не змінюється протягом життя, і його можна порівняти з іншими: для цього потрібні `__hash__` і `__eq__`.[^py314-glossary-term-hashable] Якщо `__hash__` дорівнює `None`, отримання hash дає `TypeError`.[^py314-reference-datamodel-object-hash] Змінювані контейнери, `list` і `dict`, не hashable.[^py314-glossary-term-hashable]

Перший виклик обчислює результат, другий береться з cache, а `list` відхиляється ще до виконання функції:

```python
from functools import lru_cache


@lru_cache(maxsize=None)
def total(values):
    print("computing")
    return sum(values)


print(total((1, 2, 3)))    # computing, then 6
print(total((1, 2, 3)))    # 6: cache hit, nothing printed
try:
    total([1, 2, 3])
except TypeError as error:
    print(error)           # unhashable type: 'list'
```

Помилка виникає під час пошуку в cache, тому тіло функції не виконується і нічого не зберігається (перевірено на 3.13 і 3.14). `dict` дає ту саму помилку, а `tuple` з `list` всередині теж не hashable: immutable контейнер hashable лише тоді, коли hashable всі його елементи.[^py314-glossary-term-hashable] Для keyword arguments правило таке саме: `lookup(config={"x": 1})` дає `TypeError: unhashable type: 'dict'`.

Небезпечніший випадок – аргумент, який hashable, але змінюваний. Тут cache бачить той самий ключ навіть після зміни атрибутів:

```python
from functools import lru_cache


class Box:
    def __init__(self, value):
        self.value = value


@lru_cache(maxsize=None)
def read(box):
    return box.value


b = Box(1)
print(read(b))    # 1
b.value = 2
print(read(b))    # 1: same object, same hash, stale cached result
```

Тут `hashable` не означає `immutable`: cache не перевіряє стан об’єкта, тож для змінюваних аргументів кешований результат може не відповідати поточним даним.

Обхідні шляхи залежать від функції. Перетворення на `tuple` або `frozenset` працює, лише якщо функція приймає такий тип і елементи hashable: для `dict` варіант `frozenset(d.items())` вимагає hashable значень. `functools.cache` не знімає вимогу: він еквівалентний `lru_cache(maxsize=None)` і лише прибирає ліміт розміру.[^py314-library-functools-functools-cache]

**Типові помилки:**
- вважати, що `functools.cache` приймає аргументи, які `lru_cache` відхиляє: вимога однакова;
- конвертувати `list` у `tuple`, не перевіривши hashable елементи: `hash(tuple([[1]]))` все одно дає `TypeError`;
- вважати, що hashable гарантує актуальність результату для змінюваного об’єкта.

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
