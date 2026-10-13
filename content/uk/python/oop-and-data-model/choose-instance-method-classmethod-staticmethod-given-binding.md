---
id: py-oop-0014
title: "Коли обирати instance method, `@classmethod` або `@staticmethod` з огляду на потрібний binding і polymorphism?"
description: "Instance method – коли потрібен доступ до стану конкретного об’єкта; @classmethod – коли потрібен доступ до класу з підтримкою polymorphism; @staticmethod – коли метод не залежить ні від instance, ні від класу."
track: python
section: oop-and-data-model
level: middle
type: comparison
tags: [classmethod, staticmethod]
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
  - source_id: py314-howto-descriptor-class-methods
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#class-methods
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: розділ Class methods; classmethod отримує клас і при виклику через клас, і при виклику через instance."
  - source_id: py314-howto-descriptor-static-methods
    title: "Python 3.14: Howto/descriptor"
    url: https://docs.python.org/3.14/howto/descriptor.html#static-methods
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: розділ Static methods; staticmethod повертає базову функцію без змін."
---

## Short answer

**Instance method – коли потрібен доступ до стану конкретного об’єкта; `@classmethod` – коли потрібен доступ до класу з підтримкою polymorphism; `@staticmethod` – коли метод не залежить ні від instance, ні від класу.**[^py314-howto-descriptor-class-methods] `@classmethod` отримує клас, через який викликали метод, тому factory-методи при успадкуванні повертають екземпляр підкласу. `@staticmethod` не отримує ні `self`, ні `cls`.[^py314-howto-descriptor-static-methods] Тож він не знає, через який клас його викликали; перевизначити його в підкласі можна, як і будь-який атрибут класу.

## Detailed explanation

Три варіанти відрізняються першим неявним аргументом. Instance method отримує `self`: при доступі через instance це bound method. `@classmethod` отримує клас і при виклику через клас, і при виклику через instance (для instance це `type(obj)`).[^py314-howto-descriptor-class-methods] `@staticmethod` не отримує нічого: його `__get__` повертає базову функцію без змін.[^py314-howto-descriptor-static-methods]

Вибір залежить від того, що методу справді потрібно:

- instance method – коли метод читає або змінює стан конкретного об’єкта, наприклад `self.n`;
- `@classmethod` – коли потрібен сам клас: альтернативний конструктор, доступ до налаштувань класу або створення екземпляра того класу, через який викликали метод;
- `@staticmethod` – коли метод не бере ні стану, ні класу. Часто краще звичайна функція на рівні модуля: staticmethod лише групує її в namespace класу.

Приклад: `create` через `cls` повертає екземпляр підкласу, а `create_static` завжди повертає `Shape`. Коментарі показують результат запуску (CPython 3.14):

```python
class Shape:
    @classmethod
    def create(cls):
        return cls()                  # an instance of the class the call went through

    @staticmethod
    def create_static():
        return Shape()                # always Shape: there is no cls to choose from

class Square(Shape):
    pass

print(type(Square.create()).__name__)          # Square
print(type(Square().create()).__name__)        # Square: works through an instance too
print(type(Square.create_static()).__name__)   # Shape
```

Polymorphism тут має межі. `@classmethod` обирає поведінку за класом, через який викликали метод, і робить це через `cls`. `@staticmethod` теж бере участь у перевизначенні: якщо базовий метод викликає `self.kind()`, підклас з власним `kind` отримає виклик, бо пошук іде за іменем. Але сам staticmethod не знає, через який клас його викликали, тож правильний тип створити не може.[^py314-howto-descriptor-static-methods]

Межі `@classmethod`: він не має доступу до стану instance, бо `cls` – це клас, а не `self`. Клас визначається викликом, а не місцем оголошення: `Square.create()` повертає `Square`, хоча метод описаний у `Shape`.[^py314-howto-descriptor-class-methods]

**Типові помилки:**
- писати фабрику через `@staticmethod` з жорстко вказаним іменем класу: підклас отримає базовий тип;
- робити `@classmethod` без потреби в класі лише через те, що метод не використовує `self`;
- вважати, що `@staticmethod` не можна перевизначити в підкласі.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
