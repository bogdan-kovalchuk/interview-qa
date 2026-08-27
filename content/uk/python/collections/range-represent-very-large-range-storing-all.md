---
id: py-coll-0002
title: "Чому `range` може представляти дуже великий діапазон без зберігання всіх integers у пам’яті?"
description: "range зберігає лише три значення – start, stop, step – і обчислює елементи на вимогу, тому споживає O(1) пам'яті незалежно від діапазону."
track: python
section: collections
level: middle
type: mechanism
tags: [range]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/sequences.md#L406-L428
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**`range` зберігає лише три значення – `start`, `stop`, `step` – і обчислює елементи на вимогу, тому споживає O(1) пам'яті незалежно від діапазону.**[^py314-library-stdtypes] `range(10**15)` і `range(10)` займають однаковий обсяг пам'яті. Операції `in` (арифметична перевірка) та індексація виконуються за O(1).

## Detailed explanation

`range` – це не контейнер з елементами, а компактний опис арифметичної прогресії: об'єкт зберігає
лише три числа (`start`, `stop`, `step`) і формулу для обчислення i-го елемента –
`start + i * step`.[^py314-library-stdtypes] Саме тому `range(10**15)` і `range(10)` створюються
миттєво і займають однаковий, фіксований обсяг пам'яті: різниця в розмірі діапазону не впливає на
розмір самого об'єкта, бо жоден елемент ніколи не матеріалізується заздалегідь.

Це відрізняє `range` від generator-а, який теж лінивий, але вміє лише йти вперед послідовно й не
знає власної довжини наперед. `range` реалізує `__len__`, `__getitem__` і `__contains__` напряму
через арифметику, тому `range(10**15)[500]` обчислюється за O(1) простою підстановкою у формулу, а
не переходом через 500 проміжних значень. Membership-перевірка `x in r` теж O(1): достатньо
перевірити, що `x` лежить у межах `[start, stop)` і що `(x - start) % step == 0`, без жодного
перебору.

Ітерація (`for i in range(...)`) створює окремий `range_iterator`, який на кожному кроці просто
додає `step` до поточного значення – O(1) на елемент, O(n) на весь прохід, але без збереження
попередніх значень: пам'ять, потрібна для ітерації, не залежить від того, скільки елементів уже
пройдено.

Зрізи (`range(...)[a:b:c]`) теж не матеріалізують нічого – результат зрізу є новим об'єктом `range`
з перерахованими `start`/`stop`/`step`, а не списком елементів, тому навіть узяти зріз з
мільярдного `range` – операція O(1). Якщо ж перетворити `range` на `list(range(10**15))`, Python
дійсно спробує виділити пам'ять під кожен елемент окремо, і це закономірно провалиться з
`MemoryError` набагато раніше, ніж буде вичерпано диск.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
