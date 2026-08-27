---
id: py-compfn-0001
title: "Яку scope має iteration variable у list comprehension на Python 3 і чи замінює вона однойменний outer variable?"
description: "Iteration variable у list comprehension виконується в окремій неявній вкладеній scope і не витікає в enclosing scope."
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

**Iteration variable у list comprehension виконується в окремій неявній вкладеній scope і не витікає в enclosing scope.**[^py314-howto-functional] Тому однойменна зовнішня змінна зберігає своє значення: після `x = 99; result = [x for x in range(3)]` змінна `x` дорівнює `99`, а не `2`. Це відрізняє comprehension від звичайного циклу `for`, де iteration variable залишається в поточній scope.

## Detailed explanation

Ізоляція scope реалізована технічно: починаючи з Python 3, comprehension компілюється у власний
implicit код-об'єкт (як маленька вкладена функція), яка викликається одразу з переданим їй першим
(найзовнішнішим) iterable як аргументом.[^py314-howto-functional] Саме тому змінна `x` живе лише
всередині цього прихованого виклику й ніколи не потрапляє в enclosing scope – це не спеціальний
виняток для comprehension, а звичайна ізоляція locals функції.

Це відрізняється від поведінки Python 2, де list comprehension (на відміну від generator expression
і set/dict comprehension, які завжди мали власну scope) виконувався у поточній scope і залишав
iteration variable доступною після себе; Python 3 уніфікував усі чотири види comprehension так, щоб
вони всі мали власну implicit scope.

Наслідок для closures: функції (наприклад, `lambda`), створені всередині тіла comprehension,
захоплюють iteration variable з implicit scope самого comprehension, а не з enclosing scope. Це
означає, що список `[lambda: i for i in range(3)]` створює lambda-функції, які після виконання
comprehension усі повертають `2` – класична проблема пізнього зв'язування (late binding), але вона
відбувається всередині власної, ізольованої scope comprehension, а не enclosing.

Якщо в comprehension кілька `for`, окрему implicit scope отримує весь comprehension цілком, а не
кожен `for` окремо: усі iteration variables усіх рівнів вкладеності живуть в одній і тій самій
прихованій функції й однаково недоступні зовні. Винятком залишається лише ітерований вираз
найпершого `for` – він обчислюється в enclosing scope до входу в implicit функцію, тому саме він
може безпечно посилатися на змінні, які інакше конфліктували б з іменами всередині comprehension.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
