---
id: py-compfn-0002
title: "У якому порядку обчислюються clauses у comprehension з кількома `for` та `if`?"
description: "Clauses обчислюються зліва направо, як вкладені цикли: кожен for – новий рівень вкладеності, а if фільтрує на поточному рівні."
track: python
section: comprehensions-and-functional
level: middle
type: mechanism
tags: []
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
---

## Short answer

**Clauses обчислюються зліва направо, як вкладені цикли: кожен `for` – новий рівень вкладеності, а `if` фільтрує на поточному рівні.**[^py314-howto-functional] Результат еквівалентний вкладеним `for`/`if` блокам зліва направо, де вираз-результат обчислюється щоразу на найглибшому рівні. Наприклад, `[(i,j) for i in range(3) for j in range(2) if (i+j) % 2 == 0]` дає `[(0, 0), (1, 1), (2, 0)]`.

## Detailed explanation

Порядок `for`/`if` у comprehension безпосередньо визначає, на якому етапі відбувається фільтрація, а
не лише семантику результату. Компілятор транслює comprehension у послідовність вкладених циклів
буквально: кожен наступний `for` компілюється як тіло попереднього, тому змінна, оголошена в
першому `for`, доступна всім наступним `for` та `if` праворуч від неї, але жоден `for` не бачить
змінних, які будуть оголошені пізніше.[^py314-reference-expressions-displays-for-lists-sets-and-dict]

Місце `if` у ланцюжку впливає на кількість ітерацій, а не тільки на те, що потрапить у результат.
Якщо `if` стоїть одразу після `for x`, він відсікає непридатні `x` ще до входу у вкладений цикл за
`y` – тому елементи, що не пройшли умову, взагалі не породжують ітерацій внутрішнього циклу. Якщо
той самий `if` перенести в кінець, після обох `for`, зовнішній і внутрішній цикли все одно
виконаються повністю для кожної пари, а фільтрація відбудеться вже на найглибшому рівні. Різниця не
в результаті (він однаковий), а у кількості виконаних ітерацій і, отже, у вартості обчислення при
дорогих `for`-джерелах.

Кілька `if` підряд на одному рівні (без `for` між ними) працюють як послідовність умов з коротким
замиканням, еквівалентна `if cond1 and cond2`: якщо `cond1` хибна, `cond2` взагалі не обчислюється.
Це важливо, коли друга умова може підняти exception на елементах, які перша умова вже відсіяла –
порядок `if`-ів у такому разі є вибором, а не випадковістю.

Сам вираз-результат (перед першим `for`) обчислюється не одразу для всіх комбінацій, а щоразу, коли
виконання доходить до найглибшого рівня вкладеності і всі `if` на цьому шляху пройдені – так само,
як тіло найвнутрішнішого циклу у явному коді.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
