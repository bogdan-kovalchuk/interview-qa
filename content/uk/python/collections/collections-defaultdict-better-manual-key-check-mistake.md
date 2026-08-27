---
id: py-coll-0009
title: "Коли `collections.defaultdict` кращий за ручну перевірку key і яку помилку може приховати неправильна default factory?"
description: "defaultdict кращий, коли потрібно групувати або акумулювати значення за ключами: він автоматично створює default-значення через default_factory при зверненні через __getitem__."
track: python
section: collections
level: middle
type: comparison
tags: [collections-defaultdict]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L173-L190
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`defaultdict` кращий, коли потрібно групувати або акумулювати значення за ключами: він автоматично створює default-значення через `default_factory` при зверненні через `__getitem__`.**[^py314-library-stdtypes] <span class="warn">Будь-яке звернення `d[key]` для відсутнього ключа тихо створює запис, тому випадковий lookup збільшує словник помилковими записами. Метод `d.get(key)` не викликає `default_factory` і не створює ключ.</span>

## Detailed explanation

Механізм, на якому побудований `defaultdict`, – перевизначений `__missing__`: коли `__getitem__`
не знаходить ключ, замість `KeyError` викликається `default_factory()` без аргументів, а
результат одразу записується в словник і повертається.[^py314-library-collections] Це відрізняє
`defaultdict` від `dict.setdefault(key, default)`: `setdefault` обчислює вираз-default щоразу під
час виклику, навіть якщо ключ уже існує і default не використовується, тоді як `default_factory`
викликається лише в разі реального промаху.

Типове застосування – групування: `d = defaultdict(list); d[key].append(item)` уникає ручного
`if key not in d: d[key] = []`. Для лічильників природний вибір – `defaultdict(int)`, бо `int()`
повертає `0`. Для вкладених структур можна передати не сам тип, а callable:
`defaultdict(lambda: defaultdict(int))` створює дерево словників на льоту.

Помилка, яку легко приховати, – неправильна factory, що приймає аргументи або має side effects:
`default_factory` викликається без параметрів, тож `defaultdict(list.append)` чи будь-яка factory,
що очікує на key, зламається на першому промаху з `TypeError`. Ще одна пастка – переплутати
`defaultdict(list)` із `defaultdict(list())`: другий варіант передає вже створений список як
`default_factory`, а не сам тип, і виклик `list()(...)` впаде з `TypeError`, бо список не
викликається.

Механізм тісно повʼязаний із `__missing__` у звичайних словниках qid:py-coll-0012 – `defaultdict`
є, по суті, найпростішим прикладом його застосування.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
