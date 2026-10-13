---
id: py-itergen-0014
title: "Яку проблему створює передавання одного iterator двом consumers, які читають його по черзі?"
description: "Iterator – односпрямований і stateful: два consumers ділять один cursor, тому елементи, прочитані одним, стають недоступними для іншого."
track: python
section: iterators-and-generators
level: middle
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
  - source_id: py314-glossary-term-iterable
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-iterable
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: визначення iterable; iter() повертає iterator для одного проходу."
  - source_id: py314-glossary-term-iterator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-iterator
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: визначення iterator і exhausted."
  - source_id: py314-library-itertools-tee
    title: "Python 3.14: Library/itertools"
    url: https://docs.python.org/3.14/library/itertools.html#itertools.tee
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: itertools.tee(), незалежні iterators з одного iterable і вимоги до сховища."
---

## Short answer

**Iterator – односпрямований і stateful: два consumers ділять один cursor, тому елементи, прочитані одним, стають недоступними для іншого.**[^py314-library-stdtypes-iterator-types] Наприклад, якщо перший consumer витягнув три елементи, другий почне з четвертого, а не з першого. Щоб обидва отримали повну копію даних, передайте iterable (наприклад, `list`), з якого кожен consumer бере власний iterator.[^py314-glossary-term-iterable] Або використайте `itertools.tee()`, який створює незалежні iterators ціною додаткової пам’яті.[^py314-library-itertools-tee]

## Detailed explanation

Iterable – це об’єкт, який може віддавати свої елементи по одному. Коли iterable передають у `iter()`, результатом є iterator, призначений для одного проходу по значеннях.[^py314-glossary-term-iterable] Iterator повертає наступні елементи потоку, а коли даних більше немає, піднімає `StopIteration` і стає exhausted.[^py314-glossary-term-iterator] Сам iterator зберігає позицію: кожен `next()` бере наступний елемент і просувається вперед.[^py314-library-stdtypes-iterator-types] Тому позиція належить самому iterator, а не споживачеві. Якщо два споживачі тримають один і той самий iterator, вони ділять одну позицію.

Приклад: два споживачі читають один iterator по черзі. Кожен отримує лише частину даних, і жоден не бачить повної послідовності. Коментарі показують вивід на CPython 3.13 і 3.14:

```python
it = iter(range(6))
a_items, b_items = [], []
for _ in range(3):
    a_items.append(next(it))        # consumer A reads one item
    b_items.append(next(it))        # consumer B reads the next one
print('A:', a_items, 'B:', b_items) # A: [0, 2, 4] B: [1, 3, 5]
```

Перший спосіб виправити це – передати iterable, а не iterator. Контейнер має повертати новий iterator при кожному `iter()`, тож кожен споживач отримує власну позицію з початку.[^py314-reference-datamodel-object-iter] Наприклад, `list(values)` можна викликати двічі для одного списку, і кожен виклик починає з першого елемента. Якщо ж джерело саме є iterator, наприклад generator, його можна лише зберегти в `list` або розділити через `tee()`.

Другий спосіб – `itertools.tee()`, який повертає кілька незалежних iterators над одним джерелом:[^py314-library-itertools-tee]

```python
import itertools

it = iter(range(4))
x, y = itertools.tee(it, 2)
print(list(x), list(y))             # [0, 1, 2, 3] [0, 1, 2, 3]
```

`tee()` має ціну. Документація попереджає, що він може потребувати значного додаткового сховища. Якщо один iterator використовує майже всі дані до того, як почне інший, швидше використати `list()`.[^py314-library-itertools-tee]

Проблема виникає лише тоді, коли споживачі тримають один і той самий iterator. Generator, переданий двом споживачам, має ту саму проблему, бо generator сам є iterator. Якщо ж кожен споживач сам викликає `iter()` для iterable, спільної позиції немає.[^py314-reference-datamodel-object-iter]

**Типові помилки:**
- передавати один iterator або generator двом функціям і очікувати, що кожна отримає повну послідовність;
- вважати `tee()` безкоштовним: він може потребувати значного додаткового сховища;
- переводити iterator у `list`, не оцінивши розмір даних: якщо вони не вміщуються в пам’ять, це окрема проблема.

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
