---
id: py-funcs-0016
title: "Чому всі функції, створені як `[lambda: i for i in range(3)]`, після завершення comprehension повертають те саме значення?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-faq-programming-why-do-lambdas-defined-in-a-loop-with
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-do-lambdas-defined-in-a-loop-with-different-values-all-return-the-same-result
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
  - source_id: py314-reference-expressions-lambda
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#lambda
  - source_id: py314-reference-expressions-displays-for-lists-sets-and-dictionaries
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#displays-for-lists-sets-and-dictionaries
---

## Short answer

**Усі lambda захоплюють одну й ту саму змінну `i`, а не її значення на момент створення; після завершення comprehension вона дорівнює 2, тож кожен виклик повертає `2`.**[^py314-faq-programming-why-do-lambdas-defined-in-a-loop-with] 

```python
funcs = [lambda: i for i in range(3)]
print([f() for f in funcs])  # [2, 2, 2]
```

Щоб зафіксувати поточне значення, використовують default argument: `lambda i=i: i`.

## Detailed explanation

Lambda, створена в comprehension, є closure, і вона не копіює значення `i` під час створення. Вона посилається на змінну `i` із зовнішнього scope через її cell, тому значення читається в момент виклику, а не визначення. FAQ Python пояснює саме це: змінна читається під час виклику lambda.[^py314-faq-programming-why-do-lambdas-defined-in-a-loop-with]

Comprehension виконується у власному implicitly nested scope, тож `i` не лишається в зовнішньому scope: `print(i)` після comprehension дає `NameError`.[^py314-reference-expressions-displays-for-lists-sets-and-dictionaries] Усі ітерації використовують одну cell, тож після завершення comprehension вона зберігає останнє значення 2, і кожна lambda бачить 2 через ту саму cell.

Щоб зафіксувати значення, lambda приймає його як параметр із default, а default обчислюється в момент створення lambda:

```python
fixed = [lambda i=i: i for i in range(3)]
print([f() for f in fixed])  # [0, 1, 2]: each lambda has its own parameter i
```

Правило default таке саме, як для `def`: значення обчислюється один раз, коли виконується визначення функції.[^py314-reference-compound-stmts-function-definitions] Lambda поводиться як функція, визначена через `def`, тож це правило діє і для неї.[^py314-reference-expressions-lambda] Той самий ефект дає фабрика, наприклад `def make(n): return lambda: n`, бо кожен її виклик створює нову cell.

Цей прийом має межу: default – звичайний параметр, тож виклик із аргументом його перекриває. `fixed[0](99)` поверне `99`, а `list(map(fixed[2], [10, 20]))` поверне `[10, 20]`. Якщо lambda не має приймати позиційні аргументи, параметр можна зробити keyword-only: `lambda *, i=i: i`, тоді виклик `f(99)` дасть `TypeError`.

**Типові помилки:**
- вважати, що `[lambda: i for i in range(3)]` дає 0, 1, 2, бо значення нібито фіксується на кожній ітерації;
- додати default до lambda, яку `map` або callback викликає з аргументами, і не помітити, що аргумент замінює default;
- шукати `i` після comprehension: змінна не лишається в зовнішньому scope, тому `print(i)` дає `NameError`.
