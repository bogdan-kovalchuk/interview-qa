---
id: py-framew-0001
title: "Чим runtime validation у Pydantic відрізняється від static type checking?"
track: python
section: oop-and-data-model
sources:
  - source_id: py314-library-typing
    title: "Python 3.14: typing - Support for type hints"
    url: https://docs.python.org/3.14/library/typing.html#typing-support-for-type-hints
  - source_id: pep-0484
    title: "PEP 484: Type Hints"
    url: https://peps.python.org/pep-0484/
  - source_id: pydantic-models
    title: "Pydantic documentation: Models"
    url: https://pydantic.dev/docs/validation/latest/concepts/models/
  - source_id: pydantic-strict-mode
    title: "Pydantic documentation: Strict Mode"
    url: https://pydantic.dev/docs/validation/latest/concepts/strict_mode/
---

## Short answer

**Static type checker перевіряє анотації офлайн, без запуску програми.**[^pep-0484] Runtime Python не застосовує анотації функцій і змінних як перевірку типів.[^py314-library-typing] Pydantic читає анотації під час validation недовіреного входу і повертає model, поля якої відповідають оголошеним типам, або викидає `ValidationError`.[^pydantic-models] У Pydantic v2 за замовчуванням він приводить сумісні значення (`"42"` стає `42`), а strict mode це відхиляє.[^pydantic-strict-mode] Static checking знаходить невідповідності до запуску, а Pydantic перевіряє дані під час виконання; одне не замінює інше.

## Detailed explanation

Static type checker (наприклад mypy або pyright) читає анотації з вихідного коду і перевіряє їх офлайн, без запуску програми. PEP 484 описує анотації як дані, доступні в runtime через `__annotations__`, але без перевірки типів під час виконання: типи перевіряє окремий офлайн checker.[^pep-0484] Сам Python анотації функцій і змінних як перевірку типів не застосовує.[^py314-library-typing] Тому функція з анотацією `n: int` приймає рядок без помилки під час запуску:

```python
def double(n: int) -> int:
    return n * 2


print(double("ab"))  # prints abab; mypy reports the call as an error
```

Pydantic читає ті самі анотації під час виконання. Модель – клас, що наслідує `BaseModel` і описує поля як анотовані атрибути. Під час validation вона повертає екземпляр, поля якого відповідають оголошеним типам, або піднімає `ValidationError`.[^pydantic-models] Документація уточнює межу: гарантія стосується типів результату, а не вхідних даних. Недовірені дані передаються в model, і після validation її поля відповідають типам.[^pydantic-models]

```python
from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name: str


print(User(id="42", name="Ann"))  # id=42 name='Ann'
try:
    User(id="abc", name="Ann")
except ValidationError:
    print("rejected")  # rejected
```

Межі залежать від режиму. У Pydantic v2 за замовчуванням він намагається привести значення до потрібного типу, коли це можливо: `"42"` стає `42`.[^pydantic-strict-mode] Strict mode відхиляє таке приведення і повертає помилку, якщо тип даних не той.[^pydantic-strict-mode] Статичний checker на рядок `User(id="42", name="Ann")` у коді видасть помилку (`str` замість `int`), хоча lax mode у Pydantic v2 прийняв би той самий вхід у runtime. Отже checker оцінює текст програми, а Pydantic оцінює конкретне значення під час виконання.

Static checking і Pydantic доповнюють одне одного. Checker знаходить невідповідності в коді до запуску. Pydantic стоїть на межі, де дані приходять ззовні, наприклад з JSON, HTTP-запиту чи змінних середовища, і перевіряє їх під час виконання. Жоден не замінює інший: checker не побачить, що зовнішній JSON містить `"abc"`, а Pydantic не знайде помилку у внутрішньому виклику, який не створює model.

**Типові помилки:**
- вважати, що `def f(x: int)` перевіряє тип аргумента під час виклику;
- вважати, що Pydantic-модель перевіряє весь внутрішній код; вона перевіряє дані, що входять у model;
- очікувати, що `"42"` для поля `int` відхилиться без strict mode; у Pydantic v2 за замовчуванням воно стає `42`.
