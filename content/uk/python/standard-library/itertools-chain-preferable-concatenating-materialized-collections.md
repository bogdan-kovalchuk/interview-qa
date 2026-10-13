---
id: py-stdlib-0004
title: "Коли `itertools.chain()` доречніший за конкатенацію матеріалізованих collections?"
description: "chain() по черзі обходить вхідні iterable лініво, без побудови списку з усіх елементів, тож не створює додаткової копії даних."
track: python
section: standard-library
level: middle
type: comparison
tags: [itertools-chain]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-collections
    title: "Python 3.14: Library/collections"
    url: https://docs.python.org/3.14/library/collections.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-itertools
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-pathlib
    title: "Python 3.14: Library/pathlib"
    url: https://docs.python.org/3.14/library/pathlib.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-datetime
    title: "Python 3.14: Library/datetime"
    url: https://docs.python.org/3.14/library/datetime.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-re
    title: "Python 3.14: Library/re"
    url: https://docs.python.org/3.14/library/re.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-itertools-chain
    title: "Python 3.14: Library/itertools, chain"
    url: https://docs.python.org/3.14/library/itertools.html#itertools.chain
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: itertools.chain і chain.from_iterable (послідовний обхід iterable, еквівалент через yield from, лінива обробка)."
  - source_id: py314-library-stdtypes-common-sequence-operations
    title: "Python 3.14: Library/stdtypes, common sequence operations"
    url: https://docs.python.org/3.14/library/stdtypes.html#common-sequence-operations
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: операція конкатенації s + t для sequence types; не стосується iterable, які не є sequence."
---

## Short answer

**`chain()` по черзі віддає елементи вхідних iterable лініво, без проміжного списку, тому доречний, коли результат потрібно лише пройти один раз: сам `chain` новий список не створює, навіть якщо входи є `list`.**[^py314-library-itertools-chain] Конкатенація двох `list` через `a + b` створює новий список завдовжки `len(a) + len(b)`.[^py314-library-stdtypes-common-sequence-operations] Для generators `+` не працює взагалі. Якщо один iterable містить інші iterable, використовуйте `chain.from_iterable()`.[^py314-library-itertools-chain]

## Detailed explanation

`chain()` приймає кілька iterable і повертає один ітератор. Він віддає елементи першого iterable, доки той не вичерпається, а потім переходить до наступного. Документація описує це як еквівалент `for iterable in iterables: yield from iterable`.[^py314-library-itertools-chain] Тому сам `chain` не будує список: кожен елемент віддається в момент запиту, і додаткової копії даних немає. Вхідні колекції, якщо вони вже існують, лишаються в пам’яті без змін.

Порівняння з конкатенацією тут головне. Для двох `list` вираз `a + b` створює новий список, у який копіюються посилання на всі елементи обох операндів, тож додаткова пам’ять пропорційна `len(a) + len(b)`. Для generator оператор `+` не працює взагалі, бо generator не є sequence і не має `len()`:

```python
from itertools import chain

a = [1, 2, 3]
b = (x * 10 for x in range(3))  # a generator: no len(), no +
try:
    a + b
except TypeError as error:
    print('TypeError:', error)  # can only concatenate list (not "generator") to list
print(list(chain(a, b)))        # [1, 2, 3, 0, 10, 20]
```

Лінивість видно, коли входи створюють дані з побічними ефектами. Перший `next()` запускає лише перший генератор, а другий не чіпається, доки перший не вичерпано:

```python
from itertools import chain

def produce(label, n):
    for i in range(n):
        print(f'{label} produces {i}')
        yield i

it = chain(produce('first', 2), produce('second', 1))
print('chain created')   # no item has been produced yet
print(next(it))          # first produces 0, then 0
print(list(it))          # first produces 1, second produces 0, then [1, 0]
```

Повторний `list()` від того самого `chain` дає порожній список, бо результат можна пройти один раз (це поведінка ітератора). Тому для повторних проходів, `len()` чи індексації потрібна sequence. `chain` доречний, коли входи є iterable без `len()` або індексації (generators, результати `map` чи `filter`, рядки файлу), результат споживається одним проходом, а проміжний список був би дорогим. Якщо ж результат однаково треба зберегти як `list`, то `list(chain(a, b))` теж створює новий список, і виграшу немає.

**Типові помилки:**
- вважати, що `chain` створює копію даних: він лише обходить входи, а копію створює `list(chain(...))`;
- очікувати від `chain` індексування, `len()` або повторного обходу;
- очікувати, що `chain(['AB', 'CD'])` розбиває рядки на символи: він віддає `'AB'` і `'CD'` цілими; для розгортання одного iterable з iterable-елементами потрібен `chain.from_iterable()`.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
