---
id: py-oop-0003
title: "Що станеться, якщо `__init__` явно поверне значення, відмінне від `None`, і чому?"
description: "Python підніме TypeError: __init__() should return None, not '...'."
track: python
section: oop-and-data-model
level: middle
type: pitfall
tags: [init]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-descriptor
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-howto-mro
    title: "Python 3.14: Howto/mro"
    url: https://docs.python.org/3.14/howto/mro.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-library-dataclasses
    title: "Python 3.14: Library/dataclasses"
    url: https://docs.python.org/3.14/library/dataclasses.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel-object-init
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__init__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: розділ object.__init__ моделі даних."
---

## Short answer

**Python підніме `TypeError: __init__() should return None, not '...'`.**[^py314-reference-datamodel-object-init] Під час виклику класу інтерпретатор перевіряє, що повернув `__init__`: будь-яке значення, відмінне від `None` (зокрема `0` чи `False`), є помилкою, бо `__new__` і `__init__` разом створюють об’єкт, а `__init__` лише налаштовує вже створений instance.[^py314-reference-datamodel-object-init]

## Detailed explanation

Виклик класу, наприклад `Point(1, 2)`, створює об’єкт через `__new__`, передає його в `__init__` для налаштування і повертає цей об’єкт. Значення, яке повернув би `__init__`, не стає результатом виклику класу. Замість нього Python вимагає `None` і піднімає `TypeError`, якщо отримав щось інше.[^py314-reference-datamodel-object-init]

Приклад показує обидві поведінки: повернення `0` дає помилку, а `return None` – ні.

```python
class Bad:
    def __init__(self):
        return 0            # any value other than None

try:
    Bad()
except TypeError as e:
    print(e)                # __init__() should return None, not 'int'

class Good:
    def __init__(self):
        return None         # same as a bare return or no return at all

print(type(Good()).__name__)  # Good
```

Перевірка стосується саме виклику класу. Якщо викликати `__init__` напряму для вже створеного об’єкта, це звичайна функція, і `obj.__init__()` поверне `0` без винятку. Тож правило про `None` діє тоді, коли інтерпретатор створює instance через виклик класу.[^py314-reference-datamodel-object-init]

Якщо `__init__` має сигналізувати про помилку, правильний спосіб – підняти виняток, наприклад `raise ValueError(...)`. Виняток зупиняє створення об’єкта і передає повідомлення назовні, тоді як повернене значення при виклику класу призводить лише до `TypeError`.

**Типові помилки:**
- закінчити `__init__` рядком `return self`, що дає `TypeError` під час виклику класу;
- повертати `False` або код помилки з `__init__` замість `raise`;
- очікувати, що `Cls()` поверне значення, яке повернув `__init__`.

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
