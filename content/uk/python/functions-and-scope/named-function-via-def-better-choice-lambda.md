---
id: py-funcs-0021
title: "Коли іменована функція через `def` є кращим вибором за `lambda`, навіть якщо обидві можуть реалізувати той самий короткий вираз?"
track: python
section: functions-and-scope
sources:
  - source_id: py314-reference-expressions-lambdas
    title: "Python 3.14: Reference/expressions"
    url: https://docs.python.org/3.14/reference/expressions.html#lambdas
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
  - source_id: pep-8
    title: "PEP 8: Style Guide for Python Code"
    url: https://peps.python.org/pep-0008/#programming-recommendations
---

## Short answer

**`def` кращий, коли потрібне зрозуміле ім’я для traceback, docstring, type annotations або кілька інструкцій у тілі.**[^py314-reference-expressions-lambdas] Lambda обмежена одним виразом і не підтримує statements чи анотації.[^py314-reference-expressions-lambdas] Її `__name__` за замовчуванням дорівнює `"<lambda>"`, що ускладнює діагностику.[^pep-8] `def` створює function object із власним іменем, яке видно в traceback.

## Detailed explanation

Lambda і `def` створюють об’єкти одного роду: обидва дають function object, який можна викликати, передати як callback або зберегти в змінній. Різниця в записі та можливостях. Lambda – це вираз, який за документацією поводиться як function object, визначений через `def <lambda>(parameters): return expression`. Тому в її тілі є лише один вираз, без інструкцій, анотацій і docstring.[^py314-reference-expressions-lambdas]

Ім’я важливе тоді, коли функцію треба розпізнати поза кодом: у traceback, у repr, у логах. `def` визначає user-defined function object і прив’язує його до імені.[^py314-reference-compound-stmts-function-definitions] Lambda, навіть присвоєна змінній, має загальне ім’я `<lambda>`, тож у стеку викликів не видно, яка саме функція впала:

```python
def normalize_price(value: str) -> float:
    """Convert a price string to cents."""
    return float(value) * 100

as_lambda = lambda value: float(value) * 100

print(normalize_price.__name__)          # normalize_price
print(as_lambda.__name__)                # <lambda>
print(normalize_price.__annotations__)   # {'value': <class 'str'>, 'return': <class 'float'>}
print(normalize_price.__doc__)           # Convert a price string to cents.
print(as_lambda.__doc__)                 # None
```

Збій усередині такої функції дає в traceback рядок `in normalize_price` для `def` і `in <lambda>` для lambda. Саме тому PEP 8 прямо рекомендує використовувати `def` замість присвоєння lambda безпосередньо змінній: ім’я функції тоді стає справжнім, а не загальним `<lambda>`.[^pep-8] Коротший запис не є підставою для lambda, якщо функцію треба перевикористати, задокументувати або діагностувати.

**Типові помилки:**
- вважати, що lambda і `def` відрізняються лише записом: lambda не може містити кілька інструкцій, анотацій і docstring;
- присвоювати lambda змінній і очікувати в traceback справжнього імені, хоча там буде `<lambda>`;
- вибирати lambda лише через коротший запис, коли функцію потрібно повторно використовувати або діагностувати.
