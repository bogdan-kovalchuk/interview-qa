---
id: py-compfn-0003
title: "Чому iteration variable comprehension не витікає в containing scope, але target assignment expression у comprehension може зв’язуватися в containing scope?"
description: "Comprehension створює окрему неявну scope для iteration variable, але := (assignment expression) спеціально прив'язує свій target у containing scope, оминаючи цю ізоляцію."
track: python
section: comprehensions-and-functional
level: senior
type: pitfall
tags: []
status: published
updated: 2026-09-27
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

**Comprehension створює окрему неявну scope для iteration variable, але `:=` (assignment expression) спеціально прив'язує свій target у containing scope, оминаючи цю ізоляцію.**[^py314-howto-functional] Наприклад, після `[y := x for x in data]` ім'я `y` доступне поза comprehension, тоді як `x` – ні. <span class="warn">Якщо в containing scope є `nonlocal` або `global` декларація для цього імені, `:=` її поважає.</span>

## Detailed explanation

В ізоляції змінних ітерації та поведінці оператора `:=` у comprehension проявляється навмисна еволюція системи областей видимості (scoping rules) у Python.[^py314-howto-functional]

В історичних версіях Python 2 змінні циклу `for` у list comprehensions витікали в навколишній контекст, перезаписуючи змінні функції чи модуля. Починаючи з Python 3, кожний comprehension (list, set, dict та generator expressions) компілюється в окрему неявну функціональну область видимості (nested code object), тому його ітераційні змінні є локальними для цього блоку і видаляються після завершення обчислення.[^py314-reference-expressions-displays-for-lists-sets-and-dict]

Коли PEP 572 додав оператор assignment expression (`:=`), розробники свідомо заклали виняток із цього правила для comprehensions: присвоєння через `:=` завжди прив'язує ім'я в найближчу *зовнішню* область видимості (containing scope функції або модуля), а не всередині неявної функції comprehension.[^py314-reference-expressions-displays-for-lists-sets-and-dict] Це зроблено прагматично, щоб дозволити збереження проміжних результатів або фільтрів (наприклад, вирахуваного дорогого значення для фільтрації та формування елемента списку). Водночас Python забороняє використовувати ім'я ітераційної змінної comprehension як ціль для `:=` (наприклад, `[i := i + 1 for i in range(5)]` викличе `SyntaxError`), щоб уникнути конфлікту між локальною та зовнішньою областями видимості.

Ізоляція змінної ітерації та зовнішнє зв'язування walrus operator:

```python
data = [1, 2, 3, 4]

# 1. Iteration variable 'item' is isolated within the comprehension scope:
squares = [item * item for item in data]
print("item" in locals())  # False: iteration variable does not leak

# 2. Walrus operator ':=' deliberately binds in the enclosing scope:
filtered = [last := x * 10 for x in data if x > 2]
print(filtered)            # [30, 40]
print("last" in locals())  # True: target leaks into containing scope
print(last)                # 40 (holds the value from the last matching iteration)

# 3. Reusing the comprehension variable as a walrus target is a SyntaxError:
# [x := x + 1 for x in data] -> SyntaxError: assignment expression cannot rebind comprehension iteration variable
```

**Підводні камені та архітектурні обмеження:**
- ненавмисне затінення (shadowing) чи перезапис змінних навколишньої функції через оператор `:=` всередині генераторних виразів чи comprehensions;
- спроба прив'язати ціль `:=` до самої змінної ітерації, що викликає `SyntaxError` ще на етапі компіляції;
- використання `:=` у comprehension на рівні класу, де scoping rules забороняють зв'язування з простором імен класу, викликаючи `TargetScopeError` / `SyntaxError`;
- залежність від значення змінної walrus після порожнього або відфільтрованого comprehension, якщо жоден елемент не пройшов фільтр `if`.

## Symptom

TODO

## Why it happens

TODO

## How to avoid

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
