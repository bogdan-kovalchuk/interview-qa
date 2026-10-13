---
id: py-testing-0011
title: "Чому під час `patch()` треба замінювати name там, де його lookup робить code under test?"
description: "patch() змінює об’єкт, на який посилається ім’я в конкретному namespace, тому патчити треба те місце, звідки code under test це ім’я бере."
track: python
section: testing
level: middle
type: pitfall
tags: [patch]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-library-unittest
    title: "Python 3.14: Library/unittest"
    url: https://docs.python.org/3.14/library/unittest.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-unittest-mock
    title: "Python 3.14: Library/unittest.mock"
    url: https://docs.python.org/3.14/library/unittest.mock.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: pytest-docs
    title: "pytest documentation"
    url: https://docs.pytest.org/en/stable/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація pytest."
  - source_id: hypothesis-docs
    title: "Hypothesis documentation"
    url: https://hypothesis.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація Hypothesis (property-based testing)."
  - source_id: mutmut-docs
    title: "mutmut documentation"
    url: https://mutmut.readthedocs.io/en/latest/
    accessed: 2026-09-04
    kind: official
    version: null
    applicability: "Офіційна документація mutmut (mutation testing)."
  - source_id: py314-library-unittest-mock-where-to-patch
    title: "Python 3.14: Library/unittest.mock, Where to patch"
    url: https://docs.python.org/3.14/library/unittest.mock.html#where-to-patch
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14, розділ Where to patch: патч застосовується там, де код, що тестується, шукає ім’я."
---

## Short answer

**`patch()` змінює об’єкт, на який посилається ім’я в конкретному namespace, тому патчити треба те місце, звідки code under test це ім’я бере.**[^py314-library-unittest-mock-where-to-patch] Якщо модуль `b` робить `from a import SomeClass`, то `b` вже має власне посилання на клас, і `patch('a.SomeClass')` не вплине на код у `b`. Правильний патч – `patch('b.SomeClass')`.

## Detailed explanation

`patch()` тимчасово замінює об’єкт, на який вказує ім’я, але лише в тому namespace, який названо в аргументі target. Тому важить не те, де клас визначено, а те, де код, що тестуємо, шукає ім’я під час виконання. Документація `unittest.mock` формулює правило так: патчити треба місце пошуку, а не обов’язково місце визначення.[^py314-library-unittest-mock-where-to-patch]

Припустімо, `a.py` визначає `SomeClass`, метод якого `run()` повертає `"real"`, а `b.py` містить `from a import SomeClass` і функцію `some_function()`, яка повертає `SomeClass().run()`. Під час імпорту `b` отримує власне посилання на клас. Патч `a.SomeClass` змінює атрибут модуля `a`, але `b` уже тримає старе посилання. Приклад: патч у неправильному місці не потрапляє в `b`, а патч у `b` потрапляє.

```python
from unittest import mock
import b  # b.py: from a import SomeClass; some_function() calls SomeClass().run()

# Wrong: replaces a.SomeClass, but b already holds the real class
with mock.patch("a.SomeClass") as fake:
    fake.return_value.run.return_value = "fake"
    print(b.some_function())  # real

# Right: replaces the name in b, where some_function looks it up
with mock.patch("b.SomeClass") as fake:
    fake.return_value.run.return_value = "fake"
    print(b.some_function())  # fake
```

Правило не змінюється, коли код звертається до класу через модуль. Якщо `c.py` пише `import a` і викликає `a.SomeClass()` уже під час виконання функції, то `patch('a.SomeClass')` працює, бо `c` щоразу шукає ім’я в `a`. Універсального «патчити в a» немає: треба знайти, де код, що тестуємо, читає ім’я, і патчити саме там.

**Типові помилки:**
- патчити `a.SomeClass`, коли модуль зробив `from a import SomeClass`, і вважати тест перевіреним, хоча він звертається до реального класу;
- патчити місце визначення, не перевіривши, як тестований модуль імпортує ім’я;
- «лікувати» патч зміною імпортів у коді, замість того щоб патчити місце використання.

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
