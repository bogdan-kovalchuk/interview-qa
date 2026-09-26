---
id: py-decor-0001
title: "Коли обчислюється decorator expression і коли викликається wrapper, який decorator повернув?"
description: "Decorator expression обчислюється один раз під час визначення функції, а wrapper викликається при кожному виклику декорованої функції."
track: python
section: decorators
level: middle
type: mechanism
tags: []
status: published
updated: 2026-09-27
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-glossary-term-decorator
    title: "Python 3.14: Glossary"
    url: https://docs.python.org/3.14/glossary.html#term-decorator
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-functools-functools-wraps
    title: "Python 3.14: Library/functools"
    url: https://docs.python.org/3.14/library/functools.html#functools.wraps
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-compound-stmts-function-definitions
    title: "Python 3.14: Reference/compound Stmts"
    url: https://docs.python.org/3.14/reference/compound_stmts.html#function-definitions
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**Decorator expression обчислюється один раз під час визначення функції, а wrapper викликається при кожному виклику декорованої функції.**[^py314-glossary-term-decorator] Тобто `@dec` виконує `dec(func)` immediately в scope, де визначена функція, і повертає wrapper-об'єкт. Сам wrapper запускається лише тоді, коли хтось викликає декороване ім'я. Це означає, що важка логіка ініціалізації (наприклад, відкриття файлу) потрапляє в decoration time, а per-call логіка – у wrapper.

## Detailed explanation

У Python інструкція `def` є виконуваним виразом, тому синтаксичний цукор `@decorator` обчислюється і застосовується негайно в момент визначення функції (definition time), тоді як повернута функція-обгортка (`wrapper`) виконується лише під час фактичних наступних викликів (call time).[^py314-reference-compound-stmts-function-definitions] Запис `@decorator def func(): ...` є еквівалентом створення стандартного об'єкта функції з наступним присвоєнням `func = decorator(func)`.

Якщо функція оголошена на рівні модуля, decorator викликається рівно один раз під час першого імпорту або запуску цього модуля. Усередині тіла самого decorator виконується ініціалізаційна логіка: реєстрація функції в реєстрах (наприклад, маршрутизаторах вебфреймворків), перевірка сигнатури чи підготовка замикання. Повернутий об'єкт зв'язується з оригінальним ім'ям `func` у поточному просторі імен.

Код обгортки `wrapper`, задекорований за допомогою `@functools.wraps`, не запускається під час оголошення функції.[^py314-library-functools-functools-wraps] Він очікує прямого виклику `func(*args, **kwargs)` у процесі роботи програми й виконується стільки разів, скільки викликається функція. Це фундаментальне розмежування життєвого циклу: важкі обчислення налаштування або одноразова реєстрація повинні відбуватися в зовнішньому тілі decorator, а динамічна валідація аргументів, вимірювання часу чи обробка винятків – усередині `wrapper`.

Демонстрація послідовності виконання на етапі визначення та під час викликів:

```python
from functools import wraps

def audit(func):
    print(f"1. Decorator applied to '{func.__name__}' at definition time")

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"2. Wrapper called for '{func.__name__}' at runtime")
        return func(*args, **kwargs)

    return wrapper

print("Before function definition")

@audit
def greet(name):
    return f"Hello, {name}!"

print("After function definition")

# The wrapper executes only on runtime calls
print(greet("Alice"))
print(greet("Bob"))
```

**Типові помилки та практичні наслідки:**
- Розміщення логіки, яка залежить від аргументів запиту чи сесії, у зовнішньому тілі decorator замість `wrapper`: такий код виконається лише один раз під час завантаження модуля, а не для кожного запиту.
- Виконання тривалих операцій (мережеві запити, підключення до бази даних) на рівні визначення decorator, що сповільнює імпорт модуля або взагалі завершується аварійно, якщо ресурси ще не ініціалізовані.
- Приховування побічних ефектів під час тестів: оскільки імпорт модуля одразу викликає всі його decorators, тестовий імпорт може ненавмисно модифікувати глобальні реєстри чи викликати системні ресурси.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
