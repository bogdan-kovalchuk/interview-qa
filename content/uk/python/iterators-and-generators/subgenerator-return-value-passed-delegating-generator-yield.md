---
id: py-itergen-0010
title: "Як значення `return` у subgenerator передається delegating generator через `yield from`?"
description: "return value у subgenerator встановлює StopIteration.value, а yield from витягує це значення як результат виразу."
track: python
section: iterators-and-generators
level: senior
type: mechanism
tags: [yield-from]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-stdtypes-iterator-types
    title: "Python 3.14: Library/stdtypes"
    url: https://docs.python.org/3.14/library/stdtypes.html#iterator-types
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-expressions-yield-expressions
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#yield-expressions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-object-iter
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__iter__
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-exceptions-stopiteration
    title: "Python 3.14: Library/exceptions"
    url: https://docs.python.org/3.14/library/exceptions.html#StopIteration
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: StopIteration і його атрибут value; return у generator задає це значення."
---

## Short answer

**`return value` у subgenerator встановлює `StopIteration.value`, а `yield from` повертає це значення як результат виразу.**[^py314-library-exceptions-stopiteration] Коли subgenerator виконує `return value`, він завершується і піднімає `StopIteration`, у якому `value` дорівнює цьому значенню. Вираз `yield from` бере це значення і використовує його як власний результат, який можна присвоїти змінній у delegating generator.[^py314-reference-expressions-yield-expressions]

## Detailed explanation

Вираз `yield from` делегує виконання subgenerator: значення, які той віддає через `yield`, передаються викликаючому коду без змін. Значення, яке subgenerator повертає через `return`, не передається як звичайне `yield`-значення. Коли тіло завершується, Python піднімає `StopIteration`, і повернене значення зберігається в його атрибуті `value`.[^py314-library-exceptions-stopiteration] Коли subiterator завершився, це значення стає результатом виразу `yield from`, тому `result = yield from sub()` присвоює `result` саме те, що `sub` повернув через `return`.[^py314-reference-expressions-yield-expressions]

Функція `sub` віддає два значення і повертає `'done'`. Функція `delegating` отримує це значення через `yield from` і сама повертає своє значення:

```python
def sub():
    yield 1
    yield 2
    return 'done'                   # becomes StopIteration.value

def delegating():
    result = yield from sub()       # result is 'done' after sub() finishes
    print('sub returned:', result)
    return result.upper()           # the value of delegating's own StopIteration

g = delegating()
print(next(g))                      # 1
print(next(g))                      # 2
try:
    next(g)                         # prints 'sub returned: done'
except StopIteration as stop:
    print('value:', stop.value)     # value: DONE
```

Перші два `next()` повертають `1` і `2`. Третій `next()` завершує `sub`: `yield from` отримує `'done'`, друкується `sub returned: done`, а `delegating` завершується власним `return`. Його `StopIteration.value` дорівнює `'DONE'`, бо саме це значення повернула `delegating`, а не `sub`.

Умови тут важливі. Якщо subgenerator не має `return` або повертає без значення, результат `yield from` дорівнює `None`. Автоматичне перенесення значення стосується випадку, коли subiterator є generator.[^py314-reference-expressions-yield-expressions] Для iterator, який не є generator, значення береться лише з явно заданого `StopIteration(value)`; інакше `value` дорівнює `None`.[^py314-reference-expressions-yield-expressions][^py314-library-exceptions-stopiteration] Тому власний клас, який сам піднімає `StopIteration('explicit')`, дає `yield from` значення `'explicit'`.

**Типові помилки:**
- очікувати, що `return` стане звичайним значенням для `next()` або `for`: `return` видно лише як `StopIteration.value` або через `yield from`;
- вважати, що `yield from` без `return` дає осмислений результат: він дорівнює `None`;
- очікувати `value` від iterator, який не є generator, без явного `StopIteration(value)`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
