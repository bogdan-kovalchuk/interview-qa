---
id: py-coll-0022
title: "Чому membership у list зазвичай має linear cost, а в set або dict очікується average constant-time lookup?"
description: "Для list оператор in виконує лінійний пошук: порівнює x з кожним елементом через == – O(n)."
track: python
section: collections
level: middle
type: comparison
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
    version: null
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/set_and_dict.md#L540-L592
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Для `list` оператор `in` виконує лінійний пошук: порівнює `x` з кожним елементом через `==` – O(n).**[^py314-library-stdtypes] `set` і `dict` у CPython використовують hash-таблицю: обчислюється `hash(key)`, за ним знаходиться бакет, і лише там викликається `==` – average O(1). <span class="warn">У найгіршому випадку (багато collision-ів) lookup у hash-таблиці деградує до O(n).</span>

## Detailed explanation

У `list` немає жодної допоміжної структури, яка пов'язувала б значення з позицією: єдиний спосіб
перевірити `x in lst` – пройти елементи по черзі й порівняти кожен через `==`, доки не знайдено
збіг або не скінчиться список. Це лінійно за визначенням, незалежно від того, відсортований список
чи ні; використати щось швидше за O(n) без побудови додаткової структури неможливо, бо в `list`
немає індексу за значенням, лише індекс за позицією.[^py314-library-stdtypes]

`set` і `dict` замість цього індексують елементи за `hash(x)`: значення потрапляє в конкретний
бакет одразу при вставці, тому lookup обчислює `hash(x)` один раз і перевіряє лише кандидатів у
цьому бакеті – в середньому один-два елементи, а не всі n. CPython підтримує це "в середньому",
автоматично розширюючи таблицю, коли вона заповнюється більш ніж приблизно на дві третини, тому
load factor і, відповідно, довжина probe-послідовності залишаються малими навіть коли елементів
стає багато.

Ця перевага коштує двох речей. По-перше, елементи `set`/`dict` мають бути hashable – список чи
інший мутабельний контейнер не можна покласти в `set` узагалі, тому для колекцій зі списками
всередині доводиться або конвертувати їх у `tuple`, або залишатися на лінійному пошуку по `list`.
По-друге, побудова самого `set` із наявного `list` коштує O(n) і додаткової пам'яті під hash-таблицю
– вигідно, коли membership перевіряється неодноразово (`m` перевірок по `set` коштують
O(n + m) сумарно проти O(n * m) для `list`), але не варте того для одноразової перевірки в
маленькій колекції, де накладні витрати на побудову й хешування можуть переважити виграш.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
