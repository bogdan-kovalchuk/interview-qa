---
id: py-compfn-0010
title: "Коли `singledispatch` краще від extensible `if/elif` chain і за яким argument воно обирає implementation?"
description: "singledispatch обирає implementation за типом першого аргументу, використовуючи MRO для знаходження найближчого зареєстрованого типу."
track: python
section: comprehensions-and-functional
level: senior
type: comparison
tags: [singledispatch, if-elif]
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-howto-functional
    title: "Python 3.14: Howto/functional"
    url: https://docs.python.org/3.14/howto/functional.html
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
  - source_id: py314-reference-expressions-displays-for-lists-sets-and-dict
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: predecessor-answer
    title: "tavor118/pj_python_interview_questions_and_answers (community)"
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/functional_programming.md#L49-L64
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`singledispatch` обирає implementation за типом першого аргументу, використовуючи MRO для знаходження найближчого зареєстрованого типу.**[^py314-howto-functional] Він кращий за `if/elif` chain, коли потрібна extensibility: нові типи реєструються через `@fn.register(type)` без модифікації існуючого коду (open/closed principle). Базова implementation (для `object`) слугує fallback. <span class="warn">Dispatch відбувається лише за першим аргументом; типи інших параметрів не впливають на вибір.</span>

## Detailed explanation

Резолюція типу відбувається не простим порівнянням на рівність, а проходом по `__mro__` конкретного
типу аргументу: `singledispatch` шукає найближчого зареєстрованого предка в порядку лінеаризації
класу і викликає саме цю implementation, а не обов'язково ту, що зареєстрована для точного класу
екземпляра.[^py314-library-functools] Тому підклас, для якого окрему implementation не
зареєстровано, автоматично отримує implementation свого найближчого зареєстрованого предка – це і є
головна відмінність від `if isinstance(...)` chain, де таку поведінку довелося б виписувати вручну
для кожного підкласу.

Результат резолюції кешується: після першого виклику з конкретним типом `singledispatch`
запам'ятовує знайдену implementation для цього типу, тому наступні виклики з тим самим типом не
повторюють обхід `__mro__`. Кеш скидається автоматично щоразу, коли реєструється нова implementation
через `register`, щоб уже викликані типи могли переоцінити свій вибір.

Якщо через множинне успадкування у типу є два зареєстровані предки на однаковій відстані в
`__mro__` і жоден з них не є предком іншого, `singledispatch` не обирає довільний варіант – він
підіймає `RuntimeError` про неоднозначність, вимагаючи явно зареєструвати implementation для самого
проблемного типу.

Реєструвати implementation можна двома способами: явно, `@fn.register(SomeType)`, або – починаючи з
Python 3.7 – через анотацію типу першого параметра функції, `@fn.register` без аргументу, якщо
функція оголошена як `def _(arg: SomeType): ...`. Для методів класу існує окремий
`functools.singledispatchmethod`, який ігнорує `self` і диспетчеризує за типом першого аргументу
після нього.[^py314-library-functools]

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
