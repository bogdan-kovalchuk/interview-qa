---
id: py-oop-0028
title: "Які trade-offs щодо пам’яті та успадкування має `__slots__` і чому це не універсальна performance-оптимізація?"
description: "__slots__ прибирає `__dict__` екземпляра й може зменшити пам’ять, але обмежує атрибути, слабкі посилання та успадкування."
track: python
section: oop-and-data-model
level: senior
type: practical
tags: [slots]
status: published
updated: 2026-10-13
content_revision: 2
reconciled_with:
  en: 2
applies_to:
  - product: "CPython"
    version: null
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
  - source_id: py314-reference-datamodel-slots
    title: "Python 3.14: Reference/datamodel (__slots__)"
    url: https://docs.python.org/3.14/reference/datamodel.html#slots
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: розділ __slots__ про відсутність __dict__ і __weakref__, успадкування, обмеження множинного успадкування та конфлікт з атрибутами класу."
---

## Short answer

**`__slots__` замінює `__dict__` екземпляра фіксованим набором слотів, тому пам’ять може зменшитися, але клас втрачає гнучкість.**[^py314-reference-datamodel-slots] Нових атрибутів поза `__slots__` не створити, доки не додано `__dict__` до `__slots__`, а слабкі посилання потребують `__weakref__` у `__slots__`.[^py314-reference-datamodel-slots] Subclass без власного `__slots__` отримує `__dict__`, тож економія для його екземплярів зникає, а з кількох батьківських класів лише один може мати непорожні слоти, інакше `TypeError`.[^py314-reference-datamodel-slots]

## Detailed explanation

Без `__slots__` кожен екземпляр зберігає атрибути у власному словнику `__dict__`. Коли клас задає `__slots__`, під перелічені імена резервується місце, а доступ до них реалізовано дескрипторами рівня класу.[^py314-reference-datamodel-slots] Відсутність словника для кожного екземпляра дає економію пам’яті, яка може бути істотною, і швидкість доступу до атрибутів також може покращитися.[^py314-reference-datamodel-slots] Виграш росте з кількістю екземплярів, тому його треба вимірювати на реальному навантаженні. Нижче клас зі слотами, який не приймає нових атрибутів:

```python
class Point:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(1, 2)
print(hasattr(p, "__dict__"))  # False: there is no per-instance dict
try:
    p.z = 3
except AttributeError as error:
    print(error)  # 3.13+: 'Point' object has no attribute 'z' and no __dict__ for setting new attributes
```

Успадкування змінює картину. Батьківський клас зі `__slots__` не має `__dict__`, але subclass без власного `__slots__` отримує `__dict__` і `__weakref__` для кожного екземпляра, тож економія пам’яті для його екземплярів зникає:[^py314-reference-datamodel-slots]

```python
class Base:
    __slots__ = ("x",)


class Child(Base):  # Child defines no __slots__
    pass


c = Child()
print(hasattr(c, "__dict__"))  # True: Child instances get a __dict__
c.extra = 1                    # allowed, so the savings from __slots__ are gone for Child
```

Множинне успадкування теж обмежене. Якщо два батьківські класи мають непорожні слоти, визначення класу з ними завершується `TypeError`, бо лише один базовий клас може мати атрибути, створені слотами.[^py314-reference-datamodel-slots] Ще одна пастка: значення за замовчуванням не можна задати атрибутом класу з тим самим ім’ям, що слот, бо атрибут класу перекриє дескриптор слота.[^py314-reference-datamodel-slots] У CPython така помилка видна вже під час створення класу як `ValueError`.

Підсумок: `__slots__` підходить для великої кількості однотипних об’єктів із фіксованою структурою, а не як загальна оптимізація. Гнучкість можна повернути, додавши `__dict__` або `__weakref__` до `__slots__`, але тоді частина економії зникає.[^py314-reference-datamodel-slots]

**Типові помилки:**
- очікувати економію пам’яті від `__slots__` у subclass без власного `__slots__`;
- вважати, що `__slots__` автоматично прискорює код, без вимірювання на реальному навантаженні;
- задавати значення за замовчуванням атрибутом класу з іменем слота.

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
