---
id: py-coll-0004
title: "Чому repeated concatenation списку в циклі може бути гіршою за `append`/`extend`, навіть якщо результат однаковий?"
description: "Операція lst = lst + [x] щоразу створює новий список і копіює всі елементи, що дає O(n²) для n ітерацій."
track: python
section: collections
level: middle
type: comparison
tags: [append, extend]
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
    url: https://github.com/tavor118/pj_python_interview_questions_and_answers/blob/02d57a7a9f34fd386eb8aa5c0094fe3f3c3ba141/docs/python/sequences.md#L292-L321
    accessed: 2026-09-04
    kind: community
    version: null
    applicability: "Джерело виявлення теми з попередньої (community) бази питань; текст відповіді написаний окремо і не копіює це джерело."
---

## Short answer

**Операція `lst = lst + [x]` щоразу створює новий список і копіює всі елементи, що дає O(n²) для n ітерацій.**[^py314-library-stdtypes] Натомість `lst.append(x)` працює за амортизоване O(1), а `lst.extend(iterable)` або `lst += iterable` модифікують список на місці. <span class="warn">Саме `lst = lst + [x]` (з переприв'язкою) є повільним; `lst += [x]` – це in-place операція, еквівалентна `extend`.</span>

## Detailed explanation

Різниця в поведінці випливає з того, що `list` – це масив покажчиків із наперед виділеною ємністю,
більшою за поточну довжину. `append(x)` в амортизованому випадку просто записує вказівник у вже
виділену комірку; лише коли ємність вичерпується, CPython перевиділяє масив і копіює всі елементи –
але робить це вдвічі рідше з кожним разом, тому сумарна вартість n викликів append залишається
O(n), а не O(n²).[^py314-library-stdtypes]

`lst = lst + [x]`, навпаки, щоразу створює абсолютно новий список: оператор `+` для list виділяє
пам'ять під `len(lst) + 1` елементів і копіює туди всі наявні покажчики плюс новий. Це відбувається
на кожній ітерації циклу незалежно від того, скільки вільної ємності мав попередній список –
переприв'язка імені `lst` не залишає альтернативи. Для n ітерацій сума копіювань 1 + 2 + ... + n
дає O(n²).

`extend(iterable)` уникає цієї проблеми інакше, ніж `append`: якщо `iterable` підтримує `__len__`,
CPython може одразу перевиділити список під потрібний розмір і скопіювати елементи один раз, за
O(k) для k нових елементів, замість k окремих перевиділень.[^py314-howto-sorting]

Практичний наслідок: у циклі, де на кожній ітерації додається один елемент, треба обирати між
`append` (по одному) і накопиченням у тимчасовий список з подальшим одноразовим `extend` – обидва
лінійні. Помилка трапляється саме тоді, коли код виглядає майже так само, як `append`, але
використовує `+` замість `+=`: `lst = lst + [x]` і `lst += [x]` дають однаковий результат, але
перший завжди O(n) на виклик, а другий – амортизовано O(1), бо `+=` для list викликає `__iadd__`,
тобто `extend` на місці, а не створення нового об'єкта.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
