---
id: py-decor-0005
title: "Чим decorator factory відрізняється від самого decorator і на якому етапі обробляються її arguments?"
description: "Decorator factory – це функція, що повертає decorator; її аргументи обчислюються один раз при decoration, а повернутий decorator потім застосовується до функції."
track: python
section: decorators
level: middle
type: comparison
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

**Decorator factory – це функція, що повертає decorator; її аргументи обчислюються один раз при decoration, а повернутий decorator потім застосовується до функції.**[^py314-glossary-term-decorator] Наприклад, `@has_perm('view')` спочатку викликає `has_perm('view')` (factory), яка повертає справжній decorator, і вже він отримує декоровану функцію. Без factory синтаксис `@decorator(arg)` неможливий, бо decorator приймає лише один аргумент – callable.

## Detailed explanation

Decorator factory – це функція вищого порядку, яка приймає довільні конфігураційні параметри та повертає справжній decorator, тоді як сам decorator приймає лише один фіксований аргумент – об'єкт функції або класу, що декорується.[^py314-reference-compound-stmts-function-definitions] Це трирівнева структура замість дворівневої: фабрика створює decorator, decorator створює wrapper, а wrapper виконує цільову логіку.

Обробка аргументів фабрики відбувається під час визначення функції (definition time) у два чітких кроки. Спочатку інтерпретатор обчислює вираз виклику фабрики `@factory(*args, **kwargs)`, створюючи область видимості замикання (closure), де зберігаються передані налаштування. Потім повернутий фабрикою callable негайно викликається з об'єктом цільової функції як аргументом. Повернутий на цьому другому кроці `wrapper`, задекорований за допомогою `@functools.wraps`, замінює оригінальне ім'я у просторі імен.[^py314-library-functools-functools-wraps]

На етапі виконання (call time) аргументи фабрики вже зафіксовані в замиканні й не переобчислюються. Кожен виклик декорованої функції активує `wrapper`, який має прямий доступ як до аргументів конкретного виклику, так і до конфігураційних значень фабрики, збережених у замиканні.

Три рівні взаємодії (фабрика, decorator, wrapper) та послідовність етапів:

```python
from functools import wraps

def repeat(num_times: int):
    # Stage 1: Factory called with configuration arguments
    print(f"Stage 1: Factory created with num_times={num_times}")

    def decorator(func):
        # Stage 2: Decorator receives the target callable
        print(f"Stage 2: Decorator applied to {func.__name__}")

        @wraps(func)
        def wrapper(*args, **kwargs):
            # Stage 3: Wrapper executes on each runtime call
            print(f"Stage 3: Running {func.__name__} {num_times} times")
            result = None
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return decorator

# Definition time: Stage 1 runs, then Stage 2 runs
@repeat(num_times=2)
def greet(name: str) -> str:
    return f"Hello, {name}!"

# Call time: Stage 3 runs on every call
greet("Alice")
```

**Типові помилки та підводні камені:**
- Пропуск виклику фабрики (`@repeat` замість `@repeat()`): якщо фабрика вимагає дужок, використання імені без виклику передасть функцію замість аргументів конфігурації, викликаючи незрозумілий `TypeError`.
- Змінні об'єкти як значення за замовчуванням у фабриці: передача списків або словників у параметри фабрики розділяє спільний стан між усіма декорованими функціями.
- Спроба динамічно змінити конфігурацію фабрики під час виконання: оскільки аргументи фабрики замикаються на етапі визначення, зміна зовнішніх змінних після визначення функції не оновить поведінку wrapper, якщо фабрика явно не читає мутабельний об'єкт за посиланням.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
