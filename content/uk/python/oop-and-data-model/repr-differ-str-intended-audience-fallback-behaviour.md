---
id: py-oop-0021
title: "Чим `__repr__` відрізняється від `__str__` за аудиторією та fallback behavior?"
description: "__repr__ повертає «official» рядок для налагодження, а __str__ – «informal» читабельне подання, яке використовують str() і print()."
track: python
section: oop-and-data-model
level: middle
type: comparison
tags: [repr, str]
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
  - source_id: py314-reference-datamodel-object-repr
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__repr__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: object.__repr__, призначення repr() і fallback для str(), коли є лише __repr__."
  - source_id: py314-reference-datamodel-object-str
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html#object.__str__
    accessed: 2026-10-13
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14: object.__str__, його використання в str(), print() і стандартному __format__, та виклик object.__repr__."
---

## Short answer

**`__repr__` повертає «official» рядок для налагодження, який має бути однозначним і, якщо можливо, виглядати як валідний Python-вираз.**[^py314-reference-datamodel-object-repr] `__str__` повертає «informal» рядок для `str()` і `print()`, і від нього не вимагають бути Python-виразом.[^py314-reference-datamodel-object-str] Якщо клас визначає лише `__repr__`, `str()` використовує його як fallback.[^py314-reference-datamodel-object-repr] Стандартний `object.__str__` сам викликає `object.__repr__`.[^py314-reference-datamodel-object-str]

## Detailed explanation

`repr()` і `str()` – це два окремі способи подати об’єкт, і їхні цілі різні. `repr(obj)` викликає `__repr__` і повертає «official» рядок, призначений насамперед для налагодження, тому він має бути інформативним і однозначним. Якщо це можливо, рядок має виглядати як Python-вираз, з якого можна відтворити об’єкт із тим самим значенням; якщо ні, документація радить форму `<...опис...>`. Стандартну реалізацію надає сам клас `object`.[^py314-reference-datamodel-object-repr]

`str(obj)` викликає `__str__` і повертає «informal» рядок, призначений для читання людиною. Документація не вимагає від нього бути Python-виразом, тож можна обрати коротше або зручніше подання.[^py314-reference-datamodel-object-str] Цей метод використовують `str()`, `print()` і стандартний `__format__`, тому f-рядок `{obj}` теж показує `__str__`, якщо клас не перевизначає `__format__`.[^py314-reference-datamodel-object-str]

Fallback працює лише в один бік. Якщо клас визначає тільки `__repr__`, то `str()` і `print()` показують його результат, бо стандартний `object.__str__` викликає `object.__repr__`.[^py314-reference-datamodel-object-str] Зворотного правила немає: клас, що має лише `__str__`, у `repr()` отримує стандартний рядок, який не відтворює значення; у CPython це, наприклад, `<__main__.Plain object at 0x...>`.

Приклад: один клас з обома методами і три виклики, кожен з яких використовує інший механізм.

```python
class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __repr__(self):
        return f"Money({self.amount!r}, {self.currency!r})"

    def __str__(self):
        return f"{self.amount:.2f} {self.currency}"

m = Money(12.5, "USD")
print(repr(m))  # Money(12.5, 'USD'): unambiguous, valid Python expression
print(str(m))   # 12.50 USD: readable text for people
print([m])      # [Money(12.5, 'USD')]: containers show the repr of their items
```

У CPython контейнери, як-от список, кортеж і словник, показують `repr` своїх елементів, тому `print([m])` виводить `repr`, хоча `print(m)` виводить `str`.

**Типові помилки:**
- вважати, що `print()` використовує `__repr__`; він викликає `__str__`, а без нього – `__repr__`;
- писати в `__repr__` лише зручний для людини текст, через що в логах бракує однозначного опису стану;
- визначати тільки `__str__` і очікувати, що `repr()` покаже вміст об’єкта.

## Comparison

TODO

## When to choose which

TODO

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
