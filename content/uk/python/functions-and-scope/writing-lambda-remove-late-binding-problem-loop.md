---
id: py-funcs-0017
title: "Чому запис `lambda i=i: i` усуває late-binding проблему в циклі, хоча default arguments самі можуть бути джерелом помилок?"
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
  - source_id: py314-faq-programming-why-are-default-values-shared-between
    title: "Python 3.14: Faq/programming"
    url: https://docs.python.org/3.14/faq/programming.html#why-are-default-values-shared-between-objects
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#user-defined-functions
---

## Short answer

**Default arguments обчислюються один раз – у момент виконання `def` або `lambda`, тому `i=i` зберігає поточне значення `i` як локальний параметр кожної lambda.**[^py314-reference-compound-stmts-function-definitions][^py314-reference-expressions-lambda] Кожна lambda отримує власний параметр `i` з фіксованим значенням, і виклик `f()` повертає саме його. Ризик: якщо default – мутабельний об’єкт (наприклад, `[]`), його зміна в одному виклику вплине на всі наступні виклики цієї функції.[^py314-faq-programming-why-are-default-values-shared-between]

## Detailed explanation

Default parameter values обчислюються один раз, коли виконується визначення функції, і зберігаються в атрибуті `__defaults__`.[^py314-reference-compound-stmts-function-definitions][^py314-reference-datamodel] Для `lambda` це те саме правило, бо lambda поводиться як функція, визначена через `def`.[^py314-reference-expressions-lambda] Вираз `i=i` тому виконується на кожній ітерації циклу: правий `i` читається в момент створення lambda, і його значення стає default параметра. Параметр `i` є локальною змінною lambda, тож вона більше не читає спільну змінну циклу, а має власну копію значення.[^py314-faq-programming-why-do-lambdas-defined-in-a-loop-with]

Атрибут `__defaults__` показує, що кожна lambda зберегла своє значення:

```python
fixed = [lambda i=i: i for i in range(3)]
print([f() for f in fixed])             # [0, 1, 2]
print([f.__defaults__ for f in fixed])  # [(0,), (1,), (2,)]
```

Та сама механіка робить мутабельний default спільним для всіх викликів: об’єкт створюється один раз, і його зміна переживає виклики.[^py314-faq-programming-why-are-default-values-shared-between]

```python
def add(x, bucket=[]):
    bucket.append(x)
    return bucket

print(add(1), add(2))  # [1, 2] [1, 2]: both calls return the same list object
```

Стандартний прийом для такого випадку – `None` як default і створення нового об’єкта в тілі функції, після явної перевірки.[^py314-reference-compound-stmts-function-definitions]

Межа самого прийому: default – звичайний параметр, тож позиційний аргумент від викликача його перекриває. `list(map(fixed[2], [10, 20]))` дає `[10, 20]`, бо `map` передає аргументи, і вони замінюють default. Тому `i=i` безпечний для lambda, яку викликають без аргументів; якщо можливі позиційні аргументи, параметр робиться keyword-only: `lambda *, i=i: i`.

**Типові помилки:**
- вважати, що `i=i` обчислюється під час кожного виклику lambda, а не один раз при її створенні;
- використовувати мутабельний default (`[]`, `{}`) як порожній стан для накопичення між викликами;
- передавати функцію з default у `map` або callback, які передають аргументи, і не помітити, що вони замінюють default.
