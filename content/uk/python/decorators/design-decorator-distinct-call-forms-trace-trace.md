---
id: py-decor-0006
title: "Як спроєктувати decorator з двома чіткими call forms, `@trace` і `@trace(level=2)`, не переплутавши decorated callable з configuration arguments?"
description: "Треба перевірити, чи перший аргумент є callable: якщо func is not None – це bare @trace, інакше повернути partial-декоратор з конфігурацією."
track: python
section: decorators
level: senior
type: practical
tags: [trace, trace-level-2]
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

**Треба перевірити, чи перший аргумент є callable: якщо `func is not None` – це bare `@trace`, інакше повернути partial-декоратор з конфігурацією.**[^py314-glossary-term-decorator] Типовий патерн: outer-функція приймає `func=None, *, level=1`. Якщо `func` – callable, застосувати wrapper одразу; якщо `None` – повернути decorator, який замкне `level`. Альтернатива – `functools.partial` або окремий factory. Головне – не намагатися відрізнити callable від конфігурації за типом аргументу, бо callable може бути будь-яким об'єктом з `__call__`.

## Detailed explanation

Підтримка двох форм виклику (`@trace` без дужок і `@trace(level=2)` з аргументами) вирішується через використання першого необов'язкового позиційного параметра `func=None` у поєднанні з обов'язковими іменованими параметрами (`keyword-only parameters`) для конфігурації.[^py314-reference-compound-stmts-function-definitions] Синтаксис `@trace` передає декоровану функцію першим позиційним аргументом, тоді як синтаксис `@trace(level=2)` викликає функцію без позиційного аргументу `func`, залишаючи його рівним `None`.

Ключовим архітектурним рішенням є відмова від перевірки типу першого аргументу через `callable(arg)`. Якщо конфігураційний параметр сам по собі є callable-об'єктом (наприклад, валідатор, предикат фільтрації або серіалізатор), позиційна передача призведе до непереборної колізії, де decorator сприйме конфігураційну функцію за декоровану. Оголошення всіх параметрів конфігурації як keyword-only (`*`) після `func=None` усуває неоднозначність на рівні граматики Python: значення конфігурації фізично неможливо передати в позицію `func`.

Коли `func is None`, функція виступає у ролі фабрики й повертає частково застосовану версію самої себе за допомогою `functools.partial(trace, level=level)` або внутрішнього замикання.[^py314-library-functools-functools-wraps] Коли цей повернутий об'єкт отримує реальну цільову функцію, він викликає той самий код `trace(func, level=level)`, застосовуючи стандартний `wrapper`, загорнутий через `@functools.wraps`. Цей патерн також автоматично підтримує виклик з порожніми дужками `@trace()`.

Реалізація універсального decorator з підтримкою обох форм виклику:

```python
from functools import partial, wraps

def trace(func=None, *, level=1):
    """Decorator supporting both @trace and @trace(level=2) forms."""
    if func is None:
        # Called with arguments or empty parentheses: return a configured decorator
        return partial(trace, level=level)

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[TRACE L{level}] Calling {func.__name__}")
        return func(*args, **kwargs)

    return wrapper

# Form 1: Bare decorator without parentheses
@trace
def add(a, b):
    return a + b

# Form 2: Parametrized decorator with keyword arguments
@trace(level=2)
def multiply(a, b):
    return a * b

# Form 3: Empty parentheses with default configuration
@trace()
def subtract(a, b):
    return a - b

add(2, 3)       # [TRACE L1] Calling add
multiply(2, 3)  # [TRACE L2] Calling multiply
subtract(5, 2)  # [TRACE L1] Calling subtract
```

**Архітектурні компроміси та підводні камені:**
- Дозвіл позиційних конфігураційних аргументів: якщо написати `def trace(func=None, level=1)`, виклик `@trace(2)` призведе до того, що число `2` потрапить у `func`, викликаючи помилку під час спроби застосування.
- Спроба перевірки через `callable(func)` без keyword-only параметрів: якщо декоратор приймає функцію як аргумент конфігурації (наприклад, `@retry(predicate=is_transient)`), позиційна передача помилково запустить гілку bare decorator.
- Підтримка виклику з порожніми дужками: форма `@trace()` повинна коректно повертати частково застосований декоратор, що природно гарантується умовою `if func is None`.
- Типізація у статичних аналізаторах: для повноцінної підтримки mypy та автодоповнення в IDE таку функцію слід перевантажувати через `@typing.overload`, описуючи окремо гілку без аргументів та гілку з параметрами.

## Environment

TODO

## Deliverable

TODO

## Acceptance criteria

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
