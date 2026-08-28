---
id: py-fund-0012
title: "Як executable nature інструкцій `def` і `class` впливає на умовне визначення, повторне визначення та import-time side effects?"
description: "def і class – виконувані інструкції (executable statements): вони створюють об'єкт функції або класу та прив'язують ім'я під час виконання, а не на етапі компіляції."
track: python
section: fundamentals
level: senior
type: mechanism
tags: []
status: published
updated: 2026-09-05
content_revision: 2
reconciled_with:
  en: 2
anki:
  export: true
sources:
  - source_id: py314-reference-executionmodel
    title: "Python 3.14: Reference/executionmodel"
    url: https://docs.python.org/3.14/reference/executionmodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-reference-datamodel
    title: "Python 3.14: Reference/datamodel"
    url: https://docs.python.org/3.14/reference/datamodel.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
  - source_id: py314-faq-general
    title: "Python 3.14: Faq/general"
    url: https://docs.python.org/3.14/faq/general.html
    accessed: 2026-09-04
    kind: official
    version: "3.14"
    applicability: "Офіційна документація Python 3.14."
---

## Short answer

**`def` і `class` – виконувані інструкції (executable statements): вони створюють об'єкт функції або класу та прив'язують ім'я під час виконання, а не на етапі компіляції.**[^py314-reference-executionmodel] Тому їх можна розміщувати всередині `if`/`else`, циклів і вкладених scope – визначиться лише та гілка, яка справді виконається. Повторний `def` або `class` з тим самим ім'ям у тій самій області просто переприв'язує ім'я до нового об'єкта. Оскільки тіло модуля виконується згору вниз при import, будь-який код на рівні модуля (I/O, мережеві виклики, print) стає import-time side effect, що ускладнює тестування та повторне використання.

## Detailed explanation

`def` і `class` не оголошують нічого на етапі компіляції – це інструкції, які виконуються, коли до
них доходить керування. `def` створює об'єкт функції й прив'язує ім'я; `class` виконує тіло класу в
окремому namespace, створює об'єкт класу і прив'язує
ім'я.[^py314-reference-executionmodel]

Звідси перший наслідок: обидві інструкції можна ставити будь-де, де можна поставити інструкцію –
всередині `if`, циклу, іншої функції. Виконається лише та гілка, до якої дійшло керування, тож
визначення умовне не «формально», а буквально.

```python
if sys.platform == 'win32':
    def newline():
        return '\r\n'
else:
    def newline():
        return '\n'

# only one of the two objects was ever created; the other `def` never ran
```

Другий наслідок: повторний `def` з тим самим іменем у тій самій області нічого не перевизначає в
сенсі перевантаження – він просто переприв'язує ім'я до нового об'єкта, а попередній стає
недосяжним. Тому в Python немає overloading за сигнатурою: останній `def` виграє.

```python
def handle(x):
    return 'first'

def handle(x, y):      # not an overload - it replaces the name binding
    return 'second'

handle(1)              # TypeError: handle() missing 1 required positional argument: 'y'
```

Третій наслідок стосується import. Тіло модуля – теж послідовність інструкцій, яка виконується згори
вниз під час першого import. Усе, що написано на рівні модуля, виконається саме тоді: `def` і
`class` створять об'єкти, а будь-що інше зробить свій побічний
ефект.[^py314-reference-executionmodel]

**Що з цього випливає на практиці:**
- декоратор застосовується в момент виконання `def`, а не при виклику функції – тому декоратор бачить
  функцію один раз, під час визначення;
- значення default-аргументів обчислюються при виконанні `def`, один раз, а не на кожен виклик;
- код на рівні модуля, який читає файл, ходить у мережу або друкує, стає import-time side effect:
  його неможливо не виконати, якщо модуль імпортовано;
- саме тому вхідну точку ховають за `if __name__ == '__main__':` – щоб import модуля не запускав
  програму.

Практична вигода умовного визначення реальна: платформенні або версійні варіанти функції пишуться
без обгортки-диспетчера, і на гарячому шляху не лишається жодної перевірки умови.[^py314-faq-general]

## Evaluation guide

TODO

## Sources

<!-- generated from frontmatter -->
