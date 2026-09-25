---
id: py-compfn-0009
title: "Як `functools.partial` змінює call interface без негайного виклику wrapped callable?"
description: "functools.partial повертає новий callable-об'єкт, у якому частину positional або keyword arguments «заморожено», але оригінальна функція не викликається до виклику partial-об'єкта."
track: python
section: comprehensions-and-functional
level: middle
type: mechanism
tags: [functools-partial]
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

**`functools.partial` повертає новий callable-об'єкт, у якому частину positional або keyword arguments «заморожено», але оригінальна функція не викликається до виклику partial-об'єкта.**[^py314-howto-functional] Додаткові arguments при виклику доповнюють заморожені; нові keyword arguments мають пріоритет над попередньо заданими. Наприклад, `functools.partial(pow, 2)` створює функцію обчислення квадрата: `f(10)` -> `1024`.

## Detailed explanation

Функція `functools.partial` повертає новий екземпляр спеціального типу `partial`, який обгортає вихідний callable і фіксує частину його позиційних та іменованих аргументів без його виконання.[^py314-library-functools] Створений об'єкт зберігає три доступні для читання атрибути: `.func` (посилання на оригінальний callable), `.args` (кортеж заморожених positional arguments) та `.keywords` (словник або `None` із замороженими keyword arguments).

У момент виклику об'єкта `partial(*more_args, **more_kwargs)` відбувається динамічне злиття аргументів безпосередньо перед передачею в оригінальну функцію. Позиційні аргументи об'єднуються конкатенацією кортежів `self.args + more_args` (заморожені завжди йдуть першими), а іменовані – об'єднанням словників `{**self.keywords, **more_kwargs}`, де нові значення перекривають раніше зафіксовані. Сама функція викликається лише тоді, коли викликається сам об'єкт `partial`.

Оскільки `partial` є самостійним типом, а не звичайною функцією Python, він не реалізує стандартний descriptor protocol для прив'язки методів екземпляра в класах (для методів класів існує `functools.partialmethod`). Крім того, об'єкт `partial` не копіює атрибути `__name__` і `__doc__` автоматично, хоча модуль `inspect` коректно відображає його актуальну сигнатуру виклику.

Створення частково застосованої функції та дослідження її внутрішніх атрибутів:

```python
from functools import partial


def greet(greeting: str, name: str, punctuation: str = "!") -> str:
    return f"{greeting}, {name}{punctuation}"


# Freeze the first positional argument 'greeting'
say_hello = partial(greet, "Hello")

# Attributes stored on the partial object
print(say_hello.func is greet)  # True
print(say_hello.args)  # ('Hello',)

# Calling the partial object with the remaining arguments
print(say_hello("Alice"))
# Output: Hello, Alice!

# Overriding a default keyword argument at call time
print(say_hello("Bob", punctuation="?"))
# Output: Hello, Bob?
```

**Особливості та типові обмеження `functools.partial`:**
- позиційні аргументи завжди додаються попереду: неможливо стандартним `partial` «заморозити» другий аргумент, залишивши перший незаповненим (у такому разі слід використовувати keyword arguments або `lambda`);
- відсутність підтримки дескрипторів: для методів класів слід використовувати `functools.partialmethod`, інакше `partial` не передасть `self` автоматично;
- об'єкти `partial` не копіюють автоматично метадані `__name__` і `__doc__`, звертатися до них потрібно через атрибут `.func`.

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
